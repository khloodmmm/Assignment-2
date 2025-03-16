class Room:
    # Represents a room in the hotel.

    def __init__(self, room_number: int, room_type: str, amenities: list, price_per_night: float):
        # Initialize a Room object.
        #
        # Parameters:
        # - room_number: Unique identifier for the room (e.g., 101).
        # - room_type: Type of room (e.g., single, double, suite).
        # - amenities: List of amenities (e.g., Wi-Fi, TV, mini-bar).
        # - price_per_night: Price per night for the room (e.g., 150.0).
        self._room_number = room_number  # Private attribute for room number
        self._room_type = room_type  # Private attribute for room type
        self._amenities = amenities  # Private attribute for amenities
        self._price_per_night = price_per_night  # Private attribute for price per night
        self._availability_status = True  # Default to available

    # Getter and Setter Methods
    def get_room_number(self) -> int:
        # Returns the room number.
        return self._room_number

    def get_room_type(self) -> str:
        # Returns the room type.
        return self._room_type

    def get_amenities(self) -> list:
        # Returns the list of amenities.
        return self._amenities

    def get_price_per_night(self) -> float:
        # Returns the price per night.
        return self._price_per_night

    def is_available(self) -> bool:
        # Returns the availability status of the room.
        return self._availability_status

    def set_availability(self, status: bool) -> None:
        # Sets the availability status of the room.
        self._availability_status = status

    def __str__(self) -> str:
        # Returns a string representation of the Room object.
        return (f"Room Number: {self._room_number}, Type: {self._room_type}, "
                f"Amenities: {', '.join(self._amenities)}, Price/Night: ${self._price_per_night}, "
                f"Available: {self._availability_status}")
