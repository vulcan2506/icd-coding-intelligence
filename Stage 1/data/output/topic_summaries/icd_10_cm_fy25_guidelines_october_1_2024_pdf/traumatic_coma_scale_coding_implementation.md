# Traumatic Coma Scale Coding Implementation
*Source: ICD-10-CM FY25 Guidelines October 1, 2024.pdf*

**Feature:** Traumatic Coma Scale Coding Implementation

**Key Behaviors:**
- Coma scale codes (R40.21- to R40.24-) must be sequenced after the primary diagnosis code(s) and used in conjunction with traumatic brain injury codes.
- The 7th character indicating when the scale was recorded must match across all three codes used to complete the scale.
- At a minimum, report the initial score documented on presentation at the facility (e.g., by EMT or in the emergency department).
- If only the total score is documented, assign code R40.24-; if multiple scores are captured within the first 24 hours, assign only the code for the admission time score.
- Coma scores reported after admission but less than 24 hours later are not classified by ICD-10-CM.

**Requirements / Properties:**
- Codes cannot be used with R40.2A (Nontraumatic coma due to underlying condition).
- Documentation must include the specific time the scale was recorded to determine the correct 7th character.
- For multiple scores within the first 24 hours, the admission time score is the mandatory selection.
- Total score documentation alone requires the specific R40.24- code assignment.
- Clinician documentation must follow Section I.B.14 guidelines if not provided by the patient's provider.

**Deprecated in this version:**
- Using coma scale codes with R40.2A.
- Reporting coma scores occurring after admission but before 24 hours as valid ICD-10-CM classifications.
- Assigning multiple coma scale codes for scores captured within the first 24 hours of admission.
- Sequencing coma scale codes before the primary diagnosis code.
- Failing to ensure the 7th character matches across all three codes in the scale.

**New in this version:**
- Explicit requirement to sequence coma scale codes after the diagnosis code(s).
- Mandatory use of the 7th character to indicate the timing of the scale recording.
- Specific instruction to assign R40.24- when only the total score is available.
- Clarification that initial presentation scores (EMT/ED) are the minimum reporting requirement.
- Reference to Section I.B.14 for non-provider clinician documentation protocols.
