# Project Documentation: Data Anonymization & Privacy Compliance Framework

## 1. Executive Summary
**Context:** This document establishes the privacy framework used to de-identify high-PII (Personally Identifiable Information) marketing data from a Canadian professional event. 

**Objective:** To transform a raw operational dataset into a safe, research-ready portfolio asset. The primary goal was to ensure absolute data privacy while maintaining internal data structure and analytical utility for downstream visualization.

---

## 2. Regulatory Alignment: PIPEDA & Privacy by Design
This framework was engineered in strict accordance with the **Personal Information Protection and Electronic Documents Act (PIPEDA)**, Canada's federal private-sector privacy law. 

I implemented a **Privacy by Design** methodology, ensuring that data protection was embedded automatically into the data preparation lifecycle rather than treated as a post-processing afterthought.

### Core Privacy Controls Applied:
* **Limiting Disclosure & Retention (Principle 5):** Direct identifiers were entirely removed from the environment, mitigating data leak risks.
* **Safeguards (Principle 7):** Processing was executed completely within a closed local environment, preventing un-scrubbed citizen data from interacting with public clouds or external servers.

---

## 3. The Human-AI Anonymization Workflow
To accelerate development while ensuring programmatic accuracy, I paired with an AI collaborator using **Prompt Engineering** to design an anti-recursion data mapping loop.

### The AI Prompt Strategy
Standard find-and-replace loops run into a "recursive error" where characters inside newly injected fake names get targeted by subsequent replacement loops, destroying the text structure. To solve this, I engineered a specific contextual prompt:

> **System Prompt:** *"I am anonymizing a CRM dataset using Python and Pandas. The `custom_fields` column contains a messy string of nested PII. I have an array of synthetic names (e.g., 'Kendall Roy'). Write a Python function using `pd.notna()` that maps and replaces real emails, first names, and last names with synthetic variables simultaneously. The script must sort the replacement mapping keys by length in reverse order to ensure full names are replaced before partial strings, preventing recursive character looping."*

---

## 4. Technical Implementation
The programmatic pipeline has been completely decoupled from this documentation to maintain a clean presentation layer. 

The fully automated pipeline scales the logic to the entire dataset using a vectorization approach, maintaining structural dimensions while ensuring 0% true PII exposure.

* **Core Script:** The full ETL pipeline script can be reviewed in [`anonymization_pipeline.py`](./anonymization_pipeline.py).
* **Key Technique:** Vectorized mapping using Pandas `.apply()` and anti-recursive dictionary sorting.

---

## 5. Anonymization Data Dictionary

| Tabular Column | Transformation Type | Post-Scrub State / Format | Analytical Purpose |
| :--- | :--- | :--- | :--- |
| **First / Last Name** | Complete Substitution | Synthetic Personas | Categorization & Counting |
| **Email / Phone** | Masked / Synthetic | `name@fictional-corp.com` / `416-555-XXXX` | Format Validation Testing |
| **City / Province** | Generalization | Canadian Hubs (e.g., `Toronto`, `ON`) | Geographic Trend Analysis |
| **custom_fields** | Re-serialization | Anonymized CRM Metadata String | Operational System Simulation |
