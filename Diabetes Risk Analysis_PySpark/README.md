📌 Project Overview
- Developed a full-stack data pipeline using Databricks and PySpark to analyze diabetes risk factors. By implementing the Medallion Architecture, I transformed raw health data into high-value business insights, focusing on the correlation between Leisure Vitality (Active Fun) and metabolic health.

⚙️ The Medallion Pipeline Architecture
- I structured the pipeline into three distinct layers to ensure data reliability and scalability:
  - Bronze Layer (Raw Ingestion):
    - Ingested raw pre-diabetes datasets into Delta tables.
    - Preserved data lineage from the landing zone to ensure auditability.
  - Silver Layer (Quality Assurance & Validation):
    - Implemented a Quality Audit Report system (Valid vs. Invalid records).
    - Performed rigorous data cleaning, handling nulls and outliers to achieve high data integrity.
  - Gold Layer (Business Logic & Aggregation):
    - Aggregated refined data to create a diabetes_insight_summary.
    - Calculated specialized metrics like leisure_vitality_score to prepare for strategic analysis.

📊 Ad-hoc Analysis & Key Insights: "The Active Fun Shield"
- Beyond the pipeline, I conducted advanced statistical analysis to find actionable health indicators:
  - Discovery: Leisure Vitality (Vigorous Play) is a stronger independent predictor of lower diabetes rates than BMI or work-related physical intensity.
  - The "Efficiency" Insight: High-intensity leisure activities offer the highest "Return on Investment (ROI)" for diabetes prevention. Even one day of intense, voluntary play is more effective than mandatory moderate effort at work.
  - Correlation Mapping: Used heatmaps and regression comparisons to prove that "how you move for fun" directly improves insulin response, independent of weight loss.
 
🚀 Key Engineering Achievements
- Delta Lake Implementation: Utilized Delta tables for ACID transactions and efficient time-travel debugging.
- End-to-End Automation: Built a modular pipeline where each layer (bronze.ipynb to gold.ipynb) can be independently scaled and managed.
- Statistical Validation: Integrated Shapiro-Wilk and Mann-Whitney U tests to ensure the ad-hoc findings were statistically significant.

🛠️ Tech Stack
- Platform: Databricks (Unified Analytics Platform)
- Language: Python (PySpark), SparkSQL
- Architecture: Medallion (Bronze, Silver, Gold), Delta Lake
- Libraries: Seaborn, Matplotlib, SciPy
