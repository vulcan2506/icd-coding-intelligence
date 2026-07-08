# October 1, 2024 → October 2025 — Feature Evolution Report

Constructive value-add narratives, synthesized from delta_analyzer.py's already-extracted profiles and classified deltas. Reversals/contradictions, no-change/unrelated pairs, deprecations, and purely administrative edits are intentionally excluded here; see version_delta_report.md for those.

## Summary

| # | Feature | Change Type |
|---|---------|-------------|
| 1 | **Code Assignment and Diagnosis Exception Logic** | Definition Expansion |
| 2 | **Postoperative Pain Coding Guidelines** | Coding Guideline Clarification |
| 3 | **Severe Sepsis Coding Guidelines** | Coding Guideline Clarification |
| 4 | **Hypertensive Disease Coding Guidelines** | Definition Expansion |
| 5 | **Diabetes Mellitus Coding Guidelines** | Coding Guideline Clarification |
| 6 | **Respiratory Failure Coding Guidelines** | Coding Guideline Clarification |
| 7 | **HIV Disease Coding Logic** | Coding Guideline Clarification |
| 8 | **HIV Admission Diagnosis Coding Guidelines** | Coding Guideline Clarification |
| 9 | **Superficial Injury Coding Exclusion** | Coding Guideline Clarification |
| 10 | **ICD-10 Pain Code Differentiation** | Coding Guideline Clarification |
| 11 | **ICD-10 Combination Code Implementation** | Definition Expansion |
| 12 | **ICD-10 Status Code Definitions** | Coding Guideline Clarification |
| 13 | **ICD-10-CM Prophylactic Surgery Coding** | Coding Guideline Clarification |
| 14 | **Presymptomatic Type 1 Diabetes Coding** | Coding Guideline Clarification |
| 15 | **ICD-10-CM Myocardial Infarction Coding Guidelines** | Coding Guideline Clarification |
| 16 | **ICD-10-CM Coding Syntax Definitions** | Definition Expansion |
| 17 | **ICD-10-CM Principal Diagnosis Sequencing** | Coding Guideline Clarification |
| 18 | **ICD-10-CM Diagnosis Coding Guidelines** | Coding Guideline Clarification |
| 19 | **ICD-10-CM Section 21 Factors and Screening** | Coding Guideline Clarification |
| 20 | **COVID-19 Diagnosis Coding Guidelines** | Coding Guideline Clarification |
| 21 | **ICD-10-CM Bilateral Coding Guidelines** | Coding Guideline Clarification |
| 22 | **Factors Influencing Health Status and Contact** | Coding Guideline Clarification |
| 23 | **External Cause Code Usage Restrictions** | Code Assignment Restriction |
| 24 | **Y38 Terrorism Secondary Effects Coding** | Coding Guideline Clarification |
| 25 | **Code O80 Assignment Guidelines** | Coding Guideline Clarification |
| 26 | **Primary Malignancy Coding Guidelines** | Coding Guideline Clarification |
| 27 | **Extranodal Lymphoma Coding Rules** | Coding Guideline Clarification |
| 28 | **HIV Medication Coding Guidelines** | Coding Guideline Clarification |
| 29 | **Z Code Usage and Specificity Guidelines** | Coding Guideline Clarification |
| 30 | **Z28 Underimmunization Code Mapping** | Definition Expansion |
| 31 | **Z Code Guidelines for Specified Encounters** | Coding Guideline Clarification |
| 32 | **Inpatient Z-Code Classification Guidelines** | Coding Guideline Clarification |
| 33 | **O80 Delivery Code Usage for Z37.0** | Coding Guideline Clarification |

---

## Feature Knowledge Cards

### 1. Code Assignment and Diagnosis Exception Logic
**Location:** ICD-10-CM Coding Guidelines → Clinical Coding Guidelines  
**Appears in:** October 1, 2024 → October 2025  
**Change type:** Definition Expansion

**Foundation (October 1, 2024):** The October 1, 2024 guidelines established that code assignment relies on the provider's diagnostic statement, with exceptions allowing non-provider documentation only for BMI, pressure ulcer stage, and coma scale.

**Value added (October 2025):**
- Explicit inclusion of depth of non-pressure chronic ulcers, laterality, and firearm injury intent as permissible exceptions for non-provider documentation.
- Expansion of the exception list to include Social Determinants of Health (SDOH) and underimmunization status alongside the original metrics.
- Clarification that the requirement for associated diagnoses to be documented by the patient's provider applies strictly to all expanded exception categories.

**Narrative:** The October 1, 2024 guidelines introduced the baseline rule that code assignment relies on the provider's statement, permitting non-provider documentation only for BMI, pressure ulcer stage, and coma scale. The October 2025 update builds on this by explicitly adding depth of non-pressure chronic ulcers, laterality, firearm injury intent, SDOH, and underimmunization status to the list of permissible exceptions. This evolution enables a broader scope of metrics to be assigned based on non-provider documentation while maintaining the strict requirement that associated diagnoses remain documented by the patient's provider.

*Traceability: Chunk `27_41` (October 1, 2024) vs Chunk `459_473` (October 2025)*

---

### 2. Postoperative Pain Coding Guidelines
**Location:** ICD-10-CM Coding Guidelines → Pain Coding and Classification  
**Appears in:** October 1, 2024 → October 2025  
**Change type:** Coding Guideline Clarification

**Foundation (October 1, 2024):** The October 1, 2024 guidelines established that routine postoperative pain should not be coded and that uncomplicated pain belongs in category G89.

**Value added (October 2025):**
- Explicit instruction to assign postoperative pain associated with specific complications to Chapter 19 codes (e.g., for painful wire sutures) rather than category G89.
- Mandatory requirement to use additional codes from category G89 (G89.18 or G89.28) alongside Chapter 19 codes to identify acute or chronic pain status.
- New mandate to query provider documentation for clarification if the pain status (acute vs. chronic) is unspecified.

