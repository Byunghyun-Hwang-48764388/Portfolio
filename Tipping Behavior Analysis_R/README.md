📌 Project Overview
- Driven by personal curiosity about the "pressured tipping culture" in the U.S., I analyzed 244 restaurant transactions to identify which factors truly influence tipping behavior. This project focuses on challenging social assumptions by using rigorous statistical testing to determine what constitutes a "reasonable" tip and which customer segments are the most generous.

💡 Research Strategy & Hypothesis Testing
- To identify the key drivers of tipping, I segmented the data and applied non-parametric tests to account for the non-normal distribution of tip rates:
  - The "Spending Paradox" Hypothesis: Investigated whether higher total bills lead to higher tip percentages.
  - Situational Dynamics: Analyzed the impact of Group Size (Social pressure), Meal Time (Lunch vs. Dinner), and Day of the Week (Weekend vs. Weekday).
  - Statistical Rigor: Performed Wilcoxon Rank-Sum and Kruskal-Wallis tests after filtering outliers via the IQR method to ensure the integrity of the findings.

🔍 Major Discovery: The Inverse Relationship
- The Findings: Contrary to popular belief, tipping rates do not scale linearly with spending. There is a statistically significant inverse relationship where customers who spend less on their meals tend to leave a higher percentage in tips.
- The Interpretation: This suggests that tipping behavior in the U.S. is driven more by fixed social norms and status-seeking motivations rather than a purely percentage-based reward for service value.

🛠️ Tech Stack
- Language: R (Demonstrating proficiency in statistical programming)
- Libraries: ggplot2 (Visualization), dplyr (Data Manipulation), scales
- Methodology: Wilcoxon Rank-Sum Test, Kruskal-Wallis Test, IQR Outlier Filtering
