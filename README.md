# UK Energy Grid Climate Risk Exposure & Financial Performance Pipeline

A production-ready data engineering pipeline designed to evaluate how real-time climate risk factors correlate with the equity market performance of major UK energy infrastructure operators. 

## 👤 About Me & Project Motivations
My academic dissertation directly investigated whether **climate risk disclosure affects the financial performance of UK energy firms**. While that research relied on historical corporate reporting documents, this project adapts that exact business logic into an automated, modern data pipeline. 

I am applying to the **Data Engineer position at The Information Lab / The Data School** to bridge the gap between financial risk theory and production-grade data automation. I chose this architecture to showcase my ability to ingest disparate web data feeds, handle real-world API anomalies, model structures in a local database engine, and serve clean metrics for downstream analytics.

---

## 🎯 Target Audience & Problem Solved
*   **Target Audience:** ESG (Environmental, Social, and Governance) Investment Analysts at UK Asset Management Firms.
*   **The Problem:** ESG analysts want to know if carbon emissions spike or drop at the exact same moments an energy operator's stock valuation shifts. However, tracking this manually is difficult because grid emissions update every 30 minutes, whereas equity assets update once per day on the London Stock Exchange.
*   **The Solution:** This pipeline automatically extracts half-hourly carbon intensities, transforms them into a structured model, down-samples the granularity into daily averages, and merges them alongside live closing prices into a single, clean analytic dataset.

---

## 🔌 Data Sources & Ingestion Framework
This application is completely self-contained and pulls data entirely from free, public endpoints without requiring paid subscription keys:
1.  **Climate Feed:** [National Grid ESO Carbon Intensity API](https://carbonintensity.org.uk) – Delivers half-hourly actual and forecast carbon intensity (gCO₂/kWh) for the UK electricity grid.
2.  **Financial Feed:** [Yahoo Finance API Engine](https://pypi.org) – Downloads live and historical market equity indices for National Grid plc (`NG.L`) trading on the London Stock Exchange.

---

## 🛠️ Data Pipeline Architecture