# Code Assignment and Diagnosis Exception Logic
*Source: ICD-10-CM FY25 Guidelines October 1, 2024.pdf*

**Feature:** Code Assignment and Diagnosis Exception Logic

**Key Behaviors:**
- Code assignment is based on the provider's diagnostic statement that the condition exists, not on clinical criteria used to establish the diagnosis.
- If there is conflicting medical record documentation, the provider must be queried for clarification.
- Exceptions allow code assignment based on documentation from non-provider clinicians (e.g., dietitians, nurses) for specific metrics like BMI, pressure ulcer stage, and coma scale.
- The associated diagnosis for these exceptions must still be documented by the patient's provider.
- Codes for BMI, coma scale, NIHSS, blood alcohol level, SDOH, and underimmunization status must only be reported as secondary diagnoses.

**Requirements / Properties:**
- The provider's statement that the patient has a particular condition is sufficient for code assignment.
- For exceptions, the associated diagnosis (e.g., obesity, acute stroke) must be documented by the patient's provider.
- Specific metrics (BMI, ulcer depth, etc.) may be documented by permitted non-provider clinicians per regulatory or internal policies.
- Conflicting documentation from any clinician requires a provider query before finalizing codes.
- Exception codes must be assigned as secondary diagnoses, not primary.
- The associated diagnosis for exception codes must be documented by the patient's provider (physician or other qualified healthcare practitioner legally accountable for establishing the patient's diagnosis).
- Code assignment relies on documentation by the patient's provider unless a specific exception applies based on regulatory or accreditation requirements or internal hospital policies.

**New in this version:**
- Explicit inclusion of Social Determinants of Health (SDOH) classified to Chapter 21 as an exception for non-provider documentation.
- Clarification that underimmunization status is an exception allowing non-provider documentation of the metric.
- Mandatory restriction that exception codes (BMI, NIHSS, etc.) are limited to secondary diagnosis reporting.
- Laterality is included as an exception allowing code assignment based on documentation from non-provider clinicians.
- Codes for depth of non-pressure chronic ulcers are included as an exception allowing code assignment based on documentation from non-provider clinicians.
