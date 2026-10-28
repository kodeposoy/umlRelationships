class Room:
    def __init__(self, name: str, area_sqft: float):
        self.name = name
        self.area_sqft = area_sqft

    def get_details(self) -> str:
        return f"Room: {self.name} ({self.area_sqft} sq ft)"


class House:
    def __init__(self, address: str):
        self.address = address
        self.rooms = []

    def add_room(self, name: str, area_sqft: float):
        # In Composition, the parent creates and owns the lifecycle of the child objects
        room = Room(name, area_sqft)
        self.rooms.append(room)

    def total_area(self) -> float:
        return sum(room.area_sqft for room in self.rooms)

    def display_floor_plan(self):
        print(f"--- House at {self.address} (Total: {self.total_area()} sq ft) ---")
        for room in self.rooms:
            print(f" - {room.get_details()}")


if __name__ == "__main__":
    house = House("123 Maple Street")
    house.add_room("Living Room", 350.0)
    house.add_room("Master Bedroom", 250.0)
    house.add_room("Kitchen", 180.0)
    house.display_floor_plan()
