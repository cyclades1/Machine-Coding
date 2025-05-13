from abc import ABC, abstractmethod
import threading
import time
from collections import deque

class RateLimiter(ABC):
    @abstractmethod
    def allow_request(self) -> bool:
        pass


class TokenBucketRateLimiter(RateLimiter):
    def __init__(self, capacity: int, refill_rate_per_sec: float):
        self.capacity = capacity
        self.tokens = capacity
        self.refill_rate = refill_rate_per_sec
        self.last_refill_timestamp = time.time()
        self.lock = threading.Lock()

    def allow_request(self) -> bool:
        with self.lock:
            now = time.time()
            elapsed = now - self.last_refill_timestamp
            added_tokens = elapsed * self.refill_rate
            self.tokens = min(self.capacity, self.tokens + added_tokens)
            self.last_refill_timestamp = now

            if self.tokens >= 1:
                self.tokens -= 1
                return True
            return False


class LeakyBucketRateLimiter(RateLimiter):
    def __init__(self, capacity: int, leak_rate_per_sec: float):
        self.capacity = capacity
        self.leak_rate = leak_rate_per_sec
        self.queue = deque()
        self.lock = threading.Lock()
        self.last_check = time.time()

    def allow_request(self) -> bool:
        with self.lock:
            now = time.time()
            elapsed = now - self.last_check
            leaked = int(elapsed * self.leak_rate)
            for _ in range(min(leaked, len(self.queue))):
                self.queue.popleft()
            self.last_check = now

            if len(self.queue) < self.capacity:
                self.queue.append(now)
                return True
            return False
        
class RateLimiterFactory:
    @staticmethod
    def create_limiter(limiter_type: str, capacity: int, rate: float) -> RateLimiter:
        if limiter_type == "token":
            return TokenBucketRateLimiter(capacity, rate)
        elif limiter_type == "leaky":
            return LeakyBucketRateLimiter(capacity, rate)
        else:
            raise ValueError("Unsupported limiter type")

def simulate_traffic(limiter: RateLimiter, thread_name: str):
    for i in range(10):
        allowed = limiter.allow_request()
        print(f"[{thread_name}] Request {i+1}: {'Allowed' if allowed else 'Blocked'}")
        time.sleep(0.2)

if __name__ == "__main__":
    # Choose either 'token' or 'leaky'
    limiter = RateLimiterFactory.create_limiter("token", capacity=5, rate=2.0)

    threads = []
    for i in range(3):
        t = threading.Thread(target=simulate_traffic, args=(limiter, f"Thread-{i+1}"))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
