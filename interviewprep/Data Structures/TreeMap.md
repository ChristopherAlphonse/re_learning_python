# TreeMap

```py
from sortedcontainers import SortedDict

class TreeMap:
def **init**(self):
self.map = SortedDict()

    def put(self, key, value):
        """ Inserts a key-value pair into the TreeMap. """
        self.map[key] = value

    def get(self, key):
        """ Retrieves the value associated with the given key. """
        return self.map.get(key, None)

    def remove(self, key):
        """ Removes the key-value pair if the key exists. """
        if key in self.map:
            del self.map[key]

    def contains(self, key):
        """ Checks if a key exists in the TreeMap. """
        return key in self.map

    def sub_map(self, from_key, to_key):
        """ Returns a submap within the given key range [from_key, to_key). """
        return {k: self.map[k] for k in self.map.irange(from_key, to_key, (True, False))}

    def first_key(self):
        """ Returns the first (smallest) key. """
        return self.map.peekitem(0)[0] if self.map else None

    def last_key(self):
        """ Returns the last (largest) key. """
        return self.map.peekitem(-1)[0] if self.map else None
```
