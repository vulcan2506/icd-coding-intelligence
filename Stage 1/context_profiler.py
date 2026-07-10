"""
context_profiler.py
───────────────────
Builds domain-aware profiles from document content to dynamically adapt
all downstream LLM prompts.  Runs once per unique document type.

Pipeline position:  After enrichment, before quality filter.

Architecture:
  1. Group chunks by source_doc → derive a type_key per document family
     (e.g. both '25.2_HR_Payer_Release_Notes.pdf' and
      '26.1_HR_Payer_Release_Notes.pdf' share key 'HR_Payer_Release_Notes')
  2. For each unique type_key, collect:
       - Captured TOC text (stored by ingest.py before discard)
       - Section header distribution
       - Top keywords by frequency
       - 3 high-quality, diverse sample chunks
  3. Single LLM call produces a domain profile:
       domain, document_purpose, specialist_role, analyst_role,
       entity_types, key_terminology, labeling_few_shots
  4. Profile is cached to disk — subsequent runs skip the LLM call
  5. Downstream modules call get_profile(source_doc) to fetch it

Bridge profiles (cross-document connections):
  When multiple type_keys exist in the same pipeline run, a lightweight
  bridge context is generated capturing how the document families relate.
"""

import json
import re
import logging
from pathlib import Path
from collections import Counter
from typing import Dict, List, Optional

import config
import llm_client

log = logging.getLogger(__name__)

PROFILE_CACHE_DIR = config.OUTPUT_DIR / "profiles"
PROMPT_OUTPUT_DIR = config.PROMPT_OUTPUT_DIR

_profiles: Dict[str, dict] = {}
_toc_store: Dict[str, str] = {}
_bridge_context: Optional[dict] = None


# ══════════════════════════════════════════════════════════════════════════════
# TOC CAPTURE  (called by ingest.py)
# ══════════════════════════════════════════════════════════════════════════════

def store_toc(source_doc: str, toc_text: str):
    """Called by ingest.py to preserve TOC text before it is discarded."""
    if source_doc in _toc_store:
        _toc_store[source_doc] += "\n\n" + toc_text
    else:
        _toc_store[source_doc] = toc_text


# ══════════════════════════════════════════════════════════════════════════════
# TYPE KEY DERIVATION
# ══════════════════════════════════════════════════════════════════════════════

_MONTH_NAMES = (
    r"january|february|march|april|may|june|july|august|"
    r"september|october|november|december"
)  # local copy — avoids coupling context_profiler (an early pipeline stage)
   # to delta_analyzer's heavier pydantic/langchain-based module for a
   # 12-item constant.


