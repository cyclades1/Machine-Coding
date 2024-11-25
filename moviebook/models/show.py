# models/show.py
from typing import List
from models.movie import Movie
from models.screen import Screen

class Show:
    def __init__(self, movie: Movie, screen: Screen, show_time: str):
        self.movie = movie
        self.screen = screen
        self.show_time = show_time

    def get_available_seats(self) -> List[str]:
        return [seat.seat_number for seat in self.screen.seats if not seat.is_reserved]
