# October 1, 2024 → October 2025 — Feature Evolution Report

Constructive value-add narratives, synthesized from delta_analyzer.py's already-extracted profiles and classified deltas. Reversals/contradictions, no-change/unrelated pairs, deprecations, and purely administrative edits are intentionally excluded here; see version_delta_report.md for those.

## Summary

| # | Feature | Change Type |
|---|---------|-------------|
| 1 | **Code Assignment and Diagnosis Exception Logic** | Scope Expansion |
| 2 | **G89 Pain Classification Guidelines** | Definition Revision |
| 3 | **Postoperative Pain Coding Guidelines** | Coding Rule Clarification |
| 4 | **Sepsis Coding Sequencing Rules** | Coding Rule Clarification |
| 5 | **Severe Sepsis Coding Guidelines** | Coding Rule Clarification |
| 6 | **Hypertensive Disease Coding Guidelines** | Scope Expansion |
| 7 | **HIV Disease Coding Logic** | Coding Rule Clarification |
| 8 | **HIV Admission Diagnosis Coding Guidelines** | Scope Expansion |
| 9 | **ICD-10 Combination Code Implementation** | Scope Expansion |
| 10 | **ICD-10 Status Code Definitions** | Coding Rule Clarification |
| 11 | **ICD-10-CM Prophylactic Surgery Coding** | Scope Expansion |
| 12 | **ICD-10-CM Myocardial Infarction Coding Guidelines** | Coding Rule Clarification |
| 13 | **ICD-10-CM Code Specificity Requirements** | Coding Rule Clarification |
| 14 | **ICD-10 Chapter 19 Character Requirements** | Coding Rule Clarification |
| 15 | **FY 2025 ICD-10-CM Coding Guidelines** | Coding Rule Clarification |
| 16 | **COVID-19 Diagnosis Coding Guidelines** | Definition Revision |
| 17 | **COVID-19 Follow-Up Evaluation Coding** | Scope Expansion |
| 18 | **External Cause Code Usage Restrictions** | Coding Rule Clarification |
| 19 | **Y38 Terrorism Secondary Effects Coding** | Coding Rule Clarification |
| 20 | **Code O80 Assignment Guidelines** | Coding Rule Clarification |
| 21 | **Newborn Birth Episode Coding** | Coding Rule Clarification |
| 22 | **Primary Malignancy Coding Guidelines** | Scope Expansion |
| 23 | **HIV Medication and Status Coding** | Scope Expansion |
| 24 | **Z Code Usage and Specificity** | Coding Rule Clarification |
| 25 | **Z28 Underimmunization Code Mapping** | Scope Expansion |
| 26 | **Counseling Z Code Mapping Updates** | Coding Rule Clarification |
| 27 | **Inpatient Z-Code Classification Guidelines** | Scope Expansion |

---

## Feature Knowledge Cards

### 1. Code Assignment and Diagnosis Exception Logic
**Location:** ICD-10-CM Coding Guidelines → Clinical Coding Guidelines  
**Appears in:** October 1, 2024 → October 2025  
**Change type:** Scope Expansion

**Foundation (October 1, 2024):** The October 1, 2024 version established that code assignment relies on the provider's diagnostic statement while allowing exceptions for specific metrics like BMI and pressure ulcer stage to be documented by non-provider clinicians.

**Value added (October 2025):**
- Expansion of the exception scope to explicitly include laterality and firearm injury intent codes alongside existing metrics.
- Clarification that the associated diagnosis for the newly added laterality and firearm injury intent exceptions must be documented by the patient's provider.
- Refinement of conflict resolution protocols to explicitly cover conflicting documentation from both the same and different clinicians.

**Narrative:** The October 1, 2024 version introduced a framework where provider statements suffice for diagnosis assignment, with limited exceptions for non-provider documentation. The October 2025 update builds on this by broadening the list of assignable exceptions to include laterality and firearm injury intent, while reinforcing the requirement for provider-documented associated diagnoses for these new categories.

*Traceability: Chunk `27_41` (October 1, 2024) vs Chunk `459_473` (October 2025)*

---

### 2. G89 Pain Classification Guidelines
**Location:** ICD-10-CM Coding Guidelines → Pain Coding and Classification  
**Appears in:** October 1, 2024 → October 2025  
**Change type:** Definition Revision

**Foundation (October 1, 2024):** The October 1, 2024 guideline established general rules for G89 usage, including exclusions for psychological disorders and requirements for acute/chronic specification.

