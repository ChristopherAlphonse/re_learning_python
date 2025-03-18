# LRU Cache

A Least Recently Used Cache is typically implemented with a Doubly-Linked List and a Map:

```python
class Entry:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = Entry(0, 0)
        self.tail = Entry(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def insert_head(self, entry: Entry):
        entry.prev = self.head
        entry.next = self.head.next
        self.head.next.prev = entry
        self.head.next = entry

    def remove(self, entry: Entry):
        entry.prev.next = entry.next
        entry.next.prev = entry.prev

    def remove_tail(self) -> int:
        node = self.tail.prev
        key = node.key
        self.remove(node)
        return key

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.list = DoublyLinkedList()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self._update(key, self.cache[key])
        return self.cache[key].value

    def put(self, key: int, value: int):
        if key in self.cache:
            self.list.remove(self.cache[key])
        elif len(self.cache) >= self.capacity:
            removed_key = self.list.remove_tail()
            del self.cache[removed_key]

        new_entry = Entry(key, value)
        self.list.insert_head(new_entry)
        self.cache[key] = new_entry

    def _update(self, key: int, entry: Entry):
        self.list.remove(entry)
        self.list.insert_head(entry)
        self.cache[key] = entry

```
