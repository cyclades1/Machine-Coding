# notification_system.py

import threading
import queue
import time

class NotificationSystem:
    def __init__(self):
        self.subscribers = set()
        self.message_queue = queue.Queue()
        self.lock = threading.Lock()
        threading.Thread(target=self._deliver_loop, daemon=True).start()

    def subscribe(self, user_id):
        with self.lock:
            self.subscribers.add(user_id)
            print(f"{user_id} subscribed.")

    def unsubscribe(self, user_id):
        with self.lock:
            self.subscribers.discard(user_id)
            print(f"{user_id} unsubscribed.")

    def send_notification(self, message):
        self.message_queue.put(message)

    def _deliver_loop(self):
        while True:
            message = self.message_queue.get()
            with self.lock:
                for user in self.subscribers:
                    print(f"Delivered to {user}: {message}")
            time.sleep(0.5)

if __name__ == "__main__":
    ns = NotificationSystem()
    ns.subscribe("user1")
    ns.subscribe("user2")
    ns.send_notification("Hello Users!")
    time.sleep(1)
    ns.unsubscribe("user1")
    ns.send_notification("Goodbye!")
    time.sleep(2)
