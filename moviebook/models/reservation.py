# models/reservation.py
from typing import List
from models.show import Show

class Reservation:
    def __init__(self, user_id: str, show: Show, seats: List[str]):
        self.user_id = user_id
        self.show = show
        self.seats = seats