def _derive_type_key(filename: str) -> str:
    """
    Strip version signal to get a shared document type key, so different
    versions of the same document collapse to one profile.

    Layer 1 (original): strip a leading numeric version prefix.
    '25.2_HR_Payer_Release_Notes.pdf'  →  'HR_Payer_Release_Notes'
    '26.1_HR_Payer_Release_Notes.pdf'  →  'HR_Payer_Release_Notes'

    Layer 2 (added): if layer 1 found no numeric prefix, also strip embedded
    FY/month/year/trailing-index tokens — filenames like the ICD-10-CM
    corpus ("ICD-10-CM FY25 Guidelines October 1, 2024" /
    "icd_10_cm_october_2025_guidelines_0") don't start with a bare version
    number, so layer 1 alone leaves each version as its own unrelated type,
    fragmenting the profile/prompt-caching machinery that assumes one type
    per document family.

    Layer 2 only activates when it actually finds a version-shaped token —
    'Clinical_Trial_Report_v3.pdf' has none of FY/month-name/4-digit-year/
    trailing-index, so it returns unchanged from today's behavior, same as
    'HR_Payer_Release_Notes' above (no token found there either — the
    numeric prefix was already consumed by layer 1). This guarantees any
    filename layer 1 already resolves correctly keeps producing the exact
    same type_key string as before (type_key is used as a literal cache
    filename, so changing an already-working case would orphan existing
    caches).

    Known accepted tradeoff: a hypothetical "25.2_HR_Payer_Release_Notes_2"
    would trigger the trailing-index rule and get case-folded to
    "hr_payer_release_notes" — a casing change vs. today. Neither the ICD
    nor the HealthRules corpus currently has this filename shape.
    """
    stem = Path(filename).stem
    stripped = re.sub(r'^\d+[\.\d]*[_\s-]+', '', stem)
    stripped = stripped if stripped else stem

    # Real spaces (not just underscore/dash) so \b-anchored token regexes
    # below can match inside underscore/dash-joined stems — underscore is a
    # \w character, so \b never fires on either side of it otherwise.
    spaced = re.sub(r'[_\-]+', ' ', stripped)

    tokenless = spaced
    found_token = False
    for pattern in (
        r'\bFY\.?\s?\d{2,4}\b',
        rf'\b(?:{_MONTH_NAMES})\b(?:\s+\d{{1,2}}(?:st|nd|rd|th)?\b,?)?',
        r'\b(?:19|20)\d{2}\b',
        r'(?<=\s)\d+\Z',   # trailing bare numeric index/export-artifact, e.g. "..._0"
    ):
        tokenless, n = re.subn(pattern, ' ', tokenless, flags=re.IGNORECASE)
        found_token = found_token or n > 0

    if not found_token:
        return stripped   # no version signal detected — unchanged from today

    normalized = re.sub(r'[^a-z0-9]+', '_', tokenless.lower()).strip('_')
    return normalized or stripped




# ══════════════════════════════════════════════════════════════════════════════
# COLLECTION HELPERS
# ══════════════════════════════════════════════════════════════════════════════

def _collect_section_headers(chunks: List[Dict]) -> List[str]:
    seen = set()
    headers = []
    for c in chunks:
        h = c.get("section_header", "").strip()
        if h and h not in seen:
            seen.add(h)
            headers.append(h)
    return headers


def _collect_top_keywords(chunks: List[Dict], top_n: int = 30) -> List[str]:
    counter = Counter()
    for c in chunks:
        for kw in c.get("keywords", []):
            counter[kw.lower().strip()] += 1
    return [kw for kw, _ in counter.most_common(top_n)]


def _select_sample_chunks(chunks: List[Dict], n: int = 3) -> List[Dict]:
    scored = [c for c in chunks if c.get("text_quality_score", 0) > 0]
    scored.sort(key=lambda c: c.get("text_quality_score", 0), reverse=True)

    selected = []
    seen_headers = set()
    for c in scored:
        h = c.get("section_header", "")
        if h not in seen_headers:
            selected.append(c)
            seen_headers.add(h)
            if len(selected) >= n:
                break

    for c in scored:
        if c not in selected:
            selected.append(c)
            if len(selected) >= n:
                break

    return selected[:n]


# ══════════════════════════════════════════════════════════════════════════════
# PROFILE PROMPT
# ══════════════════════════════════════════════════════════════════════════════