**Narrative:** The October 1, 2024 guidelines introduced the foundational rule that routine pain is uncodable and uncomplicated pain falls under category G89. The October 2025 update builds on this by explicitly directing coders to Chapter 19 for pain linked to specific complications and requiring additional G89 codes to specify acute or chronic status, enabling more precise differentiation between general postoperative pain and pain resulting from specific procedural injuries.

*Traceability: Chunk `152_153` (October 1, 2024) vs Chunk `582` (October 2025)*

---

### 3. Severe Sepsis Coding Guidelines
**Location:** ICD-10-CM Coding Guidelines → Sepsis and Burn Coding Guidelines  
**Appears in:** October 1, 2024 → October 2025  
**Change type:** Coding Guideline Clarification

**Foundation (October 1, 2024):** The October 1, 2024 guidelines established the requirement for a minimum of two codes (underlying infection and R65.2) and mandated specific provider queries for negative blood cultures and the nonspecific term 'urosepsis'.

**Value added (October 2025):**
- Generalization of provider query mandates to cover any complex case or unclear documentation rather than specific clinical scenarios.
- Explicit reinforcement that documentation must identify both the underlying systemic infection and the associated acute organ dysfunction before code assignment.

**Narrative:** The October 1, 2024 guidelines introduced specific actionable instructions for querying providers regarding negative blood cultures and the term 'urosepsis'. The October 2025 version builds on this by generalizing these instructions into a broader mandate to query providers whenever the case is complex or documentation is unclear, enabling more flexible application of the two-code minimum requirement across diverse clinical contexts.

*Traceability: Chunk `64_65` (October 1, 2024) vs Chunk `493` (October 2025)*

---

### 4. Hypertensive Disease Coding Guidelines
**Location:** ICD-10-CM Coding Guidelines → Chronic Disease Coding Guidelines  
**Appears in:** October 1, 2024 → October 2025  
**Change type:** Definition Expansion

**Foundation (October 1, 2024):** The October 1, 2024 guidelines established the core requirement to assign codes from categories I10-I15 based on whether hypertension is controlled, uncontrolled, untreated, or not responding to therapy.

**Value added (October 2025):**
- Introduction of specific logic for 'Hypertensive Disease Coding with Heart Conditions' to determine when to use category I11 versus separate coding.
- Explicit instruction to sequence codes based on admission circumstances when hypertension and heart conditions are documented as unrelated.
- Granular clinical logic defining when additional codes from I50 or I51 are required versus when they are deprecated for specific heart conditions like I51.5 or I51.7.
- Requirement for providers to document the relationship between hypertension and heart conditions to guide coding decisions.

**Narrative:** The October 1, 2024 guidelines introduced the fundamental distinction between controlled and uncontrolled hypertension using categories I10-I15. The October 2025 update builds on this by expanding the scope to include complex interactions with heart conditions, enabling precise sequencing and accurate code assignment for related versus unrelated comorbidities.

*Traceability: Chunk `172_173` (October 1, 2024) vs Chunk `593_600_601` (October 2025)*

---

### 5. Diabetes Mellitus Coding Guidelines
**Location:** ICD-10-CM Coding Guidelines → Chronic Disease Coding Guidelines  
**Appears in:** October 1, 2024 → October 2025  
**Change type:** Coding Guideline Clarification

**Foundation (October 1, 2024):** The October 1, 2024 guidelines established that diabetes mellitus codes are combination codes including type, body system affected, and complications, sequenced based on the reason for the encounter.

**Value added (October 2025):**
- Explicit requirement to assign Z79.84 for long-term use of oral hypoglycemic drugs.
- Explicit requirement to assign Z79.85 for long-term use of injectable non-insulin antidiabetic drugs.
- Clarification that Z79.4 is excluded for temporary insulin use in type 2 diabetes.
- Mandate to use combination codes that integrate type, system, and complications.
- Guidance to query providers if diabetes type is missing rather than defaulting without documentation.

**Narrative:** The October 1, 2024 guidelines introduced the foundational rules for sequencing diabetes codes and the general assignment of Z79 codes for medication use. The October 2025 update builds on this by explicitly defining requirements for Z79.84 and Z79.85, reducing coder variance and enabling more precise identification of long-term medication regimens.

*Traceability: Chunk `129_132_135` (October 1, 2024) vs Chunk `555_559` (October 2025)*

---

### 6. Respiratory Failure Coding Guidelines
**Location:** ICD-10-CM Coding Guidelines → Respiratory and Infectious Disease Coding  
**Appears in:** October 1, 2024 → October 2025  
**Change type:** Coding Guideline Clarification

**Foundation (October 1, 2024):** The October 1, 2024 guidelines established the general rule for sequencing acute respiratory failure codes (J96.0 or J96.2) as a principal diagnosis when chiefly responsible for admission, while deferring to chapter-specific guidelines.

**Value added (October 2025):**
- Explicit distinction between uncomplicated cases and acute exacerbations in categories J44 and J45.
- Clarification that an acute exacerbation is a worsening of a chronic condition, not equivalent to a superimposed infection.
- Deprecation of coding practices that classify acute exacerbations as simple infections superimposed on chronic conditions.

**Narrative:** The October 1, 2024 guidelines introduced the foundational sequencing rules for acute respiratory failure as a principal diagnosis. The October 2025 update builds on this by adding specific definitions for J44 and J45 exacerbations, explicitly separating worsening chronic conditions from superimposed infections. This evolution reduces coder variance and prevents the misclassification of complex respiratory events.

*Traceability: Chunk `187` (October 1, 2024) vs Chunk `616_617` (October 2025)*

---

### 7. HIV Disease Coding Logic
**Location:** ICD-10-CM Coding Guidelines → Respiratory and Infectious Disease Coding  
**Appears in:** October 1, 2024 → October 2025  
**Change type:** Coding Guideline Clarification

