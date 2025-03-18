# Queue

```py
from heapq import heappush, heappop

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.front = self.rear = None

    def enqueue(self, value):
        """ Adds an item to the queue. """
        new_node = Node(value)
        if self.rear:
            self.rear.next = new_node
        self.rear = new_node
        if not self.front:
            self.front = new_node

    def dequeue(self):
        """ Removes and returns the front item of the queue. """
        if self.is_empty():
            raise IndexError("Dequeue from an empty queue")
        value = self.front.value
        self.front = self.front.next
        if not self.front:
            self.rear = None
        return value

    def peek(self):
        """ Returns the front item without removing it. """
        return self.front.value if self.front else None

    def is_empty(self):
        """ Checks if the queue is empty. """
        return self.front is None

class PriorityQueue:
    def __init__(self):
        self.heap = []

    def enqueue(self, value, priority):
        """ Adds an item with priority to the queue. """
        heappush(self.heap, (priority, value))

    def dequeue(self):
        """ Removes and returns the highest priority item. """
        if self.is_empty():
            raise IndexError("Dequeue from an empty priority queue")
        return heappop(self.heap)[1]

    def peek(self):
        """ Returns the highest priority item without removing it. """
        return self.heap[0][1] if self.heap else None

    def is_empty(self):
        """ Checks if the priority queue is empty. """
        return not self.heap
```
