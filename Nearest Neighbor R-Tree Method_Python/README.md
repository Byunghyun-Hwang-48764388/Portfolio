📌 Project Overview
- Developed a high-efficiency spatial search engine to solve the Nearest Neighbor (NN) problem, matching 200 user queries to their closest parking spaces among 150,000 available points. By implementing R-Tree Indexing and optimizing it with Divide-and-Conquer strategies, I achieved a 95% reduction in total processing time.

📊 Performance Benchmarking
- Sequential Scan (Baseline): 11.036090 sec
- Branch and Bound (BaB): 1.692319 sec (~6.5x Faster)
- BaB with Divide-and-Conquer: 0.540460 sec (~20.4x Faster) 

🔍 Key Engineering Achievements
- The Ultimate Optimization (Divide-and-Conquer): Beyond standard indexing, I integrated a Divide-and-Conquer approach to further partition the search space. This strategy reduced computational overhead by an additional 68% compared to the standard BaB method, achieving a sub-second response time.
- 20.4x Speedup: Successfully optimized the core search logic from 11s (Sequential) to 0.54s for 200 concurrent user queries against a massive dataset.
- Scalability & Pruning: Leveraged R-Tree spatial indexing to implement efficient pruning, ensuring O(log N) search complexity and proving the system's readiness for large-scale, real-time environments.

🖥️ Business Impact & Actionable Use Cases
- Real-time Parking Discovery: This engine can be deployed in navigation apps to find the nearest available parking lot among hundreds of thousands of options in milliseconds, ensuring a seamless user experience.
- Infrastructure Cost Reduction: By optimizing the algorithm to be 20 times more efficient, the system significantly reduces server CPU load, allowing the platform to handle much higher traffic without increasing infrastructure costs.
