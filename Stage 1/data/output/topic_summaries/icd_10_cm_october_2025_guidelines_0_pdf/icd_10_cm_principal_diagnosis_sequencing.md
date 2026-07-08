# ICD-10-CM Principal Diagnosis Sequencing
*Source: icd_10_cm_october_2025_guidelines_0.pdf*

**Feature:** Etiology/Manifestation Sequencing and Principal Diagnosis Rules

**Key Behaviors:**
- Underlying etiology conditions must be sequenced first, followed by manifestation codes when a combination exists.
- Codes titled 'in diseases classified elsewhere' are never permitted as first-listed or principal diagnosis codes.
- Alphabetic Index entries listing etiology followed by manifestation codes in brackets indicate the bracketed code must be sequenced second.
- When two or more interrelated conditions meet the definition of principal diagnosis, either may be sequenced first unless specific circumstances indicate otherwise.
- 'Code first' and 'Use additional code' notes serve as sequencing rules for both etiology/manifestation combinations and other specific codes.

**Requirements / Properties:**
- Manifestation codes must be used in conjunction with an underlying condition code and listed following it.
- Clinical documentation must support the existence of an underlying etiology and its specific manifestations.
- The Tabular List or Alphabetic Index must explicitly indicate the sequencing order via instructional notes.
- Admission circumstances and therapy provided must be evaluated to determine if specific conditions override general sequencing rules.
- Codes from categories like F02 (Dementia in other diseases classified elsewhere) must follow the etiology/manifestation convention.
- The 'use additional code' note must be present at the etiology code to validate the sequencing of the etiology/manifestation combination.
- The 'code first' note must be present at the manifestation code to validate the sequencing of the etiology/manifestation combination.

**Deprecated in this version:**
- Using 'in diseases classified elsewhere' codes as the principal diagnosis.
- Sequencing manifestation codes before their underlying etiology codes.
- Ignoring 'Code first' or 'Use additional code' instructional notes in the Tabular List.
- Failing to sequence Alphabetic Index bracketed codes as secondary diagnoses.
- Selecting a principal diagnosis without considering the circumstances of admission or therapy provided.

**New in this version:**
- Explicit requirement to query for clarification if the relationship between etiology and manifestation is not documented.
- Mandatory use of specific Alphabetic Index entry structures to identify etiology/manifestation pairs.
- Expanded application of 'Code first' and 'Use additional code' notes to non-etiology/manifestation combinations.
- Updated guidance on sequencing interrelated conditions based on admission circumstances and therapy.
- Specific examples provided for categories like G20 and F02 to illustrate the convention.
