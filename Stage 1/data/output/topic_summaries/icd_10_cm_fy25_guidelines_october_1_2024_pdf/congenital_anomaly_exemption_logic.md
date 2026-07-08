# Congenital Anomaly Exemption Logic
*Source: ICD-10-CM FY25 Guidelines October 1, 2024.pdf*

**Feature:** Congenital Anomaly Exemption Logic

**Key Behaviors:**
- Assign 'Y' for congenital conditions and anomalies except for categories Q00-Q99
- Categories Q00-Q99 are on the exempt list and do not receive 'Y' assignment
- Congenital conditions are always considered present on admission

**Requirements / Properties:**
- The condition must be a congenital anomaly to be evaluated for exemption logic
- The specific ICD-10-CM category must be outside the Q00-Q99 range to be coded with 'Y'
