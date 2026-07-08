# Pregnancy Complication Diagnosis Sequencing
*Source: icd_10_cm_october_2025_guidelines_0.pdf*

**Feature:** Pregnancy Complication Diagnosis Sequencing

**Key Behaviors:**
- In episodes without delivery, sequence the principal complication necessitating the encounter first.
- If multiple complications are treated or monitored, any may be sequenced first.
- When delivery occurs, sequence the condition prompting admission as principal diagnosis.
- For cesarean delivery, select the condition resulting in the procedure as principal if it prompted admission.
- If admission reason is unrelated to cesarean indication, sequence the admission reason condition first.

**Requirements / Properties:**
- Documentation must identify the specific complication necessitating the encounter in non-delivery episodes.
- Clinical records must confirm multiple complications were treated or monitored to allow flexible sequencing.
- Admission notes must clearly link the condition to the delivery event for obstetric patients.
- Cesarean procedure documentation must specify if the indication was the admission reason or unrelated.
- Provider queries are required if the relationship between admission reason and delivery outcome is unclear.

**Deprecated in this version:**
- Sequencing delivery codes as principal diagnosis when no delivery occurred.
- Ignoring the admission reason when multiple conditions prompted the encounter.
- Coding all complications as additional diagnoses regardless of treatment status.
- Selecting unrelated conditions as principal diagnosis in cesarean cases without clinical justification.
- Failing to distinguish between admission reasons and delivery indications in sequencing logic.

**New in this version:**
- Explicit rule for sequencing when multiple complications are treated or monitored.
- Clarification on prioritizing admission reason over delivery indication in cesarean cases.
- Mandatory consideration of treatment status for complication sequencing in non-delivery episodes.
- Updated guidance on handling unrelated admission reasons in obstetric admissions.
- Enhanced documentation requirements for distinguishing cesarean indications from admission reasons.
