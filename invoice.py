class Invoice:
    # Represents an invoice for a booking.

    def __init__(self, invoice_id: int, booking: 'Booking'):
        # Initialize an Invoice object.
        #
        # Parameters:
        # - invoice_id: Unique identifier for the invoice (e.g., 1).
        # - booking: Booking object associated with the invoice.
        self._invoice_id = invoice_id  # Private attribute for invoice ID
        self._booking = booking  # Private attribute for booking
        self._additional_charges = 0.0  # Default to no additional charges
        self._discounts = 0.0  # Default to no discounts

    # Getter and Setter Methods
    def get_invoice_id(self) -> int:
        # Returns the invoice ID.
        return self._invoice_id

    def get_booking(self) -> 'Booking':
        # Returns the booking associated with the invoice.
        return self._booking

    def get_additional_charges(self) -> float:
        # Returns the additional charges.
        return self._additional_charges

    def set_additional_charges(self, charges: float) -> None:
        # Sets the additional charges.
        self._additional_charges = charges

    def get_discounts(self) -> float:
        # Returns the discounts.
        return self._discounts

    def set_discounts(self, discounts: float) -> None:
        # Sets the discounts.
        self._discounts = discounts

    def calculate_total_amount(self) -> float:
        # Calculates the total amount to be paid.
        return self._booking.get_total_cost() + self._additional_charges - self._discounts

    def __str__(self) -> str:
        # Returns a string representation of the Invoice object.
        return (f"Invoice ID: {self._invoice_id}, Booking ID: {self._booking.get_booking_id()}, "
                f"Total Amount: ${self.calculate_total_amount()}")
