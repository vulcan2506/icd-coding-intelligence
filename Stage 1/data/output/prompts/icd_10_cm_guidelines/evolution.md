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
  "foundation": "The older version established that complications of care were only reportable if they were unexpected and not routinely associated with the procedure.",
  "value_added": [
    "Removal of the 'unexpected' qualifier to ensure all complications are captured.",
    "Explicit instruction to code regardless of expectation status."
  ],
  "narrative": "The older version introduced a restrictive rule requiring complications to be unexpected to be coded. The newer version builds on this by removing the expectation constraint, enabling the capture of all documented complications of care for better quality reporting."
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