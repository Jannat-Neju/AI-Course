from collections import deque

def breadth_first_search(graph, start_node):
    visited = set()  
    queue = deque([start_node]) 
    while queue: 
        current_node = queue.popleft()  
        
        if current_node not in visited: 
            print(current_node)  
            visited.add(current_node) 
            for connected_node in graph[current_node]:  
                if connected_node not in visited: 
                    queue.append(connected_node)  

# Predefined graph
graph = {
    
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F','G'],
    'D': [],
    'E': [],
    'F': [],
    'G': [],
}

# Run BFS from the starting node 'S'
breadth_first_search(graph, 'A')