**Value added (October 2025):**
- Explicitly implements the classification of chronic pain under subcategory G89.2.
- Removes specific time-frame requirements, mandating selection based solely on provider documentation.
- Clarifies that the encounter reason must be pain control/management, not management of the underlying condition, if an underlying diagnosis is known.

**Narrative:** The October 1, 2024 guideline introduced general rules for G89 usage without specific subcategory definitions for chronic pain. The October 2025 version builds on this by explicitly classifying chronic pain under subcategory G89.2 and removing time-frame constraints, enabling coders to rely solely on provider documentation for accurate classification.

*Traceability: Chunk `139_148_150` (October 1, 2024) vs Chunk `569_578_580_583` (October 2025)*

---

### 3. Postoperative Pain Coding Guidelines
**Location:** ICD-10-CM Coding Guidelines → Pain Coding and Classification  
**Appears in:** October 1, 2024 → October 2025  
**Change type:** Coding Rule Clarification

**Foundation (October 1, 2024):** The October 1, 2024 guidelines established that postoperative pain must be documented by the provider and assigned to category G89 unless associated with a specific complication.

**Value added (October 2025):**
- Explicit direction to assign complication-associated pain to Chapter 19 codes, illustrated by the example of painful wire sutures.
- Mandatory requirement to use additional G89.18 or G89.28 codes to specify the acute or chronic nature of pain when a complication is present.
- Alignment with Section III and Section IV guidelines for reporting additional diagnoses in the outpatient setting.

**Narrative:** The October 1, 2024 guidelines introduced the rule that pain associated with complications should use complication codes without specifying the chapter. The October 2025 update builds on this by explicitly directing coders to Chapter 19 and requiring specific G89 sub-codes to define pain acuity, enabling more precise clinical documentation and compliance.

*Traceability: Chunk `152_153` (October 1, 2024) vs Chunk `582` (October 2025)*

---

### 4. Sepsis Coding Sequencing Rules
**Location:** ICD-10-CM Coding Guidelines → Sepsis and Burn Coding Guidelines  
**Appears in:** October 1, 2024 → October 2025  
**Change type:** Coding Rule Clarification

**Foundation (October 1, 2024):** The October 1, 2024 guidelines established that underlying systemic infections must be sequenced first when severe sepsis is present on admission and meets the principal diagnosis definition.

**Value added (October 2025):**
- Explicit mandate to use code T81.44 for sepsis following a procedure, clarifying the specific sequencing component previously omitted.
- Introduction of a specific principal diagnosis rule requiring code D59.31 for infection-associated hemolytic-uremic syndrome with severe sepsis.
- Refinement of postprocedural wound infection sequencing to explicitly pair site-specific codes with the new T81.44 sepsis code.
- Clarification that non-infectious conditions leading to infection should be sequenced first only if they meet the principal diagnosis definition.

**Narrative:** The October 1, 2024 guidelines introduced the foundational rule that underlying infections must be sequenced first for severe sepsis meeting principal diagnosis criteria. The October 2025 version builds on this by explicitly mandating code T81.44 for postprocedural sepsis and establishing D59.31 as the principal diagnosis for hemolytic-uremic syndrome, enabling precise capture of complex clinical scenarios.

*Traceability: Chunk `67_70_72` (October 1, 2024) vs Chunk `495_498_500` (October 2025)*

---

### 5. Severe Sepsis Coding Guidelines
**Location:** ICD-10-CM Coding Guidelines → Sepsis and Burn Coding Guidelines  
**Appears in:** October 1, 2024 → October 2025  
**Change type:** Coding Rule Clarification

**Foundation (October 1, 2024):** The October 1, 2024 guidelines established that severe sepsis codes require explicit documentation of the condition or associated acute organ dysfunction alongside an underlying systemic infection.

**Value added (October 2025):**
- Retained the mandatory requirement for a minimum of two codes: one for the underlying systemic infection and one from subcategory R65.2.
- Maintained the instruction to assign code A41.9 when the causal organism is not documented.
- Generalized specific query triggers for negative blood cultures and 'urosepsis' into a broader directive to query providers when the case complexity requires clarification.

**Narrative:** The October 1, 2024 version introduced strict, specific criteria for querying providers regarding negative blood cultures and the term 'urosepsis'. The October 2025 update builds on this foundation by consolidating these specific triggers into a single, generalized instruction to query for case complexity, enabling a more streamlined approach to handling ambiguous documentation while preserving core coding requirements.

*Traceability: Chunk `64_65` (October 1, 2024) vs Chunk `493` (October 2025)*

