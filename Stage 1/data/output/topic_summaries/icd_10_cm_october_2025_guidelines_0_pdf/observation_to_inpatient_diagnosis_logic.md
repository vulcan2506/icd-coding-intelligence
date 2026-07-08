# Observation to Inpatient Diagnosis Logic
*Source: icd_10_cm_october_2025_guidelines_0.pdf*

**Feature:** Observation to Inpatient Diagnosis Logic

**Key Behaviors:**
- When a patient is admitted to an observation unit for a medical condition, which either worsens or does not improve, and is subsequently admitted as an inpatient of the same hospital for this same medical condition, the principal diagnosis would be the medical condition which led to the hospital admission.

**Requirements / Properties:**
- The patient must be admitted to an observation unit for a specific medical condition.
- The condition must either worsen or fail to improve during the observation period.
- The patient must be subsequently admitted as an inpatient to the same hospital.
- The inpatient admission must be for the same medical condition that led to the observation admission.
