class Feedback:
  # Represents feedback provided by a guest.

  def __init__(self, feedback_id: int, guest: 'Guest', rating: int, comments: str):
      # Initialize a Feedback object.
      # - feedback_id: Unique identifier for the feedback (e.g., 1).
      # - guest: Guest object providing the feedback.
      # - rating: Rating provided by the guest (1-5).
      # - comments: Comments provided by the guest.
      self._feedback_id = feedback_id  # Private attribute for feedback ID
      self._guest = guest  # Private attribute for guest
      self._rating = rating  # Private attribute for rating
      self._comments = comments  # Private attribute for comments

  # Getter Methods
  def get_feedback_id(self) -> int:
      # Returns the feedback ID.
      return self._feedback_id

  def get_guest(self) -> 'Guest':
      # Returns the guest associated with the feedback.
      return self._guest

  def get_rating(self) -> int:
      # Returns the rating provided by the guest.
      return self._rating

  def get_comments(self) -> str:
      # Returns the comments provided by the guest.
      return self._comments

  def __str__(self) -> str:
      # Returns a string representation of the Feedback object.
      return (f"Feedback ID: {self._feedback_id}, Guest: {self._guest.get_name()}, "
              f"Rating: {self._rating}, Comments: {self._comments}")