---

### 6. Hypertensive Disease Coding Guidelines
**Location:** ICD-10-CM Coding Guidelines → Chronic Disease Coding Guidelines  
**Appears in:** October 1, 2024 → October 2025  
**Change type:** Scope Expansion

**Foundation (October 1, 2024):** The October 1, 2024 guidelines established the assignment of I10-I15 codes for existing hypertension that is either under control by therapy or uncontrolled.

**Value added (October 2025):**
- Introduction of specific rules for assigning I11 codes when hypertension coexists with heart conditions classified to I50.-, I51.4, I51.89, or I51.9.
- Explicit instruction to omit additional heart condition codes when the condition is classified to I51.5 or I51.7.
- Requirement to code hypertension and heart conditions separately only when the provider documents they are unrelated, sequencing based on admission circumstances.
- New criteria requiring provider documentation of uncertainty or specific conditions (e.g., myocardial degeneration) to determine if additional codes are necessary.

**Narrative:** The October 1, 2024 guidelines introduced a strict framework for coding controlled and uncontrolled hypertension using I10-I15 categories. The October 2025 update builds on this foundation by expanding the scope to explicitly handle complex comorbidities with heart conditions, enabling precise differentiation between cases requiring additional codes versus those subsumed under I11.

*Traceability: Chunk `172_173` (October 1, 2024) vs Chunk `593_600_601` (October 2025)*

---

### 7. HIV Disease Coding Logic
**Location:** ICD-10-CM Coding Guidelines → Respiratory and Infectious Disease Coding  
**Appears in:** October 1, 2024 → October 2025  
**Change type:** Coding Rule Clarification

**Foundation (October 1, 2024):** The October 1, 2024 version established that the sequencing decision is irrelevant to whether a patient is newly diagnosed or has a history of HIV admissions.

**Value added (October 2025):**
- Explicit instruction to code B20 when 'AIDS' or 'HIV disease' is documented.
- Mandatory assignment of B20 if the patient is treated for any HIV-related illness.
- Requirement to code B20 for any condition resulting from HIV positive status.

**Narrative:** The October 1, 2024 version introduced a rule stating that sequencing is irrelevant to a patient's HIV history. The October 2025 update builds on this by defining specific clinical triggers—documentation of AIDS/HIV disease, treatment for related illnesses, or resulting conditions—enabling precise operational logic for assigning the primary HIV code.

*Traceability: Chunk `54` (October 1, 2024) vs Chunk `485` (October 2025)*

---

### 8. HIV Admission Diagnosis Coding Guidelines
**Location:** ICD-10-CM Coding Guidelines → Respiratory and Infectious Disease Coding  
**Appears in:** October 1, 2024 → October 2025  
**Change type:** Scope Expansion

**Foundation (October 1, 2024):** The October 1, 2024 guidelines established that B20 must be assigned as the principal diagnosis only when the admission is specifically for an HIV-related condition, with a specific exception for hemolytic-uremic syndrome.

**Value added (October 2025):**
- Explicit instruction to assign the unrelated condition as the principal diagnosis and B20 as secondary when a patient with HIV is admitted for an unrelated condition.
- New guidance to assign Z21 for asymptomatic HIV infection status when 'HIV positive' is documented without symptoms or HIV-related illness.
- Clarification that sequencing decisions for newly diagnosed HIV disease admissions do not affect the coding of HIV conditions.

**Narrative:** The October 1, 2024 guidelines introduced strict rules for coding HIV-related admissions and specific exceptions for hemolytic-uremic syndrome. The October 2025 version builds on this foundation by expanding the scope to explicitly define rules for unrelated condition admissions and asymptomatic status, enabling accurate principal diagnosis assignment and comprehensive reporting across all HIV encounter types.

*Traceability: Chunk `52` (October 1, 2024) vs Chunk `486` (October 2025)*

---

### 9. ICD-10 Combination Code Implementation
**Location:** Clinical Coding & Compliance → ICD-10-CM Coding Guidelines  
**Appears in:** October 1, 2024 → October 2025  
**Change type:** Scope Expansion

**Foundation (October 1, 2024):** The October 1, 2024 guidelines established prohibitions against assigning additional codes for symptoms covered by combination codes and for external cause codes in categories T36-T65.

**Value added (October 2025):**
- Mandatory assignment of codes from category I13 when hypertension is present with both heart disease and chronic kidney disease.
- Requirement to assign an additional code from category I50 to identify the type of heart failure alongside I13 codes.
- Mandate to use a secondary code from category N18 to identify the stage of chronic kidney disease with I13.
- Specific sequencing rules for acute renal failure and chronic kidney disease codes based on admission circumstances.

