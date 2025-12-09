import math 
import time 
from rtree import RTree 

# --------------------
# Common Functions
# --------------------

# Compute Euclidean distance between two points (x1, y1) and (x2, y2)
def euc_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

# Import spatial points from a text file
def read_data(filename):
    points = []  # Create a list to store (x, y, id) tuples
    with open(filename, 'r') as given_data:
        for line in given_data:  
            fields = line.strip().split()  # Split by whitespace and remove extra space
            if len(fields) == 3:
                _id, x, y = fields
                # Store data as (x, y, id) for spatial operations
                points.append((float(x), float(y), int(_id)))
    return points

# --------------------
# Task1_1: Sequential Scan Based Method
# --------------------

def run_sequential_scan():
    # Import parking location data
    parking_locations = read_data("parking.txt")
    # Import user location data
    user_points = read_data("query_points.txt")

    # Start recording the processing time
    start_time = time.time()
    results = []

    # Sequentially find nearest neighbor for each query
    for user_x, user_y, user_id in user_points:
        # Initialize variables to store nearest neighbor data
        min_distance = float('inf')
        nearest_id = None
        nearest_x = None
        nearest_y = None

        # Check each parking point and compute its distance to the user point
        for parking_x, parking_y, parking_id in parking_locations:
            dist = euc_distance((parking_x, parking_y), (user_x, user_y))
            # If this parking point is closer than the current nearest, update nearest info
            if dist < min_distance:
                min_distance = dist
                nearest_id = parking_id
                nearest_x = parking_x
                nearest_y = parking_y
        # Format and store the nearest parking result for the current user
        each_line = f"point_id = {nearest_id}, x = {nearest_x}, y = {nearest_y} for user {user_id} (distance = {min_distance:.4f})"
        results.append(each_line)

    # Stop recording the processing time
    end_time = time.time()
    # Compute the total processing time
    total_time = end_time - start_time

    return results, total_time

# --------------------
# Task1_2: Branch-and-Bound (BaB) Method
# --------------------

# --------------------
# 1. Define functions
# --------------------

# Create a function computing the minimum distance between a point and a node's MBR
def min_dist_to_mbr(node, point):
    x, y = point
    x1, y1, x2, y2 = node.MBR['x1'], node.MBR['y1'], node.MBR['x2'], node.MBR['y2']
    # Compute horizontal and vertical distance: 0 if the point lies within the MBR along that axis 
    x_distance = max(x1 - x, 0, x - x2)
    y_distance = max(y1 - y, 0, y - y2)
    # Return Euclidean distance from the point to the MBR 
    return math.sqrt(x_distance * x_distance + y_distance * y_distance)

# Create a function implementing the Branch-and-Bound nearest neighbor search on an R-tree
def branch_and_bound(rtree, user_location):
    # Make a list of candidate nodes to explore
    # Start from from the root node
    # Since the root node covers the entire space, the distance is zero 
    node_list_explore = [(0, rtree.root)]
    # Initialize variables to store closest point and its distance
    closest_point = None
    shortest_dist = float('inf')
    # Continue exploring candidate nodes while there are still nodes to examine
    while node_list_explore:
        # Reset per-iteration closest candidate
        current_minimum_dist = float('inf')
        current_index = -1
        # Search the candidate node with the smallest distance bound
        for index, (dist, node) in enumerate(node_list_explore):
            if dist < current_minimum_dist:
                current_minimum_dist = dist
                current_index = index
        # Take out the nearest node efficiently (swap with last node, then remove)
        # For example, to remove node B: (A, B, C, D) -> (A, D, C, D) -> (A, D, C) 
        node_dist, node = node_list_explore[current_index]
        node_list_explore[current_index] = node_list_explore[-1]
        node_list_explore.pop()
        
        # After a nearest point is found, skip nodes whose MBR distance is greater than the current shortest distance
        if closest_point is not None and node_dist > shortest_dist:
            continue
        
        # if the node is a leaf, it contains actual data points (not child MBRs)
        if node.is_leaf():
            for point in node.data_points:
                # Compute distance from the query point to each data point
                point_dist = euc_distance(point, user_location)
                # If this point is closer than the current closest, update it
                if point_dist < shortest_dist:
                    shortest_dist = point_dist
                    closest_point = point
        else:
            # If it is not a leaf node, examine its child MBRs
            for child in node.child_nodes:
                # Compute the minimum possible distance from the query point to this child's MBR
                minimum_dist = min_dist_to_mbr(child, user_location)
                # Explore this child only if its MBR could contain a closer point
                if minimum_dist <= shortest_dist:
                   node_list_explore.append((minimum_dist, child))

    # Return the nearest point and its distance
    return closest_point, shortest_dist

