# Z21 HIV Asymptomatic Status Application
*Source: ICD-10-CM FY25 Guidelines October 1, 2024.pdf*

**Feature:** Z21 HIV Asymptomatic Status Application Logic

**Key Behaviors:**
- Apply Z21 code when patient is documented as 'HIV positive', 'known HIV', or 'HIV test positive' without symptoms
- Exclude Z21 if documentation includes 'AIDS' or 'HIV disease' terminology
- Exclude Z21 if patient is treated for any HIV-related illness
- Exclude Z21 if patient has any condition resulting from HIV positive status
- Use B20 code instead of Z21 for cases involving AIDS, HIV disease, or HIV-related conditions

**Requirements / Properties:**
- Clinical documentation must explicitly state HIV positive status without symptom indicators
- Absence of treatment records for HIV-related illnesses is required for Z21 assignment
