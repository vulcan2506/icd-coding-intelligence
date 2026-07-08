# ICD-10 POA Reporting Logic
*Source: icd_10_cm_october_2025_guidelines_0.pdf*

**Feature:** ICD-10 POA Reporting Logic

**Key Behaviors:**
- Leave the 'present on admission' field blank if the condition is on the 'Exempt from Reporting' list.
- Assign 'Y' for conditions explicitly documented as present on admission, diagnosed prior to admission, or clearly present before admission.
- Assign 'N' for conditions explicitly documented as not present at the time of admission.
- Assign 'U' when documentation is unclear regarding presence on admission, or 'W' when it cannot be clinically determined.
- Assign 'Y' for possible/probable/suspected diagnoses based on findings present at admission, and 'N' if based on findings not present at admission.
- Assign 'Y' for conditions diagnosed during admission if they were documented as suspected, possible, rule out, differential diagnosis, or underlying cause of a symptom present at admission.
- Assign 'Y' for conditions developing during an outpatient encounter prior to a written order for inpatient admission.

**Requirements / Properties:**
- The 'present on admission' field must be left blank only for conditions on the official 'Exempt from Reporting' list.
- Assignments of 'Y', 'N', 'U', or 'W' must be based strictly on explicit provider documentation or clinical determination of presence at the time of admission.
- The 'U' code should not be routinely assigned and is reserved for limited circumstances where documentation is unclear.
- For conditions diagnosed during admission but clearly present before admission, the assignment must be 'Y'.
- For conditions developing during an outpatient encounter prior to a written order for inpatient admission, the assignment must be 'Y'.
- Coders are encouraged to query providers when documentation is unclear regarding presence on admission.
- The 'U' flag should not be routinely assigned and is reserved for limited circumstances where documentation is unclear.