_PROFILE_PROMPT = """\
You are a document analysis expert.  Analyze the document metadata and \
content samples below, then produce a domain profile JSON that will be \
used to adapt LLM prompts for processing this type of document.

DOCUMENT TYPE KEY: {type_key}
SOURCE FILES: {filenames}

{toc_section}

SECTION HEADERS ({n_headers} unique):
{section_headers}

TOP KEYWORDS (by frequency):
{top_keywords}

SAMPLE CONTENT:
{samples}

Output ONLY a JSON object — no markdown, no preamble.  Close all braces.

{{
  "domain": "<specific domain, e.g. 'healthcare claims administration'>",
  "document_purpose": "<what these documents are, e.g. 'software release notes'>",
  "specialist_role": "<prompt persona, e.g. 'a healthcare payer systems specialist'>",
  "analyst_role": "<analysis persona, e.g. 'a healthcare IT analyst'>",
  "entity_types": ["<5-8 key entity types found in the content>"],
  "key_terminology": {{
    "<ACRONYM>": "<definition>",
    "<ACRONYM>": "<definition>"
  }},
  "labeling_few_shots": [
    {{
      "text_snippet": "<1-2 sentence excerpt from the samples above>",
      "master_label": "<specific 2-5 word noun phrase>",
      "description": "<1-2 sentence description>"
    }},
    {{
      "text_snippet": "<different excerpt — prefer table/structured data if present>",
      "master_label": "<specific 2-5 word noun phrase>",
      "description": "<1-2 sentence description>"
    }},
    {{
      "text_snippet": "<different excerpt — different content type from above>",
      "master_label": "<specific 2-5 word noun phrase>",
      "description": "<1-2 sentence description>"
    }}
  ],
  "delta_change_types": [
    {{"name": "<domain-native category for a MEANINGFUL change, e.g. 'Coding Rule Clarification' for medical coding or 'Deprecation' for software>", "description": "<when to use this category, 1 sentence>"}},
    {{"name": "<category>", "description": "<...>"}},
    {{"name": "<category>", "description": "<...>"}},
    {{"name": "<category — include one for a REVERSAL/contradiction between versions>", "description": "<...>"}},
    {{"name": "<category — include one for 'no meaningful change / unrelated pair'>", "description": "<...>"}}
  ],
  "delta_field_meaning": {{
    "requirements": "<what a prerequisite/condition/mandate means for THIS domain — e.g. 'coding sequence prerequisite' vs 'runtime config flag'>",
    "deprecated_items": "<what 'removed or superseded' means for THIS domain>",
    "new_items": "<what 'newly introduced' means for THIS domain>"
  }},
  "delta_field_labels": {{
    "requirements": "<a SHORT (2-4 word) section heading for a list of requirement/prerequisite items in THIS domain, no markdown, no trailing colon — e.g. 'Coding Prerequisites' for medical coding or 'Requirements / Properties' for software>",
    "deprecated_items": "<a SHORT (2-4 word) heading for a list of removed/superseded items in THIS domain — e.g. 'Superseded Guidance' for medical coding; do NOT use a software-deprecation phrase unless the domain IS software>",
    "new_items": "<a SHORT (2-4 word) heading for a list of newly introduced items in THIS domain — e.g. 'Newly Introduced Guidance'>"
  }},
  "delta_few_shots": [
    {{
      "topic": "<short illustrative topic name plausible for this domain — invented, not from the samples>",
      "version_a": "<1-2 sentence plausible OLDER-version behavior in this domain's own style>",
      "version_b": "<1-2 sentence plausible NEWER-version behavior showing a COMMON/ENHANCEMENT-style change from version_a — old behavior still holds, new capability added>",
      "change_type": "<must exactly match one \"name\" from delta_change_types above — pick the enhancement/common one>",
      "analysis": "<2-3 sentences explaining the delta, modeling the reasoning style an analyst in this domain would use>"
    }},
    {{
      "topic": "<a DIFFERENT illustrative topic — not the same as the first example>",
      "version_a": "<1-2 sentence plausible OLDER-version behavior>",
      "version_b": "<1-2 sentence plausible NEWER-version behavior that EXPLICITLY REVERSES or CONTRADICTS version_a — not just an addition>",
      "change_type": "<must exactly match the REVERSAL/contradiction category name from delta_change_types above>",
      "analysis": "<2-3 sentences explaining the delta>"
    }}
  ],
  "qna_few_shots": [
    {{"q": "<a WHY/HOW/WHAT-IF question a curious practitioner in this domain would ask about a change like delta_few_shots[0]>", "a": "<2-3 sentence reasoned answer>"}},
    {{"q": "<a different WHY/HOW/WHAT-IF question, different angle>", "a": "<2-3 sentence reasoned answer>"}}
  ],
  "evolution_few_shot": {{
    "topic": "<same topic/change as delta_few_shots[0] — the enhancement-style one>",
    "foundation": "<one sentence: what the OLDER version established, matching delta_few_shots[0].version_a>",
    "value_added": ["<concrete capability the NEWER version adds on top>", "<another, max 3>"],
    "narrative": "<2-3 sentences: older version introduced X; newer version builds on it by Y, enabling Z>"
  }}
}}

RULES:
- Base the profile on the ACTUAL content provided — do not invent terms.
- specialist_role and analyst_role must be specific to the detected domain.
- labeling_few_shots MUST use real text from the samples, not invented text.
- delta_change_types, delta_few_shots, and qna_few_shots MAY be invented
  illustrative examples (this domain's two document versions aren't both
  available yet at profiling time) — but their STYLE, vocabulary, and change
  categories must fit THIS domain specifically. Do not reuse software-release
  concepts (runtime properties, UI tabs, API deprecation) unless the actual
  domain IS software release notes.
- delta_few_shots MUST contain 2 DIFFERENT examples with 2 DIFFERENT
  change_type values (one common/enhancement-style, one reversal-style) —
  showing only one category leaves every other category (including
  mismatched/no-change pairs) with zero worked example to calibrate against.
- evolution_few_shot re-tells delta_few_shots[0] (not a new invented topic)
  as a constructive "what value did the newer version add" narrative — it
  feeds evolution_analyzer.py, which only ever processes constructive
  change types, so one worked example (not a contrasting pair) is enough.
- key_terminology: 5-10 most important acronyms/abbreviations found.
- entity_types: the recurring nouns/concepts that chunk labels should reference.
- delta_field_labels values must be plain short phrases suitable as a bold
  markdown section heading (no leading verb, no trailing colon/punctuation) —
  these render directly in generated reports, so they must read naturally to
  a domain practitioner, not a software engineer, unless the domain IS software.
- Output ONLY JSON.  No text before or after.  Close all braces."""


