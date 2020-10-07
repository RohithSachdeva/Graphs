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


DFT
---
Uses a stack (last in, first out) (nearest neighbors get put in the back of the line)
Go to one neighbor ... add all their neighbors to the front of the queue... so basically one of the neighbors from your initial starting point keeps getting sent to the back of the queue 


"""



class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

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

    def get_neighbors(self, v):
        return self.vertices[v]

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

                visited.add(v) #set method to add 

                for neighbor in self.get_neighbors(v):
                    q.enqueue(neighbor)
    
    def dft(self):
        q = Stack()
        visited = set()
        
        #init
        q.push(starting_vertex_id) #append the first starting vertex to the queue

        #while queue isn't empty
        while q.size() > 0:
            
            v = q.pop()

            if v not in visited:
                print(v) #Visit the node

                visited.add(v) #set method to add 

                for neighbor in self.get_neighbors(v):
                    q.push(neighbor)
    
    def bfs(self, starting_vertex_id, target_vertex_id):
        q = Queue()
        visited = set()

        q.enqueue([starting_vertex_id])

        while q.size() > 0:
            pass

            


















		# Create an empty queue and enqueue A PATH TO the starting vertex ID
		# Create a Set to store visited vertices
		# While the queue is not empty...
			# Dequeue the first PATH
			# Grab the last vertex from the PATH
			# If that vertex has not been visited...
				# CHECK IF IT'S THE TARGET
				  # IF SO, RETURN PATH
				# Mark it as visited...
				# Then add A PATH TO its neighbors to the back of the queue
				  # COPY THE PATH
				  # APPEND THE NEIGHOR TO THE BACK







g = Graph()
g.add_vertex(1)
g.add_vertex(2)   #Instantiate the graph class... add two vertices that aren't connected to each other
g.add_vertex(3)

g.add_edge(2, 1)
g.add_edge(1, 2)
g.add_edge(2, 3)

g.bft(2)

#prints {1: {2}, 2: {1}}   1 connects to 2, 2 connects to 1 

print(g.vertices) 

