# Iterative Deepening Depth-First Search (IDDFS) in Python

class Graph:
    def _init_(self, vertices):
        self.V = vertices  # Number of vertices
        self.graph = {i: [] for i in range(vertices)}  # Graph representation
    
    # Add edge to the graph
    def add_edge(self, u, v):
        self.graph[u].append(v)

    # Depth-Limited Search (DLS)
    def dls(self, src, target, limit):
        if src == target:
            return True
        if limit <= 0:
            return False

        for neighbor in self.graph[src]:
            if self.dls(neighbor, target, limit - 1):
                return True

        return False

    # Iterative Deepening Search (IDS)
    def iddfs(self, src, target, max_depth):
        for depth in range(max_depth):
            if self.dls(src, target, depth):
                return True
        return False


# Example Usage
g = Graph(7)  # Initialize a graph with 7 nodes

# Add edges
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 5)
g.add_edge(2, 6)

# Source and target
src = 0
target = 6
max_depth = 3  # Set max depth

# Run IDDFS
if g.iddfs(src, target, max_depth):
    print(f"Target {target} found within depth {max_depth}.")
else:
    print(f"Target {target} not found within depth {max_depth}.")
