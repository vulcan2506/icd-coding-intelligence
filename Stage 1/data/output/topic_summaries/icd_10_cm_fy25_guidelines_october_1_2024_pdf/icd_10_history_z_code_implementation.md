# ICD-10 History Z Code Implementation
*Source: ICD-10-CM FY25 Guidelines October 1, 2024.pdf*

**Feature:** ICD-10 History Z Code Implementation

**Key Behaviors:**
- Personal history codes explain past medical conditions no longer present but with potential for recurrence requiring monitoring.
- Family history codes are used when a patient has a family member with a disease causing higher risk of contracting it.
- History codes are acceptable on any medical record regardless of the reason for visit.
- The reason for the encounter (e.g., screening) should be sequenced first, with history codes assigned as additional diagnoses.
- History codes may be used in conjunction with follow-up or screening codes to explain the need for a test or procedure.
- Personal history codes may be used in conjunction with follow-up codes to explain the need for a test or procedure.
- Family history codes may be used in conjunction with screening codes to explain the need for a test or procedure.

**Requirements / Properties:**
- The condition must be a past medical history that no longer exists and is not receiving active treatment.
- The condition must have the potential for recurrence to justify the use of a personal history code.
- The patient must have a family member with a specific disease to justify the use of a family history code.
- The reason for the encounter must be documented to determine the primary sequencing order.
- The history code must be relevant to the current clinical context or monitoring needs.
- The condition must not be receiving any treatment to qualify for a personal history code.

**Deprecated in this version:**
- Coding history Z codes as the primary reason for the encounter when a specific reason (e.g., screening) exists.
- Using history codes for conditions that are currently active and receiving treatment.
- Assigning unspecified history codes without clear documentation of the specific past or familial condition.
- Placing history codes before the reason for the encounter in the sequence of diagnosis.
- Using family history codes when there is no documented familial link to the specific disease.

**New in this version:**
- Explicit categorization of Z codes into 'Personal History' (Z80-Z87) and 'Family History' (Z80-Z87) subgroups.
- Mandatory sequencing rule requiring the reason for encounter to be listed before history codes.
- Requirement to document the specific disease or condition for both personal and family history codes.
- Guidance on using history codes in conjunction with follow-up and screening codes to justify procedures.
- Inclusion of specific Z code ranges for family history of primary malignant neoplasms and other specific disorders.
- Specific mapping examples showing Family history of primary malignant neoplasm (Z80) paired with Family history of mental and behavioral disorders (Z81), certain disabilities (Z82), and other specific disorders (Z83).
