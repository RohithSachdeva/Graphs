"""
1 Hour into lecture

Creates the graph class and add_vertex function... creates two vertices 
Sets offer order(1) look up

So we are storing things as a set in a dictionary?  You can instantiate the set with set() .. using {} instantiates a dictionary
{1: {2}}   --> The : separates the key:value pair that is the usual syntax for a dictionary 

1:18 into lecture (after 4 minute break)
Now about to go into Breadth and Depth first traversals
-Shortest path = Breadth First
--You have to visit the nodes by their order of closeness.  Closest possible, then next closest, then next closest etc

BFT 
---

init:
add the starting vert to the queue

While the queue is not empty:
    pop current vert off queue
    if not visited: 
        "visit" the node
        Add all its neighbors to the queue (adjacent nodes)

Pop the queue into visited then have its adjacent nodes placed into the queue 

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
        self.vertices = {}  #keys are all the verts in the graph, values are sets of adj verts 

    def add_vertex(self, vertex):
        self.vertices[vertex] = set() #this vert is not connected to anything
        
    def add_edge(self, v_from, v_to):
        if v_from in self.vertices and v_to in self.vertices:
            self.vertices[v_from].add(v_to)
        else:
            raise IndexError("Nonexistent Vertex")

    def is_connected(self, v_from, v_to):
        if v_from in self.vertices and v_to in self.vertices:
            return v_to in self.vertices[v_from]
        else:
            raise IndexError("Nonexistent Vertex")

    def bft(self, starting_vertex_id):
        q = Queue()
        visited = set()
        
        #init
        q.enqueue(starting_vertex_id) #append the first starting vertex to the queue

        #while queue isn't empty
        while q.size() > 0:
            
            v = q.dequeue()

            if v not in visited:
                print(v) #Visit the node

                visited.add(v)





g = Graph()
g.add_vertex(1)
g.add_vertex(2)   #Instantiate the graph class... add two vertices that aren't connected to each other
g.add_vertex(3)

g.add_edge(2, 1)
g.add_edge(1, 2)
g.add_edge(2, 3)

#prints {1: {2}, 2: {1}}   1 connects to 2, 2 connects to 1 

print(g.vertices) 
