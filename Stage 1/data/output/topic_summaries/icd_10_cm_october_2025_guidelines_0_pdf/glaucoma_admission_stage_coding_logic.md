# Glaucoma Admission Stage Coding Logic
*Source: icd_10_cm_october_2025_guidelines_0.pdf*

**Feature:** Glaucoma Admission Stage Coding Logic

**Key Behaviors:**
- Assign the code for the highest stage of glaucoma documented during the admission if the stage progresses.
- Prioritize the most severe stage over earlier stages when multiple stages are recorded in the same admission.

**Requirements / Properties:**
- Clinical documentation must explicitly state the progression of the glaucoma stage during the hospital stay.
- The highest stage must be clearly identified in the medical record to support the assignment of the corresponding ICD-10-CM code.

**Deprecated in this version:**
- Coding the initial stage of glaucoma if a higher stage is documented during the same admission.
- Assigning a lower stage code when the patient's condition has advanced to a more severe stage.

**New in this version:**
- Mandatory assignment of the highest stage code when stage progression is documented.