**Foundation (October 1, 2024):** The October 1, 2024 guidelines established that the sequencing decision for HIV coding is independent of whether the patient is newly diagnosed or has had previous admissions or encounters for HIV conditions.

**Value added (October 2025):**
- Explicit operational rule to assign code B20 when 'AIDS' or 'HIV disease' is explicitly documented.
- Requirement to assign code B20 if the patient is treated for any HIV-related illness.
- Requirement to assign code B20 if the patient has any condition resulting from HIV positive status.
- Shift from focusing on the irrelevance of prior admission history to defining specific positive clinical documentation criteria.

**Narrative:** The October 1, 2024 guidelines introduced the foundational principle that sequencing decisions rely solely on current status rather than historical encounter data. The October 2025 update builds on this by defining the specific positive inclusion criteria—such as explicit documentation of 'AIDS', treatment for HIV-related illnesses, or conditions resulting from HIV positive status—enabling precise and actionable code assignment based on clinical evidence.

*Traceability: Chunk `54` (October 1, 2024) vs Chunk `485` (October 2025)*

---

### 8. HIV Admission Diagnosis Coding Guidelines
**Location:** ICD-10-CM Coding Guidelines → Respiratory and Infectious Disease Coding  
**Appears in:** October 1, 2024 → October 2025  
**Change type:** Coding Guideline Clarification

**Foundation (October 1, 2024):** The October 1, 2024 guidelines established the rule to assign B20 as the principal diagnosis for HIV-related condition admissions and specified the exception for hemolytic-uremic syndrome requiring D59.31 followed by B20.

**Value added (October 2025):**
- Mandatory assignment of Z21 for asymptomatic HIV status when only 'HIV positive' is documented without symptoms or illness.
- Explicit clarification that unrelated conditions (e.g., traumatic injury) must be coded as the principal diagnosis with B20 as secondary.
- Guidance that principal diagnosis sequencing is independent of whether the patient is newly diagnosed or has a previous HIV history.
- Requirement to code all reported HIV-related conditions as additional diagnoses when B20 is the principal diagnosis.

**Narrative:** The October 1, 2024 guidelines introduced the core rules for coding HIV-related admissions and the specific exception for hemolytic-uremic syndrome. The October 2025 version builds on this foundation by adding mandatory guidance for asymptomatic status (Z21), clarifying that unrelated conditions take precedence for principal diagnosis, and ensuring sequencing is not influenced by the timing of the HIV diagnosis.

*Traceability: Chunk `52` (October 1, 2024) vs Chunk `486` (October 2025)*

---

### 9. Superficial Injury Coding Exclusion
**Location:** ICD-10-CM Coding Guidelines → Edge Cases & Standalone Topics  
**Appears in:** October 1, 2024 → October 2025  
**Change type:** Coding Guideline Clarification

**Foundation (October 1, 2024):** The October 1, 2024 guidelines established that superficial injuries like abrasions or contusions must be excluded from coding when a more severe injury exists at the same anatomical site.

**Value added (October 2025):**
- Requirement for coders to explicitly identify the presence of the more severe injury before applying the exclusion rule.
- Mandatory review of clinical notes to confirm the severity of the associated injury justifies the exclusion.
- Clarification that the more severe injury's severity must be clinically established to trigger the suppression of superficial codes.

**Narrative:** The October 1, 2024 guidelines introduced the core logic of excluding superficial injury codes when a more severe injury is present at the same site. The October 2025 update builds on this by adding specific procedural requirements for coders to explicitly identify and clinically verify the severity of the more severe injury, enabling a reduction in coder variance through clearer evidentiary standards.

*Traceability: Chunk `284` (October 1, 2024) vs Chunk `711` (October 2025)*

---

### 10. ICD-10 Pain Code Differentiation
**Location:** Clinical Coding & Compliance → ICD-10-CM Coding Guidelines  
**Appears in:** October 1, 2024 → October 2025  
**Change type:** Coding Guideline Clarification

**Foundation (October 1, 2024):** The October 1, 2024 guidelines established the baseline rules for distinguishing Central and Chronic pain syndromes from general pain and assigning codes for device-related pain using Chapter 19 and G89 categories.

**Value added (October 2025):**
- Explicit deprecation of using G89.0 or G89.4 for general 'chronic pain' without specific syndrome documentation.
- Mandatory requirement to query providers for ambiguous documentation to avoid unspecified codes.
- Clarification that 'chronic pain' is not synonymous with 'chronic pain syndrome' for coding purposes.
- Strict enforcement of combining Chapter 19 codes with G89.18 or G89.28 for retained surgical devices.

**Narrative:** The October 1, 2024 guidelines introduced the foundational logic for differentiating specific pain syndromes and device-related pain. The October 2025 update builds on this by adding explicit prohibitions against misclassifying general pain as syndromes and mandating provider queries for ambiguous cases, enabling stricter enforcement and reduced coder variance.

*Traceability: Chunk `154_157_312` (October 1, 2024) vs Chunk `585_740` (October 2025)*

---

### 11. ICD-10 Combination Code Implementation
**Location:** Clinical Coding & Compliance → ICD-10-CM Coding Guidelines  
**Appears in:** October 1, 2024 → October 2025  
**Change type:** Definition Expansion

**Foundation (October 1, 2024):** The October 1, 2024 guidelines established the principle of assigning single combination codes for definitive diagnoses with common symptoms and mandated that T36-T65 poisoning codes include both substance and intent.

**Value added (October 2025):**
- Explicit requirement to assign codes from category I13 when hypertension is present with both heart disease and chronic kidney disease.
- Mandate to use category N18 codes as secondary codes with I13 to identify the stage of chronic kidney disease.
- Instruction to code acute renal failure and chronic kidney disease separately based on admission circumstances.
- Clarification that no additional external cause code is required for poisonings, toxic effects, adverse effects, and underdosing in categories T36-T65.

