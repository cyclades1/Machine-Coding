import time
import threading
from collections import deque

class BoundedBlockingQueue:
    def __init__(self, capacity: int):
        self.queue = deque()
        self.capacity = capacity
        self.lock = threading.Lock()
        self.not_empty = threading.Condition(self.lock)
        self.not_full = threading.Condition(self.lock)

    def enqueue(self, item):
        with self.not_full:
            while len(self.queue) == self.capacity:
                self.not_full.wait()
            self.queue.append(item)
            print(f"Enqueued: {item}")
            self.not_empty.notify()  # Notify one waiting thread in dequeue

    def dequeue(self):
        with self.not_empty:
            while len(self.queue) == 0:
                self.not_empty.wait()
            item = self.queue.popleft()
            print(f"Dequeued: {item}")
            self.not_full.notify()  # Notify one waiting thread in enqueue
            return item

    def size(self):
        with self.lock:
            return len(self.queue)



def producer(q, items):
    for item in items:
        q.enqueue(item)
        time.sleep(0.1)

def consumer(q, count):
    for _ in range(count):
        q.dequeue()
        time.sleep(0.2)

if __name__ == "__main__":
    bbqueue = BoundedBlockingQueue(2)
    
    t1 = threading.Thread(target=producer, args=(bbqueue, [1, 2, 3, 4, 5]))
    t2 = threading.Thread(target=consumer, args=(bbqueue, 5))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Final size:", bbqueue.size())
