# ICD-10 Combination Code Implementation
*Source: icd_10_cm_october_2025_guidelines_0.pdf*

**Feature:** ICD-10 Combination Code Implementation

**Key Behaviors:**
- Assign codes from combination category I13 when hypertension is present with both heart and chronic kidney disease.
- Do not assign additional codes for symptoms included in a combination code.
- Use the appropriate code from category N18 as a secondary code with a code from category I13 to identify the stage of chronic kidney disease.
- Code acute renal failure and chronic kidney disease separately, sequencing according to the circumstances of the admission/encounter.
- No additional external cause code is required for poisonings, toxic effects, adverse effects, and underdosing codes in categories T36-T65.

**Requirements / Properties:**
- Hypertension must be documented with both heart disease and chronic kidney disease to use category I13.
- If heart failure is present, an additional code from category I50 must be assigned to identify the type of heart failure.
- The Includes note at I13 specifies that conditions included at I11 and I12 are included together in I13.
- For patients with both acute renal failure and chronic kidney disease, both conditions must be coded.
- Codes in categories T36-T65 must include the substance taken as well as the intent.

**Deprecated in this version:**
- Assigning codes from I11 or I12 separately when a patient has hypertension, heart disease, and chronic kidney disease.
- Assigning an additional code for the symptom when a combination code identifies both the definitive diagnosis and common symptoms.
- Assigning an additional external cause code for poisonings, toxic effects, adverse effects, and underdosing codes in categories T36-T65.

**New in this version:**
- Category I13 is a combination code that includes hypertension, heart disease, and chronic kidney disease.
- Category N18 codes are used as secondary codes with category I13 to identify the stage of chronic kidney disease.
- Categories T36-T65 are combination codes that include the substance taken as well as the intent.
