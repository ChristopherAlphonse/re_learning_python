# WEEK 5

# Problem 1: Greatest NodeProblem 1: Greatest Node

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next


def find_max(head):
    curr_max = head.value
    while head:
        curr_max = max(curr_max, head.value)
        head = head.next

    return curr_max

# head1 = Node(5, Node(6, Node(7, Node(8))))

# # Linked List: 5 -> 6 -> 7 -> 8
# print(find_max(head1))

# head2 = Node(5, Node(8, Node(6, Node(7))))

# # Linked List: 5 -> 8 -> 6 -> 7
# print(find_max(head2))

# Problem 2: Remove Tail


def remove_tail(head):
    if not head or not head.next:
        return None

    current = head

    while current.next and current.next.next:
        current = current.next

    current.next = None
    return head


# head = Node("Isabelle", Node("Alfonso", Node("Cyd")))

# # Linked List: Isabelle -> Alfonso
# print_linked_list(remove_tail(head))

# Problem 3: Delete Duplicates in a Linked List


def delete_dupes(head):

    if not head or not head.next:
        return head

    temp_head = Node(0)
    temp_head.next = head

    current = head
    prev = temp_head

    while current and current.next:
        while current.value == current.next.value:
            current = current.next

        if prev.next == current:
            prev = prev.next
        else:
            prev.next = current.next

        current = current.next

    return temp_head.next


head = Node(1, Node(2, Node(3, Node(3, Node(3, Node(4, Node(5)))))))

# Linked List: 1 -> 2 -> 3 -> 3 -> 3 -> 4 -> 5
# p                       c
# print_linked_list(delete_dupes(head))

# Problem 4: Does it Cycle?


def has_cycle(head):
    fast = head
    slow = head

    while fast and fast.next:
        if fast == slow:
            return True
        slow = slow.next
        fast = fast.next.next

    return False


peach = Node("Peach", Node("Luigi", Node("Mario", Node("Toad"))))

# print(has_cycle(peach))


# Problem 5: Remove Nth Node From End of List

def remove_nth_from_end(head, n):

    dummy = Node(0, head)
    slow = fast = dummy

    for _ in range(n + 1):
        fast = fast.next

    while fast:
        slow = slow.next
        fast = fast.next

    slow.next = slow.next.next
    return dummy.next


head1 = Node("apple", Node("cherry", Node(
    "orange", Node("peach", Node("pear")))))
head2 = Node("Rainbow Trout", Node("Ray"))
head3 = Node("Rainbow Stag")


# print_linked_list(remove_nth_from_end(head1, 2))
# print_linked_list(remove_nth_from_end(head2, 1))
# print_linked_list(remove_nth_from_end(head3, 1))


# Problem 6: Careful Reverse

def reverse_first_k(head, k):
    """
    Reverse the first k elements of a singly linked list.
    If k is greater than the list length, reverse the entire list.
    """
    if not head or k <= 0:
        return head

    prev = None
    curr = head
    next_node = None
    count = 0

    while curr and count < k:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
        count += 1

    head.next = curr

    return prev


head = Node("apple", Node("cherry", Node(
    "orange", Node("peach", Node("pear")))))

print_linked_list(reverse_first_k(head, 3))

# orange -> cherry -> apple -> peach -> pear
