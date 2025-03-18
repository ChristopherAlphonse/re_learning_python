# Hash Table

A hash table is typically implemented using an array of linked lists and a hash function. The hash function determines the position in the array using the modulo operation.

### Steps

1. Compute the hash code of the given key. Different keys may produce the same hash code, leading to collisions.
2. Use the hash code to compute the array index: `hash(key) % array_length`. Collisions can occur when different keys map to the same index.
3. Store the key-value pair in a linked list at the computed index to handle collisions.

To minimize collisions, hash tables are typically kept around 50% full. This prevents performance degradation but requires more memory compared to a standard array.

## Big O Complexity

-   **Best case (Amortized):** O(1) for lookup, insertion, and deletion.
-   **Worst case:** O(n) when multiple keys collide and form a long linked list.

### Alternative Implementations

Instead of linked lists, a hash table can use a binary search tree (BST) to handle collisions. This reduces the worst-case time complexity to **O(log n)** while also allowing in-order key iteration.
