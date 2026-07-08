# POA Reporting Exemption Logic
*Source: icd_10_cm_october_2025_guidelines_0.pdf*

**Feature:** POA Reporting Exemption Logic

**Key Behaviors:**
- Assign 'Y' (Yes) when the condition is present on admission
- Assign 'N' (No) when the condition is not present on admission
- Assign 'U' (Unknown) when the presence on admission cannot be determined
- Assign 'W' (Clinically undetermined) when the condition is clinically undetermined
- Mark as 'Unreported/Not used' to exempt the condition from POA reporting requirements

**Requirements / Properties:**
- Accurate determination of condition presence at the time of admission is mandatory for valid coding
- Clinically undetermined conditions must be explicitly documented as such to justify 'W' assignment
- Exemption status must be clearly indicated to avoid unnecessary POA reporting for specific conditions

**Deprecated in this version:**
- Assigning 'Y' without clinical documentation supporting presence on admission
- Using unspecified codes to bypass POA reporting requirements
- Failing to document 'Unknown' status when presence on admission is unclear

**New in this version:**
- Introduction of 'W' (Clinically undetermined) as a distinct POA indicator for ambiguous cases
- Formal exemption category ('Unreported/Not used') for conditions excluded from POA reporting
