# Code Assignment and Diagnosis Exception Logic
*Source: icd_10_cm_october_2025_guidelines_0.pdf*

**Feature:** Code Assignment and Diagnosis Exception Logic

**Key Behaviors:**
- Code assignment is based on the provider's diagnostic statement that the condition exists, not on clinical criteria used to establish the diagnosis.
- If conflicting medical record documentation exists, the provider must be queried for clarification.
- Exceptions allow code assignment based on documentation from non-provider clinicians (e.g., dietitians, nurses) for specific metrics like BMI, pressure ulcer stage, and coma scale.
- The associated diagnosis for these exceptions must still be documented by the patient's provider.
- Codes for BMI, coma scale, NIHSS, blood alcohol level, SDOH, and underimmunization status must be reported as secondary diagnoses.

**Requirements / Properties:**
- The patient's provider must legally be accountable for establishing the patient's diagnosis.
- The provider's statement that a condition exists is sufficient for code assignment.
- Associated diagnoses for exception metrics must be documented by the patient's provider.
- Specific exception metrics (BMI, ulcer depth, etc.) must be documented by permitted clinicians in the official medical record.
- Exception codes must be reported as secondary diagnoses.
- If there is conflicting medical record documentation, either from the same clinician or different clinicians, the patient's provider should be queried for clarification.

**New in this version:**
- BMI, depth of non-pressure chronic ulcers, pressure ulcer stage, coma scale, NIHSS, SDOH, laterality, blood alcohol level, underimmunization status, and firearm injury intent are now permitted as exceptions for code assignment based on non-provider documentation.
- The requirement that associated diagnoses for these exceptions must be documented by the patient's provider is explicitly defined.
- The rule that these specific exception codes must only be reported as secondary diagnoses is established.
- Depth of non-pressure chronic ulcers is now permitted as an exception for code assignment based on non-provider documentation.
- Laterality is now permitted as an exception for code assignment based on non-provider documentation.
- Firearm injury intent is now permitted as an exception for code assignment based on non-provider documentation.
- Codes for social determinants of health (SDOH) classified to Chapter 21 are now permitted as exceptions for code assignment based on non-provider documentation.
