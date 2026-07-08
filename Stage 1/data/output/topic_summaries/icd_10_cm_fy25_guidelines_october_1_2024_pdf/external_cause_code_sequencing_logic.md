# External Cause Code Sequencing Logic
*Source: ICD-10-CM FY25 Guidelines October 1, 2024.pdf*

**Feature:** External Cause Code Sequencing Logic

**Key Behaviors:**
- Certain external cause codes are combination codes that identify sequential events resulting in an injury, such as a fall which results in striking against an object.
- The combination external cause code used should correspond to the sequence of events regardless of which event caused the most serious injury.
- Place of occurrence, activity, and external cause status codes are sequenced after the main external cause code(s).
- Generally, there should be only one place of occurrence code, one activity code, and one external cause status code assigned to an encounter.
- In rare instances where a new injury occurs during hospitalization, an additional place of occurrence code may be assigned.

**Requirements / Properties:**
- Documentation must clearly identify the sequence of events leading to the injury to select the appropriate combination code.
- The selected combination code must reflect the chronological order of events, not the severity of the resulting injury.
- Only one place of occurrence, activity, and external cause status code should be assigned per encounter unless a new injury occurs during hospitalization.

**Deprecated in this version:**
- Assigning multiple place of occurrence, activity, or external cause status codes for a single injury event without a new injury occurring.
- Selecting a combination code based on the severity of the injury rather than the sequence of events.

**New in this version:**
- Explicit instruction to prioritize the sequence of events over injury severity when selecting combination external cause codes.
