class Node:
    def __init__(self, val):
        self.value = val
        self.next = None


class LinkedList:
    def __init__(self, val):
        new_node = Node(val)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value, end=" -> ")
            temp = temp.next
        print("None")  # Mark the end of the list

    def append(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def prepend(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while temp.next is not None:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp

    def get_length(self):
        print("Linked List length:", self.length)

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
            # print(temp.value)
        return temp

    def set_value(self, index, val):
        temp = self.get(index)
        if temp is not None:
            temp.value = val
            return True
        return False

    def insert(self, index, val):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(val)
        if index == self.length:
            return self.append(val)
        new_node = Node(val)
        temp = self.get(index - 1)
        if temp is None:
            return False
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index > self.length:
            return None
        if index == self.length:
            temp = self.pop()
            return temp
        if index == 0:
            temp = self.pop_first()
            return temp
        else:
            prev = self.get(index - 1)
            temp = prev.next


ll = LinkedList(2)
ll.append(3)
ll.prepend(1)
ll.prepend(111)

ll.set_value(1, 55)
ll.insert(0, 88)

ll.remove()
ll.print_list()
ll.get_length()
