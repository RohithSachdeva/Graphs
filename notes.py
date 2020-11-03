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





"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    def __repr__(self):
        return f'Node({repr(self.value)})'

head = Node('A')
head.next = 