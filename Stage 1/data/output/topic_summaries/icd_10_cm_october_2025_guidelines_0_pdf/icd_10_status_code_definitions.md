# ICD-10 Status Code Definitions
*Source: icd_10_cm_october_2025_guidelines_0.pdf*

**Feature:** ICD-10 Status Code Definitions and Application

**Key Behaviors:**
- Status codes indicate a patient is a carrier of a disease or has sequelae/residuals of a past condition, including prosthetic devices.
- Status codes are distinct from history codes, which indicate the patient no longer has the condition.
- Status codes should not be used with diagnosis codes from body system chapters if the diagnosis code already includes the status information.
- For encounters involving weaning from a mechanical ventilator, assign Chronic respiratory failure followed by Dependence on respirator status.
- Genetic susceptibility codes (Z15) generally should not be used as principal or first-listed codes unless the patient has the condition or is being seen for follow-up after treatment.

**Requirements / Properties:**
- Status codes must be assigned when the patient carries a gene associated with a disease that may be passed to offspring.
- Status codes must be assigned when the patient has sequelae or residuals of a past disease or condition.
- Status codes must be assigned for the presence of prosthetic or mechanical devices resulting from past treatment.
- When a status code is assigned, it must not duplicate information already provided by a specific diagnosis code from a body system chapter.
- For genetic susceptibility encounters, sequencing rules require the current condition or follow-up code to be listed first over the susceptibility code.

**Deprecated in this version:**
- Using status codes in conjunction with diagnosis codes from body system chapters when the diagnosis code already encompasses the status information.
- Assigning genetic susceptibility codes (Z15) as principal or first-listed codes when the patient has the actual condition or is in follow-up after treatment.
- Failing to distinguish between status codes (current carrier/residual) and history codes (no longer has condition).

**New in this version:**
- Explicit definition of status codes covering carriers, sequelae, residuals, and prosthetic devices.
- Specific instruction to sequence Chronic respiratory failure (J96.1) followed by Dependence on respirator status (Z99.11) for weaning encounters.
- Clarified sequencing hierarchy for genetic susceptibility (Z15) versus current conditions and genetic counseling encounters (Z31.5).
- Genetic carrier status (Z14) is defined as carrying a gene associated with a disease that may be passed to offspring, where the person does not currently have the disease.
- Genetic susceptibility (Z15) is defined as having a gene that increases the risk of developing a disease.
- For genetic counseling encounters (Z31.5), this code must be assigned as the first-listed code followed by a code from category Z15.
