import threading
import time

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # key -> node
        self.head = Node(0, 0)  # dummy head
        self.tail = Node(0, 0)  # dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head
        self.lock = threading.Lock()

    def _add_node(self, node):
        """Add to the front (right after head)"""
        nxt = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = nxt
        nxt.prev = node

    def _remove_node(self, node):
        """Remove node from the list"""
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    def _move_to_front(self, node):
        """Move accessed node to the front"""
        self._remove_node(node)
        self._add_node(node)

    def _evict_lru(self):
        """Remove least recently used node (before tail)"""
        lru = self.tail.prev
        self._remove_node(lru)
        del self.cache[lru.key]

    def get(self, key: int) -> int:
        with self.lock:
            if key not in self.cache:
                return -1
            node = self.cache[key]
            self._move_to_front(node)
            return node.value

    def put(self, key: int, value: int) -> None:
        with self.lock:
            if key in self.cache:
                node = self.cache[key]
                node.value = value
                self._move_to_front(node)
            else:
                if len(self.cache) >= self.capacity:
                    self._evict_lru()
                new_node = Node(key, value)
                self.cache[key] = new_node
                self._add_node(new_node)




def worker(cache: LRUCache, key, value):
    cache.put(key, value)
    print(f"Put: ({key}, {value})")
    time.sleep(0.1)
    val = cache.get(key)
    print(f"Get: {key} -> {val}")

if __name__ == "__main__":
    cache = LRUCache(2)
    t1 = threading.Thread(target=worker, args=(cache, 1, 100))
    t2 = threading.Thread(target=worker, args=(cache, 2, 200))
    t3 = threading.Thread(target=worker, args=(cache, 3, 300))

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()
