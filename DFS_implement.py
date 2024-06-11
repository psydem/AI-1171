# Step 1: Initialize the graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Step 2: Define the DFS function
def dfs(graph, node, visited):
    if node not in visited:
        # Step 3: Mark the current node as visited
        visited.add(node)
        # Step 4: Process the current node (e.g., print the node)
        print(node, end=' ')

        # Step 5: Recursively visit all adjacent nodes
        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)

# Step 6: Start the DFS traversal
visited = set()  # Set to keep track of visited nodes
start_node = 'B'  # Starting node for the DFS traversal
dfs(graph, start_node, visited)
