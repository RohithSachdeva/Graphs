"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy
class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()
    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("nonexistent vertex")
    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]
    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Create an empty queue
        q = Queue()
        # Add starting vertex id
        q.enqueue(starting_vertex)
        # Create a set for visited verts
        visited = set()
        # While queue is not empty
        while q.size() > 0:
            # Dequeue a vert
            v = q.dequeue()
            # If not visited
            if v not in visited:
                # Visit it!
                print(v)
                # Mark as visited
                visited.add(v)
                # Add all neighbors to the queue
                for neighbor in self.get_neighbors(v):
                    q.enqueue(neighbor)
    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        q = Stack()
        visited = set()
		# Init:
        q.push(starting_vertex)
		# While queue isn't empty
        while q.size() > 0:
            v = q.pop()
            if v not in visited:
                print(v)   # "Visit" the node
                visited.add(v)
                for neighbor in self.get_neighbors(v):
                    q.push(neighbor)
    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        # default immutable parameters
        if visited is None: 
            visited = set()
        visited.add(starting_vertex)
        print(starting_vertex)
        for neighbor in self.vertices[starting_vertex]:
            if neighbor not in visited:
                self.dft_recursive(neighbor, visited)
        # Check if visited is None. If so, initialize it as an empty set
        # if visited is None:
        #     visited = set()
        # # If the node hasn't been visited...
        # if starting_vertex not in visited:
        #     # Mark the node as visited
        #     visited.add(starting_vertex)
        #     # Then call DFT_recursive on each child
        #     for neighbor in self.vertices[starting_vertex]:
        #         self.dft_recursive(neighbor, visited)
        # visited = set()
        # def dft(vertex):
        #     if vertex in visited:
        #         return
        #     else:
        #         visited.add(vertex)
        #         print(vertex)
        #     for neighbor in self.get_neighbors(vertex):
        #         dft(neighbor)
        # dft(starting_vertex)
    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create an empty queue and enqueue A PATH TO the starting vertex ID
        q = Queue()
        q.enqueue([starting_vertex])
        # Create a set to store visited vertices
        visited = set()
        # While the queue is not empty...
        while q.size() > 0:
            # Dequeue the first PATH
            path = q.dequeue()
            # Grab the last vertex from the PATH
            v = path[-1]
            # If vertext = target
            if v == destination_vertex:
                # Return path
                return path
            # IF that vertex has not been visited:
            if v not in visited:
                # mark it as visited
                visited.add(v)
                # Then add A PATH TO all of its neighbors to the back of the queue
                for neighbor in self.vertices[v]:
                    # Copy the path
                    path_copy = list(path)
                    # Append neighbor to the back of the copy
                    path_copy.append(neighbor)
                    # Enqueue copy
                    q.enqueue(path_copy)
    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Create an empty set to store visited nodes
        visited = set()
        # Create an empty Stack and push A PATH to the starting vertex
        s = Stack()
        s.push( [starting_vertex] )
        # While the Stack is not empty...
        while s.size() > 0:
            # Pop the first PATH from the stack
            path = s.pop()
            # Grab the vertex from the end of the path
            v = path[-1]
            # If Vertex = target
            if v == destination_vertex:
                # return path
                return path
            # If that vertex has not been visited...
            if v not in visited:
                # Mark it as visited
                visited.add(v)
                # Then add A PATH TO all of its neighbors to the top of the Stack
                for neighbor in self.vertices[v]:
                    # Copy the path
                    path_copy = list(path)
                    # Append the path to that neighbor to the back of the copy
                    path_copy.append(neighbor)
                    # Push copy to Stack
                    s.push(path_copy)
    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        This should be done using recursion.
        """
        if visited is None:
            visited = set()
        if path is None:
            path = []
        visited.add(starting_vertex)
        # path = path + [starting_vertex] # subtly makes a copy of the path
        # same as line of code above
        path = list(path) # make a copy
        path.append(starting_vertex)
        if starting_vertex == destination_vertex:
            return path
        for neighbor in self.get_neighbors(starting_vertex):
            if neighbor not in visited:
                new_path = self.dfs_recursive(neighbor, destination_vertex, visited, path)
                if new_path is not None:
                    return new_path
        return None
        # Check if visited is None. If so, initialize it as an empty set
        # visited = set()
        # if starting_vertex == destination_vertex:
        #     return starting_vertex
        # if starting_vertex not in visited:
        #     visited.add(starting_vertex)
        # for v in self.vertices[starting_vertex]:
        #     if v not in visited:
        #         new_path = list(visited)
        #         new_path.append(v)
        #     return self.dfs_recursive(new_path, destination_vertex)
if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)
    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)
    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)
    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)
    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))
    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))