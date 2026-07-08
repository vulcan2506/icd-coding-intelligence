# ICD-10-CM CKD Classification Logic
*Source: ICD-10-CM FY25 Guidelines October 1, 2024.pdf*

**Feature:** ICD-10-CM CKD Classification Logic

**Key Behaviors:**
- The word 'and' in titles should be interpreted to mean either 'and' or 'or' when classifying cases.
- CKD severity is designated by stages 1-5, with specific codes assigned for mild (Stage 2), moderate (Stage 3), and severe (Stage 4) CKD.
- Code N18.6 (End stage renal disease) is assigned when the provider documents ESRD.
- If both a stage of CKD and ESRD are documented, assign code N18.6 only.
- Cases involving multiple anatomical sites (e.g., bones and joints) are classified to a single subcategory if applicable.

**Requirements / Properties:**
- Provider must document the specific stage of CKD (1-5) or explicitly document End Stage Renal Disease (ESRD).
- When ESRD is documented alongside a CKD stage, the CKD stage code must be suppressed in favor of N18.6.
- Titles containing 'and' must be interpreted flexibly to include 'or' for accurate classification of multi-site conditions.

**Deprecated in this version:**
- Assigning separate codes for CKD stages when ESRD is also documented.
- Using strict 'and' interpretation in titles that excludes 'or' for multi-site conditions.

**New in this version:**
- Explicit mapping of CKD stages to specific code ranges: N18.2 for mild, N18.30-N18.32 for moderate, and N18.4 for severe.
- Mandatory assignment of N18.6 as the sole code when ESRD is documented, overriding any concurrent CKD stage codes.
