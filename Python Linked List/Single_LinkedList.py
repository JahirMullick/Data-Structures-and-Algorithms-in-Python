
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
        print("\ninsert at the beginning -->")
        nb = Node(data)     #nb = Node(66)
        nb.next = self.head  # nb.next = n1
        self.head = nb       # sll.head = nb

    def insert_at_End(self,data):
        print("\ninsert at the End -->")
        ne = Node(data)
        a = self.head
        while a.next is not None:
            a = a.next
        a.next = ne


    def insert_at_Specified_Node(self,pos,data):
        print("\ninsert at Specified Node-->")
        npn = Node(data)
        a = self.head
        for i in range(1,pos-1):
            a = a.next
        npn.next = a.next
        a.next = npn


    def deletion_at_beginning(self):
        print("\ndeletion at beginning -->")
        a = self.head
        self.head = a.next
        a.next = None

    def Deletion_at_End(self):
        print("\nDeletion at End -->")
        prev = self.head
        a = self.head.next
        while a.next is not None:
            a = a.next
            prev = prev.next
        prev.next = None

    def Deletion_at_specified_position(self,pos):
        print("\nDeletion node at specified position -->")
        prev = self.head
        a = self.head.next
        for i in range(1, pos-1):
            a = a.next
            prev = prev.next
        prev.next = a.next
        a.next = None



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
sll.insert_at_End(39)
sll.traversal()
sll.insert_at_Specified_Node(3,100)
sll.traversal()
sll.deletion_at_beginning()
sll.traversal()
sll.Deletion_at_End()
sll.traversal()
sll.Deletion_at_specified_position(3)
sll.traversal()
