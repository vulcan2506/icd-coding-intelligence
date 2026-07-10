# ICD-10-CM Placeholder Character Implementation
*Source: ICD-10-CM FY25 Guidelines October 1, 2024.pdf*

**Feature:** ICD-10-CM Placeholder Character Implementation

**Key Behaviors:**
- The placeholder character 'X' is utilized at specific code positions to allow for future expansion.
- The 'X' is required at certain codes (e.g., categories T36-T50) to ensure the code is considered valid.
- Failure to use the placeholder 'X' where required renders the code invalid.
- The placeholder 'X' acts as a structural delimiter to ensure the code maintains a consistent seven-character length.
- A consistent seven-character length is critical for automated data processing and sorting algorithms.

**Mandatory Coding Criteria:**
- The placeholder character 'X' must be used in its designated position for codes within categories such as T36-T50.
- A code is only valid if the required placeholder character is present.
