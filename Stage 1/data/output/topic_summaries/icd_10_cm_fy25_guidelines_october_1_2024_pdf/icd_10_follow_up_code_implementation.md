# ICD-10 Follow-Up Code Implementation
*Source: ICD-10-CM FY25 Guidelines October 1, 2024.pdf*

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
- Follow-up codes must be sequenced before the associated history code.

**Deprecated in this version:**
- Using follow-up codes for ongoing care of a healing condition.
- Using follow-up codes for sequelae of an injury.
- Using follow-up codes for subsequent encounters.
- Using aftercare codes to explain completed treatment surveillance.
- Sequencing history codes before follow-up codes.

**New in this version:**
- Z08 Encounter for follow-up examination after completed treatment for malignant neoplasm.
- Z09 Encounter for follow-up examination after completed treatment for conditions other than malignant neoplasm.
- Mandatory sequencing of follow-up code first, then history code.
- Requirement to replace follow-up code with active diagnosis code upon recurrence.
- Explicit distinction required between follow-up codes and aftercare/subsequent encounter codes.
