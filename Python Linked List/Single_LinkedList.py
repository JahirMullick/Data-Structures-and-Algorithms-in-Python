
# <-- Creating a Node in Single Linked List ---->

class Node:
    def __init__(self,data):
        self.data = data;
        self.reference = None;
node1 = Node(7)
print(node1.data)
print(node1.reference)
