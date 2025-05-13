import uuid
import threading
import time
from enum import Enum
from collections import defaultdict


class VehicleType(Enum):
    CAR = "CAR"
    BIKE = "BIKE"
    TRUCK = "TRUCK"


class Vehicle:
    def __init__(self, number: str, v_type: VehicleType):
        self.number = number
        self.type = v_type


class ParkingSpot:
    def __init__(self, spot_id: str, spot_type: VehicleType):
        self.spot_id = spot_id
        self.spot_type = spot_type
        self.vehicle = None

    def is_available(self):
        return self.vehicle is None

    def assign_vehicle(self, vehicle: Vehicle):
        if self.spot_type == vehicle.type and self.is_available():
            self.vehicle = vehicle
            return True
        return False

    def remove_vehicle(self):
        self.vehicle = None


class ParkingFloor:
    def __init__(self, floor_number: int, spots_per_type: int):
        self.floor_number = floor_number
        self.spots = []
        for v_type in VehicleType:
            for i in range(spots_per_type):
                spot_id = f"{floor_number}-{v_type.name}-{i}"
                self.spots.append(ParkingSpot(spot_id, v_type))

    def find_available_spot(self, vehicle_type: VehicleType):
        for spot in self.spots:
            if spot.spot_type == vehicle_type and spot.is_available():
                return spot
        return None


class Ticket:
    def __init__(self, vehicle: Vehicle, floor: int, spot: ParkingSpot):
        self.ticket_id = str(uuid.uuid4())
        self.vehicle = vehicle
        self.floor = floor
        self.spot_id = spot.spot_id
        self.entry_time = time.time()
        self.exit_time = None


class ParkingLot:
    def __init__(self, num_floors: int, spots_per_type: int):
        self.floors = [ParkingFloor(i, spots_per_type) for i in range(num_floors)]
        self.active_tickets = {}
        self.lock = threading.Lock()

    def park_vehicle(self, vehicle: Vehicle):
        with self.lock:
            for floor in self.floors:
                spot = floor.find_available_spot(vehicle.type)
                if spot:
                    spot.assign_vehicle(vehicle)
                    ticket = Ticket(vehicle, floor.floor_number, spot)
                    self.active_tickets[ticket.ticket_id] = (floor, spot, ticket)
                    print(f"[{threading.current_thread().name}] Parked {vehicle.number} at {spot.spot_id}")
                    return ticket
            print(f"[{threading.current_thread().name}] No spot available for {vehicle.number}")
            return None

    def unpark_vehicle(self, ticket: Ticket):
        with self.lock:
            record = self.active_tickets.pop(ticket.ticket_id, None)
            if record:
                floor, spot, real_ticket = record
                spot.remove_vehicle()
                ticket.exit_time = time.time()
                fee = self.calculate_fee(real_ticket)
                print(f"[{threading.current_thread().name}] Vehicle {ticket.vehicle.number} exited from {spot.spot_id}. Fee: ₹{fee:.2f}")
            else:
                print("Invalid Ticket")

    def calculate_fee(self, ticket: Ticket):
        duration_minutes = (time.time() - ticket.entry_time) / 60
        rate_per_minute = 2.0
        return max(10, duration_minutes * rate_per_minute)  # Minimum ₹10


# -------- Multithreaded Simulation -------- #

def simulate_vehicle(lot: ParkingLot, number: str, v_type: VehicleType, wait_before_exit=2):
    vehicle = Vehicle(number, v_type)
    ticket = lot.park_vehicle(vehicle)
    if ticket:
        time.sleep(wait_before_exit)  # Simulate time parked
        lot.unpark_vehicle(ticket)


if __name__ == "__main__":
    lot = ParkingLot(num_floors=2, spots_per_type=2)

    vehicles = [
        ("KA01AA0001", VehicleType.CAR),
        ("KA01AA0002", VehicleType.CAR),
        ("KA01BB0003", VehicleType.BIKE),
        ("KA01CC0004", VehicleType.TRUCK),
        ("KA01DD0005", VehicleType.BIKE),
        ("KA01EE0006", VehicleType.CAR),
    ]

    threads = []
    for number, v_type in vehicles:
        t = threading.Thread(target=simulate_vehicle, args=(lot, number, v_type, 1), name=number)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("Simulation complete.")
