class ServiceRequest:
    # Represents a service request made by a guest.

    def __init__(self, request_id: int, guest: 'Guest', service_type: str):
        # Initialize a ServiceRequest object.
        #
        # Parameters:
        # - request_id: Unique identifier for the request (e.g., 1).
        # - guest: Guest object making the request.
        # - service_type: Type of service requested (e.g., housekeeping, room service).
        self._request_id = request_id  # Private attribute for request ID
        self._guest = guest  # Private attribute for guest
        self._service_type = service_type  # Private attribute for service type
        self._request_status = "Pending"  # Default status

    # Getter and Setter Methods
    def get_request_id(self) -> int:
        # Returns the request ID.
        return self._request_id

    def get_guest(self) -> 'Guest':
        # Returns the guest associated with the request.
        return self._guest

    def get_service_type(self) -> str:
        # Returns the type of service requested.
        return self._service_type

    def get_request_status(self) -> str:
        # Returns the status of the request.
        return self._request_status

    def set_request_status(self, status: str) -> None:
        # Sets the status of the request.
        self._request_status = status

    def __str__(self) -> str:
        # Returns a string representation of the ServiceRequest object.
        return (f"Request ID: {self._request_id}, Guest: {self._guest.get_name()}, "
                f"Service Type: {self._service_type}, Status: {self._request_status}")
