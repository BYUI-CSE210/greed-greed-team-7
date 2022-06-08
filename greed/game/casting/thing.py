from game.casting.actor import Actor


class Thing(Actor):
    """
    A thing that falls from the sky. It can be either a stone or a gem.

    Attributes: 
        _gem (string): The things that fall from the sky that you want to collect. Worth 100 points.
        _stone (string): The things that fall from the sky that you want to avoid. Worth -100 points
    """

    def __init__(self):
        super().__init__()
        self._gem = ""
        self._stone = ""
    
    def get_gem(self):
        """Establishes the gem in the Greed game

        Args:
            message (string): The things that displays *

        """
        return self._gem

    def get_stone(self):
        """Establishes the stone in the Greed game

        Args:
            message (string): The things that displays o
        
        """
        return self._stone

    