def _build_profile_prompt(
    type_key: str,
    filenames: List[str],
    toc_text: str,
    section_headers: List[str],
    top_keywords: List[str],
    sample_chunks: List[Dict],
) -> str:
    toc_section = (
        f"TABLE OF CONTENTS (captured from document):\n{toc_text[:2000]}"
        if toc_text.strip()
        else "TABLE OF CONTENTS: Not available — using section headers instead."
    )

    samples_text = ""
    for i, c in enumerate(sample_chunks, 1):
        header = c.get("section_header", "Unknown")
        text = c.get("text", "")[:500]
        kws = ", ".join(c.get("keywords", [])[:5])
        samples_text += (
            f"--- Sample {i} (Section: {header}) ---\n"
            f"{text}\n"
            f"Keywords: {kws}\n\n"
        )

    return _PROFILE_PROMPT.format(
        type_key=type_key,
        filenames=", ".join(filenames),
        toc_section=toc_section,
        n_headers=len(section_headers),
        section_headers="\n".join(f"  - {h}" for h in section_headers[:40]),
        top_keywords=", ".join(top_keywords),
        samples=samples_text,
    )


# ══════════════════════════════════════════════════════════════════════════════
# BRIDGE PROMPT  (cross-document-type connections)
# ══════════════════════════════════════════════════════════════════════════════

_BRIDGE_PROMPT = """\
You are a document analysis expert.  Two or more document families are \
being processed together.  Describe how they relate so that cross-document \
analysis can maintain context.

DOCUMENT FAMILIES:
{family_descriptions}

Output ONLY a JSON object:
{{
  "relationship": "<1-2 sentences describing how these document families connect>",
  "shared_entities": ["<entities/concepts that appear across families>"],
  "cross_reference_notes": "<guidance for analysts comparing content across families>"
}}

Output ONLY JSON.  Close all braces."""


