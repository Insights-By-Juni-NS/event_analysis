# Operational Event Attendee Dataset Overview

## 1. Context & Dataset Origin
This directory contains the core dataset utilized for the event analytics and marketing automation lifecycle. 

The data asset is a **replicated, synthesized, and structurally mapped version** of a real-world enterprise CRM export managed during my previous professional tenure as a Data-Driven Marketing Specialist. To maintain absolute corporate data confidentiality while displaying data architecture competencies, the dataset was completely rebuilt from scratch using realistic operational frameworks. 

* **The Problem with the Raw Export:** Critical operational variables were locked in unstructured string cells, rendering standard filtering, sorting, or ingestion impossible.
* **The Transformed State:** This core repository hosts a clean, fully unbundled relational database ready for downstream Business Intelligence (BI) visualization and lead scoring workflows.

---

## 2. Repository Directory Map
To audit the data pipeline lifecycle, navigate through the components below in sequential order:

1. 📊 **[Dataset Overview (Current File)](./README.md)**: The structural entry point, business objectives, and final data dictionary.
2. 📝 **[Data Preparation Deep-Dive](./data_preparation_overview.md)**: Detailed technical documentation covering the replication logic, Regex pattern design, and human-AI workflows.
3. 🐍 **[Programmatic Pipeline Script](./anonymization_pipeline.py)**: The production Python code executing the automated extraction, mapping, and re-serialization loops.
4. 📄 **[Raw Nested Data Export](./raw_nested_data.csv)**: The initial flat-file CRM export containing the unstructured, nested text strings.
5. 🗃️ **[Cleaned Relational Database](./cleaned_nested_data.csv)**: The final, production-ready dataset optimized for downstream BI tools and marketing automation.
---

## 3. Core Business Objectives
This dataset was engineered to resolve two specific cross-functional operational bottlenecks:

1. **Personalized Marketing Reach:** Unbundling individual attendee contact points to migrate the marketing department from targeting only the "Primary B2B Payer" to driving personalized, individual "Know Before You Go" event lifecycle campaigns.
2. **Onsite Operational Efficiency:** Eliminating manual data cross-referencing to feed clean, structured tabular data directly to badge-printing hardware, reducing onsite check-in database troubleshooting errors by an estimated 95%.

---

## 4. Post-Extraction Data Dictionary
Following the programmatic extraction and structural preparation, the final schema contains **13 operational dimensions** optimized for relational reporting:

| Field Name | Data Type | Structural Source | Downstream Analytical Utility |
| :--- | :--- | :--- | :--- |
| **First Name** | String | Extracted / Tabular | Onsite Badge Generation / Personalization |
| **Last Name** | String | Extracted / Tabular | Onsite Badge Generation / Personalization |
| **Email** | String | Extracted / Tabular | Unique Lead Identification / Active Outreach |
| **Company Name** | String | Extracted / Tabular | Firmographic Account Ingestion & Tier-Scoring |
| **Company Type** | Categorical | Extracted via Regex | B2B Account Segmentation (e.g., Agency vs. Tech) |
| **Job Title** | String | Extracted via Regex | Persona-Based Content Mapping |
| **Job Position** | Categorical | Extracted via Regex | Executive Seniority Trend Aggregation |
| **Phone** | String | Generated / Tabular | System Format Validation Testing |
| **Address** | String | Generated / Tabular | Regional Demographics Verification |
| **City** | String | Generated / Tabular | Regional Marketing Hub Clustering |
| **State / Province** | Categorical | Generated / Tabular | Canadian Provincial Market Penetration Reporting |
| **Postal Code** | String | Generated / Tabular | Geographic Proximity Ingestion |
| **Country** | String | Standardized | Global Market Partitioning |
