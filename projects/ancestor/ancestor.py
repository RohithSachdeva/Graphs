#BFT OR DFT CAN WORK;  Both will produce the same path cause graph is acyclic

#Support hours; Using BFT 
"""
First step.. build a graph 
We have all these different pairs of information 
[(v1, v2),
(v1, v2)]

Earliest ancestor based on longest path
"""

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)


class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("Nonexistent Vertex")

    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id]


def earliest_ancestor(ancestors, starting_node):
    g = Graph()
    
    for pair in ancestors:
        g.add_vertex(pair[0])
        g.add_vertex(pair[1])
        g.add_edge(pair[1], pair[0]) 
        
    
    q = Queue()
    q.enqueue([starting_node])
    
    oldest_ancestor = -1 #this is returned if node has no parents
    max_path_length = 1

    
    while q.size() > 0: #while it exists; dequeue the path
        
        path = q.dequeue()
        vertex = path[-1]

        if len(path) >= max_path_length and vertex < oldest_ancestor:
            oldest_ancestor = vertex
            max_path_length = len(path)
            
        elif (len(path) > max_path_length):
            max_path_length = len(path)
            oldest_ancestor = vertex

        for neighbor in g.vertices[vertex]:
            path_copy = list(path)
            path_copy.append(neighbor)
            q.enqueue(path_copy)
            
    print(g.vertices)
    return oldest_ancestor



"""
def earliest_ancestor(ancestors, starting_node):
    # Build the graph
    graph = Graph()
    for pair in ancestors:
        graph.add_vertex(pair[0])
        graph.add_vertex(pair[1])
        # Build edges in reverse
        graph.add_edge(pair[1], pair[0])
    # Do a BFS (storing the path)
    q = Queue()
    q.enqueue([starting_node])
    max_path_len = 1
    earliest_ancestor = -1
    while q.size() > 0:
        path = q.dequeue()
        v = path[-1]
        # If the path is longer or equal and the value is smaller, or if the path is longer)
        if (len(path) >= max_path_len and v < earliest_ancestor) or (len(path) > max_path_len):
            earliest_ancestor = v
            max_path_len = len(path)
        for neighbor in graph.vertices[v]:
            path_copy = list(path)
            path_copy.append(neighbor)
            q.enqueue(path_copy)
    return earliest_ancestor

"""








    