**Narrative:** The October 1, 2024 guidelines introduced the foundational rule for combining diagnoses and intent within T36-T65 categories. The October 2025 update builds on this by expanding the scope to include specific sequencing rules for hypertensive heart and chronic kidney disease (I13) and clarifying the separate coding of acute versus chronic renal failure, enabling more precise capture of complex comorbidities.

*Traceability: Chunk `275_301` (October 1, 2024) vs Chunk `595_702_728` (October 2025)*

---

### 12. ICD-10 Status Code Definitions
**Location:** Clinical Coding & Compliance → ICD-10-CM Coding Guidelines  
**Appears in:** October 1, 2024 → October 2025  
**Change type:** Coding Guideline Clarification

**Foundation (October 1, 2024):** The October 1, 2024 guidelines established that status codes indicate a patient is a carrier, has sequelae, or has prosthetic devices, and must not be used if the diagnosis code already includes that information.

**Value added (October 2025):**
- Explicit distinction defining 'Genetic carrier' (Z14) as carrying a gene without the disease versus 'Genetic susceptibility' (Z15) as having a gene that increases risk.
- Clarified sequencing hierarchy requiring the current condition or follow-up code to be listed first over genetic susceptibility codes.
- Specific instruction to sequence Chronic respiratory failure followed by Dependence on respirator status for weaning encounters.
- Refined definition of genetic susceptibility to explicitly state it involves a gene increasing the risk of developing a disease.

**Narrative:** The October 1, 2024 guidelines introduced the core definitions for status codes and basic sequencing rules. The October 2025 update builds on this by explicitly differentiating between genetic carriers and those with increased susceptibility, clarifying sequencing hierarchies for genetic counseling, and providing granular definitions to reduce coder variance.

*Traceability: Chunk `344_345_346` (October 1, 2024) vs Chunk `774_775` (October 2025)*

---

### 13. ICD-10-CM Prophylactic Surgery Coding
**Location:** Clinical Coding & Compliance → ICD-10-CM Coding Guidelines  
**Appears in:** October 1, 2024 → October 2025  
**Change type:** Coding Guideline Clarification

**Foundation (October 1, 2024):** The October 1, 2024 guidelines established that category Z40 serves as the principal diagnosis for prophylactic organ removal, with strict prohibitions against using these codes for therapeutic treatment of existing malignancies.

**Value added (October 2025):**
- Explicit inclusion of subcategory Z40.8 as a valid principal diagnosis option alongside Z40.0 for encounters involving other prophylactic surgeries.
- Clarification that Z40.0 is reserved specifically for malignant neoplasm risk factors, while Z40.8 covers other prophylactic procedures.
- Reinforced requirement to distinguish between prophylactic encounters and therapeutic removal of known cancers in the selection of the principal diagnosis.

**Narrative:** The October 1, 2024 guidelines introduced the core rules for assigning Z40 codes for prophylactic organ removal and prohibited their use for therapeutic malignancy treatment. The October 2025 update builds on this foundation by explicitly expanding the principal diagnosis options to include subcategory Z40.8 for other prophylactic surgeries, enabling more precise coding of diverse preventive procedures beyond those related to malignant neoplasms.

*Traceability: Chunk `371` (October 1, 2024) vs Chunk `801` (October 2025)*

---

### 14. Presymptomatic Type 1 Diabetes Coding
**Location:** Clinical Coding & Compliance → ICD-10-CM Coding Guidelines  
**Appears in:** October 1, 2024 → October 2025  
**Change type:** Coding Guideline Clarification

**Foundation (October 1, 2024):** The October 1, 2024 guidelines established that codes E10.A- are assigned for early-stage type 1 diabetes that predates the onset of symptoms.

**Value added (October 2025):**
- Coding is now explicitly restricted to cases where the diagnosis is confirmed before clinical symptoms appear.
- Clinical documentation must explicitly confirm the diagnosis of Type 1 diabetes mellitus prior to symptom onset.
- The condition must be identified as presymptomatic to utilize the E10.A- code series.

**Narrative:** The October 1, 2024 guidelines introduced the rule for assigning E10.A- codes to early-stage type 1 diabetes predating symptoms. The October 2025 update builds on this by adding explicit constraints requiring documentation to confirm the diagnosis prior to symptom onset and mandating that the condition be identified as presymptomatic, enabling more precise prevention of misclassification for symptomatic cases.

*Traceability: Chunk `131` (October 1, 2024) vs Chunk `557` (October 2025)*

---

### 15. ICD-10-CM Myocardial Infarction Coding Guidelines
**Location:** Clinical Coding & Compliance → ICD-10-CM Coding Guidelines  
**Appears in:** October 1, 2024 → October 2025  
**Change type:** Coding Guideline Clarification

**Foundation (October 1, 2024):** The October 1, 2024 guidelines established that category I22 is restricted to subsequent type 1 or unspecified AMIs within 4 weeks, while directing type 2 and type 4/5 AMIs to specific I21.A1 and I21.A9 codes.

**Value added (October 2025):**
- Explicit reinforcement that code I21.A1 must be used for type 2 AMIs even if the documentation describes them as NSTEMI or STEMI.
- Mandatory constraint that codes I21.0-I21.4 are exclusively for type 1 AMIs, preventing misclassification of other types.
- Stricter behavioral constraints to prevent the misclassification of type 2 events by clarifying the specific application of I21.A1.

**Narrative:** The October 1, 2024 guidelines introduced the foundational rule restricting I22 codes to type 1 or unspecified AMIs while assigning specific I21 codes to other types. The October 2025 update builds on this by explicitly mandating I21.A1 for type 2 AMIs regardless of NSTEMI or STEMI descriptions and enforcing exclusive use of I21.0-I21.4 for type 1 AMIs. This evolution enables more precise coding by eliminating ambiguity in assigning specific codes to non-type 1 myocardial infarctions.

