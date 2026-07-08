# ICD-10 POA Reporting Logic
*Source: ICD-10-CM FY25 Guidelines October 1, 2024.pdf*

**Feature:** ICD-10 POA Reporting Logic

**Key Behaviors:**
- Leave the 'present on admission' field blank if the condition is on the 'Exempt from Reporting' list.
- Assign 'Y' for conditions explicitly documented as present on admission, diagnosed prior to admission, or present before admission but diagnosed during admission.
- Assign 'N' for conditions explicitly documented as not present at the time of admission.
- Assign 'U' when documentation is unclear regarding presence on admission, or 'W' when it cannot be clinically determined.
- Assign 'Y' or 'N' based on whether signs/symptoms for possible/probable/suspected diagnoses were present at admission.
- Assign 'Y' for conditions that develop during an outpatient encounter prior to a written order for inpatient admission.
- Assign 'Y' for a single code identifying both a chronic condition and an acute exacerbation if the code contains multiple clinical concepts.

**Requirements / Properties:**
- The 'present on admission' field must be left blank only for conditions on the official 'Exempt from Reporting' list.
- Assignments of 'Y', 'N', 'U', or 'W' must be strictly based on explicit provider documentation or clinical determination of presence at the time of admission.
- The 'U' code should not be routinely assigned and is reserved for very limited circumstances where documentation is unclear.
- For conditions diagnosed during admission, 'Y' is required only if they were clearly present before admission occurred.
- For possible, probable, suspected, or rule out diagnoses, assignment depends on whether the underlying signs/symptoms were present at admission.
- Coders are encouraged to query providers when documentation is unclear regarding presence on admission.
- The 'U' flag must be used only in very limited circumstances where documentation is unclear.
