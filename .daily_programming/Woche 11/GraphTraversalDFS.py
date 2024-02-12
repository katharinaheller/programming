class Graph:
    def __init__(self):
        # Initialize the graph as an empty dictionary
        self.graph = {}

    def add_edge(self, u, v):
        # Add an edge from vertex u to vertex v
        # If u is not already in the graph, create a new list for it
        if u not in self.graph:
            self.graph[u] = []
        # Append v to the list of neighbors for vertex u
        self.graph[u].append(v)

    def dfs_util(self, v, visited):
        # Mark the current vertex as visited
        visited.add(v)
        # Print the vertex being visited
        print(v, end=' ')

        # Check if the current vertex has neighbors
        if v in self.graph:
            # Traverse all neighbors of the current vertex
            for neighbor in self.graph[v]:
                # If the neighbor is not visited yet, recursively call dfs_util on it
                if neighbor not in visited:
                    self.dfs_util(neighbor, visited)

    def dfs(self, start):
        # Create an empty set to keep track of visited vertices
        visited = set()
        # Call dfs_util starting from the given start vertex
        self.dfs_util(start, visited)

# Example usage
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

print("Depth First Traversal (Starting from vertex 2):")
# Perform DFS traversal starting from vertex 2
g.dfs(2)
