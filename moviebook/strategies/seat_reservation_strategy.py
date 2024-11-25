# strategies/seat_reservation_strategy.py
from typing import List
from models.seat import Seat

class SeatReservationStrategy:
    def reserve_seats(self, seats: List[Seat], seat_numbers: List[str]) -> bool:
        raise NotImplementedError("This method should be overridden.")

class StandardReservationStrategy(SeatReservationStrategy):
    def reserve_seats(self, seats: List[Seat], seat_numbers: List[str]) -> bool:
        selected_seats = []
        for seat in seats:
            if seat.seat_number in seat_numbers:
                if seat.reserve():
                    selected_seats.append(seat)
                else:
                    # Release previously reserved seats if failure
                    for s in selected_seats:
                        s.release()
                    return False
        return True
