# services/show_service.py
from models.show import Show
from models.movie import Movie
from models.screen import Screen

class ShowService:
    def __init__(self):
        self.shows = {}

    def add_show(self, show_id: str, movie: Movie, screen: Screen, show_time: str):
        show = Show(movie, screen, show_time)
        self.shows[show_id] = show

    def get_show(self, show_id: str) -> Show:
        return self.shows.get(show_id)