# --------------------
# 2. Execute Branch-and-Bound (BaB) Method
# --------------------

# Create a function implementing Branch-and-Bound (BaB) method
def run_BaB():
    parking_points = read_data("parking.txt")
    query_points = read_data("query_points.txt")

    # Create an empty R-tree
    rtree = RTree()
    for x, y, _ in parking_points:
        # Insert all parking points (as (x, y) coordinate tuples) one by one
        # The RTree.insert() method automatically chooses subtrees, updates MBRs, and perform node splitting
        rtree.insert(rtree.root, (x, y))

    # Create a list to store results
    results = [] 
    # Start recording the processing time (R-tree construction excluded)
    start_time = time.time() 

    # For each query point, run BaB and store the result
    for user_x, user_y, user_id in query_points:
        # Run BaB to find the nearest parking point and its distance
        nn_point, nn_dist = branch_and_bound(rtree, (user_x, user_y))
        if nn_point:
            # Identify the corresponding parking point ID from the original data
            nn_id = next(parking_id for x, y, parking_id in parking_points if (x, y) == nn_point)
            # Extract coordinates of the nearest parking point
            x_p, y_p = nn_point

            # format and save the result 
            line = f"point_id = {nn_id}, x = {x_p}, y = {y_p} for user {user_id} (distance = {nn_dist:.4f})"
            results.append(line)

    # End recording the processing time
    end_time = time.time()
    # Compute the total processing time
    total_time = end_time - start_time

    return results, total_time

# --------------------
# Task1_3: BaB with Divide-and-Conquer Method
# --------------------

# --------------------
# 1. Define functions
# --------------------

# Create a function computing the minimum distance between a point and an axis-aligned MBR
def mbr_point_distance(point, mbr):
    x, y = point
    # Extract MBR boundaries 
    x1, y1, x2, y2 = mbr['x1'], mbr['y1'], mbr['x2'], mbr['y2'] 

    # Compute horizontal distance (0 if the point lies inside MBR in x-axis)
    x_distance = max(x1 - x, 0, x - x2)
    # Compute vertical distance (0 if the point lies inside MBR in y-axis)
    y_distance = max(y1 - y, 0, y - y2)
    
    # Return the minimum Euclidean distance from the point to the MBR
    return math.sqrt(x_distance * x_distance + y_distance * y_distance)

# Create a function identifying the Nearest Neighbor within an R-tree
def nn_identifier(rtree, user_location):
    # Initialize variables to store the closest point and its distance  
    closest_point = None 
    shortest_dist = float('inf') 
    
    def identifier(node):
        # Call these outer variables
        nonlocal shortest_dist, closest_point 
        # Check if current node is a leaf node
        if node.is_leaf(): 
            # Examine all data points
            for point in node.data_points: 
                # If point is stored without ID (e.g., split tree), change the format
                # Divide data point (x, y) and point ID
                if len(point) == 2: 
                    x, y = point
                    point_id = None
                else:
                    x, y, point_id = point
                
                # Compute Euclidean distance from the query point
                dist = euc_distance(user_location, (x,y)) 
                # Update the current closest point and its distance if this point is closer
                if dist < shortest_dist: 
                    shortest_dist = dist
                    closest_point = (x, y, point_id) if point_id is not None else (x, y)
        
        # Otherwise, explore child MBRs
        else:
            # Examine all child nodes
            for child in node.child_nodes:
                # Compute minimum possible distance from query to child MBR
                min_dist = mbr_point_distance(user_location, child.MBR)
                
                # Explore child only if it may contain a closer point (pruning process)
                if min_dist < shortest_dist:
                    identifier(child)
                
                # Otherwise, prune the child (no action to take)
             
    # Conduct the search from the root node
    identifier(rtree.root) 
    
    return closest_point, shortest_dist

# --------------------
# 2. Divide and Conquer
# --------------------

