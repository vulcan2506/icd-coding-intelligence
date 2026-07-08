# Congenital Anomaly Exemption Logic
*Source: icd_10_cm_october_2025_guidelines_0.pdf*

**Feature:** Congenital Anomaly Exemption Logic

**Key Behaviors:**
- Assign 'Y' for congenital conditions and anomalies except for categories Q00Q99
- Categories Q00Q99 (Congenital anomalies) are on the exempt list and do not receive 'Y' assignment
- Congenital conditions are always considered present on admission

**Requirements / Properties:**
- The condition must be a congenital anomaly or condition to be evaluated for 'Y' assignment
- The specific ICD-10-CM category must not fall within Q00Q99 to be eligible for 'Y' assignment
