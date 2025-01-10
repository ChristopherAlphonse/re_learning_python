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
            print(temp.value,  end=" -> ")
            temp = temp.next
            if temp is None:
                print(self.tail.next)
        return temp

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
            temp = self.head
            new_node.next = temp
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

    def get_length(self):
        print("Linked List length: ", self.length)

    def get(self, index):
        if index < 0 or self.length == 0:
            print("-1 Value not found")
        temp = self.head
        while temp is not None:
            if temp.value == index:
                print("Found:", temp.value)
                return temp
            temp = temp.next
        print("Nothing was found")
        return None

    def set_value(self, index, val):
        temp = self.get(index)
        if temp is not None:
            temp.value = val
            return True
        return False


ll = LinkedList(2)
ll.append(3)
ll.prepend(1)
ll.prepend(111)

ll.set_value(1, 55)
ll.print_list()
ll.get_length()
