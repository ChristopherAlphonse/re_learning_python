
class Node:
    def __init__(self, val):
        self.next = None
        self.prev = None
        self.val = val

    def __str__(self):
        return str(self.val)


class DoublyList:
    def __init__(self, val=0):
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

    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp

    def prepend(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        if index < self.length / 2:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev
        return temp

    def set_value(self, index, val):
        temp = self.get(index)
        if temp is not None:
            temp.val = val
            return True
        return False

    def insert_at(self, index, val):
        if index < 0 or index >= self.length:
            return None
        new_node = Node(val)
        temp = self.get(index)
        if temp.prev is None:
            temp = self.prepend(val)
        elif index == self.length:
            temp = self.append(val)
        else:
            temp.prev.next = new_node
            new_node.prev = temp.prev
            new_node.next = temp
        self.length += 1
        return temp

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()

        temp = self.get(index)
        before = temp.next
        after = temp.prev

        before.prev = after
        after.next = before

        temp.next = None
        temp.prev = None

        self.length -= 1
        return temp

    def swap_first_last(self):
        if self.head is None or self.head == self.tail:
            return
        self.head, self.tail = self.tail, self.head


DL = DoublyList()
DL.append(1)
DL.append(2)
DL.append(3)
DL.append(4)

# DL.set_value(2, 120)
# DL.remove(1)

DL.swap_first_last()
# print(DL.length)
DL.display()
