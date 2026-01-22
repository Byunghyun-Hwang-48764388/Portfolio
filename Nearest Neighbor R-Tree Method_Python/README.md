

📌 Project Overview
- This project focuses on optimizing spatial data queries by comparing different algorithms to find the nearest parking lot for each user. It demonstrates an understanding of spatial indexing and algorithmic complexity by benchmarking three distinct search methods.

🛠️ Tech StackLanguage 
- PythonKey Libraries: Rtree, Scipy (Spatial)
- PandasData Structures: R-Tree (Spatial Indexing), Linear Arrays

📊 Benchmarking & Performance Analysis
- Brute-Force Search: Established a baseline by calculating distances between all user-parking pairs.
- Linear Search Optimization: Implemented a simplified linear approach to evaluate basic improvements.
- R-Tree Method: Leveraged R-Tree indexing to achieve logarithmic search time, drastically reducing computational overhead for large-scale spatial datasets.

🖥️ Key Findings
- Optimization Impact: The R-Tree method significantly outperformed traditional searches as the data volume increased, proving the necessity of spatial indexing in real-time location-based services.
- Scalability: Validated the scalability of the R-Tree approach for high-density geographic data.
