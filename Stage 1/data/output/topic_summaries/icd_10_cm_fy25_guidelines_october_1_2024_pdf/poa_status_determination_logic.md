# POA Status Determination Logic
*Source: ICD-10-CM FY25 Guidelines October 1, 2024.pdf*

**Feature:** POA Status Determination Logic

**Key Behaviors:**
- Assign 'Y' when condition is present at the time of inpatient admission
- Assign 'N' when condition is not present at the time of inpatient admission
- Assign 'U' when documentation is insufficient to determine if condition is present on admission
- Assign 'W' when provider is unable to clinically determine whether condition was present on admission or not

**Mandatory Coding Criteria:**
- Condition must be present at the time of inpatient admission to be coded as 'Y'
- Condition must be absent at the time of inpatient admission to be coded as 'N'
- Documentation must be sufficient to determine presence on admission for 'Y' or 'N' assignment
- Clinical determination must be possible by the provider to avoid 'W' assignment
