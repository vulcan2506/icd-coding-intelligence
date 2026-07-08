# POA Reporting Exemption Logic
*Source: ICD-10-CM FY25 Guidelines October 1, 2024.pdf*

**Feature:** POA Reporting Exemption Logic

**Key Behaviors:**
- Assign 'Y' (Yes) when the condition is present on admission
- Assign 'N' (No) when the condition is not present on admission
- Assign 'U' (Unknown) when the presence on admission cannot be determined
- Assign 'W' (Clinically undetermined) when the condition is clinically undetermined
- Mark as 'Unreported/Not used' to exempt the condition from POA reporting requirements

**Requirements / Properties:**
- Accurate determination of condition presence at the time of admission is mandatory for valid coding
- Clinically undetermined status requires specific clinical justification for the 'W' assignment
- Exemption status must be explicitly designated to avoid compliance penalties for unreported conditions

**Deprecated in this version:**
- Assigning 'Y' or 'N' without clinical documentation supporting the timing of onset
- Using 'U' or 'W' as a default when admission status is clearly documented
- Failing to distinguish between clinically undetermined and unknown status

**New in this version:**
- Incorporation of 'Unreported/Not used' status to streamline reporting for exempt conditions
- Standardized definitions for 'Clinically undetermined' to reduce ambiguity in coding assignments