**Narrative:** The October 1, 2024 guidelines introduced foundational rules prohibiting redundant symptom and external cause coding. The October 2025 update builds on this by expanding the scope to include mandatory assignment and sequencing rules for hypertensive heart and chronic kidney disease (I13), enabling precise capture of heart failure types and kidney disease stages.

*Traceability: Chunk `275_301` (October 1, 2024) vs Chunk `595_702_728` (October 2025)*

---

### 10. ICD-10 Status Code Definitions
**Location:** Clinical Coding & Compliance → ICD-10-CM Coding Guidelines  
**Appears in:** October 1, 2024 → October 2025  
**Change type:** Coding Rule Clarification

**Foundation (October 1, 2024):** The October 1, 2024 version established that status codes indicate a patient is a carrier, has sequelae, or has prosthetic devices, while distinguishing them from history codes.

**Value added (October 2025):**
- Clarification that genetic carrier status (Z14) specifically indicates carrying a gene that may be passed to offspring, refining the previous general definition.
- Introduction of a specific sequencing rule for genetic susceptibility (Z15) where the current condition is coded first if present, or follow-up is coded first if the condition no longer exists.
- Explicit requirement that status codes must be assigned when a patient is a carrier or has sequelae, even if the condition is not currently active.

**Narrative:** The October 1, 2024 version introduced the core distinction between status codes and history codes regarding disease presence and sequelae. The October 2025 update builds on this by refining the definition of genetic carrier status and adding specific sequencing logic for genetic susceptibility based on current condition status, enabling more precise coding of genetic encounters.

*Traceability: Chunk `344_345_346` (October 1, 2024) vs Chunk `774_775` (October 2025)*

---

### 11. ICD-10-CM Prophylactic Surgery Coding
**Location:** Clinical Coding & Compliance → ICD-10-CM Coding Guidelines  
**Appears in:** October 1, 2024 → October 2025  
**Change type:** Scope Expansion

**Foundation (October 1, 2024):** The October 1, 2024 guideline established that Category Z40 codes serve as the principal or first-listed code for encounters specifically for prophylactic organ removal.

**Value added (October 2025):**
- Explicit expansion of principal code selection to include subcategory Z40.8 for other prophylactic surgeries beyond the general Z40 category.
- Mandatory requirement to assign additional codes for associated risk factors when applicable, rather than just following them with appropriate codes.
- Clarification that removal must be due to risk factors related to malignant neoplasms to justify the coding logic.

**Narrative:** The October 1, 2024 guideline introduced the use of Category Z40 codes for prophylactic organ removal. The October 2025 update builds on this by explicitly including subcategory Z40.8 and mandating additional coding for risk factors, enabling more precise capture of diverse prophylactic scenarios and their underlying genetic or familial drivers.

*Traceability: Chunk `371` (October 1, 2024) vs Chunk `801` (October 2025)*

---

### 12. ICD-10-CM Myocardial Infarction Coding Guidelines
**Location:** Clinical Coding & Compliance → ICD-10-CM Coding Guidelines  
**Appears in:** October 1, 2024 → October 2025  
**Change type:** Coding Rule Clarification

**Foundation (October 1, 2024):** The October 1, 2024 guidelines established that subsequent Type 1 or unspecified AMIs within 4 weeks must use category I22, while Type 2 and Type 4/5 AMIs were restricted to codes I21.A1 and I21.A9 respectively.

**Value added (October 2025):**
- Clarification that Type 2 AMIs described as NSTEMI or STEMI must exclusively use code I21.A1, removing ambiguity about sub-classification.
- Specific prohibition against assigning code I24.89 for demand ischemia in Type 2 AMI scenarios, refining the exclusion criteria.
- Explicit requirement for documentation to specify NSTEMI or STEMI status for Type 2 AMIs to ensure correct coding to I21.A1.

**Narrative:** The October 1, 2024 guidelines introduced the foundational rules for sequencing subsequent AMIs and restricting Type 2/4/5 codes to I21.A1/I21.A9. The October 2025 update builds on this by clarifying that NSTEMI or STEMI descriptions for Type 2 AMIs do not alter the code assignment and by specifically banning I24.89 for demand ischemia, enabling more precise capture of clinical documentation nuances.

*Traceability: Chunk `183_184` (October 1, 2024) vs Chunk `614` (October 2025)*

---

