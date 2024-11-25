# models/seat.py
import threading

class Seat:
    def __init__(self, seat_number: str):
        self.seat_number = seat_number
        self.is_reserved = False
        self.lock = threading.Lock()

    def reserve(self) -> bool:
        with self.lock:
            if not self.is_reserved:
                self.is_reserved = True
                return True
            return False

    def release(self) -> None:
        with self.lock:
            self.is_reserved = False
