# Event Analytics & Marketing Optimization

## Project Overview
This repository contains an end-to-end data lifecycle project that transforms messy, raw transactional checkout logs into structured enterprise datasets and interactive, self-serve business intelligence applications. 

The project evaluates marketing campaign performance, customer acquisition dynamics, and attendee demographics across professional hierarchies. It is split into two specialized analytical phases to mirror standard corporate operations: tracking pre-event campaign velocity and evaluating post-event customer profiles.

---

## 📂 Repository Architecture

To navigate the components of this pipeline, follow the structural sequence below:

### 1. Main Analysis Overview (`README.md`)
*   *Current File:* High-level directory routing, tech stack orchestration, and core data preparation frameworks.

### 2. [Pre-Event Marketing Performance Analysis](./event_data_analysis/pre_event_marketing.md/)
*   **Focus:** Evaluation of acquisition channels, daily registration velocity, and promotional code ROI.
*   **Asset:** Live interactive campaign tracking dashboard application.

### 3. [Post-Event Insights & Demographics Report](./pst_event_analysis/)
*   **Focus:** Audience segmentation, B2B product-market fit (ticket tier distribution), and campaign engagement matrices.
*   **Asset:** Live interactive audience breakdown dashboard application.

### 4. [Event Cleaned Data](./event_cleaned_data.csv/)
*   **Asset:** `event_cleaned_data.csv` (The final, processed master dataset serving as the unified source of truth for all downstream Looker Studio dashboards).

---

##  Tech Stack & Data Infrastructure
*   **Data Sourcing:** Raw multi-channel checkout registration logs.
*   **Data Engineering & Preprocessing:** Microsoft Excel / Google Sheets (Structural normalization, text truncation fixes, format harmonization, validation scripting).
*   **Business Intelligence & Analytics:** Looker Studio (Multi-page app-style dashboard architecture, cross-page report-level filtering, and conditional heatmap profiling).

---

## Core Data Preparation Framework

Before conducting any analytical operations, the raw master file underwent a rigorous data cleaning pipeline to ensure absolute metric integrity:

*   **Categorical Text Standardization:** Resolved high-cardinality truncation bugs within dimensions such as `REFERRAL CHANNEL` and `SENIORITY` (e.g., standardizing clipped inputs like `"Academia, Non-"` to `"Academia, Non-Profit"`).
*   **Type Casting & Date Harmonization:** Standardized unformatted string timestamps into uniform chronological fields (`YYYY-MM-DD`) to unlock daily campaign velocity metrics. 
*   **Null-Value Optimization:** Replaced blank promotional entries with an explicit `"ORGANIC"` string literal placeholder. This safely decoupled full-price revenue calculations from discounted rows without dropping critical transaction volume.
*   **De-duplication Check:** Enforced strict one-row-per-ticket boundaries by filtering out system-generated transactional duplicates.

---

## 🔗 Live Application Access
The final processed file, `event_cleaned_data.csv`, directly feeds the live interactive dashboard application. 

👉 **[Click Here to Explore the Live Interactive Looker Studio Application](https://datastudio.google.com/s/gsWi2F-fQhA)**
