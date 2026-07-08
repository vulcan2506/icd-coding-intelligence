# External Cause Code Sequencing Logic
*Source: icd_10_cm_october_2025_guidelines_0.pdf*

**Feature:** External Cause Code Sequencing Logic

**Key Behaviors:**
- Certain external cause codes are combination codes that identify sequential events resulting in an injury, such as a fall which results in striking against an object.
- The combination external cause code used should correspond to the sequence of events regardless of which event caused the most serious injury.
- Place of occurrence, activity, and external cause status codes are sequenced after the main external cause code(s).
- Generally, there should be only one place of occurrence code, one activity code, and one external cause status code assigned to an encounter.
- In rare instances where a new injury occurs during hospitalization, an additional place of occurrence code may be assigned.

**Requirements / Properties:**
- Documentation must clearly identify sequential events leading to an injury to justify the use of combination codes.
- The selected combination code must accurately reflect the chronological sequence of events, not just the severity of the injury.
- Encounters must be limited to one place of occurrence, one activity, and one external cause status code unless a new injury occurs during hospitalization.
- Additional place of occurrence codes are only permitted if a new injury is documented during the hospitalization period.

**Deprecated in this version:**
- Assigning a combination code based solely on the most serious injury rather than the sequence of events.
- Assigning multiple place of occurrence, activity, or external cause status codes for a single injury event without a new injury occurring.

**New in this version:**
- Explicit instruction to prioritize the sequence of events over injury severity when selecting combination external cause codes.
