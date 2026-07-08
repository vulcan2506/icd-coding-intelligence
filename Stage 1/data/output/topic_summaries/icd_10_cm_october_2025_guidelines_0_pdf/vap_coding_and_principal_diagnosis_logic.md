# VAP Coding and Principal Diagnosis Logic
*Source: icd_10_cm_october_2025_guidelines_0.pdf*

**Feature:** VAP Coding and Principal Diagnosis Logic

**Key Behaviors:**
- Principal diagnosis is assigned the pneumonia code (J12-J18) diagnosed at admission if the patient is admitted with pneumonia.
- Ventilator associated pneumonia (J95.851) is assigned as an additional diagnosis only if documented by the provider.
- The presence of VAP does not override the admission diagnosis if the patient was admitted for a different type of pneumonia.

**Requirements / Properties:**
- Provider must document the presence of ventilator associated pneumonia for code J95.851 to be valid.
- Admission diagnosis must be confirmed as pneumonia (categories J12-J18) at the time of admission.
