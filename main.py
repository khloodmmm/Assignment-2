from room import Room
from guest import Guest
from booking import Booking
from invoice import Invoice
from loyalty_program import LoyaltyProgram
from service_request import ServiceRequest
from feedback import Feedback

# Create a room
room = Room(2002, "Double", ["Table", "TV", "Fridge"], 400.0)

# Create a guest
guest = Guest(1, "Khlood Mohamed", "Khlood.mohamed@hotmail.com")

# Create a booking
booking = Booking(1, guest, room, "2025-03-15", "2025-03-17")

# Add booking to guest's reservation history
guest.add_reservation(booking)

# Create an invoice
invoice = booking.get_invoice()
invoice.set_additional_charges(70.0)  # Add room service charges
invoice.set_discounts(40.0)  # Apply a discount

# Create a loyalty program for the guest
loyalty_program = LoyaltyProgram(guest)
loyalty_program.earn_points(250)  # Earn points for the stay

# Create a service request
service_request = ServiceRequest(1, guest, "Room Service")
service_request.set_request_status("Completed")

# Create feedback
feedback = Feedback(1, guest, 5, "Very good")

# Display details
print(room)
print(guest)
print(booking)
print(invoice)
print(loyalty_program)
print(service_request)
print(feedback)