### 13. ICD-10-CM Code Specificity Requirements
**Location:** Clinical Coding & Compliance → ICD-10-CM Coding Guidelines  
**Appears in:** October 1, 2024 → October 2025  
**Change type:** Coding Rule Clarification

**Foundation (October 1, 2024):** The October 1, 2024 guidelines established that diagnosis codes must be reported at their highest level of specificity and invalidated any code not fully expanded to its required character length.

**Value added (October 2025):**
- Explicit prohibition on using categories or subcategories for reporting, mandating only specific codes.
- Reinforced requirement to utilize fourth, fifth, and sixth characters whenever the category allows subdivision.
- Clarification that a code is invalid if it lacks the full number of characters required, including the 7th character when applicable.

**Narrative:** The October 1, 2024 guidelines introduced the core mandate to use codes at the highest level of specificity and to invalidate codes that were not fully expanded. The October 2025 update builds on this by explicitly excluding categories and subcategories from reporting and reinforcing the necessity of using intermediate characters (4th through 6th) whenever subdivision is permitted, enabling stricter validation of claim data accuracy.

*Traceability: Chunk `29` (October 1, 2024) vs Chunk `442_461` (October 2025)*

---

### 14. ICD-10 Chapter 19 Character Requirements
**Location:** Clinical Coding & Compliance → ICD-10-CM Coding Guidelines  
**Appears in:** October 1, 2024 → October 2025  
**Change type:** Coding Rule Clarification

**Foundation (October 1, 2024):** The October 1, 2024 guidelines established that 7th character assignment relies on active treatment status rather than provider encounter history.

**Value added (October 2025):**
- Clarification that the specific type of sequela must be sequenced first, followed by the injury code.
- Explicit requirement for additional 7th character values beyond A, D, and S for traumatic fractures.
- Refinement of Z code usage instructions to specify exclusion for aftercare of injuries or poisonings where 7th characters are provided.

**Narrative:** The October 1, 2024 guidelines introduced the core rule that 7th character assignment depends on active treatment status. The October 2025 update builds on this by clarifying the sequencing logic for sequela codes and expanding character requirements for traumatic fractures, enabling more precise coding of complex injury scenarios.

*Traceability: Chunk `282` (October 1, 2024) vs Chunk `709` (October 2025)*

---

### 15. FY 2025 ICD-10-CM Coding Guidelines
**Location:** Clinical Coding & Compliance → ICD-10-CM Coding Guidelines  
**Appears in:** October 1, 2024 → October 2025  
**Change type:** Coding Rule Clarification

**Foundation (October 1, 2024):** The October 1, 2024 version established that primary malignant neoplasms overlapping contiguous sites must be classified to the .8 'overlapping lesion' subcategory unless specifically indexed elsewhere.

**Value added (October 2025):**
- Explicit definition of 'encounter' to encompass all healthcare settings, including hospital admissions.
- Formalization of guidelines into four distinct sections covering structure, principal diagnosis, additional diagnoses, and outpatient coding.
- Clarification that the combination of overlapping sites must not be specifically indexed elsewhere before using the .8 code, refining sequencing logic.
- Explicit requirement for a joint effort between the healthcare provider and the coder for accurate documentation and code assignment.

**Narrative:** The October 1, 2024 version introduced foundational rules for neoplasm sequencing and histological referencing. The October 2025 version builds on this by structuring guidelines into four specific sections and clarifying key terms like 'encounter' and 'provider', enabling more precise adherence to HIPAA requirements and improved coding accuracy across all healthcare settings.

*Traceability: Chunk `0_2_97` (October 1, 2024) vs Chunk `433_437_525` (October 2025)*

---

### 16. COVID-19 Diagnosis Coding Guidelines
**Location:** Clinical Coding & Compliance → ICD-10 Coding Guidelines and Implementation  
**Appears in:** October 1, 2024 → October 2025  
**Change type:** Definition Revision

**Foundation (October 1, 2024):** The October 1, 2024 version established that assigning code U07.1 required a definitive diagnosis confirmed by a positive test result.

**Value added (October 2025):**
- Removal of the mandatory positive test result requirement, allowing code U07.1 assignment based solely on provider documentation of a confirmed diagnosis.
- Explicit exclusion of terms like 'suspected,' 'possible,' 'probable,' or 'inconclusive' from qualifying for code U07.1, mandating symptom codes instead.
- Clarification that code U07.1 serves as an exception to hospital inpatient guideline Section II, H.

