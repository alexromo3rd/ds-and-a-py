# Vertex (Node) or Vertices if there are more than one
# between vertices are Edge or Connection
# No limit to how many other vertices that a vertex can
# connect to

# Weighted edges - used in something like Google maps app
# Also, network routing protocols

# Edges can be weighted or not weighted
# Can also be directional or bi-directional
# Trees are a form of graphs but have the limitation that
# each node can only point to two other nodes

# Two ways we're going to look at being able to represent a graph
# Adjacency Matrix

#      A   B   C   D   E
# A    0   1   0   0   1
# B    1   0   1   0   0
# C    0   1   0   1   0
# D    0   0   1   0   1
# E    1   0   0   1   0


# Adjacency List - represented with a Dictionary
# {
#   'A': ['B', 'E']
#   'B': ['A', 'C']
#   'C': ['B', 'D']
#   'D': ['C', 'E']
#   'E': ['A', 'D']
# }

# Graph - Big O
# Adjacency Matrix - Space Complexity - Number of Vertices Squared - O(|V|^2)
# Adjacency List - Space Complexity - Number of Vertices Plus number of edges - O(|V| + |E|)

# Adding a new vertex in a Adjacency List is O(1) - Need to add new key/value pair
# Adding a new vertex in a Adjacency Matrix is O(|V|^2) - Need to add new row
# and new column

# Adding an edge to either matrix or list is O(1)
# Removing an edge in the list is O(|E|) - dependent on the number of edges
# Removing an edge in the matrix is O(1)

# Removing a vertex in a list - remove vertex and edges that point to that vertex
# You'd need to touch everything in the list - O(|V| + |E|)

# Matrix - You'd need to rewrite the entire matrix (|V|^2)

class Graph:
    def __init__(self):
        self.adj_list = {}

    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex, ':', self.adj_list[vertex])

    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False
    
    def add_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False
    
    def remove_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            try:
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
            except ValueError:
                pass
            return True
        return False
    
    def remove_vertex(self, vertex):
        if vertex in self.adj_list.keys():
            for other_vertex in self.adj_list[vertex]:
                self.adj_list[other_vertex].remove(vertex)
            del self.adj_list[vertex]
            return True
        return False

my_graph = Graph()
my_graph.add_vertex('A')
my_graph.add_vertex('B')
my_graph.add_vertex('C')
my_graph.add_vertex('D')

my_graph.add_edge('A','B')
my_graph.add_edge('A','C')
my_graph.add_edge('A','D')
my_graph.add_edge('B','D')
my_graph.add_edge('C','D')

my_graph.remove_vertex('D')

my_graph.print_graph()