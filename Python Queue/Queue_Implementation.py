# Implement the following fumctions in Queue:-
    # 1. Enqueue
    # 2. Dequeue
    # 3. Display
    # 4. peekfirst()
    # 5. peeklast()


class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self, item):
        self.queue.append(item)
    def dequeue(self):
        if len(self.queue) < 1:
            return self.queue
        return self.queue.pop(0)
    def display(self):
        print(self.queue)
    def size(self):
        return len(self.queue)
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
q.display()
q.dequeue()
q.dequeue()
print("\nAfter removing two element..")
q.display()