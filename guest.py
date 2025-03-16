from booking import Booking

class Guest:
    # Represents a guest staying at the hotel.

    def __init__(self, guest_id: int, name: str, contact_info: str):
        # Initialize a Guest object.
        #
        # Parameters:
        # - guest_id: Unique identifier for the guest (e.g., 1).
        # - name: Name of the guest (e.g., John Doe).
        # - contact_info: Contact information of the guest (e.g., john.doe@example.com).
        self._guest_id = guest_id  # Private attribute for guest ID
        self._name = name  # Private attribute for guest name
        self._contact_info = contact_info  # Private attribute for contact info
        self._reservation_history = []  # List to store booking history
        self._loyalty_status = "None"  # Default loyalty status

    # Getter and Setter Methods
    def get_guest_id(self) -> int:
        # Returns the guest ID.
        return self._guest_id

    def get_name(self) -> str:
        # Returns the guest's name.
        return self._name

    def get_contact_info(self) -> str:
        # Returns the guest's contact information.
        return self._contact_info

    def get_loyalty_status(self) -> str:
        # Returns the guest's loyalty status.
        return self._loyalty_status

    def set_loyalty_status(self, status: str) -> None:
        # Sets the guest's loyalty status.
        self._loyalty_status = status

    def add_reservation(self, booking: Booking) -> None:
        # Adds a booking to the guest's reservation history.
        self._reservation_history.append(booking)

    def view_reservation_history(self) -> list:
        # Returns the guest's reservation history.
        return self._reservation_history

    def __str__(self) -> str:
        # Returns a string representation of the Guest object.
        return (f"Guest ID: {self._guest_id}, Name: {self._name}, "
                f"Contact Info: {self._contact_info}, Loyalty Status: {self._loyalty_status}")