*Traceability: Chunk `183_184` (October 1, 2024) vs Chunk `614` (October 2025)*

---

### 16. ICD-10-CM Coding Syntax Definitions
**Location:** Clinical Coding & Compliance → ICD-10-CM Coding Guidelines  
**Appears in:** October 1, 2024 → October 2025  
**Change type:** Definition Expansion

**Foundation (October 1, 2024):** The October 1, 2024 guidelines established rules for syntax symbols like brackets, parentheses, and colons, along with precedence logic for subentries versus nonessential modifiers.

**Value added (October 2025):**
- Explicit definitions for 'Not elsewhere classifiable' and 'Not otherwise specified' abbreviations to clarify their semantic meaning.
- Clarification that 'Not elsewhere classifiable' represents 'other specified' for conditions where a specific code is unavailable.
- Specification that 'Not otherwise specified' is the equivalent of unspecified codes.
- Definition of commas in the Alphabetic Index to denote alternate verbiage, essential or nonessential modifiers, or alternatives for 'and/or'.

**Narrative:** The October 1, 2024 guidelines introduced a comprehensive set of syntax rules for symbols and precedence. The October 2025 update builds on this by explicitly defining specific abbreviations like 'Not elsewhere classifiable' and 'Not otherwise specified', enabling coders to accurately interpret conditions where specific codes are unavailable or unspecified.

*Traceability: Chunk `13` (October 1, 2024) vs Chunk `445` (October 2025)*

---

### 17. ICD-10-CM Principal Diagnosis Sequencing
**Location:** Clinical Coding & Compliance → ICD-10-CM Coding Guidelines  
**Appears in:** October 1, 2024 → October 2025  
**Change type:** Coding Guideline Clarification

**Foundation (October 1, 2024):** The October 1, 2024 guidelines established that underlying etiology conditions must be sequenced first, followed by manifestation codes, relying on instructional notes like 'code first' and 'use additional code' to define the order.

**Value added (October 2025):**
- Mandates a provider query for clarification if the relationship between etiology and manifestation is not explicitly documented in the clinical record.
- Explicitly requires the presence of specific instructional notes at both the etiology and manifestation codes to validate the sequencing combination.
- Provides specific examples for categories like G20 and F02 to illustrate the application of the etiology/manifestation convention.

**Narrative:** The October 1, 2024 guidelines introduced the general rule that underlying etiology codes must precede manifestation codes based on instructional notes. The October 2025 update builds on this by shifting from a descriptive rule to a prescriptive validation process, requiring explicit documentation of the relationship and specific note presence to validate sequencing. This evolution enables more rigorous verification of clinical documentation and reduces ambiguity in coding interrelated conditions.

*Traceability: Chunk `21_384` (October 1, 2024) vs Chunk `453_817` (October 2025)*

---

### 18. ICD-10-CM Diagnosis Coding Guidelines
**Location:** Clinical Coding & Compliance → ICD-10-CM Coding Guidelines  
**Appears in:** October 1, 2024 → October 2025  
**Change type:** Coding Guideline Clarification

**Foundation (October 1, 2024):** The October 1, 2024 version established a comprehensive protocol for borderline diagnosis coding, requiring coders to treat them as confirmed unless a specific index entry exists and mandating provider queries for unclear documentation.

**Value added (October 2025):**
- Removal of specific instructions regarding borderline diagnosis protocols to focus strictly on general hierarchy.
- Elimination of care setting distinctions (inpatient vs. outpatient) previously noted for borderline conditions.
- Streamlined guidance that prioritizes listing the condition chiefly responsible for services first without conditional logic for borderline cases.

**Narrative:** The October 1, 2024 version introduced detailed rules for handling borderline diagnoses, including specific instructions to code them as confirmed and query providers for clarity. The October 2025 version narrows this scope by omitting the specific borderline logic and care setting distinctions, focusing exclusively on the fundamental requirement to list the chief reason for the encounter first.

*Traceability: Chunk `44_409` (October 1, 2024) vs Chunk `842` (October 2025)*

---

### 19. ICD-10-CM Section 21 Factors and Screening
**Location:** Clinical Coding & Compliance → ICD-10-CM Coding Guidelines  
**Appears in:** October 1, 2024 → October 2025  
**Change type:** Coding Guideline Clarification

**Foundation (October 1, 2024):** The October 1, 2024 guidelines established that factors influencing health status and screening codes should only be assigned when they are the reason for the encounter or significantly affect care, with positive screening results requiring a confirmed diagnosis.

**Value added (October 2025):**
- Explicit restriction of screening codes to cases where a specific screening procedure is actually performed, removing ambiguity for asymptomatic patients who did not undergo testing.
- Mandatory requirement for documentation to explicitly state the specific condition being screened for, reducing coder variance in determining encounter intent.
- Clarification that screening codes are deprecated as primary diagnoses for symptomatic encounters, ensuring accurate differentiation between screening and diagnostic evaluations.

**Narrative:** The October 1, 2024 guidelines introduced broad criteria for coding factors and screening based on encounter purpose and confirmed diagnoses. The October 2025 update builds on this by explicitly restricting screening codes to performed procedures and mandating specific documentation of the screened condition, enabling more precise coding and reduced ambiguity in clinical intent.

*Traceability: Chunk `418` (October 1, 2024) vs Chunk `851` (October 2025)*

---

### 20. COVID-19 Diagnosis Coding Guidelines
**Location:** Clinical Coding & Compliance → ICD-10 Coding Guidelines and Implementation  
**Appears in:** October 1, 2024 → October 2025  
**Change type:** Coding Guideline Clarification

**Foundation (October 1, 2024):** The October 1, 2024 guidelines established that a definitive diagnosis was required to assign specific COVID-19 codes, mandating positive test results for asymptomatic individuals and implying a high burden of proof for the U07.1 code.

