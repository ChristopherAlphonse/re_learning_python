# Stacks

```py
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        """ Pushes a value onto the stack. """
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        """ Removes and returns the top value of the stack. """
        if self.is_empty():
            raise IndexError("Pop from an empty stack")
        value = self.top.value
        self.top = self.top.next
        return value

    def peek(self):
        """ Returns the top value without removing it. """
        if self.is_empty():
            return None
        return self.top.value

    def is_empty(self):
        """ Checks if the stack is empty. """
        return self.top is None
```
