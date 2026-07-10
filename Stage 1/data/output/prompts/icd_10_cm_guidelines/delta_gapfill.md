You are {analyst_role} doing a careful second pass on a {doc_purpose} about "{topic}".

A colleague already extracted this initial profile from the text:
{rough_profile}
{qna_hints}
Re-read the FULL TEXT below and find facts MISSING from the profile above.

Output ONLY a JSON object — nothing before or after it. Max 5 items per list. Close all braces.

{{
  "additional_behaviors": ["<missed behavior, or empty list>"],
  "additional_requirements": ["<missed Mandatory coding criteria or conditions that must be met before a specific code can be assigned (e.g., 'code first' notes, POA status)., or empty list>"],
  "additional_deprecated": ["<missed Guidelines or code assignments that are no longer valid, superseded by new guidelines or removed from the code set., or empty list>"],
  "additional_new_items": ["<missed Newly introduced guidelines, codes, or reporting requirements effective from a specific date., or empty list>"]
}}

Rules:
- Add a fact ONLY if it is GENUINELY MISSING from the initial profile.
- Do NOT repeat facts already captured (even if worded differently).
- additional_deprecated/additional_new_items: only add an item if the text EXPLICITLY states something was removed/discontinued/no-longer-permitted, or EXPLICITLY introduces something as new/added. Do not add an item just because it describes standing/current guidance — that belongs in additional_behaviors or additional_requirements instead.
- If nothing is missing, write [] for every key.
- No text before or after the JSON. Close all braces.

TOPIC: {topic}
FULL TEXT:
{text}

OUTPUT (JSON only — close all braces):