# thread_pool.py

import threading
import queue
import time

class ThreadPoolExecutor:
    def __init__(self, max_workers):
        self.tasks = queue.Queue()
        self.threads = []
        self.shutdown_flag = False

        for _ in range(max_workers):
            t = threading.Thread(target=self._worker)
            t.daemon = True
            t.start()
            self.threads.append(t)

    def submit(self, fn, *args, **kwargs):
        self.tasks.put((fn, args, kwargs))

    def _worker(self):
        while not self.shutdown_flag:
            try:
                fn, args, kwargs = self.tasks.get(timeout=1)
                fn(*args, **kwargs)
                self.tasks.task_done()
            except queue.Empty:
                continue

    def shutdown(self, wait=True):
        self.shutdown_flag = True
        if wait:
            for t in self.threads:
                t.join()

def sample_task(name, delay):
    print(f"{name} started")
    time.sleep(delay)
    print(f"{name} completed")

if __name__ == "__main__":
    pool = ThreadPoolExecutor(max_workers=3)
    for i in range(5):
        pool.submit(sample_task, f"Task-{i+1}", 2)
    pool.shutdown(wait=True)
    print("All tasks completed.")
