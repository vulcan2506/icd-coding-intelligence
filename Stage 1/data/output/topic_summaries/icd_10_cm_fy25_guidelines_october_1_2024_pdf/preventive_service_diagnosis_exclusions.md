# Preventive Service Diagnosis Exclusions
*Source: ICD-10-CM FY25 Guidelines October 1, 2024.pdf*

**Feature:** Preventive Service Diagnosis Exclusions

**Key Behaviors:**
- Excludes Z00 encounters for general examinations from preventive service diagnosis codes
- Excludes Z00.6 encounters from the general examination exclusion rule
- Excludes Z01 encounters for other special examinations from preventive service diagnosis codes
- Excludes Z02 encounters for administrative examinations from preventive service diagnosis codes
- Exclusions apply to principal/first-listed diagnoses unless multiple encounters on the same day have combined medical records

**Requirements / Properties:**
- System must identify principal/first-listed diagnosis codes on claims
- System must detect multiple encounters on the same day to determine if records are combined

**New in this version:**
- Exclusion logic for Z00 series codes (excluding Z00.6)
- Exclusion logic for Z01 series codes
- Exclusion logic for Z02 series codes
