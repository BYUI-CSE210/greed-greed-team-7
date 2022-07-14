from game.casting.actor import Actor
import random


class RockGem(Actor):
    """
    A thing that falls from the sky. It can be either a rock or a gem.

    Attributes: 
        _gem (string): The things that fall from the sky that you want to collect. Worth 100 points.
        _rock (string): The things that fall from the sky that you want to avoid. Worth -100 points
        _special_item (int): Random number to create a bigger "Special" item. Worth 1000 points for Gems & -1000 point for rocks
    """

    def __init__(self):
        super().__init__()
        self._gem = ""
        self._rock = 0
        self._special_item = 0
    
    def get_gem(self):
        """Establishes the gem in the Greed game

        Args:
            self._gem (string): The gem that you want to collect

        """
        return self._gem

    def get_rock(self):
        """Establishes the rock in the Greed game

        Args:
            self._rock (string): The rock that you want to avoid
        
        """
        return self._rock

    def get_special_item(self):
        """Returns a random number. When that number equals 100, a larger object that carries a different score change is created
        
        (Item generation & Score Change are handled in the Director class)
        
        Args:
            special_item (int): Random number to create a bigger object
        """
        self._special_item = random.randint(0, 250)
        if self._special_item == 100:
            self._special_item = True
        return self._special_item