def run_BaB_DaC():
    parking_points = read_data("parking.txt")
    user_points = read_data("query_points.txt")

    # 1. Sort parking points based on x-coordinate and split them into two halves
    parking_points.sort(key = lambda p: p[0])
    # Compute the median x-value based on (p[0] = x-value)
    mid = len(parking_points) // 2
    # Define points in left half
    left_points = parking_points[:mid]
    # Define points in right half
    right_points = parking_points[mid:]

    # 2. Build an Rtree for each partition
    rtree_left = RTree()
    for x, y, _id in left_points:
        rtree_left.insert(rtree_left.root, (x, y, _id))

    rtree_right = RTree()
    for x, y, _id in right_points:
        rtree_right.insert(rtree_right.root, (x, y, _id))

    # 3. Find the nearest neighbor in both partitions 
    # Create a list to store results
    results = []
    # Start recording the processing time (R-tree construction excluded)
    start_time = time.time() 

    for user_x, user_y, user_id in user_points:
        # Search Nearest Neighbor in the left partition 
        nn_left, dist_left = nn_identifier(rtree_left, (user_x, user_y))
        # Search Nearest Neighbor in the right partition 
        nn_right, dist_right = nn_identifier(rtree_right, (user_x, user_y))

        # Select the closer Nearest Neighbor from left or right R-tree 
        if dist_left < dist_right:
            nearest_point, dist = nn_left, dist_left
        else:
            nearest_point, dist = nn_right, dist_right
        # Format the results
        if nearest_point:
            # Extract coordinates and ID (handle case where ID may be missing)
            if len(nearest_point) == 3:
                x_p, y_p, point_id = nearest_point
            else:
                x_p, y_p = nearest_point
                point_id = "Unknown"
            
            results.append(f"point_id = {point_id}, x = {x_p}, y = {y_p} for user {user_id} (distance = {dist:.4f})")
        else:
            results.append(f"User ID {user_id}: No nearest point found")

    # End recording the processing time
    end_time = time.time()
    # Compute the total processing time
    total_time = end_time - start_time

    return results, total_time

# --------------------
# Combined Execution: Save all results in one file
# --------------------

def execute_entire_methods():
    output_file = "Task_1_output.txt" 
  
    # Record the processing time of each method (R-tree construction excluded)
    results_1_1, time_1_1 = run_sequential_scan()
    results_1_2, time_1_2 = run_BaB()
    results_1_3, time_1_3 = run_BaB_DaC()

    # Record the total processing time (R-tree construction excluded)
    total_runtime = time_1_1 + time_1_2 + time_1_3

    parking_points = read_data("parking.txt")
    query_points = read_data("query_points.txt")
    num_parking = len(parking_points)
    num_queries = len(query_points)

    with open(output_file, "w") as f:
        f.write("Result of Task 1\n\n")
        f.write(f"Loaded {num_parking} parking points and {num_queries} user queries for each method\n\n")

        f.write(f"1. Sequential Scan Based Method: {num_queries} points, time = {time_1_1:.6f} sec\n")
        f.write(f"2. Branch and Bound (BaB) Method: {num_queries} points, time = {time_1_2:.6f} sec\n")
        f.write(f"3. BaB with Divide-and-Conquer Method : {num_queries} points, time = {time_1_3:.6f} sec\n\n")

        f.write(f"Total runtime of the entire process: {total_runtime:.6f} sec\n\n")

        f.write(f"------------------------------------------------------------------\n\n")
        
        # ----- Task 1_1 -----
        f.write("Task 1_1\n")
        f.write("Sequential Scan Based Method:\n\n")
        for line in results_1_1:
            f.write(line + "\n")
        f.write(f"\nProcessing time for Sequential Scan Method: {time_1_1:.3f} seconds\n\n")

        f.write(f"------------------------------------------------------------------\n\n")

        # ----- Task 1_2 -----
        f.write("Task 1_2\n")
        f.write("Branch and Bound (BaB) Method:\n\n")
        for line in results_1_2:
            f.write(line + "\n")
        f.write(f"\nProcessing time for BaB Method: {time_1_2:.3f} seconds\n\n")

        f.write(f"------------------------------------------------------------------\n\n")

        # ----- Task 1_3 -----
        f.write("Task 1_3\n")
        f.write("BaB with Divide-and-Conquer Method:\n\n")
        for line in results_1_3:
            f.write(line + "\n")
        f.write(f"\nProcessing time for BaB with Divide-and-Conquer Method: {time_1_3:.3f} seconds\n")
    
    # After file is closed, print summary to console
    print(f"Seq Scan: {time_1_1:.4f}s, BaB: {time_1_2:.4f}s, BaB-DaC: {time_1_3:.4f}s")
    print(f"Total: {total_runtime:.4f}s")
    print(f"✅ All results saved to {output_file}")

# Run the full pipeline only when this script is executed directly
if __name__ == "__main__":
    execute_entire_methods()



    