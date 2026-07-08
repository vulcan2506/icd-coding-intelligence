# ICD-10-CM Diagnosis Code Assignment Logic
*Source: icd_10_cm_october_2025_guidelines_0.pdf*

**Feature:** ICD-10-CM Diagnosis Code Assignment Logic for Multiple Conditions

**Key Behaviors:**
- Assign 'Y' if all conditions represented by the single ICD-10-CM code were present on admission.
- Assign 'N' if any of the conditions represented by the single ICD-10-CM code was not present on admission.

**Requirements / Properties:**
- The logic applies when the same ICD-10-CM diagnosis code is used for two or more conditions during the same encounter.
- The determination of 'Y' or 'N' depends strictly on whether the conditions were present at the time of admission.
- Examples include bilateral unspecified age-related cataracts (Y) versus traumatic secondary and recurrent hemorrhage where only one condition was present on admission (N).