**Value added (October 2025):**
- Explicit authorization to assign code U07.1 based solely on provider documentation of a confirmed diagnosis without requiring a positive test result.
- Strict definition that terms such as 'suspected', 'possible', 'probable', or 'inconclusive' preclude the use of U07.1, mandating symptom codes instead.
- Clarification that U07.1 serves as an exception to hospital inpatient guideline Section II, H.

**Narrative:** The October 1, 2024 guidelines introduced the requirement for positive testing results to classify asymptomatic individuals and implied reliance on test data for confirmation. The October 2025 version builds on this by removing the mandatory test result requirement for confirmed cases while strictly defining terminology exclusions, enabling coders to assign U07.1 based on provider documentation alone.

*Traceability: Chunk `91` (October 1, 2024) vs Chunk `506_517` (October 2025)*

---

### 21. ICD-10-CM Bilateral Coding Guidelines
**Location:** Clinical Coding & Compliance → Edge Cases & Standalone Topics  
**Appears in:** October 1, 2024 → October 2025  
**Change type:** Coding Guideline Clarification

**Foundation (October 1, 2024):** The October 1, 2024 guidelines established the core behaviors for assigning separate codes for left and right sides, using unspecified codes only when side identification is impossible, and querying providers for conflicting documentation.

**Value added (October 2025):**
- Explicit instruction to base code assignment on medical record documentation from other clinicians if laterality is not documented by the patient's provider.
- Clarification that the bilateral code applies to the first encounter treating a bilateral condition, including specifically for the encounter to treat the first side.
- Refined requirement that the condition must still exist on both sides to assign the bilateral code for the first encounter.

**Narrative:** The October 1, 2024 guidelines introduced the fundamental rules for bilateral coding and the protocol for querying providers regarding conflicting documentation. The October 2025 update builds on this by shifting the resolution of missing laterality to documentation from other clinicians and clarifying that the bilateral code is appropriate for the first encounter treating the first side, enabling more accurate coding when provider-specific records are incomplete.

*Traceability: Chunk `40_126` (October 1, 2024) vs Chunk `472_553` (October 2025)*

---

### 22. Factors Influencing Health Status and Contact
**Location:** Clinical Coding & Compliance → Edge Cases & Standalone Topics  
**Appears in:** October 1, 2024 → October 2025  
**Change type:** Coding Guideline Clarification

**Foundation (October 1, 2024):** The October 1, 2024 guidelines established that factors influencing health status and contact with health services should be coded to describe the reason for the encounter or the patient's current health situation when a more specific diagnosis does not exist.

**Value added (October 2025):**
- Explicit requirement to distinguish between routine monitoring and active intervention for follow-up codes.
- Clarification that follow-up codes indicate monitoring for a condition or treatment outcome rather than just general effects.
- Enhanced specificity in documentation to support the distinction between passive monitoring and active treatment outcomes.

**Narrative:** The October 1, 2024 guidelines introduced general instructions for using follow-up codes to indicate monitoring for conditions or treatment effects. The October 2025 update builds on this by refining the requirement to explicitly distinguish between routine monitoring and active intervention, enabling more precise tracking of patient progress and the nature of the contact with health services.

*Traceability: Chunk `123` (October 1, 2024) vs Chunk `550` (October 2025)*

---

### 23. External Cause Code Usage Restrictions
**Location:** Clinical Coding & Reporting Standards → External Cause Coding Guidelines  
**Appears in:** October 1, 2024 → October 2025  
**Change type:** Code Assignment Restriction

**Foundation (October 1, 2024):** The October 1, 2024 guidelines established the fundamental rule that an external cause code can never be assigned as a principal (first-listed) diagnosis.

**Value added (October 2025):**
- Retention of the prohibition against using external cause codes as principal diagnoses.
- Introduction of a restriction prohibiting the simultaneous use of sequela external cause codes with related current nature of injury codes.
- Prevention of conflicting coding scenarios where a condition is treated as both a current injury and a sequela.

**Narrative:** The October 1, 2024 guidelines introduced the basic constraint that external cause codes cannot serve as principal diagnoses. The October 2025 update builds on this foundation by adding a specific prohibition against pairing sequela external cause codes with related current nature of injury codes, enabling more accurate compliance with coding standards and preventing contradictory injury classifications.

*Traceability: Chunk `323` (October 1, 2024) vs Chunk `751_763` (October 2025)*

---

### 24. Y38 Terrorism Secondary Effects Coding
**Location:** Clinical Coding & Reporting Standards → Terrorism Injury Coding  
**Appears in:** October 1, 2024 → October 2025  
**Change type:** Coding Guideline Clarification

**Foundation (October 1, 2024):** The October 1, 2024 guidelines established the core logic for assigning code Y38.9 to conditions occurring subsequent to a terrorist event while prohibiting its use for injuries directly caused by the initial act.

**Value added (October 2025):**
- Explicit mandate that the Federal Government (FBI) must identify the cause of injury as terrorism before assigning any code from category Y38.
- Requirement to assign the first-listed external cause code from category Y38 when terrorism is confirmed, with additional codes for place of occurrence (Y92.-).
- Clarification that multiple Y38 codes are required if the injury results from more than one mechanism of terrorism.

**Narrative:** The October 1, 2024 guidelines introduced the fundamental distinction between initial act injuries and subsequent secondary effects for terrorism coding. The October 2025 update builds on this by adding the mandatory requirement for Federal Government (FBI) identification of the cause and clarifying sequencing rules, enabling precise differentiation between confirmed terrorist acts and other events while ensuring accurate external cause reporting.

*Traceability: Chunk `337` (October 1, 2024) vs Chunk `765_767` (October 2025)*

---

### 25. Code O80 Assignment Guidelines
**Location:** Clinical Coding Standards → Obstetric and Perinatal Coding  
**Appears in:** October 1, 2024 → October 2025  
**Change type:** Coding Guideline Clarification

