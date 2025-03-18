# Array List

## When to Use an Array List

Prefer an Array List over a Linked List when:

-   You frequently need to access data at random positions.
-   You need extreme performance on lookups (**O(1)** access time).
-   You know the size of the dataset in advance (resizing incurs a performance penalty).

### Resizing Behavior

-   Arrays typically do not resize automatically.
-   `ArrayList` in Java resizes dynamically, usually doubling in size when full.
-   Resizing takes **O(n)** but happens infrequently, making the **amortized insertion time O(1)**.

## Big O Complexity

### Time Complexity

-   **O(n)** to add or remove an item at the start of the list.
-   **O(1)** to add or remove an item at the end of the list.
-   **O(1)** to access an item via an index.
-   **O(1)** to update or replace an item.
-   **O(n)** to insert or remove an item elsewhere.

### Space Complexity

-   Uses contiguous memory, which improves performance due to data locality.
-   Space required: **O(n)**, where `n` is the number of elements.
