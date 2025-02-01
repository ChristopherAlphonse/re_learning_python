class ListNode:
    def __init__(self, val):
        self.value = val
        self.next = None

    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self, val):
        new_ListNode = ListNode(val)
        self.head = new_ListNode
        self.tail = new_ListNode
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value, end=" -> ")
            temp = temp.next
        print()

    def append(self, val):
        new_ListNode = ListNode(val)
        if self.head is None:
            self.head = new_ListNode
            self.tail = new_ListNode
        else:
            self.tail.next = new_ListNode
            self.tail = new_ListNode
        self.length += 1
        return True

    def prepend(self, val):
        new_ListNode = ListNode(val)
        if self.head is None:
            self.head = new_ListNode
            self.tail = new_ListNode
        else:
            new_ListNode.next = self.head
            self.head = new_ListNode
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
        return temp

    def set_value(self, index, val):
        temp = self.get(index)
        if temp is not None:
            temp.value = val
            return True
        return False

    def insert(self, index, value):
        new_ListNode = ListNode(value)
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(new_ListNode)
        if index == self.length:
            return self.append(new_ListNode)
        temp = self.get(index - 1)
        new_ListNode.next = temp.next
        temp.next = new_ListNode
        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            print("Out of bound -1")

        if index == self.length - 1:
            return self.pop()
        if index == 0:
            return self.pop_first()
        prev = self.get(index - 1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp

    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return None

        previous, current = None, head
        while current:
            _next = current.next
            current.next = previous
            previous = current
            current = _next

        return previous


def remove_kth_from_end(ll, k):
    slow = ll.head
    fast = ll.head

    for _ in range(k - 1):
        if fast is None:
            return None
        fast = fast.next

    while fast:
        slow = slow.next
        fast = fast.next
    slow.next = slow.next.next

    return slow


def find_kth_from_end(ll, k):
    slow = ll.head
    fast = ll.head

    for _ in range(k):
        if fast is None:
            return None
        fast = fast.next

    while fast:
        slow = slow.next
        fast = fast.next

    return slow


def reverse_recursively(head):
    if head is None:
        return

    reverse_recursively(head.next)
    print(head, end=' -> ')


my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)
my_linked_list.append(6)
my_linked_list.append(7)
my_linked_list.append(8)


print("Original list:")
my_linked_list.print_list()


reversed_head = my_linked_list.reverseList(my_linked_list.head)
print("\nReversed list:")
current = reversed_head
while current:
    print(current.value, end=" -> ")
    current = current.next
print()


# print("\nRecursively reversed list:")
# reverse_recursively(my_linked_list.head)
