# External Cause Code Exemption Logic
*Source: ICD-10-CM FY25 Guidelines October 1, 2024.pdf*

**Feature:** External Cause Code Exemption Logic

**Key Behaviors:**
- No external cause code from Chapter 20 is needed if the external cause and intent are included in a code from another chapter
- Codes such as T36.0X1- (Poisoning by penicillins, accidental) inherently include the external cause and intent
- Redundant external cause codes should not be assigned when the information is already captured in the primary code

**Requirements / Properties:**
- The external cause and intent must be explicitly included within the code from another chapter to qualify for exemption
- The primary code must be from a chapter other than Chapter 20 to trigger the exemption logic

**Deprecated in this version:**
- Assigning separate external cause codes when the intent and cause are already specified in the primary diagnosis code

**New in this version:**
- Recognition of specific codes like T36.0X1- as self-contained units that obviate the need for additional Chapter 20 codes
