
# <-- Creating a Node in Single Linked List ---->

class Node:
    def __init__(self,data):
        self.data = data;  # n1.data = 5, n2.data = 10, n3.data = 25, n4.data = 59, nb.data = 66
        self.next = None;  # n1.next = None, n2.next = None, n3.next = None, n4.next = None, nb.next = None
node1 = Node(7)
print(node1.data)
print(node1.next)

# <-- Creating a Class of Single Linked List ---->

class LinkedList:
    def __init__(self) -> None:
        self.head = None  # sll.head = None


# <-- Creating a traversal function in Single Linked List ---->
    def traversal(self):
        if self.head is None:
            print("Single linked list is empty")
        else:
            a=self.head             # a = sll.head
            while a is not None:    # a = sll.head = n1
                print(a.data, end = " ") # a.data = n1.data
                a = a.next               # a = n1.next

    

    def insert_at_beginning(self,data):  # data = 66
        print()
        nb = Node(data)     #nb = Node(66)
        nb.next = self.head  # nb.next = n1
        self.head = nb       # sll.head = nb


n1 = Node(5)
sll = LinkedList()
sll.head = n1
n2 = Node(10)
n1.next = n2
n3 = Node(25)
n2.next = n3
n4 = Node(59)
n3.next = n4
sll.traversal()

# Calling the insert_at_beginning() 
sll.insert_at_beginning(66)
sll.traversal()