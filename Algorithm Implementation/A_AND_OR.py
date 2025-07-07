class Edge:
    def __init__(self, child):
        self.child = child

class Group:
    def __init__(self, group_type, edges):
        self.group_type = group_type  # "AND" or "OR"
        self.edges = edges

class Node:
    def __init__(self, state, heuristic):
        self.state = state
        self.heuristic = heuristic
        self.solved = False
        self.children = []  # List of Groups

def ao_star(node):
    if node.solved:
        return

    print(f"Expanding: {node.state}")

    if not node.children:
        node.solved = True
        return

    best_cost = float('inf')

    for group in node.children:
        if group.group_type == "AND":
            cost = 0
            for edge in group.edges:
                ao_star(edge.child)
                edge_cost = 1 + edge.child.heuristic
                cost += edge_cost
        else:  # OR group
            cost = float('inf')
            for edge in group.edges:
                ao_star(edge.child)
                edge_cost = 1 + edge.child.heuristic
                cost = min(cost, edge_cost)

        if cost < best_cost:
            best_cost = cost

    node.heuristic = best_cost
    node.solved = True

    print(f"Solved: {node.state} with cost: {node.heuristic}")

# Create Nodes
A = Node("A", 999)
B = Node("B", 4)
C = Node("C", 2)
D = Node("D", 3)
E = Node("E", 6)
F = Node("F", 8)
G = Node("G", 2)
H = Node("H", 0)
L = Node("L", 0)
J = Node("J", 0)

# Setup Children
A.children.append(Group("OR", [Edge(B)]))
A.children.append(Group("AND", [Edge(C), Edge(D)]))
B.children.append(Group("OR", [Edge(E), Edge(F)]))
C.children.append(Group("OR", [Edge(G)]))
C.children.append(Group("AND", [Edge(H), Edge(L)]))
D.children.append(Group("OR", [Edge(J)]))

# Run AO* Algorithm
ao_star(A)

print(f"\nFinal heuristic value of root node '{A.state}': {A.heuristic}")