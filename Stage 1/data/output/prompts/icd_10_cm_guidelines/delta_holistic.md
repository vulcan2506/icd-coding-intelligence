You are {analyst_role}. Read the {doc_purpose} text below about "{topic}" and extract a structured behavioral profile.

CRITICAL RULES:
- Output ONLY a single JSON object — nothing before or after it.
- Do NOT output the structure definition itself; fill in real values.
- Keep each list to a MAXIMUM of 5 items so the JSON stays concise.
- If the text covers multiple features, combine their behaviors under one   profile using a descriptive feature_name like "Feature A + Feature B".
- Use exact property names where mentioned (e.g. WORKBASKET_RULE_OPTIMIZATION_ENABLE).
- If a list has no items write [].
- Complete the closing braces — never leave the JSON unfinished.
- Only include an item in "deprecated_items" if the text EXPLICITLY states it is removed, discontinued, replaced, or no longer permitted going forward. Only include an item in "new_items" if the text EXPLICITLY frames it as newly introduced or added. Standing/current guidance that simply describes correct vs. incorrect practice (with no explicit before/after framing) is NOT a deprecation or a new item — leave both lists empty rather than inventing an entry just to have something to report. See EXAMPLE D.

Output this exact structure with real values:

{{
  "feature_name": "<short descriptive name — combine if multiple features>",
  "key_behaviors": [
    "<behavior 1>",
    "<behavior 2>",
    "<behavior 3 — max 5 total>"
  ],
  "requirements": [
    "<Mandatory coding criteria or conditions that must be met before a specific code can be assigned (e.g., 'code first' notes, POA status). — max 5 total>"
  ],
  "deprecated_items": [
    "<Guidelines or code assignments that are no longer valid, superseded by new guidelines or removed from the code set. — max 5 total>"
  ],
  "new_items": [
    "<Newly introduced guidelines, codes, or reporting requirements effective from a specific date. — max 5 total>"
  ]
}}

### EXAMPLE 1 ###

TOPIC: Documentation of Complications of Care
TEXT: Complications of care must now be coded regardless of whether they were expected, provided they are documented as complications of care.

OUTPUT:
{{
  "feature_name": "Documentation of Complications of Care",
  "key_behaviors": ["Complications of care must now be coded regardless of whether they were expected, provided they are documented as complications of care."],
  "requirements": [],
  "deprecated_items": [],
  "new_items": []
}}

### EXAMPLE 2 ###

TOPIC: Reporting of Borderline Diagnoses
TEXT: A diagnosis may be coded if the documentation indicates the condition is suspected or probable, even if not confirmed, provided the provider documents the uncertainty.

OUTPUT:
{{
  "feature_name": "Reporting of Borderline Diagnoses",
  "key_behaviors": ["A diagnosis may be coded if the documentation indicates the condition is suspected or probable, even if not confirmed, provided the provider documents the uncertainty."],
  "requirements": [],
  "deprecated_items": [],
  "new_items": []
}}

### ACTUAL TASK ###
TOPIC: {topic}
TEXT:
{text}

OUTPUT (JSON only — close all braces, max 5 items per list):