def _build_bridge(profiles: Dict[str, dict]) -> Optional[dict]:
    if len(profiles) < 2:
        return None

    descs = ""
    for key, p in profiles.items():
        descs += (
            f"- {key}: domain={p.get('domain','?')}, "
            f"purpose={p.get('document_purpose','?')}, "
            f"entities={p.get('entity_types',[])} \n"
        )

    prompt = _BRIDGE_PROMPT.format(family_descriptions=descs)

    try:
        raw = llm_client.generate(prompt, max_tokens=500, enable_thinking=False)
        bridge = _extract_json(raw)
        if bridge and "relationship" in bridge:
            return bridge
    except Exception as e:
        log.warning(f"Bridge generation failed: {e}")

    return None


# ══════════════════════════════════════════════════════════════════════════════
# JSON EXTRACTION
# ══════════════════════════════════════════════════════════════════════════════

def _extract_json(raw: str) -> Optional[dict]:
    cleaned = re.sub(r"```(?:json)?|```", "", raw).strip()
    try:
        return json.loads(cleaned)
    except json.JSONDecodeError:
        pass

    start = cleaned.find('{')
    if start == -1:
        return None

    stack: list = []
    in_str = escape = False
    for i, ch in enumerate(cleaned[start:], start):
        if escape:
            escape = False
            continue
        if ch == '\\' and in_str:
            escape = True
            continue
        if ch == '"':
            in_str = not in_str
            continue
        if in_str:
            continue
        if ch in '{[':
            stack.append(ch)
        elif ch in '}]':
            if stack:
                stack.pop()
                if not stack:
                    try:
                        return json.loads(cleaned[start:i + 1])
                    except json.JSONDecodeError:
                        break

    # Repair truncated JSON
    if stack:
        closings = ''.join(']' if b == '[' else '}' for b in reversed(stack))
        base = cleaned[start:].rstrip()
        candidates = [
            base,
            re.sub(r',?\s*"[^"]*$', '', base),
            re.sub(r',\s*$', '', base),
        ]
        for candidate in candidates:
            try:
                return json.loads(candidate + closings)
            except json.JSONDecodeError:
                pass

    return None


# ══════════════════════════════════════════════════════════════════════════════
# DEFAULT / FALLBACK PROFILE
# ══════════════════════════════════════════════════════════════════════════════

_DEFAULT_PROFILE = {
    "domain": "general technical documentation",
    "document_purpose": "technical documentation",
    "specialist_role": "a technical documentation specialist",
    "analyst_role": "a technical analyst",
    "entity_types": ["documents", "features", "components", "configurations"],
    "key_terminology": {},
    "labeling_few_shots": [],
    "delta_change_types": [],
    "delta_field_meaning": {},
    "delta_field_labels": {},
    "delta_few_shots": [],
    "qna_few_shots": [],
    "evolution_few_shot": {},
}


# ══════════════════════════════════════════════════════════════════════════════
# MAIN ENTRY POINT
# ══════════════════════════════════════════════════════════════════════════════

