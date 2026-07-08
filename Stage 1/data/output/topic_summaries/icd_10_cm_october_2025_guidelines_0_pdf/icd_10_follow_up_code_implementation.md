# ICD-10 Follow-Up Code Implementation
*Source: icd_10_cm_october_2025_guidelines_0.pdf*

**Feature:** ICD-10 Follow-Up Code Implementation

**Key Behaviors:**
- Follow-up codes imply the condition has been fully treated and no longer exists.
- Follow-up codes should not be confused with aftercare codes or subsequent encounter codes.
- Follow-up codes may be used in conjunction with history codes to provide the full picture of the healed condition.
- The follow-up code is sequenced first, followed by the history code.
- If a condition recurs on a follow-up visit, the diagnosis code for the condition replaces the follow-up code.

**Requirements / Properties:**
- Documentation must indicate the condition has been fully treated and no longer exists.
- The encounter must be for continuing surveillance following completed treatment.
- History codes must be present to describe the healed condition when used with follow-up codes.
- Recurrence of the condition invalidates the use of the follow-up code for that visit.
- Follow-up codes must be sequenced before any associated history codes.

**Deprecated in this version:**
- Using follow-up codes for ongoing care of a healing condition.
- Using follow-up codes for sequelae of an injury.
- Using follow-up codes when the condition has not been fully treated.
- Using follow-up codes for subsequent encounters of injury codes.
- Sequencing history codes before follow-up codes.

**New in this version:**
- Use of Z08 for follow-up examination after completed treatment for malignant neoplasm.
- Use of Z09 for follow-up examination after completed treatment for conditions other than malignant neoplasm.
- Mandatory sequencing of Z08/Z09 before associated history codes.
- Requirement to replace Z08/Z09 with specific disease codes if recurrence is documented.
- Explicit distinction between follow-up codes and aftercare codes in coding guidelines.
