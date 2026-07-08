# ICD-10 Combination Code Implementation
*Source: ICD-10-CM FY25 Guidelines October 1, 2024.pdf*

**Feature:** ICD-10 Combination Code Implementation

**Key Behaviors:**
- Assign combination codes that identify both the definitive diagnosis and common symptoms without assigning an additional code for the symptom.
- For categories T36-T65, assign combination codes that include the substance taken and the intent, eliminating the need for additional external cause codes.

**Requirements / Properties:**
- The combination code must explicitly identify the definitive diagnosis.
- The combination code must explicitly identify the common symptoms associated with that diagnosis.
- No additional code should be assigned for symptoms already included in the combination code.
- For poisonings and toxic effects in categories T36-T65, the code must include both the substance and the intent.

**Deprecated in this version:**
- Assigning an additional code for symptoms when a combination code is available.
- Assigning separate external cause codes for poisonings, toxic effects, adverse effects, and underdosing when a combination code in categories T36-T65 is used.

**New in this version:**
- Mandatory use of combination codes for categories T36-T65 to capture substance and intent in a single code.
