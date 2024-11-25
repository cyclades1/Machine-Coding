from strategies.seat_reservation_strategy import SeatReservationStrategy, StandardReservationStrategy
from models.seat import Seat
class SeatService:
    def __init__(self, seats: list[Seat], strategy: SeatReservationStrategy = StandardReservationStrategy()):
        self.seats = seats
        self.strategy = strategy
    
    def get_available_seats(self) -> list[str]:
        return [seat.seat_number for seat in self.seats if not seat.is_reserved]


    def reserve_seats(self, seat_numbers: list[str]) -> bool:
        return self.strategy.reserve_seats(self.seats, seat_numbers)