**Narrative:** The October 1, 2024 version introduced a restrictive rule requiring a positive test result to confirm infection and assign code U07.1. The October 2025 version builds on this by decoupling the diagnosis from test results, relying instead on provider documentation while strictly defining uncertainty terms as exclusions, enabling more flexible yet precise coding of confirmed cases.

*Traceability: Chunk `91` (October 1, 2024) vs Chunk `506_517` (October 2025)*

---

### 17. COVID-19 Follow-Up Evaluation Coding
**Location:** Clinical Coding & Compliance → ICD-10 Coding Guidelines and Implementation  
**Appears in:** October 1, 2024 → October 2025  
**Change type:** Scope Expansion

**Foundation (October 1, 2024):** The October 1, 2024 guideline established specific logic for assigning codes Z09 and Z86.16 to follow-up visits after resolved infections, requiring negative test results and the absence of residual symptoms.

**Value added (October 2025):**
- Removal of the specific behavioral rules for post-resolution follow-up evaluations to narrow the scope.
- Elimination of instructions directing cases with residual symptoms to other guideline sections.

**Narrative:** The October 1, 2024 guideline introduced detailed requirements for coding resolved follow-up visits based on symptom status and test results. The October 2025 version builds on this by removing those specific post-resolution instructions, focusing exclusively on the assignment of Z11.52 for screening and preoperative testing.

*Traceability: Chunk `90_92` (October 1, 2024) vs Chunk `516` (October 2025)*

---

### 18. External Cause Code Usage Restrictions
**Location:** Clinical Coding & Reporting Standards → External Cause Coding Guidelines  
**Appears in:** October 1, 2024 → October 2025  
**Change type:** Coding Rule Clarification

**Foundation (October 1, 2024):** The October 1, 2024 guideline established that external cause codes must be assigned as additional codes only and can never serve as the principal diagnosis.

**Value added (October 2025):**
- Retention of the prohibition against using external cause codes as the principal diagnosis.
- Introduction of a mutual exclusivity rule preventing the simultaneous assignment of sequela external cause codes and related current nature of injury codes.
- Clarification of specific interactions between code types to ensure accurate temporal coding of injuries.

**Narrative:** The October 1, 2024 guideline introduced the fundamental rule that external cause codes cannot be principal diagnoses. The October 2025 update builds on this foundation by adding a critical restriction that prohibits using sequela codes alongside current nature of injury codes, enabling more precise temporal coding of injury events.

*Traceability: Chunk `323` (October 1, 2024) vs Chunk `751_763` (October 2025)*

---

### 19. Y38 Terrorism Secondary Effects Coding
**Location:** Clinical Coding & Reporting Standards → Terrorism Injury Coding  
**Appears in:** October 1, 2024 → October 2025  
**Change type:** Coding Rule Clarification

**Foundation (October 1, 2024):** The October 1, 2024 version established general instructions to assign code Y38.9 for conditions occurring subsequent to a terrorist event while excluding those directly caused by the initial act.

**Value added (October 2025):**
- Explicit requirement that the cause of injury must be identified by the Federal Government (FBI) as terrorism to trigger the use of category Y38 codes.
- Mandate to assign Y38 as the first-listed external cause code when terrorism is the identified cause.
- Introduction of a requirement to use an additional code Y92.- for the place of occurrence.
- Clarification that multiple Y38 codes may be assigned if the injury results from more than one mechanism of terrorism.

**Narrative:** The October 1, 2024 version introduced general rules for coding subsequent effects of terrorism without specifying the authority for classification. The October 2025 version builds on this by requiring explicit FBI identification of the cause and enforcing specific sequencing and place-of-occurrence rules, enabling more precise and authoritative external cause reporting.

*Traceability: Chunk `337` (October 1, 2024) vs Chunk `765_767` (October 2025)*

---

### 20. Code O80 Assignment Guidelines
**Location:** Clinical Coding Standards → Obstetric and Perinatal Coding  
**Appears in:** October 1, 2024 → October 2025  
**Change type:** Coding Rule Clarification

**Foundation (October 1, 2024):** The October 1, 2024 guidelines established that Code O80 is assigned for full-term normal deliveries with single healthy infants only when no complications exist antepartum, during delivery, or postpartum.

**Value added (October 2025):**
- Explicit permission to use Code O80 when a prior antepartum complication has resolved before the delivery admission.
- Clarification that Code O80 remains valid if no current complications require Chapter 15 codes, distinguishing between active and resolved conditions.

