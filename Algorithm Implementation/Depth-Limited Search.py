visited = set()        
path = []               
found = False           

def depth_limited_search(graph, node, depth, limit, goal):
    global found
    if found:          
        return
    if node == goal:    
        found = True
        path.append(node)
        return
    if depth > limit:   
        return
    if node not in visited:           
        path.append(node)             
        visited.add(node)            
        for neighbour in graph[node]: 
            depth_limited_search(graph, neighbour, depth + 1, limit, goal)

# গ্রাফ স্ট্রাকচার
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H', 'I'],
    'E': ['J', 'K'],
    'F': ['L', 'M'],
    'G': ['N', 'O'],
    'H': [],
    'I': [],
    'J': [],
    'K': [],
    'L': [],
    'M': [],
    'N': [],
    'O': []
}

# অনুসন্ধান চালানো হচ্ছে
depth_limited_search(graph, 'B', 0, 3, 'M') 



print("->".join(path))   
print("goal not found")                   
