# kv_store.py

import threading
import time

class KeyValueStore:
    def __init__(self):
        self.store = {}
        self.ttl = {}
        self.lock = threading.Lock()
        threading.Thread(target=self._ttl_cleaner, daemon=True).start()

    def put(self, key, value, ttl_seconds=None):
        with self.lock:
            self.store[key] = value
            if ttl_seconds:
                self.ttl[key] = time.time() + ttl_seconds

    def get(self, key):
        with self.lock:
            if key in self.ttl and time.time() > self.ttl[key]:
                del self.store[key]
                del self.ttl[key]
                return None
            return self.store.get(key)

    def delete(self, key):
        with self.lock:
            self.store.pop(key, None)
            self.ttl.pop(key, None)

    def _ttl_cleaner(self):
        while True:
            with self.lock:
                expired = [k for k, v in self.ttl.items() if time.time() > v]
                for k in expired:
                    self.store.pop(k, None)
                    self.ttl.pop(k, None)
            time.sleep(1)

if __name__ == "__main__":
    kv = KeyValueStore()
    kv.put("foo", "bar", ttl_seconds=2)
    print("Initial:", kv.get("foo"))
    time.sleep(3)
    print("After TTL:", kv.get("foo"))
