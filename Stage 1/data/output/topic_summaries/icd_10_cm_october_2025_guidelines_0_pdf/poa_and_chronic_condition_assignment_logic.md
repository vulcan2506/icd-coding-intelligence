# POA and Chronic Condition Assignment Logic
*Source: icd_10_cm_october_2025_guidelines_0.pdf*

**Feature:** POA and Chronic Condition Assignment Logic

**Key Behaviors:**
- Assign 'Y' for acute conditions present at time of admission and 'N' for those not present.
- Assign 'Y' for chronic conditions even if diagnosed after admission.
- Refer to POA guidelines for codes containing multiple clinical concepts.

**Requirements / Properties:**
- Acute conditions must be documented as present at the time of admission to receive 'Y'.
- Chronic conditions require 'Y' assignment regardless of diagnosis timing relative to admission.
- Codes identifying both acute and chronic conditions must follow specific POA guidelines.
