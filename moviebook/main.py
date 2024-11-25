# main.py
from models.movie import Movie
from models.screen import Screen
from utils.reservation_system import ReservationSystem

def test_reservation_system():
    movie = Movie("Inception", 120)
    screen = Screen(screen_id=1, num_seats=5)

    system = ReservationSystem()
    system.add_show(show_id="1", movie=movie, screen=screen, show_time="10:00 AM")

    assert system.view_available_seats("1") == ["S1", "S2", "S3", "S4", "S5"]

    assert system.reserve_seats(user_id="user1", show_id="1", seat_numbers=["S1", "S2"]) == True
    assert system.view_available_seats("1") == ["S3", "S4", "S5"]

    assert system.reserve_seats(user_id="user2", show_id="1", seat_numbers=["S1"]) == False

    reservations = system.view_reservations("user1")
    assert reservations == [ 
        {
            "movie": "Inception",
            "show_time": "10:00 AM",
            "seats": ["S1", "S2"]
        }
    ]

    assert system.reserve_seats(user_id="user2", show_id="1", seat_numbers=["S3", "S4"]) == True
    assert system.view_available_seats("1") == ["S5"]

    print("All tests passed.")

# Run tests
test_reservation_system()