**Narrative:** The October 1, 2024 guidelines introduced a strict prohibition on using Code O80 if any other Chapter 15 code was needed, implicitly excluding cases with a history of complications. The October 2025 update builds on this by explicitly permitting Code O80 when antepartum complications are resolved prior to admission, enabling more accurate coding of uncomplicated deliveries where previous issues have been managed.

*Traceability: Chunk `238` (October 1, 2024) vs Chunk `667` (October 2025)*

---

### 21. Newborn Birth Episode Coding
**Location:** Clinical Coding Standards → Obstetric and Perinatal Coding  
**Appears in:** October 1, 2024 → October 2025  
**Change type:** Coding Rule Clarification

**Foundation (October 1, 2024):** The October 1, 2024 guidelines established that category Z38 codes serve as the principal diagnosis for newborns at birth and must be excluded for transfers or maternal records.

**Value added (October 2025):**
- Explicit instruction to sequence Chapter 16 codes first when the encounter reason is a perinatal condition.
- Permission to use codes from other chapters alongside Chapter 16 codes to provide more specific detail.
- Clarification that codes for signs and symptoms may be assigned when a definitive diagnosis has not been established.

**Narrative:** The October 1, 2024 guidelines introduced the fundamental rule that Z38 codes are the principal diagnosis for newborns at birth. The October 2025 update builds on this by adding specific sequencing rules for perinatal conditions and allowing additional codes for greater specificity, enabling more accurate documentation of complex newborn encounters.

*Traceability: Chunk `256` (October 1, 2024) vs Chunk `684` (October 2025)*

---

### 22. Primary Malignancy Coding Guidelines
**Location:** Clinical Coding Standards → Neoplasm Coding Guidelines  
**Appears in:** October 1, 2024 → October 2025  
**Change type:** Scope Expansion

**Foundation (October 1, 2024):** The October 1, 2024 guidelines established a binary framework for assigning primary malignancy codes versus Z85 history codes based strictly on whether treatment was completed or the malignancy was excised with no further directed treatment.

**Value added (October 2025):**
- Explicit instruction to code secondary malignant neoplasms to the affected site as the principal diagnosis with Z85 as a secondary code.
- Specific sequencing rules assigning Z51.0, Z51.11, or Z51.12 as the principal diagnosis for encounters chiefly for antineoplastic therapy administration.
- Detailed differentiation in sequencing malignancy codes versus Z51.0 for brachytherapy complications versus external beam therapy complications.

**Narrative:** The October 1, 2024 version introduced a foundational rule distinguishing between active primary malignancies and excised history codes. The October 2025 update builds on this by expanding the scope to explicitly define sequencing for secondary malignancies and detailing specific principal diagnosis assignments for antineoplastic therapy and brachytherapy encounters.

*Traceability: Chunk `100_120` (October 1, 2024) vs Chunk `529_534_547` (October 2025)*

---

### 23. HIV Medication and Status Coding
**Location:** Clinical Coding Standards → ICD-10 Coding Guidelines  
**Appears in:** October 1, 2024 → October 2025  
**Change type:** Scope Expansion

**Foundation (October 1, 2024):** The October 1, 2024 guideline established the assignment of code B20 for documented HIV disease and code Z79.899 for long-term antiretroviral medication use.

**Value added (October 2025):**
- Explicit assignment of code Z21 for asymptomatic HIV status when no HIV disease is documented.
- Introduction of code R75 for encounters with inconclusive HIV serology documentation.
- Establishment of strict sequencing priority for code O98.7 over B20 or Z21 in pregnancy, childbirth, or puerperium cases.
- Addition of code Z11.4 for HIV screening encounters and Z71.7 for counseling during testing.

**Narrative:** The October 1, 2024 guideline introduced a foundational rule for coding documented HIV disease and medication use. The October 2025 version builds on this by expanding the scope to include asymptomatic status, inconclusive serology, and specific sequencing priorities for pregnancy cases, enabling more precise capture of the full spectrum of HIV-related encounters.

*Traceability: Chunk `60` (October 1, 2024) vs Chunk `487_488` (October 2025)*

---

### 24. Z Code Usage and Specificity
**Location:** Clinical Coding Standards → ICD-10 Coding Guidelines  
**Appears in:** October 1, 2024 → October 2025  
**Change type:** Coding Rule Clarification

**Foundation (October 1, 2024):** The October 1, 2024 guidelines established that Z codes are applicable in any healthcare setting and may serve as first-listed or secondary diagnoses based on encounter circumstances.

