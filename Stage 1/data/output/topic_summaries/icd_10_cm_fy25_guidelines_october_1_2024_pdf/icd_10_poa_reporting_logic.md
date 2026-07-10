# ICD-10 POA Reporting Logic
*Source: ICD-10-CM FY25 Guidelines October 1, 2024.pdf*

**Feature:** ICD-10 POA Reporting Logic

**Key Behaviors:**
- Leave the 'present on admission' field blank if the condition is on the exempt list.
- Assign 'Y' for conditions explicitly documented as present on admission or diagnosed prior to admission.
- Assign 'N' for conditions explicitly documented as not present at the time of admission.
- Assign 'U' when documentation is unclear regarding presence on admission.
- Assign 'W' when it cannot be clinically determined whether the condition was present on admission.
- Assign 'Y' for conditions diagnosed during the admission that were clearly present but not diagnosed until after admission occurred.
- Assign 'Y' for conditions that develop during an outpatient encounter prior to a written order for inpatient admission.

**Mandatory Coding Criteria:**
- Condition must not be on the 'Exempt from Reporting' list to require a POA indicator.
- Provider must explicitly document presence or absence of the condition for 'Y' or 'N' assignment.
- Diagnosis must be based on signs, symptoms, or clinical findings present at the time of inpatient admission to assign 'Y' for uncertain diagnoses.
- Query the provider when documentation is unclear to avoid routine assignment of 'U'.
- For single codes identifying both chronic condition and acute exacerbation, follow specific POA guidelines for multiple clinical concepts.
- Condition must be based on signs, symptoms, or clinical findings present at the time of inpatient admission to assign 'Y' for uncertain diagnoses.
- Coders are encouraged to query the provider when documentation is unclear regarding presence on admission.