def build_profiles(chunks: List[Dict]) -> Dict[str, dict]:
    """
    Build domain profiles from pre-quality-filter chunks.

    Chunks are grouped by source_doc → type_key.  Documents sharing a
    type_key (e.g. versioned release notes) get a single shared profile.
    Profiles are cached to disk so subsequent runs are instant.

    Returns {type_key: profile_dict}.
    """
    global _bridge_context
    PROFILE_CACHE_DIR.mkdir(parents=True, exist_ok=True)

    # ── Group chunks by type key ──────────────────────────────────────────────
    type_groups: Dict[str, Dict] = {}
    for c in chunks:
        doc = c.get("source_doc", "unknown")
        key = _derive_type_key(doc)
        if key not in type_groups:
            type_groups[key] = {"filenames": set(), "chunks": []}
        type_groups[key]["filenames"].add(doc)
        type_groups[key]["chunks"].append(c)

    log.info(
        f"[Context Profiler] {len(type_groups)} document type(s) detected: "
        f"{list(type_groups.keys())}"
    )

    # ── Build / load profile per type key ─────────────────────────────────────
    for type_key, group in type_groups.items():
        cache_path = PROFILE_CACHE_DIR / f"{type_key}.json"

        if cache_path.exists():
            log.info(f"[Context Profiler] Cache hit for '{type_key}'")
            with open(cache_path, "r", encoding="utf-8") as f:
                _profiles[type_key] = json.load(f)
            continue

        filenames = sorted(group["filenames"])
        doc_chunks = group["chunks"]

        log.info(
            f"[Context Profiler] Profiling '{type_key}' "
            f"({len(doc_chunks)} chunks from {len(filenames)} file(s))..."
        )

        # Collect signals
        toc_parts = [
            f"[From {fn}]\n{_toc_store[fn]}"
            for fn in filenames if fn in _toc_store
        ]
        toc_text = "\n\n".join(toc_parts)
        section_headers = _collect_section_headers(doc_chunks)
        top_keywords = _collect_top_keywords(doc_chunks)
        samples = _select_sample_chunks(doc_chunks)

        prompt = _build_profile_prompt(
            type_key, filenames, toc_text,
            section_headers, top_keywords, samples,
        )

        try:
            # Bumped from 750 -> 1600 for delta_change_types/delta_field_meaning/
            # delta_few_shots/qna_few_shots, then -> 2200 for evolution_few_shot,
            # then -> 2400 for delta_field_labels — each addition pushed
            # truncation further into the (most important, most domain-specific)
            # later fields; a real ICD profile hit exactly this truncation at
            # 1600 once evolution_few_shot was added. delta_field_labels is
            # placed right after delta_field_meaning in the schema (not at the
            # end) so it survives even if a later field still gets clipped.
            raw = llm_client.generate(prompt, max_tokens=2400, enable_thinking=False)
            profile = _extract_json(raw)

            if not profile or "domain" not in profile:
                log.warning(
                    f"[Context Profiler] Parse failed for '{type_key}', "
                    f"using defaults.  Raw output:\n{raw[:300]}"
                )
                profile = dict(_DEFAULT_PROFILE)
                profile["_parse_failed"] = True
        except Exception as e:
            log.error(f"[Context Profiler] LLM call failed for '{type_key}': {e}")
            profile = dict(_DEFAULT_PROFILE)
            profile["_error"] = str(e)

        for key, default in _DEFAULT_PROFILE.items():
            if key not in profile:
                profile[key] = default

        profile["type_key"] = type_key
        profile["source_files"] = filenames

        with open(cache_path, "w", encoding="utf-8") as f:
            json.dump(profile, f, indent=2, ensure_ascii=False)
        log.info(f"[Context Profiler] Profile cached → {cache_path}")

        _profiles[type_key] = profile

    # ── Bridge context (multi-type runs) ──────────────────────────────────────
    if len(_profiles) >= 2:
        bridge_path = PROFILE_CACHE_DIR / "_bridge.json"
        if bridge_path.exists():
            with open(bridge_path, "r", encoding="utf-8") as f:
                _bridge_context = json.load(f)
            log.info("[Context Profiler] Loaded bridge context from cache")
        else:
            log.info("[Context Profiler] Building cross-document bridge context...")
            _bridge_context = _build_bridge(_profiles)
            if _bridge_context:
                with open(bridge_path, "w", encoding="utf-8") as f:
                    json.dump(_bridge_context, f, indent=2, ensure_ascii=False)
                log.info(f"[Context Profiler] Bridge cached → {bridge_path}")

    # ── Summary ───────────────────────────────────────────────────────────────
    for key, p in _profiles.items():
        log.info(
            f"  ├─ {key}: domain='{p.get('domain','')}', "
            f"purpose='{p.get('document_purpose','')}', "
            f"{len(p.get('labeling_few_shots',[]))} few-shots, "
            f"{len(p.get('key_terminology',{}))} terms"
        )

    return dict(_profiles)


# ══════════════════════════════════════════════════════════════════════════════
# PUBLIC ACCESSORS  (used by downstream modules)
# ══════════════════════════════════════════════════════════════════════════════

