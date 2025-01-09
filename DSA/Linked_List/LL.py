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
            print(temp.value)
            temp = temp.next

    def append(self, val):
        temp = Node(val)

        if self.head is None:
            self.head = temp
            self.tail = temp
        else:
            self.tail.next = temp
            self.tail = temp
        self.length += 1

        return True


ll = LinkedList(1)
ll.append(145)
ll.append(5)


print(ll.print_list())
