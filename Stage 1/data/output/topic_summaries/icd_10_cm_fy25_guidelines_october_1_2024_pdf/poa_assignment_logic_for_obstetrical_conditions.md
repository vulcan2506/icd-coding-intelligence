# POA Assignment Logic for Obstetrical Conditions
*Source: ICD-10-CM FY25 Guidelines October 1, 2024.pdf*

**Feature:** POA Assignment Logic for Obstetrical Conditions

**Key Behaviors:**
- Whether or not the patient delivers during the current hospitalization does not affect assignment of the POA indicator.
- The determining factor for POA assignment is whether the pregnancy complication or obstetrical condition described by the code was present at the time of admission or not.
- If the pregnancy complication or obstetrical condition was present on admission (e.g., patient admitted in preterm labor), assign 'Y'.
- If the pregnancy complication or obstetrical condition was not present on admission (e.g., 2nd degree laceration during delivery, postpartum hemorrhage that occurred during current hospitalization, fetal distress develops after admission), assign 'N'.
- If the obstetrical code includes more than one diagnosis and any of the diagnoses identified by the code were not present on admission assign 'N'.

**Requirements / Properties:**
- The coder must determine if the specific pregnancy complication or obstetrical condition was present at the time of admission.
- If multiple diagnoses are included in a single obstetrical code, the presence of any condition not present on admission mandates an 'N' assignment.
- Delivery status during hospitalization is irrelevant to the POA indicator assignment.
