📌 Project Overview
- This project focuses on Binary Classification to predict whether a player will make an in-game purchase (1) or not (0) within an RPG environment. While conducted in a local environment, I simulated a Medallion Architecture (Bronze-Silver-Gold) to structure the data pipeline, focusing on how progression friction and player engagement drive monetization decisions.

💡 Medallion Pipeline & Feature Engineering
- I successfully simulated the data lifecycle to ensure structural integrity and strategic feature extraction:
  - Bronze (Raw): Ingested raw behavioral logs of RPG players.
  - Silver (Refined): Engineered high-value KPIs to capture player psychology:
    - LevelEfficiency: Measures progression speed; tests if fast growth reduces the need for paid boosts.
    - WeeklyCommitment: Quantifies time investment to analyze the "Sunk Cost Effect" on purchasing.
  - Gold (Aggregated): Finalized feature sets and applied Downsampling to address the class imbalance between purchasers (1) and non-purchasers (0).

📊 ML Model Performance
- Given the nature of the synthetic dataset, the focus was on comparing model behaviors rather than achieving absolute high scores.
  - Linear SVM: 50.40% accuracy
  - Random Forest: 51.24% accuracy
  - Gradient Boosted (GBT): 52.27% accuracy

🔍 Major Discovery & Research Limitations
- The Accuracy Paradox: The model accuracy remained around 52% primarily due to the use of Synthetic Data, which lacks the complex behavioral nuances and hidden correlations found in real-world player telemetry.
- Value Beyond Prediction: Despite the predictive constraints, the analysis identified LevelEfficiency and EngagementScore as the primary system variables. This proves that even when individual prediction is challenging, data can still provide the strategic direction needed to balance an in-game economy.

🛠️ Tech Stack
- Engine: Python (PySpark)
- Architecture: Simulated Medallion Pipeline (Bronze, Silver, Gold)
- ML Library: SparkML (LinearSVC, RandomForest, GBT)