**Foundation (October 1, 2024):** The October 1, 2024 guidelines established that Code O80 is assigned for full-term normal deliveries with single healthy infants only when no current complications require Chapter 15 codes.

**Value added (October 2025):**
- Explicit permission to assign Code O80 if a prior antepartum complication has resolved before the admission for delivery.
- Clarification that the absence of current complications includes scenarios where previous conditions have resolved prior to admission.
- Reduction of coder variance regarding the eligibility of O80 when antecedent complications are no longer active.

**Narrative:** The October 1, 2024 guidelines introduced the baseline rule that O80 applies only when no current Chapter 15 complications exist. The October 2025 update builds on this by explicitly permitting O80 assignment when prior antepartum complications have resolved before delivery, enabling more accurate coding for uncomplicated deliveries following resolved conditions.

*Traceability: Chunk `238` (October 1, 2024) vs Chunk `667` (October 2025)*

---

### 26. Primary Malignancy Coding Guidelines
**Location:** Clinical Coding Standards → Neoplasm Coding Guidelines  
**Appears in:** October 1, 2024 → October 2025  
**Change type:** Coding Guideline Clarification

**Foundation (October 1, 2024):** The October 1, 2024 guidelines established the core rule to use primary malignancy codes until treatment is completed if excised but further therapy is directed to that site, while clarifying Z85 usage for eradicated malignancies.

**Value added (October 2025):**
- Explicit instruction to sequence Z51.0, Z51.11, or Z51.12 as the first-listed diagnosis for encounters chiefly for antineoplastic therapy administration.
- Refined distinction for brachytherapy encounters requiring the malignancy code as principal diagnosis while explicitly excluding Z51.0 assignment.
- Guidance on sequencing complications (e.g., nausea, vomiting) as secondary diagnoses following the principal therapy encounter code.
- Clarification that Z85.89 is the specific code for the former site of either a primary or secondary malignancy.

**Narrative:** The October 1, 2024 guidelines introduced the fundamental sequencing rules for primary malignancies and the use of Z85 codes for history. The October 2025 update builds on this by adding specific sequencing mandates for antineoplastic therapy encounters and brachytherapy, enabling precise differentiation between therapy administration and malignancy treatment contexts.

*Traceability: Chunk `100_120` (October 1, 2024) vs Chunk `529_534_547` (October 2025)*

---

### 27. Extranodal Lymphoma Coding Rules
**Location:** Clinical Coding Standards → Neoplasm Coding Guidelines  
**Appears in:** October 1, 2024 → October 2025  
**Change type:** Coding Guideline Clarification

**Foundation (October 1, 2024):** The October 1, 2024 guidelines established the requirement to assign codes from categories C81-C85 with a final character identifying 'extranodal and solid organ sites' when a malignant neoplasm metastasizes beyond lymph nodes.

**Value added (October 2025):**
- Explicit correction of the example code from C83.39 to C83.398 to ensure the mandatory 7th character is applied.
- Clarification that the final character identifying 'extranodal and solid organ sites' is required for all categories C81-C85.
- Refinement of documentation requirements to explicitly confirm the primary diagnosis is a malignant neoplasm of lymphoid tissue.

**Narrative:** The October 1, 2024 guidelines introduced the foundational rule for using final characters for extranodal metastasis but contained an error in the cited example code. The October 2025 update builds on this by correcting the example to C83.398 and clarifying the scope across all C81-C85 categories, enabling coders to accurately reflect the metastatic nature of the condition without ambiguity.

*Traceability: Chunk `127` (October 1, 2024) vs Chunk `554` (October 2025)*

---

### 28. HIV Medication Coding Guidelines
**Location:** Clinical Coding Standards → ICD-10 Coding Guidelines  
**Appears in:** October 1, 2024 → October 2025  
**Change type:** Coding Guideline Clarification

**Foundation (October 1, 2024):** The October 1, 2024 guidelines established the basic rule to assign code B20 for patients with documented HIV disease managed on antiretroviral medications and allowed Z79.899 as an additional code for long-term use.

**Value added (October 2025):**
- Explicit prohibition of assigning Z21 or R75 codes for patients with a prior HIV-related illness diagnosis, ensuring B20 is used exclusively in those cases.
- Introduction of mandatory sequencing priority for Chapter 15 codes (O98.7) over other HIV-related codes in pregnancy, childbirth, and the puerperium contexts.
- Clarification that Z79.899 is a mandatory additional code to identify long-term antiretroviral medication use.
- Specific guidance for coding HIV infection in pregnancy with subcategory O98.7, superseding other HIV-related codes.
- New instructions for assigning code Z71.7 for HIV counseling encounters and R75 for inconclusive serology results.

**Narrative:** The October 1, 2024 guidelines introduced the fundamental criteria for coding HIV disease and long-term medication use. The October 2025 update builds on this foundation by strictly prohibiting conflicting codes like Z21 and R75 for patients with established illness, mandating specific sequencing for pregnancy contexts, and clarifying the mandatory assignment of Z79.899, enabling more precise and compliant documentation of HIV status and treatment.

*Traceability: Chunk `60` (October 1, 2024) vs Chunk `487_488` (October 2025)*

---

### 29. Z Code Usage and Specificity Guidelines
**Location:** Clinical Coding Standards → ICD-10 Coding Guidelines  
**Appears in:** October 1, 2024 → October 2025  
**Change type:** Coding Guideline Clarification

**Foundation (October 1, 2024):** The October 1, 2024 guidelines established that Z codes are applicable in any healthcare setting with position dependent on clinical circumstances, allowing them as first-listed or secondary codes.

