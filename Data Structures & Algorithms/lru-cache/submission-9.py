class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.LRU = Node(0,0)
        self.MRU = Node(0,0)
        self.LRU.next = self.MRU
        self.MRU.prev = self.LRU
        self.cap = capacity
        self.cache = {}
    
    # remove node from list
    def _remove(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    # add node to mru
    def _insert(self, node):
        prev = self.MRU.prev
        prev.next = node
        node.next = self.MRU
        node.prev = prev
        self.MRU.prev = node
        

    def get(self, key: int) -> int:
        if key in self.cache:
            self._remove(self.cache[key])
            self._insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])

        self.cache[key] = Node(key, value)
        
        self._insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.LRU.next
            self._remove(lru)
            del self.cache[lru.key]
        
