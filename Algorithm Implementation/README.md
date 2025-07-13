# Algorithm Implementation

This folder contains all the AI search algorithm codes.


Added Algorithm Implementation folder


# Breadth-First Search (BFS)

### 🔸 How It Works
BFS explores nodes level by level. It starts at the root node and explores all its neighbors before moving to the next level. It uses a queue to keep track of nodes to be explored.

### 🔹 Applications
- Shortest path in unweighted graphs
- Web crawlers
- Peer-to-peer networks
- Social networking sites (friend suggestions)

### 🔸 Time & Space Complexity
- **Time:** O(V + E)
- **Space:** O(V)



# Depth-First Search (DFS)

### 🔸 How It Works
DFS explores as far as possible along each branch before backtracking. It uses a stack (or recursion) to keep track of the path.

### 🔹 Applications
- Maze solving
- Cycle detection
- Topological sorting

### 🔸 Time & Space Complexity
- **Time:** O(V + E)
- **Space:** O(V)



# Iterative Deepening Search (IDS)

### 🔸 How It Works
IDS performs DFS to a depth limit, then increases the depth limit until the goal is found. Combines the depth-bounded efficiency of DFS with the completeness of BFS.

### 🔹 Applications
- AI problem solving (e.g., puzzles)
- Tree searching in memory-constrained environments

### 🔸 Time & Space Complexity
- **Time:** O(b^d)
- **Space:** O(d)



# Best First Search

### 🔸 How It Works
Best First Search uses a priority queue and selects the node with the lowest heuristic value to explore next. It focuses on reaching the goal quickly using an evaluation function.

### 🔹 Applications
- Pathfinding
- Puzzle solving (e.g., 8-puzzle)
- Speech recognition

### 🔸 Time & Space Complexity
- **Time:** O(n log n)
- **Space:** O(n)



# A* Algorithm

### 🔸 How It Works
A* uses the formula: `f(n) = g(n) + h(n)` where:
- `g(n)` = cost from start to current node
- `h(n)` = estimated cost to goal

It’s complete and optimal if `h(n)` is admissible.

### 🔹 Applications
- Google Maps
- Robot path planning
- Games

### 🔸 Time & Space Complexity
- **Time:** O(E)
- **Space:** O(V)



# Depth-Limited Search (DLS)

### 🔸 How It Works
DLS is a version of DFS with a maximum depth limit. It prevents infinite loops in deep or infinite trees by cutting off the search beyond a fixed depth.

### 🔹 Applications
- Games with move depth constraints
- Navigation with limited fuel/time
- Solving puzzles like 8-puzzle with a limited number of steps

### 🔸 Time & Space Complexity
- **Time:** O(b^l) where `l` is the depth limit
- **Space:** O(l)



# Bidirectional Search

### 🔸 How It Works
Bidirectional Search runs two simultaneous searches: one from the start node and one from the goal node. When they meet, the path is constructed by combining both.

### 🔹 Applications
- Pathfinding (like GPS and Maps)
- Solving puzzles (e.g., Rubik's cube, 15-puzzle)
- AI in robotics

### 🔸 Time & Space Complexity
- **Time:** O(b^(d/2))
- **Space:** O(b^(d/2))



# AO* Algorithm (AND-OR Graph Search)

### 🔸 How It Works
AO* works on AND-OR graphs, where some nodes require solving multiple sub-problems (AND) while others require only one sub-path (OR). It uses heuristics to guide the search toward optimal solution paths.

### 🔹 Applications
- Problem decomposition (planning, diagnostics)
- Automated theorem proving
- Decision making in expert systems

### 🔸 Time & Space Complexity
- **Time:** Depends on heuristic accuracy; varies
- **Space:** Depends on branching in AND/OR trees



# Hill Climbing Algorithm

### 🔸 How It Works
Hill Climbing is a local search algorithm that moves towards increasing value (better state) until it reaches a peak (local maximum). It doesn't backtrack.

### 🔹 Applications
- Function optimization
- Game AI (simple strategies)
- Machine learning model tuning

### 🔸 Time & Space Complexity
- **Time:** O(n)
- **Space:** O(1)



# Beam Search

### 🔸 How It Works
Beam Search is like BFS but only keeps the best ‘k’ paths at each level. This reduces memory usage by limiting the search width.

### 🔹 Applications
- Speech recognition
- Machine translation
- DNA sequencing

### 🔸 Time & Space Complexity
- **Time:** O(b * d)
- **Space:** O(k * d)

> `k` is the beam width, `d` is depth



# Min-Max Algorithm

### 🔸 How It Works
Min-Max is a decision-making algorithm used in 2-player games. One player tries to maximize score, the other minimizes it. It explores all possible moves and picks the best outcome assuming the opponent plays optimally.

### 🔹 Applications
- Chess
- Tic Tac Toe
- Connect 4

### 🔸 Time & Space Complexity
- **Time:** O(b^d)
- **Space:** O(bd)



# Alpha-Beta Pruning

### 🔸 How It Works
An optimization of Min-Max that avoids exploring branches that won’t affect the final decision. It uses two values (alpha and beta) to track the best already explored options for both players.

### 🔹 Applications
- Efficient game AI (e.g., chess engines)
- Strategic decision trees

### 🔸 Time & Space Complexity
- **Time:** O(b^(d/2)) [in best case]
- **Space:** O(bd)



