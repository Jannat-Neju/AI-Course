# Set to keep track of visited nodes
visited = set()

# Recursive Depth-First Search function
def depth_first_search(visited, graph, node):
    if node not in visited:  
        print(node)          
        visited.add(node)    
        for neighbor in graph[node]: 
            depth_first_search(visited, graph, neighbor)

# Predefined graph structure
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F','G'],
    'D': [],
    'E': [],
    'F': [],
    'G': [],
}

# Run DFS starting from node 'S'
depth_first_search(visited, graph, 'A')
