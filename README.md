Data Structures:

Arrays / List:

-   Read: O(1)
-   Insertion: O(n)
-   Deletion: O(n)
-   Fast at reading but slow at insertion and deletion.

![](/images/list.svg)

Linked Lists:

-   Read: O(n)
-   Insertion: O(1)
-   Deletion: O(1)
-   Slow at reading but efficient for insertion and deletion.

![](/images/linked_list.webp)

HashMaps:

-   Read: O(1)
-   Insertion: O(1)
-   Deletion: O(1)
-   Similar to arrays but with named indexes (keys); unordered but provide fast lookup.

![](/images//map.jpg)
_hash map use linked list and array list for fast memory access and collision handling_

Stacks:

-   Push: O(1)
-   Pop: O(1)
-   Peak: O(1)
-   Follow the LIFO (Last In, First Out) principle; useful for fast retrieval of the topmost element but can be cumbersome for inserting or deleting elements in the middle or end.

![](/images/stack-operations.webp)

Queues:

-   Enqueue: O(1)
-   Dequeue: O(1)
-   Front: O(1)
-   Follow the FIFO (First In, First Out) principle; the first element in line is the first to come out. Think of them as playlists for organizing items in order of arrival.
    ![](/images/que.png)

Trees:

-   Read/Search: O(log n)
-   Insertion: O(log n)
-   Deletion: O(log n)
-   Nodes connected by edges; root, parent-child connections.

![](/images/Treedatastructure.png)

Binary Trees:

-   Efficient searching of ordered values.
-   Follow a binary search property where left child nodes are less than the parent and right child nodes are greater.
-   Useful for tasks like number guessing games or dictionary implementations.

![](/images/B-tree.webp)
Graphs:

-   Traversal/Search: O(V + E) (V: number of vertices, E: number of edges)
-   Insertion: O(1)
-   Deletion: O(1)
-   Versatile models for connections between nodes and edges; can be directed or undirected with no neighboring limit. Can include cycles and weights on paths. Used for tasks like route optimizationData Structures:
