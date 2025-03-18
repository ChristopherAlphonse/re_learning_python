# Linked Lists

## When to Use a Linked List

Prefer a Linked List over an Array or String when:

-   You require very fast insertions or deletions.
-   You don't need random access to items in the list (traversal is sequential).
-   The list size is dynamic and may grow or shrink during execution.

## Big O Complexity

### Time Complexity

-   **O(1)** to add or remove an item at the start of the list.
-   **O(n)** to add or remove an item at the end of the list.
-   **O(n)** to find and access an element via an index.
-   **O(1)** to update an element.
-   **O(n)** to insert or remove an element elsewhere in the list.

## Singly Linked List

A singly linked list contains a reference to the next node:

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
```

## Doubly Linked List

A doubly linked list contains references to both the next and previous nodes:

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
```

## Delete Kth Node from Linked List

-   Use two pointers:
    -   Move the first pointer `k` steps away from the head.
    -   Move both pointers together until the first pointer reaches the end.
    -   Delete the node at the second pointer.

```python
def remove_kth_node_from_end(head, k):
    first = second = head
    for _ in range(k):
        if first is None:
            return head
        first = first.next

    if first is None:
        return head.next

    while first.next:
        first = first.next
        second = second.next

    second.next = second.next.next
    return head
```

## Reverse a Linked List

```python
def reverse_list(head):
    prev = None
    current = head

    while current:
        temp = current.next
        current.next = prev
        prev = current
        current = temp

    return prev
```
