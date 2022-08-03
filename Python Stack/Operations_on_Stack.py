
# Implementation of Stack


# Several ways to implement stack in python--->
    # 1> List
    # 2> collections.deque
    # 3> queue.LifoQueue

# Method 1- Using List

stack = [1]

stack.append("Hello World!")
print("\n")
print(f"{stack} has been added using append() Method.")
print(f"'{stack.pop()}' has been remove using pop() Method.")
print(f"The remining stack is {stack}")


# Method 2 -> Using collection.deque

#  Note: append and pop operations are faster in deque as compare to list.

# Logic-->

from collections import deque

stackd = deque()
stackd.append("abc")
stackd.append("Muhammad")
stackd.append("Jahir")
stackd.append("Rohit")
print("\n")
print("Implementation using Deque Method.\n")
print(f"{stackd} has been added")
print(f"'{stackd.pop()}' item has been remove")
print(stackd)
print("\n")


# Method 3 -> Using queue.LifoQueue Module

# Functions are available in queue module ->

    # get() - use to remove element.

    # maxsize() - use to put the maximum number of items allowed in queue.

    # empty() - return true if queue is empty else false.

    # full() - return true if queue is full.

    # put() - used to insert element in queue.

    # qsize() - Return the size of the queue.

from queue import LifoQueue

stackq = LifoQueue(maxsize=10)
stackq.put(2)
stackq.put(5)
stackq.put(8)
stackq.put(9)
stackq.put(0)
print("\n")
print(stackq.qsize())
print(stackq.full())
stackq.get()
print("\n")
