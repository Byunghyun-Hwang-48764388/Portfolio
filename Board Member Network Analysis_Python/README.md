📌 Project Title
- Strategic Board Member Network Analysis: Identifying Key M&A Influencers

📖 Project Summary
- This project identifies high-impact board members within the US IT market to optimize corporate sale strategies (M&A). By leveraging Graph Theory and Social Network Analysis (SNA), I quantified individual influence and mapped information flow across corporate boundaries to identify the most effective points of contact for potential buyers.

📊 Applied Analytics & Insights
- Centrality-based Influence Quantification:
  * Identified the Top 20 "Information Brokers" using Betweenness Centrality, pinpointing individuals who control the flow of non-redundant information between different corporate clusters.
  Utilized Eigenvector Centrality to identify nodes connected to other influential figures, distinguishing "truly influential" leaders from merely "well-connected" ones.

- Statistical Validation of Demographics:
  - Conducted ANOVA & Mann-Whitney U tests to prove that female board members possess higher direct connectivity to influential clusters than their male counterparts.
  - Correlation analysis revealed a significant link between compensation levels and network reach, providing a data-backed criteria for prioritizing outreach.

- Community Detection:
  - Applied clustering algorithms to segment board members into distinct strategic groups, allowing for tailored communication strategies based on cluster characteristics.
 
🛠️ Technical Stack & Methodologies
- Core Engine: Python (NetworkX for graph modeling, Pandas for data orchestration)
- Statistical Rigor: SciPy (Mann-Whitney U, Kruskal-Wallis, ANOVA) for hypothesis testing.
- Data Source: SEC DEF 14A Filings (Real-world corporate data).

💡 Dual-Path Identification Strategy
- To ensure a comprehensive search for the best acquisition leads, I implemented a two-pronged identification framework:
- M&A-Driven Approach (Targeting Strategic Buyers)
  - Focus: Focused on Tier-1 IT corporations with a proven track record of multiple acquisitions ("Serial Acquirers").
  - Method: Mapped board members with direct ties to these acquirers, establishing high-probability corridors to potential buyers.
  - Goal: Identifying the "shortest path" to an exit through existing corporate relationships.
- Network Centrality Approach (Mapping Influence & Information Flow)
  - Degree & Eigenvector Centrality: Pinpointed the Top 20 Power Users with extensive reach, ensuring access to a broad network of influential decision-makers.
  - Betweenness Centrality: Identified the Top 20 "Information Brokers" who act as bridges between disparate corporate clusters, essential for discreetly navigating sensitive M&A interests.
  - Community Clustering: Segmented board members into distinct clusters based on their centrality profiles, enabling differentiated negotiation strategies tailored to each group’s structural position.
 
💡 Key Strategic Insights for Outreach
- Beyond the network structure, I discovered three data-backed criteria to optimize the selection of contact persons:
  - Age Dynamics: Board members aged 60-89 are active in more companies, offering broader network coverage.
  - Gender Advantage: Female board members demonstrated more direct connections with influential figures compared to their male counterparts.
  - Compensation Correlation: High-compensation individuals tend to hold multiple board seats, indicating a higher level of cross-industry influence.
