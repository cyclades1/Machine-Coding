# utils/reservation_system.py
from models.movie import Movie
from models.screen import Screen
from services.seat_service import SeatService
from services.show_service import ShowService
from services.reservation_service import ReservationService

from utils.singleton import SingletonMeta

class ReservationSystem(metaclass=SingletonMeta):
    def __init__(self):
        self.show_service = ShowService()
        self.reservation_service = ReservationService()

    def add_show(self, show_id: str, movie: Movie, screen: Screen, show_time: str):
        self.show_service.add_show(show_id, movie, screen, show_time)

    def view_available_seats(self, show_id: str) -> list:
        show = self.show_service.get_show(show_id)
        if not show:
            raise ValueError("Show not found")
        seat_service = SeatService(show.screen.seats)
        return seat_service.get_available_seats()

    def reserve_seats(self, user_id: str, show_id: str, seat_numbers: list[str]) -> bool:
        show = self.show_service.get_show(show_id)
        if not show:
            raise ValueError("Show not found")

        seat_service = SeatService(show.screen.seats)
        if seat_service.reserve_seats(seat_numbers):
            return self.reservation_service.create_reservation(user_id, show, seat_numbers)
        return False

    def view_reservations(self, user_id: str) -> list:
        return self.reservation_service.view_user_reservations(user_id)