**Value added (October 2025):**
- Explicit prohibition of nonspecific Z codes in the inpatient setting when justification is lacking.
- Restriction of outpatient nonspecific Z code use to instances where no further documentation permits more precise coding.
- Mandatory requirement to use specific codes for signs or symptoms instead of nonspecific Z codes.
- Specific code mappings replacing vague administrative codes like Z02.9 with precise alternatives such as Z13.9, Z04.9, and Z41.9.

**Narrative:** The October 1, 2024 guidelines introduced the general rule allowing Z codes in any setting with position dependent on circumstances. The October 2025 update builds on this by explicitly prohibiting nonspecific Z codes in inpatient settings and restricting outpatient use to cases where no further documentation exists, enabling more precise coding and reducing reliance on vague administrative codes.

*Traceability: Chunk `340` (October 1, 2024) vs Chunk `770_805_806` (October 2025)*

---

### 30. Z28 Underimmunization Code Mapping
**Location:** Clinical Coding Standards → ICD-10 Coding Guidelines  
**Appears in:** October 1, 2024 → October 2025  
**Change type:** Definition Expansion

**Foundation (October 1, 2024):** The October 1, 2024 guidelines established explicit mapping rules for Z28 to Z29, Z40, and Z41 based on encounter specifics while requiring the exclusion of Z28.3 for general mappings.

**Value added (October 2025):**
- Expansion of the taxonomy to include explicit mappings for Z76.3 (Healthy person accompanying sick person) to Z76.4, Z76.5, and Z91.1-.
- Addition of a specific mapping rule for Z28 to Z53 for encounters regarding procedures not carried out.
- Clarification of requirements for Z76.3 usage in contexts involving boarder status and noncompliance with medical treatment regimens.

**Narrative:** The October 1, 2024 guidelines introduced the core framework for mapping Z28 codes to prophylactic and procedure-related categories while excluding specific underimmunization statuses. The October 2025 update builds on this foundation by broadening the scope to include related encounter mappings for healthy persons accompanying sick people and procedures not carried out, enabling more comprehensive coding for complex facility and compliance scenarios.

*Traceability: Chunk `372` (October 1, 2024) vs Chunk `802_803` (October 2025)*

---

### 31. Z Code Guidelines for Specified Encounters
**Location:** Clinical Coding Standards → ICD-10 Coding Guidelines  
**Appears in:** October 1, 2024 → October 2025  
**Change type:** Coding Guideline Clarification

**Foundation (October 1, 2024):** The October 1, 2024 guidelines established that Z codes identify reasons for encounters not related to disease or injury and must be selected based on the specific purpose documented in the medical record.

**Value added (October 2025):**
- Clarification that Z codes may be used as the principal diagnosis when the encounter is solely for the specified circumstance.
- Explicit deprecation of using Z codes to mask a primary disease diagnosis.
- Mandatory requirement for enhanced specificity in Z code selection for preventive care encounters.
- Requirement that clinical documentation must clearly support the reason for the encounter without underlying disease.

**Narrative:** The October 1, 2024 guidelines introduced the general principle that Z codes identify non-disease-related encounter reasons. The October 2025 update builds on this by clarifying that Z codes can serve as the principal diagnosis for sole-purpose encounters while explicitly preventing the masking of underlying conditions, enabling more accurate coding of preventive care and reducing ambiguity in documentation requirements.

*Traceability: Chunk `339` (October 1, 2024) vs Chunk `769` (October 2025)*

---

### 32. Inpatient Z-Code Classification Guidelines
**Location:** Clinical Coding Standards → ICD-10 Coding Guidelines  
**Appears in:** October 1, 2024 → October 2025  
**Change type:** Coding Guideline Clarification

**Foundation (October 1, 2024):** The October 1, 2024 guidelines established that Z codes are generally restricted in the inpatient setting to instances where no further documentation permits more precise coding.

**Value added (October 2025):**
- Explicit requirement that Z codes may only be reported as the principal diagnosis unless medical records for multiple encounters on the same day are combined.
- Introduction of granular mapping rules for infertility and pregnancy-related Z codes (e.g., Z31.81) based on specific clinical contexts like assisted reproductive procedures.
- Mandatory exclusion of Z00.6 from the general rule allowing Z codes as principal diagnoses for general examinations.
- Clarification that administrative examinations (Z02) and examinations for other reasons (Z04) follow standard principal diagnosis reporting rules.
- Specific documentation requirements for elective termination of pregnancy (Z33.2) to justify its use as a principal diagnosis.

**Narrative:** The October 1, 2024 guidelines introduced a broad restriction on non-specific Z code use in the inpatient setting. The October 2025 update builds on this by defining precise operational conditions, such as requiring combined same-day encounters for non-principal reporting and introducing detailed mapping for infertility and pregnancy codes, enabling more accurate and context-specific coding.

*Traceability: Chunk `374` (October 1, 2024) vs Chunk `807_808` (October 2025)*

---

### 33. O80 Delivery Code Usage for Z37.0
**Location:** Clinical Coding Standards → ICD-10 Coding Guidelines  
**Appears in:** October 1, 2024 → October 2025  
**Change type:** Coding Guideline Clarification

**Foundation (October 1, 2024):** The October 1, 2024 guidelines established that Z37.0 is the only appropriate outcome code for use with O80, while prohibiting other Z37 codes from being paired with it.

**Value added (October 2025):**
- Explicit reinforcement of the mandatory restriction requiring O80 to be paired exclusively with Z37.0.
- Clarification that unspecified delivery outcome codes are now explicitly included in the list of deprecated pairings with O80.

**Narrative:** The October 1, 2024 guidelines introduced the core restriction that Z37.0 is the sole valid outcome for O80, deprecating other Z37 codes. The October 2025 update builds on this by emphasizing the mandatory nature of this exclusive pairing and explicitly expanding the prohibition to include unspecified delivery outcome codes, thereby refining the scope of prohibited combinations.

*Traceability: Chunk `240` (October 1, 2024) vs Chunk `668` (October 2025)*

---
