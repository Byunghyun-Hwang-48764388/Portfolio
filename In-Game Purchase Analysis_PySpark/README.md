In-Game Purchase Prediction & Behavioral Analysis

📌 Project Overview
This project focuses on predicting in-game purchase behavior (Binary Classification) based on RPG player activity logs. Beyond simple prediction, it involves deep exploratory analysis of various behavioral metrics to identify which factors most significantly influence a user's decision to spend.

🛠️ Tech Stack
- Infrastructure: Databricks, Apache Spark
- Data Engineering: PySpark (Medallion Architecture: Bronze, Silver, Gold)
- Machine Learning: Spark MLlib (GBT, Random Forest, SVM)

📊 Key Actions & Analysis
1. Automated ETL Pipeline: Built a robust pipeline on Databricks to transform raw telemetry logs into a structured "Gold" dataset optimized for behavioral modeling.
2. Feature Engineering: Developed custom columns such as LevelEfficiency (progression speed) and WeeklyCommitment to quantify player loyalty and growth patterns.
3. Behavioral Analysis:
- The Progression Paradox: Discovered that exceptionally high leveling efficiency negatively correlates with purchase intent, suggesting players feel less "necessity" for paid boosts.
- Engagement Impact: Analyzed multiple behavioral columns to conclude that a composite EngagementScore is a stronger predictor of spending than isolated metrics like session frequency.

🖥️ Presentation & Results
- Full Analysis Report: I have uploaded a separate PowerPoint (PPT) slide deck containing the detailed analysis and visualization of this project. Please refer to the PPT file in this repository for the comprehensive results.
- Best Model: The GBT (Gradient Boosted Trees) Classifier outperformed other models by effectively capturing the non-linear relationships between player demographics and in-game behavior.
