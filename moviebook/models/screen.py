# models/screen.py
from models.seat import Seat

class Screen:
    def __init__(self, screen_id: int, num_seats: int):
        self.screen_id = screen_id
        self.seats = [Seat(f"S{i+1}") for i in range(num_seats)]
