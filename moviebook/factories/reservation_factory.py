# factories/reservation_factory.py
from models.reservation import Reservation
from models.show import Show

class ReservationFactory:
    @staticmethod
    def create_reservation(user_id: str, show: Show, seats: list) -> Reservation:
        # Any custom reservation creation logic can go here
        return Reservation(user_id=user_id, show=show, seats=seats)
