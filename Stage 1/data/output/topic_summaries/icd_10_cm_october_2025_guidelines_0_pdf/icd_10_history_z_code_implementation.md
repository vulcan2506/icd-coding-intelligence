# ICD-10 History Z Code Implementation
*Source: icd_10_cm_october_2025_guidelines_0.pdf*

**Feature:** ICD-10 History Z Code Implementation

**Key Behaviors:**
- Personal history codes explain past medical conditions no longer present but with potential for recurrence requiring monitoring.
- Family history codes are used when a patient has a family member with a disease causing higher risk of contracting it.
- History codes are acceptable on any medical record regardless of the reason for visit.
- The reason for the encounter (e.g., screening) should be sequenced first, with history codes assigned as additional diagnoses.
- History codes may be used in conjunction with follow-up or screening codes to explain the need for a test or procedure.

**Requirements / Properties:**
- Condition must be a past medical history that no longer exists and is not receiving treatment for personal history codes.
- Condition must be a family member's disease causing increased risk for the patient for family history codes.
- Encounter reason (e.g., screening) must be sequenced before the history Z code.
- History codes must be assigned as additional diagnoses, not as the primary reason for visit unless specified.
- Documentation must indicate the potential for recurrence or increased risk to justify the code assignment.

**Deprecated in this version:**
- Using history Z codes as the primary reason for visit when the encounter reason (e.g., screening) is more specific.
- Coding family history without documented evidence of a family member's disease causing increased risk.
- Assigning personal history codes for conditions that are currently active and receiving treatment.
- Omitting history codes when they are relevant to the treatment plan or monitoring needs.
- Using unspecified history codes when specific Z80-Z85 codes are available and applicable.

**New in this version:**
- Explicit categorization of history Z codes into personal (Z80-Z87) and family (Z80-Z85) types.
- Mandatory sequencing of encounter reason before history codes in claim documentation.
- Integration of history codes with follow-up and screening codes to justify diagnostic tests.
- Expanded list of specific Z80-Z85 codes for various diseases and conditions.
- Requirement for documentation to support the potential for recurrence or increased risk.
