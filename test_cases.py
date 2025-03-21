from room import Room
from guest import Guest
from booking import Booking
from invoice import Invoice
from loyalty_program import LoyaltyProgram
from service_request import ServiceRequest
from feedback import Feedback

# Test Case 1: Guest Account Creation
def test_guest_account_creation():
    print("\n=== Test Case 1: Guest Account Creation ===")

    # Example 1
    guest1 = Guest(1, "Khlood Mohamed", "khlood.mohamed@hotmail.com")
    print("Guest 1 Created:", guest1)

    # Example 2
    guest2 = Guest(2, "Ali Mohamed", "ali.ahmed@gmail.com")
    print("Guest 2 Created:", guest2)

# Test Case 2: Searching for Available Rooms
def test_search_available_rooms():
    print("\n=== Test Case 2: Searching for Available Rooms ===")

    # Create rooms
    room1 = Room(2002, "Double", ["Table", "TV", "Fridge"], 400.0)
    room2 = Room(2003, "Single", ["Table", "TV"], 300.0)

    # Example 1: Search for available rooms
    print("Available Rooms:")
    if room1.is_available():
        print(room1)
    if room2.is_available():
        print(room2)

    # Example 2: Mark a room as unavailable and search again
    room1.set_availability(False)
    print("\nAfter marking Room 2002 as unavailable:")
    if room1.is_available():
        print(room1)
    if room2.is_available():
        print(room2)

# Test Case 3: Making a Room Reservation
def test_make_reservation():
    print("\n=== Test Case 3: Making a Room Reservation ===")

    # Create a guest and a room
    guest = Guest(1, "Khlood Mohamed", "khlood.mohamed@hotmail.com")
    room = Room(2002, "Double", ["Table", "TV", "Fridge"], 400.0)

    # Example 1: Make a reservation
    booking1 = Booking(1001, guest, room, "2025-03-15", "2025-03-17")
    guest.add_reservation(booking1)
    print("Booking 1 Created:", booking1)

    # Example 2: Make another reservation
    booking2 = Booking(1002, guest, room, "2025-03-18", "2025-03-20")
    guest.add_reservation(booking2)
    print("Booking 2 Created:", booking2)

# Test Case 4: Booking Confirmation Notification
def test_booking_confirmation():
    print("\n=== Test Case 4: Booking Confirmation Notification ===")

    # Create a guest, room, and booking
    guest = Guest(1, "Khlood Mohamed", "khlood.mohamed@hotmail.com")
    room = Room(2002, "Double", ["Table", "TV", "Fridge"], 400.0)
    booking = Booking(1001, guest, room, "2025-03-15", "2025-03-17")

    # Example 1: Confirm booking
    print("Booking Confirmation for Booking ID:", booking.get_booking_id())
    print("Guest:", booking.get_guest().get_name())
    print("Room:", booking.get_room().get_room_number())
    print("Check-In:", booking.get_check_in_date())
    print("Check-Out:", booking.get_check_out_date())

    # Example 2: Confirm another booking
    booking2 = Booking(1002, guest, room, "2025-03-18", "2025-03-20")
    print("\nBooking Confirmation for Booking ID:", booking2.get_booking_id())
    print("Guest:", booking2.get_guest().get_name())
    print("Room:", booking2.get_room().get_room_number())
    print("Check-In:", booking2.get_check_in_date())
    print("Check-Out:", booking2.get_check_out_date())

# Test Case 5: Invoice Generation for a Booking
def test_invoice_generation():
    print("\n=== Test Case 5: Invoice Generation for a Booking ===")

    # Create a guest, room, and booking
    guest = Guest(1, "Khlood Mohamed", "khlood.mohamed@hotmail.com")
    room = Room(2002, "Double", ["Table", "TV", "Fridge"], 400.0)
    booking = Booking(1001, guest, room, "2025-03-15", "2025-03-17")

    # Generate invoice
    invoice = booking.get_invoice()
    invoice.set_additional_charges(70.0)  # Add room service charges
    invoice.set_discounts(40.0)  # Apply a discount

    # Example 1: Display invoice
    print("Invoice for Booking ID:", invoice.get_booking().get_booking_id())
    print("Total Amount:", invoice.calculate_total_amount())

    # Example 2: Another invoice
    booking2 = Booking(1002, guest, room, "2025-03-18", "2025-03-20")
    invoice2 = booking2.get_invoice()
    invoice2.set_additional_charges(50.0)
    invoice2.set_discounts(20.0)
    print("\nInvoice for Booking ID:", invoice2.get_booking().get_booking_id())
    print("Total Amount:", invoice2.calculate_total_amount())

