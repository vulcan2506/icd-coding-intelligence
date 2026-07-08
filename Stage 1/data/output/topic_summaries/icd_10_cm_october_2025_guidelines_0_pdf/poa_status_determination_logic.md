# POA Status Determination Logic
*Source: icd_10_cm_october_2025_guidelines_0.pdf*

**Feature:** POA Status Determination Logic

**Key Behaviors:**
- Assign 'Y' when condition is present at the time of inpatient admission
- Assign 'N' when condition is not present at the time of inpatient admission
- Assign 'U' when documentation is insufficient to determine if condition is present on admission
- Assign 'W' when provider is unable to clinically determine whether condition was present on admission or not

**Requirements / Properties:**
- Clinical documentation must explicitly state presence or absence of condition at admission
- Provider clinical judgment is required when documentation is ambiguous
- Insufficient documentation triggers 'U' status rather than defaulting to 'N'
- Provider inability to determine status triggers 'W' status
- Inpatient admission timing is the reference point for status determination
