from game.shared.point import Point
from game.shared.color import Color
from game.casting.rock_gem import RockGem

import random

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.
    Attributes:
        _keyboard_service (KeyboardService): For getting directional input.
        _video_service (VideoService): For providing video output.
    """

    def __init__(self, keyboard_service, video_service):
        """Constructs a new Director using the specified keyboard and video services.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
            video_service (VideoService): An instance of VideoService.
        """
        self._keyboard_service = keyboard_service
        self._video_service = video_service
        
    def start_game(self, cast):
        """Starts the game using the given cast. Runs the main game loop.
        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.open_window()
        while self._video_service.is_window_open():
            self._get_inputs(cast)
            self._do_updates(cast)
            self._do_outputs(cast)
        self._video_service.close_window()

    def _get_inputs(self, cast):
        """Gets directional input from the keyboard and applies it to the robot.
        
        Args:
            cast (Cast): The cast of actors.
        """
        player = cast.get_first_actor("player")
        velocity = self._keyboard_service.get_direction()
        player.set_velocity(velocity)
        
          

    def _do_updates(self, cast):
        """Updates the robot's position and resolves any collisions with artifacts.
        
        Args:
            cast (Cast): The cast of actors.
        """

        # Color list That we use for our gems and Rocks.
        green = Color(0, 255, 0)
        blue = Color(0, 0, 255)
        red = Color(255, 0, 0)
        white = Color(255, 255, 255)
        random_color = Color(random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))

        # Falling Objects

        #Creating instances for each one of the rocks and gems
        rock = RockGem()
        green_gem = RockGem()
        light_blue_gem = RockGem()
        blue_gem = RockGem()
        red_gem = RockGem()

        # Special rocks and gems
        special_number = RockGem.get_special_item(self)
        special_gem = RockGem()
        special_rock = RockGem()
        if special_number == True:
            special_rock.set_text("@")
            special_rock.set_velocity(Point(0,5))
            special_rock.set_color(random_color)
            special_rock.set_font_size(50)
            cast.add_actor("things", special_rock)
            special_rock.set_position(Point(random.randint(0, 900),1))
            special_gem.set_text("$")
            special_gem.set_velocity(Point(0,5))
            special_gem.set_color(random_color)
            special_gem.set_font_size(50)
            cast.add_actor("things", special_gem)
            special_gem.set_position(Point(random.randint(0, 900),1))

        #Setting the value for the Flying objects it could be a rock or a gem 
        rock.set_text("0")
        green_gem.set_text("*")
        light_blue_gem.set_text("*")
        blue_gem.set_text("*")
        red_gem.set_text("*")
        
        # Setting the rate (velocity) for the falling objects - Rocks and gems
        rock.set_velocity(Point(0,5))        
        green_gem.set_velocity(Point(0,5))
        blue_gem.set_velocity(Point(0,5))
        red_gem.set_velocity(Point(0,5))
        
        # Create a random position for each Flying object Rock and Gems
        rock.set_position(Point(random.randint(0, 900),50))
        green_gem.set_position(Point(random.randint(0, 900),1))
        light_blue_gem.set_position(Point(random.randint(0, 900),1))
        blue_gem.set_position(Point(random.randint(0, 900),1))
        red_gem.set_position(Point(random.randint(0, 900),1))

        #assigning the color to each rock and Gem
        rock.set_color(white)
        green_gem.set_color(green)
        blue_gem.set_color(blue)
        red_gem.set_color(red)

        #Using the set_font_size and a value for rocks and gems
        rock.set_font_size(25)
        green_gem.set_font_size(25)
        blue_gem.set_font_size(25)
        red_gem.set_font_size(25)

        # establishes gems and rocks
        cast.add_actor("things", rock)
        cast.add_actor("things", green_gem)
        cast.add_actor("things", light_blue_gem)
        cast.add_actor("things", blue_gem)
        cast.add_actor("things", red_gem)

        # Move everything        
        score = cast.get_first_actor("score")
        player = cast.get_first_actor("player")
        x_player = player.get_position().get_x()
        y_player = player.get_position().get_y()
        x_max = self._video_service.get_width()
        y_max = self._video_service.get_height()
        player.move_next(y_max, y_max)

        # Logic of the points system. 
        for actor in cast.get_actors("things"):
            actor.move_next(x_max, y_max)
            # Regular Gem
            if actor.get_text() == "*":
                actor_x = actor.get_position().get_x()
                actor_y = actor.get_position().get_y()

                if ((x_player - 10 < actor_x < x_player + 10) and (y_player - 10 < actor_y < y_player + 10)):
                    score.add_points(100)
                    score.set_text("Good job! You found a Gem!")
                if actor_y > y_max - 30 or ((x_player - 10 < actor_x < x_player + 10) and (y_player - 10 < actor_y < y_player + 10)):
                    cast.remove_actor("things", actor)
            # Regular Rock
            elif actor.get_text() == "0":
                actor_x = actor.get_position().get_x()
                actor_y = actor.get_position().get_y()

                if ((x_player - 10 < actor_x < x_player + 10) and (y_player - 10 < actor_y < y_player + 10)):
                    score.add_points(-100)
                    score.set_text("Bad luck! You found a rock!")
                if actor_y > y_max - 30 or ((x_player - 10 < actor_x < x_player + 10) and (y_player - 10 < actor_y < y_player + 10)):
                    cast.remove_actor("things", actor)

            # Special Gem
            elif actor.get_text() == "$":
                actor_x = actor.get_position().get_x()
                actor_y = actor.get_position().get_y()

                if ((x_player - 40 < actor_x < x_player + 50) and (y_player - 40 < actor_y < y_player + 50)):
                    score.add_points(1000)
                    score.set_text("Good job! You found a Giant Gem!")
                if actor_y > y_max - 40 or ((x_player - 40 < actor_x < x_player + 50) and (y_player - 40 < actor_y < y_player + 40)):
                    cast.remove_actor("things", actor)
                
            # Special rock
            elif actor.get_text() == "@":
                actor_x = actor.get_position().get_x()
                actor_y = actor.get_position().get_y()  

                if ((x_player - 40 < actor_x < x_player + 50) and (y_player - 40 < actor_y < y_player + 50)):
                    score.add_points(-1000)
                    score.set_text("Bad luck! You found a Giant Rock!")
                if actor_y > y_max - 40 or ((x_player - 40 < actor_x < x_player + 50) and (y_player - 40 < actor_y < y_player + 40)):
                    cast.remove_actor("things", actor)

    def _do_outputs(self, cast):
        """Draws the actors on the screen.
        
        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.clear_buffer()
        player = cast.get_first_actor("player")
        score = cast.get_first_actor("score")
        for actor in cast.get_actors("things"):
            self._video_service.draw_actor(actor)
        self._video_service.draw_actor(player)
        self._video_service.draw_actor(score)
        self._video_service.flush_buffer()
        score.set_text(f"SCORE: {score.get_points()}")