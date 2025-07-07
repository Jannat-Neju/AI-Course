from collections import deque

# গ্রাফ ডেফিনেশন (নোড: [প্রতিবেশী নোডসমূহ])
graph = {
    '1': ['2', '3'],
    '2': ['4'],
    '3': ['4'],
    '4': ['5'],
    '5': ['6'],
    '6': ['7','8'],
    '7': ['6','9'],
    '8': ['6','9'],
    '9': ['7','8'],
    
}

def bidirectional_search(graph, start, goal):
    
    forward_queue = deque([start])
    backward_queue = deque([goal])

    forward_visited = set([start])
    backward_visited = set([goal])

    
    forward_parent = {start: None}
    backward_parent = {goal: None}

    meet_node = None  

    while forward_queue and backward_queue:
        
        current_forward = forward_queue.popleft()
        for neighbor in graph.get(current_forward, []):
            if neighbor not in forward_visited:
                forward_visited.add(neighbor)
                forward_parent[neighbor] = current_forward
                forward_queue.append(neighbor)
               
                if neighbor in backward_visited:
                    meet_node = neighbor
                    break
        if meet_node:
            break

        
        current_backward = backward_queue.popleft()
        for node, neighbors in graph.items():
            if current_backward in neighbors:
                if node not in backward_visited:
                    backward_visited.add(node)
                    backward_parent[node] = current_backward
                    backward_queue.append(node)
                   
                    if node in forward_visited:
                        meet_node = node
                        break
        if meet_node:
            break

    if not meet_node:
        print("Path not found।")
        return []

   
    path_forward = []
    node = meet_node
    while node:
        path_forward.append(node)
        node = forward_parent.get(node)
    path_forward.reverse()

    
    path_backward = []
    node = backward_parent.get(meet_node)
    while node:
        path_backward.append(node)
        node = backward_parent.get(node)

    
    full_path = path_forward + path_backward

    print(f"The bidirectional search finds that the forward search from '{start}' and backward search from '{goal}' meet at '{meet_node}'.")
    print("Path:", " -> ".join(full_path))
    return full_path

# কল করে দেখা
bidirectional_search(graph, '1', '9')
