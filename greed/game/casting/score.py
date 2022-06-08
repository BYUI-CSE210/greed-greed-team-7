from game.casting.actor import Actor


class Score(Actor):
    """
    This is the score that will accumulate as you pick up either stones or gems in the game "Greed."

    Attributes:
        _points (int): The points.
    """
    def __init__(self):
        super().__init__()
        self._display = ""
        self._points = 0

    def get_points(self):
        """gets the points in the game.
        
        Returns:
            points (int): The current score.
        """
        return self._points

    def display_points(self, display):
        """Displays the points.

        Args: 
            score_counter (int): The score
        """
        return self._display

    def add_points(self, points):
        """Accumulates the points as you gather gems points
        
        Args:
            message (string): The given message.
        """
        self._points += points
        self.set_text(f"Score: {self._points}")








