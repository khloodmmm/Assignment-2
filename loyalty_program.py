class LoyaltyProgram:
  # Represents a loyalty rewards program for guests.

  def __init__(self, guest: 'Guest'):
      # Initialize a LoyaltyProgram object.
      # - guest: Guest object associated with the loyalty program.
      self._guest = guest  # Private attribute for guest
      self._points_earned = 0  # Default to 0 points earned
      self._points_redeemed = 0  # Default to 0 points redeemed

  # Getter and Setter Methods
  def get_guest(self) -> 'Guest':
      # Returns the guest associated with the loyalty program.
      return self._guest

  def get_points_earned(self) -> int:
      # Returns the points earned by the guest.
      return self._points_earned

  def earn_points(self, points: int) -> None:
      # Adds points to the guest's loyalty account.
      self._points_earned += points

  def get_points_redeemed(self) -> int:
      # Returns the points redeemed by the guest.
      return self._points_redeemed

  def redeem_points(self, points: int) -> None:
      # Redeems points from the guest's loyalty account.
      if points <= self._points_earned:
          self._points_redeemed += points
          self._points_earned -= points
      else:
          raise ValueError("Not enough points to redeem.")

  def __str__(self) -> str:
      # Returns a string representation of the LoyaltyProgram object.
      return (f"Loyalty Program for Guest: {self._guest.get_name()}, "
              f"Points Earned: {self._points_earned}, Points Redeemed: {self._points_redeemed}")
