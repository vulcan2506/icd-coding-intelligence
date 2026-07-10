# Present on Admission Clinical Assignment Logic
*Source: icd_10_cm_october_2025_guidelines_0.pdf*

**Feature:** Present on Admission Clinical Assignment Logic

**Key Behaviors:**
- Assign 'N' if at least one clinical concept in the code was not present on admission.
- Assign 'Y' if all clinical concepts included in the code were present on admission.
- Assign 'Y' for infection codes with causal organisms if infection signs were present on admission, even if culture results are known post-admission.

**Mandatory Coding Criteria:**
- Determine presence of all clinical concepts within the specific code at the time of admission.
- For infection codes, presence of infection signs on admission overrides the timing of culture result availability.
