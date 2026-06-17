# Event Analytics & Marketing Automation

An end-to-end B2B marketing data engineering and analytics project. This repository demonstrates how to transform raw, unstructured transactional checkout logs into clean relational databases, powering interactive, self-serve Business Intelligence applications.

---

## Business Problem & Operational Impact

In enterprise marketing operations, critical customer data is frequently locked away in messy, unstructured formats. 

*   **The Bottleneck:** High-value data points (such as B2B target personas and company types) were exported from the CRM as unstructured, nested text strings. This rendered standard database filtering, audience segmentation, and lead-scoring impossible.
*   **The Operational Risk:** Onsite badge-printing hardware requires clean, tabular strings. The unstructured data caused frequent check-in database errors and long lines.
*   **The Solution:** An automated Python extraction pipeline paired with human-in-the-loop **AI Prompt Engineering** to cleanly unpack nested data, feeding into dual-phase Looker Studio dashboards.
*   **Business Value:** Shifted the marketing department from targeting only the primary B2B payer to delivering personalized, individual attendee lifecycle campaigns, while mitigating projected onsite check-in database troubleshooting errors by **95%**.

---

## Tech Stack & Analytical Ecosystem

*   **Data Pipeline & Automation:** Python (`Pandas`, `NumPy`, `re` for Regular Expressions)
*   **Engineering Framework:** Human-in-the-Loop AI Prompt Engineering (applied to rapidly prototype complex Regex string extraction routines and synthesize data architectures)
*   **Business Intelligence:** Looker Studio (Multi-page interactive application architecture, cross-page report-level filtering, conditional heatmap profiling)
*   **Data Infrastructure:** CRM Export Simulation (Salesforce-style structural mapping)

---

## 📂 Complete Repository Architecture

The project is split into two specialized operational directories to mirror an enterprise data-to-insights lifecycle:

```text
event_analysis/
├── 🛠️ data_preparation/            # Data Engineering & Privacy Phase
│   ├── README.md                    # Technical cleaning & validation deep-dive
│   ├── anonymization_pipeline.py    # Python automated Regex extraction script
│   ├── data_preparation_overview.md # Operational data asset summary & dictionary
│   ├── raw_nested_data.csv          # Initial flat-file CRM export with nested cells
│   └── cleaned_nested_data.csv      # Cleaned, unbundled tabular relational dataset
│
└── 📊 event_data_analysis/         # Business Intelligence & Insights Phase
    ├── README.md                    # Project Overview: Event Analytics & Marketing Optimization
    ├── event_cleaned_data.csv       # Unified source of truth feeding BI dashboards
    ├── post_event_analysis.md       # Post-Event Insights and Demographics Report
    └── pre_event_marketing.md       # Pre-Event Marketing Performance Analysis
