
class Node:
    def __init__(self, val):
        self.next = None
        self.prev = None
        self.val = val

    def __str__(self):
        return str(self.val)


class DoublyList:
    def __init__(self, val):
        new_node = Node(val)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def display(self):
        temp = self.head
        while temp is not None:
            print(temp.val, end=" <-> ")
            temp = temp.next
        print()

    def append(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True


DL = DoublyList(0)
DL.append(1)
DL.append(2)
DL.append(3)
DL.display()
