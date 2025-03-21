from room import Room
from guest import Guest
from invoice import Invoice

class Booking:
    # Represents a reservation made by a guest.

    def __init__(self, booking_id: int, guest: Guest, room: Room, check_in_date: str, check_out_date: str):
        # Initialize a Booking object.
        # - booking_id: Unique identifier for the booking (e.g., 1).
        # - guest: Guest object making the booking.
        # - room: Room object being booked.
        # - check_in_date: Check-in date (format: YYYY-MM-DD).
        # - check_out_date: Check-out date (format: YYYY-MM-DD).
        self._booking_id = booking_id  # Private attribute for booking ID
        self._guest = guest  # Private attribute for guest
        self._room = room  # Private attribute for room
        self._check_in_date = check_in_date  # Private attribute for check-in date
        self._check_out_date = check_out_date  # Private attribute for check-out date
        self._total_cost = self.calculate_total_cost()  # Private attribute for total cost
        self._invoice = Invoice(self._booking_id, self)  # Private attribute for invoice

    # Getter Methods
    def get_booking_id(self) -> int:
        # Returns the booking ID.
        return self._booking_id

    def get_guest(self) -> Guest:
        # Returns the guest associated with the booking.
        return self._guest

    def get_room(self) -> Room:
        # Returns the room associated with the booking.
        return self._room

    def get_check_in_date(self) -> str:
        # Returns the check-in date.
        return self._check_in_date

    def get_check_out_date(self) -> str:
        # Returns the check-out date.
        return self._check_out_date

    def get_total_cost(self) -> float:
        # Returns the total cost of the booking.
        return self._total_cost

    def get_invoice(self) -> 'Invoice':
        # Returns the invoice associated with the booking.
        return self._invoice

    def calculate_total_cost(self) -> float:
        # Calculates the total cost of the booking based on the number of nights.
        from datetime import datetime
        check_in = datetime.strptime(self._check_in_date, "%Y-%m-%d")
        check_out = datetime.strptime(self._check_out_date, "%Y-%m-%d")
        nights = (check_out - check_in).days  # Calculate the number of nights
        return nights * self._room.get_price_per_night()  # Total cost = nights * price per night

    def __str__(self) -> str:
        # Returns a string representation of the Booking object.
        return (f"Booking ID: {self._booking_id}, Guest: {self._guest.get_name()}, "
                f"Room: {self._room.get_room_number()}, Check-In: {self._check_in_date}, "
                f"Check-Out: {self._check_out_date}, Total Cost: AED{self._total_cost}")
