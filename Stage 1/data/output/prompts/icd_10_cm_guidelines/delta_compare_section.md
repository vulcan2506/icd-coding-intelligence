CHANGE TYPE (pick the MOST SPECIFIC match):
  Coding Rule Clarification - Used when a guideline is updated to provide clearer instructions or resolve ambiguity in existing coding logic.
  Scope Expansion - Used when the application of a rule is extended to new conditions, body parts, or facility types.
  Definition Revision - Used when the clinical definition or criteria for a specific code or concept is altered.
  Guidance Reversal - Used when a newer version explicitly contradicts or reverses a previous guideline, often due to feedback or new clinical evidence.
  No Meaningful Change - Used when the text has been updated for formatting or minor wording but the coding logic remains identical.

### EXAMPLE 1 ###

{label_A} profile:
  Feature: Documentation of Complications of Care
  Behaviors: Complications of care were generally coded only if they were unexpected and not routinely associated with the procedure.

{label_B} profile:
  Feature: Documentation of Complications of Care
  Behaviors: Complications of care must now be coded regardless of whether they were expected, provided they are documented as complications of care.

OUTPUT:
{{
  "relevance_score": 9,
  "relevance_reason": "Both profiles describe the same topic across versions.",
  "change_type": "Coding Rule Clarification",
  "analysis": "The older version relied on the 'unexpected' qualifier to determine if a complication warranted coding. The newer version removes this qualifier, clarifying that any documented complication of care requires a code, ensuring more comprehensive reporting of adverse events.",
  "key_differences": [
    "{label_A}: Complications of care were generally coded only if they were unexpected and not routinely associated with the procedure. -> {label_B}: Complications of care must now be coded regardless of whether they were expected, provided they are documented as complications of care."
  ],
  "confidence": "medium"
}}

### EXAMPLE 2 ###

{label_A} profile:
  Feature: Reporting of Borderline Diagnoses
  Behaviors: A diagnosis should not be coded if the documentation is uncertain or if the provider has not confirmed the condition.

{label_B} profile:
  Feature: Reporting of Borderline Diagnoses
  Behaviors: A diagnosis may be coded if the documentation indicates the condition is suspected or probable, even if not confirmed, provided the provider documents the uncertainty.

OUTPUT:
{{
  "relevance_score": 9,
  "relevance_reason": "Both profiles describe the same topic across versions.",
  "change_type": "Guidance Reversal",
  "analysis": "The previous guideline strictly prohibited coding uncertain diagnoses. The newer version reverses this stance, allowing coders to assign codes for suspected conditions when the provider explicitly documents the uncertainty, thereby capturing more clinical data.",
  "key_differences": [
    "{label_A}: A diagnosis should not be coded if the documentation is uncertain or if the provider has not confirmed the condition. -> {label_B}: A diagnosis may be coded if the documentation indicates the condition is suspected or probable, even if not confirmed, provided the provider documents the uncertainty."
  ],
  "confidence": "medium"
}}