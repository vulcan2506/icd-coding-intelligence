# Outpatient to Inpatient Principal Diagnosis Selection
*Source: icd_10_cm_october_2025_guidelines_0.pdf*

**Feature:** Outpatient to Inpatient Principal Diagnosis Selection

**Key Behaviors:**
- Assign the complication as the principal diagnosis if the reason for inpatient admission is a complication.
- Assign the reason for the outpatient surgery as the principal diagnosis if no complication or other condition is documented as the reason for admission.
- Assign an unrelated condition as the principal diagnosis if the reason for inpatient admission is a condition unrelated to the surgery.

**Requirements / Properties:**
- Documentation must explicitly identify the reason for the inpatient admission.
- The complication must be documented as the reason for the inpatient admission to be selected as the principal diagnosis.
- The outpatient surgery reason must be the only documented reason for admission if no complication exists.
- The unrelated condition must be clearly documented as the reason for admission.
- The admission must occur at the same hospital where the outpatient surgery was performed.
