visited = set()        
path = []              
found = False          
# Depth Limited Search ফাংশন
def depth_limited_search(graph, node, depth, limit, goal):
    global found
    if found:               
        return
    if depth > limit:       
        return
    if node not in visited:    
        path.append(node)       
        visited.add(node)      
        if node == goal:        
            found = True
            return
        for neighbour in graph[node]:    
            depth_limited_search(graph, neighbour, depth + 1, limit, goal)

# Iterative Deepening Search ফাংশন
def iterative_deepening_search(graph, start, goal):
    limit = 0
    while True:
        global visited, path, found
        visited = set()      
        path = []            
        found = False        
        
        depth_limited_search(graph, start, 0, limit, goal)
        print(f"Depth limit: {limit}, Path: {'->'.join(path)}")
        
        if found:
            return path     
        limit += 1          

# গ্রাফ (নোড সংযোগ)
graph = {
    'A': ['B', 'C','X'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H', 'I'],
    'E': ['J', 'K'],
    'F': ['L', 'M'],
    'G': ['N', 'O'],
    'H': [], 'I': [], 'J': [], 'K': [], 'L': [], 'M': [], 'N': [], 'O': []
}

# লক্ষ্য: 'D' পর্যন্ত পথ খোঁজা
result_path = iterative_deepening_search(graph, 'A', 'D')
print("Result_path:", "->".join(result_path))