**Value added (October 2025):**
- Explicit discouragement of non-specific Z code usage in inpatient settings due to redundancy with other codes.
- Limitation of outpatient non-specific Z code use to instances where no further documentation permits more precise coding.
- Mandate to use specific codes for signs, symptoms, or reasons for visit instead of non-specific Z codes.
- Introduction of specific deprecated mappings for administrative examinations to enforce coding precision.

**Narrative:** The October 1, 2024 guidelines introduced general rules allowing Z codes as first-listed or secondary diagnoses based on encounter circumstances. The October 2025 update builds on this by explicitly discouraging non-specific Z codes in inpatient settings and limiting outpatient use to cases where no precise documentation exists, enabling more accurate and specific clinical coding.

*Traceability: Chunk `340` (October 1, 2024) vs Chunk `770_805_806` (October 2025)*

---

### 25. Z28 Underimmunization Code Mapping
**Location:** Clinical Coding Standards → ICD-10 Coding Guidelines  
**Appears in:** October 1, 2024 → October 2025  
**Change type:** Scope Expansion

**Foundation (October 1, 2024):** The October 1, 2024 guideline established that Z28 encounters map to Z29, Z40, and Z41 while strictly excluding Z28.3 from these mappings.

**Value added (October 2025):**
- Expansion of the mapping scope to include Z76.3 encounters for 'border to healthcare facility' and 'patient noncompliance' scenarios.
- Introduction of verification requirements to confirm the source code is either Z28 or Z76.3 before applying target codes.
- Addition of specific subcode exclusions for Z28.3 and Z41.9 to prevent incorrect mappings in the expanded scope.

**Narrative:** The October 1, 2024 guideline introduced a restrictive rule limiting mapping logic exclusively to Z28 encounters with specific exclusions for Z28.3. The October 2025 version builds on this foundation by significantly expanding the scope to include Z76.3 encounters, enabling the capture of additional scenarios like facility borders and noncompliance while enforcing stricter source code verification.

*Traceability: Chunk `372` (October 1, 2024) vs Chunk `802_803` (October 2025)*

---

### 26. Counseling Z Code Mapping Updates
**Location:** Clinical Coding Standards → ICD-10 Coding Guidelines  
**Appears in:** October 1, 2024 → October 2025  
**Change type:** Coding Rule Clarification

**Foundation (October 1, 2024):** The October 1, 2024 version established that counseling Z codes apply when patients receive assistance after illness/injury or support for social problems, while explicitly excluding Z71.84 and Z71.85 from the general category due to their specific high-risk contexts.

**Value added (October 2025):**
- Clarification that the system now distinguishes between general health counseling (Z71) and specific travel risk counseling (Z71.84) to ensure accurate coding for future travel purposes.
- Introduction of a new rule mapping mental health services for victims and perpetrators of abuse to contraception counseling codes, treating them as a unified counseling session.

**Narrative:** The October 1, 2024 version introduced a restrictive rule excluding specific high-risk Z71 codes from general counseling. The October 2025 update builds on this by refining the distinction between general and travel-specific counseling while simultaneously expanding the scope to include mental health services for abuse victims under contraception codes, enabling more precise capture of complex clinical counseling scenarios.

*Traceability: Chunk `363_364` (October 1, 2024) vs Chunk `794_795` (October 2025)*

---

### 27. Inpatient Z-Code Classification Guidelines
**Location:** Clinical Coding Standards → ICD-10 Coding Guidelines  
**Appears in:** October 1, 2024 → October 2025  
**Change type:** Scope Expansion

**Foundation (October 1, 2024):** The October 1, 2024 guidelines established that non-specific Z codes are discouraged in the inpatient setting to prevent redundancy with more precise codes.

**Value added (October 2025):**
- Explicit restriction of specific Z code categories (Z00, Z01, Z02, Z04) from being reported as the principal diagnosis.
- Introduction of exceptions allowing principal diagnosis status when multiple encounters occur on the same day with combined medical records.
- Specific mappings and exceptions for infertility scenarios and pregnancy supervision.
- Clarification that administrative and special examinations without complaints are restricted from principal diagnosis status.

**Narrative:** The October 1, 2024 guidelines introduced a broad discouragement of non-specific Z codes in the inpatient setting to avoid redundancy. The October 2025 update builds on this by explicitly restricting specific Z code categories as principal diagnoses while introducing nuanced exceptions for combined same-day encounters and specific clinical scenarios like infertility and pregnancy supervision.

*Traceability: Chunk `374` (October 1, 2024) vs Chunk `807_808` (October 2025)*

---
