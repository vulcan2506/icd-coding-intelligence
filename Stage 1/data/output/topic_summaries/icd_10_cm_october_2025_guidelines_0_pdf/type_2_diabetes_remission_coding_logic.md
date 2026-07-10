# Type 2 Diabetes Remission Coding Logic
*Source: icd_10_cm_october_2025_guidelines_0.pdf*

**Feature:** Type 2 Diabetes Remission Coding Logic

**Key Behaviors:**
- Assign code E11.A only when provider documentation explicitly confirms the diabetes mellitus is in remission
- Query the provider if documentation is unclear regarding whether Type 2 diabetes mellitus has achieved remission
- Do not assign remission code if documentation uses the term 'resolved' as it is not synonymous with remission
- Ensure specific condition code assignment is contingent upon confirmed remission status in the medical record
- Avoid assigning codes for conditions that have fully resolved before the encounter began (general rule application)

**Mandatory Coding Criteria:**
- Provider documentation must explicitly state the condition is in remission
- Documentation must distinguish between 'resolved' and 'remission' states
- Clinician query is required when remission status is ambiguous in the record
