def is_safe(graph, node, color, colors):
    # Check if the current color assignment is safe for the given node
    for neighbor in graph[node]:
        if colors[neighbor] == color:
            return False
    return True

def backtracking(graph, colors, color_domain, node):
    # If all nodes are assigned a color, return True
    if node == len(graph):
        return True
    
    for color in color_domain:
        if is_safe(graph, node, color, colors):
            colors[node] = color
            if backtracking(graph, colors, color_domain, node + 1):
                return True
            colors[node] = None  # Backtrack

    return False

def map_coloring(graph, color_domain):
    colors = [None] * len(graph)
    if backtracking(graph, colors, color_domain, 0):
        return colors
    else:
        return None

# Example graph representing regions and their adjacencies
# Each node represents a region, and edges represent adjacencies
graph = [
    [1, 2, 3],    # Neighbors of region 0
    [0, 2],       # Neighbors of region 1
    [0, 1, 3, 4], # Neighbors of region 2
    [0, 2, 4],    # Neighbors of region 3
    [2, 3]        # Neighbors of region 4
]

# Define the domain of possible colors
color_domain = ['Red', 'Green', 'Blue']

# Solve the map coloring problem
solution = map_coloring(graph, color_domain)

if solution:
    print("Solution found:", solution)
else:
    print("No solution exists.")
