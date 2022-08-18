
# Creating a Node

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        self.prev = None



# Creating class

class doubleLinkedList:
    def __init__(self) -> None:
        self.head = None

# Traversal

    def forward_traversal(self):
        print()
        if self.head is None:
            print("Double linked list is empty")
        else:
            a = self.head          
            while a is not None:  
                print(a.data, end = " ") 
                a = a.next    

    def backward_traversel(self):
        print()
        if self.head is None:
            print("Double linked list is empty")
        else:
            a = self.head
            while a.next is not None:
                a = a.next
            while a is not None:
                print(a.data, end=" ")
                a = a.prev

n1 = Node(5)
dll = doubleLinkedList()
dll.head = n1
n2 = Node(10)
n2.prev = n1
n1.next = n2
n3 = Node(25)
n3.prev = n2
n2.next = n3
n4 = Node(59)
n4.prev = n3
n3.next = n4
dll.forward_traversal()
dll.backward_traversel()