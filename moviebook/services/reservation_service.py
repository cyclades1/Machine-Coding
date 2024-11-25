# services/reservation_service.py
from typing import List, Dict
from models.show import Show
from observers.notification_service import NotificationService
from factories.reservation_factory import ReservationFactory

class ReservationService:
    def __init__(self):
        self.reservations = []
        self.notification_service = NotificationService()

    def create_reservation(self, user_id: str, show: Show, seats: List[str]) -> bool:
        reservation = ReservationFactory.create_reservation(user_id, show, seats)
        self.reservations.append(reservation)
        self.notification_service.notify_user(user_id, f"Your reservation for seats {seats} is confirmed.")
        return True

    def view_user_reservations(self, user_id: str) -> List[Dict]:
        return [
            {
                "movie": reservation.show.movie.title,
                "show_time": reservation.show.show_time,
                "seats": reservation.seats
            }
            for reservation in self.reservations if reservation.user_id == user_id
        ]
