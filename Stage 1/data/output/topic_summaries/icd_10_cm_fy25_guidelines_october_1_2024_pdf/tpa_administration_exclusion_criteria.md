# tPA Administration Exclusion Criteria
*Source: ICD-10-CM FY25 Guidelines October 1, 2024.pdf*

**Feature:** tPA Administration Exclusion Criteria

**Key Behaviors:**
- Excludes claims with diagnosis code Z92.82 (Status post administration of tPA)
- Applies exclusion only if the prior tPA administration occurred in a different facility
- Requires the prior administration to have happened within the last 24 hours prior to admission
- Prevents double billing or duplicate treatment claims for recent tPA administrations
- Validates facility identity to ensure the exclusion applies only to cross-facility transfers

**Requirements / Properties:**
- Diagnosis code Z92.82 must be present on the claim
- Timestamp of prior tPA administration must be within 24 hours of current admission
- Facility ID of prior administration must differ from current facility ID
