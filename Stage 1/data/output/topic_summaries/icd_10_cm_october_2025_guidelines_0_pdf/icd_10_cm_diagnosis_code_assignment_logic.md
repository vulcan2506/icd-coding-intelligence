# ICD-10-CM Diagnosis Code Assignment Logic
*Source: icd_10_cm_october_2025_guidelines_0.pdf*

**Feature:** ICD-10-CM Diagnosis Code Assignment Logic for Multiple Conditions

**Key Behaviors:**
- Assign 'Y' if all conditions represented by the single ICD-10-CM code were present on admission.
- Assign 'N' if any of the conditions represented by the single ICD-10-CM code was not present on admission.

**Mandatory Coding Criteria:**
- The same ICD-10-CM diagnosis code must apply to two or more conditions during the same encounter.
- The presence or absence of conditions on admission must be determined for each condition represented by the code.