# Test Case 6: Processing Different Payment Methods
def test_payment_processing():
    print("\n=== Test Case 6: Processing Different Payment Methods ===")

    # Create a guest, room, and booking
    guest = Guest(1, "Khlood Mohamed", "khlood.mohamed@hotmail.com")
    room = Room(2002, "Double", ["Table", "TV", "Fridge"], 400.0)
    booking = Booking(1001, guest, room, "2025-03-15", "2025-03-17")
    invoice = booking.get_invoice()

    # Example 1: Pay with credit card
    print("Payment Method: Credit Card")
    print("Invoice Total:", invoice.calculate_total_amount())
    print("Payment Successful!")

    # Example 2: Pay with mobile wallet
    print("\nPayment Method: Mobile Wallet")
    print("Invoice Total:", invoice.calculate_total_amount())
    print("Payment Successful!")

# Test Case 7: Displaying Reservation History
def test_reservation_history():
    print("\n=== Test Case 7: Displaying Reservation History ===")

    # Create a guest and add bookings
    guest = Guest(1, "Khlood Mohamed", "khlood.mohamed@hotmail.com")
    room = Room(2002, "Double", ["Table", "TV", "Fridge"], 400.0)
    booking1 = Booking(1001, guest, room, "2025-03-15", "2025-03-17")
    booking2 = Booking(1002, guest, room, "2025-03-18", "2025-03-20")
    guest.add_reservation(booking1)
    guest.add_reservation(booking2)

    # Example 1: Display reservation history
    print("Reservation History for Guest:", guest.get_name())
    for booking in guest.view_reservation_history():
        print(booking)

    # Example 2: Add another booking and display history
    booking3 = Booking(1003, guest, room, "2025-03-21", "2025-03-23")
    guest.add_reservation(booking3)
    print("\nUpdated Reservation History for Guest:", guest.get_name())
    for booking in guest.view_reservation_history():
        print(booking)

# Test Case 8: Cancellation of a Reservation
def test_cancel_reservation():
    print("\n=== Test Case 8: Cancellation of a Reservation ===")

    # Create a guest, room, and booking
    guest = Guest(1, "Khlood Mohamed", "khlood.mohamed@hotmail.com")
    room = Room(2002, "Double", ["Table", "TV", "Fridge"], 400.0)
    booking = Booking(1001, guest, room, "2025-03-15", "2025-03-17")
    guest.add_reservation(booking)

    # Example 1: Cancel a reservation
    print("Before Cancellation:")
    print(booking)
    print("Room Availability:", room.is_available())

    # Cancel booking
    guest.view_reservation_history().remove(booking)
    room.set_availability(True)
    print("\nAfter Cancellation:")
    print("Room Availability:", room.is_available())

    # Example 2: Cancel another reservation
    booking2 = Booking(1002, guest, room, "2025-03-18", "2025-03-20")
    guest.add_reservation(booking2)
    print("\nBefore Cancellation:")
    print(booking2)
    print("Room Availability:", room.is_available())

    # Cancel booking
    guest.view_reservation_history().remove(booking2)
    room.set_availability(True)
    print("\nAfter Cancellation:")
    print("Room Availability:", room.is_available())

# Run all test cases
if __name__ == "__main__":
    test_guest_account_creation()
    test_search_available_rooms()
    test_make_reservation()
    test_booking_confirmation()
    test_invoice_generation()
    test_payment_processing()
    test_reservation_history()
    test_cancel_reservation()
