from itertools import permutations

# Step 1: Initialize the graph (distance matrix)
# Example distance matrix for 4 cities
distance_matrix = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

# Number of cities
num_cities = len(distance_matrix)

# Step 2: Generate all possible routes (excluding the starting city)
cities = list(range(1, num_cities))  # Exclude starting city (0)

# Step 3: Initialize variables to track the minimum distance and best route
min_distance = float('inf')
best_route = None

# Step 4: Calculate the total distance for each route
for perm in permutations(cities):
    current_route = [0] + list(perm) + [0]  # Start and end at the starting city (0)
    current_distance = 0
    
    for i in range(num_cities):
        current_distance += distance_matrix[current_route[i]][current_route[i + 1]]
    
    # Step 5: Update the minimum distance and best route if a shorter route is found
    if current_distance < min_distance:
        min_distance = current_distance
        best_route = current_route

# Step 6: Output the shortest route and its total distance
print("Shortest Route: ", best_route)
print("Minimum Distance: ", min_distance)
