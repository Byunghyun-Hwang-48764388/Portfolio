📌 Project Overview
- This project focuses on developing a high-precision machine learning pipeline to predict heart attack risks and segment high-risk patient groups. By integrating rigorous statistical testing, advanced imbalance handling (SMOTE), and unsupervised learning (PCA & K-Means), I built a model that not only predicts risk but also identifies hidden physiological patterns in patient data.

🛠️ Tech Stack & Methodologies
- Analysis: Python (Pandas, NumPy, Scipy)
- Machine Learning: Scikit-learn (Classification, GridSearch, PCA, K-Means)
- Imbalance Handling: Imbalanced-learn (SMOTE)
- Visualization: Seaborn, Matplotlib

📊 Advanced Engineering & Analysis
- Statistical Foundation: Conducted Shapiro-Wilk and Mann-Whitney U tests to validate data distribution, ensuring the selection of appropriate non-parametric modeling techniques.
- Handling Data Imbalance: Implemented SMOTE (Synthetic Minority Over-sampling Technique) to address class imbalance, significantly improving the model's ability to detect minority high-risk cases (Recall/F1-score).
- Model Optimization: Performed Hyperparameter Tuning via GridSearchCV for Random Forest and Decision Tree models to maximize predictive accuracy.
- Unsupervised Risk Segmentation: Applied PCA for dimensionality reduction followed by K-Means Clustering to categorize patients into distinct risk profiles, enabling targeted clinical intervention strategies.

🖥️ Key Results & Actionable Insights
- Optimal Model Performance: Achieved robust classification results through systematic model comparison and tuning.
- High-Risk Profiling: Identified specific physiological thresholds (e.g., chest pain type, max heart rate) that serve as primary indicators for cardiac events.
- Strategic Recommendation: Proposed a Targeted Intervention Model where PCA-based clustering identifies "silent" high-risk groups that might be missed by standard linear analysis.
