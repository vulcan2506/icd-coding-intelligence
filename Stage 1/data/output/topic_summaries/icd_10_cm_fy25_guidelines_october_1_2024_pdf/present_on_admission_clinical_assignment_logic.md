# Present on Admission Clinical Assignment Logic
*Source: ICD-10-CM FY25 Guidelines October 1, 2024.pdf*

**Feature:** Present on Admission Clinical Assignment Logic

**Key Behaviors:**
- Assign 'N' if at least one clinical concept in the code was not present on admission.
- Assign 'Y' if all clinical concepts in the code were present on admission.
- Assign 'Y' for infection codes with causal organisms if infection signs were present on admission, even if culture results are pending.

**Requirements / Properties:**
- Clinical documentation must clearly distinguish between conditions present on admission and those developing after admission.
- For infection codes, documentation of the causal organism must be linked to signs present on admission to justify 'Y' assignment.
- All clinical concepts within a single code must be evaluated collectively to determine the 'Y' or 'N' status.
