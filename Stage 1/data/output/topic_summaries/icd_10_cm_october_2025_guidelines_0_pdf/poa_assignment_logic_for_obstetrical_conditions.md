# POA Assignment Logic for Obstetrical Conditions
*Source: icd_10_cm_october_2025_guidelines_0.pdf*

**Feature:** POA Assignment Logic for Obstetrical Conditions

**Key Behaviors:**
- Whether or not the patient delivers during the current hospitalization does not affect assignment of the POA indicator.
- The determining factor for POA assignment is whether the pregnancy complication or obstetrical condition described by the code was present at the time of admission or not.
- If the pregnancy complication or obstetrical condition was present on admission, assign 'Y'.
- If the pregnancy complication or obstetrical condition was not present on admission, assign 'N'.
- If the obstetrical code includes more than one diagnosis and any of the diagnoses identified by the code were not present on admission, assign 'N'.
- Examples of conditions assigned 'N' include 2nd degree laceration during delivery, postpartum hemorrhage occurring during the current hospitalization, and fetal distress developing after admission.
- Examples of conditions assigned 'Y' include patients admitted in preterm labor.

**Mandatory Coding Criteria:**
- Assign 'Y' if the pregnancy complication or obstetrical condition was present on admission.
- Assign 'N' if the pregnancy complication or obstetrical condition was not present on admission.
- Assign 'N' if any diagnosis within a multi-diagnosis obstetrical code was not present on admission.
