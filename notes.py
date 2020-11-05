#Monday Lecture

"""
Linked List Review
 
Created a linked list in FSM 
a -> b -> c -> d -> a     ... cyclic D -> a

Traversal - 
Visit all nodes

cur = head 

while cur is not None:
    print(cur.value) 
    cur = cur.next

Added a visited set to keep track of nodes visited

We need to keep track of which nodes we haven't gone through.

If I was a human, I'll visit a b c  then d or e?   D  ... How do we know that there was a previous choice of e? Remember that there was. Keep track of where we havne't been

I haven't been to B.. Lets go there next.  What options?  C ... I ahven't been to C lets go there ... 
Now I have D and E ...  Lets go to D first ... Take it off the list... From D I can only go to A 

I want to write down Nodes that are options, but have not been visited yet

Nodes to Visit-
A ... Ok now B is my only neighbor 

Keep track of nodes to be visited 
While not empty, go visit them.  Keep track of the options.  


INIT:
-Add the starting node to the list
-Grab a node from the to-visit list, and remove it
Add all that node's next ndoes to the to-visit list
Visit the current node (print out the value or whatever)

To Visit: [C]

When at C, we can visit D E X ... To visit list

If we go to D, then we add A to the to vist list


Queues and Stacks

start = node_b
visited = set()
to_visit = [start]


while to_visit != []:
    cur = to_visit.pop() #Grab next node to visit from end of the list; visit the node

    visited.add(cur)

    for n in cur.next:
        if n not in visited:
            to_visit.append(n)
            



Think like a human.  Keep track of where we've been.  Keep track of where we need to go


Wednesday Lecture

Refer to previous Web32 Graph codes for reference.  Study from that.  

BFT
-Starting vertex id has something to do with the graph
-Nothing else really has anything to do with the graph, just manipulating nodes and list and such
-The end; get the neighbors of any vertex.  Once we have that, we can run the traversal

Queues job 


BFT .. Front of queue ; first in first out
DFT .. Top of Stack ; last in first out 


Social network problem discussion

Show a function that shows friends and chain of friendships that link them 




"""



class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    def __repr__(self):
        return f'Node({repr(self.value)})'

head = Node('A')
head.next = 