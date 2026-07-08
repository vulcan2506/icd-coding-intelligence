You are {analyst_role} writing a "value-add" note about a change in {doc_purpose} for the feature "{topic}". You already have structured profiles for both versions and a classified delta below — do NOT re-read raw text, just re-synthesize these facts into a constructive evolution narrative.

CRITICAL RULES:
- Output ONLY a single JSON object — nothing before or after it.
- Ground every statement in the profiles/delta below — do not invent facts.
- Max 5 items in value_added. Close all braces.

Output this exact structure with real values:

{{
  "feature_name": "<short descriptive name>",
  "foundation": "<one sentence: what {vA} established>",
  "value_added": [
    "<concrete capability {vB} adds on top of that foundation>",
    "<another — max 5 total>"
  ],
  "narrative": "<2-3 sentences: {vA} introduced X; {vB} builds on it by Y, enabling Z>"
}}

### EXAMPLE ###

TOPIC: Documentation of Complications of Care

OUTPUT:
{{
  "feature_name": "Documentation of Complications of Care",
  "foundation": "The older version established that complications of care should only be coded if they occur after the onset of the condition and are not part of the natural progression of the disease.",
  "value_added": [
    "Explicit requirement that the complication must be directly related to the care provided.",
    "Clarification that the timing must be after the onset of the condition."
  ],
  "narrative": "The older version introduced the basic criteria for coding complications of care, focusing on timing and natural progression. The newer version builds on this by adding the specific constraint that the complication must be directly related to the care provided, enabling more precise identification of adverse events linked to treatment rather than the disease itself."
}}

### ACTUAL TASK ###
TOPIC: {topic}

{vA} profile:
{profile_A}

{vB} profile:
{profile_B}

Delta analysis: {delta_analysis}
Key differences: {key_differences}

OUTPUT (JSON only — close all braces, max 5 items in value_added):