def get_profile(source_doc: str) -> Optional[dict]:
    """
    Look up the cached profile for a given source document filename.

    Falls back to the on-disk cache (PROFILE_CACHE_DIR/{type_key}.json) when
    _profiles is empty for this key — _profiles is only populated in-process
    by build_profiles() (called from main.py's own process). run_tail.py is a
    SEPARATE process/invocation that never calls build_profiles(), so without
    this fallback every get_profile() call here (delta_analyzer.py,
    topic_summarizer.py, hierarchy_summarizer.py, grouper.py) silently
    returned None and fell back to generic defaults, regardless of how good
    the actual saved profile was.
    """
    key = _derive_type_key(source_doc)
    if key in _profiles:
        return _profiles[key]

    cache_path = PROFILE_CACHE_DIR / f"{key}.json"
    if cache_path.exists():
        with open(cache_path, "r", encoding="utf-8") as f:
            profile = json.load(f)
        _profiles[key] = profile
        return profile

    return None


def get_all_profiles() -> Dict[str, dict]:
    return dict(_profiles)


def get_bridge() -> Optional[dict]:
    return _bridge_context


# ══════════════════════════════════════════════════════════════════════════════
# PROMPT PERSISTENCE  (save / load dynamic prompts as .md files)
# ══════════════════════════════════════════════════════════════════════════════

def save_prompt(type_key: str, name: str, content: str):
    """
    Save a generated prompt template as a readable .md file.

    Files land in:  data/output/prompts/<type_key>/<name>.md
    Modules call this once when they first generate a dynamic prompt.
    On subsequent runs the saved file is loaded instead of regenerating,
    and users can hand-edit the .md to tweak prompt style.
    """
    prompt_dir = PROMPT_OUTPUT_DIR / type_key
    prompt_dir.mkdir(parents=True, exist_ok=True)
    path = prompt_dir / f"{name}.md"
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    log.info(f"[Prompt Saved] {path}")


def load_prompt(type_key: str, name: str) -> Optional[str]:
    """
    Load a previously saved prompt template.
    Returns None if no file exists — caller should fall back to generation.
    """
    path = PROMPT_OUTPUT_DIR / type_key / f"{name}.md"
    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            return f.read().strip()
    return None


# ── Prompt fragment builders (convenience for downstream modules) ─────────

def get_role(source_doc: str, kind: str = "specialist") -> str:
    """
    Returns the domain-appropriate role string.
    kind: 'specialist' | 'analyst'
    Falls back to a generic role if no profile exists.
    """
    p = get_profile(source_doc)
    if p:
        field = "specialist_role" if kind == "specialist" else "analyst_role"
        return p.get(field, _DEFAULT_PROFILE[field])
    return _DEFAULT_PROFILE.get(
        "specialist_role" if kind == "specialist" else "analyst_role",
        "a technical specialist",
    )


def get_terminology_block(source_doc: str) -> str:
    """Returns a formatted terminology block for injection into prompts."""
    p = get_profile(source_doc)
    if not p:
        return ""
    terms = p.get("key_terminology", {})
    if not terms:
        return ""
    lines = [f"  {k} = {v}" for k, v in list(terms.items())[:10]]
    return "KEY TERMINOLOGY:\n" + "\n".join(lines) + "\n"


def get_few_shot_block(source_doc: str) -> str:
    """Returns formatted few-shot examples for labeling prompts."""
    p = get_profile(source_doc)
    if not p:
        return ""
    shots = p.get("labeling_few_shots", [])
    if not shots:
        return ""
    parts = []
    for i, ex in enumerate(shots, 1):
        snippet = ex.get("text_snippet", "")
        label = ex.get("master_label", "")
        desc = ex.get("description", "")
        parts.append(
            f'EXAMPLE {i}:\n'
            f'TEXT: "{snippet}"\n'
            f'OUTPUT: {{"master_label": "{label}", '
            f'"description": "{desc}"}}'
        )
    return "\n\n".join(parts)
