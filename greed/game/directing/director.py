from game.shared.point import Point
from game.shared.color import Color
from game.casting.thing import Thing

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

        # Color list
        red = Color(255, 204, 204)
        orange = Color(225, 204, 153)
        yellow = Color(225, 153, 153)
        green = Color(204, 255, 204)
        light_blue = Color(205,255,255)
        blue = Color(204, 229, 255)
        purple = Color(229, 204, 255)
        gray = Color(96, 96, 96)

        # Falling Objects
        stone = Thing()
        green_gem = Thing()
        light_blue_gem = Thing()
        blue_gem = Thing()
        purple_gem = Thing()

        stone.set_text("o")
        green_gem.set_text("*")
        light_blue_gem.set_text("*")
        blue_gem.set_text("*")
        purple_gem.set_text("*")

        stone.set_velocity(Point(0,5))        
        green_gem.set_velocity(Point(0,5))
        light_blue_gem.set_velocity(Point(0,5))
        blue_gem.set_velocity(Point(0,5))
        purple_gem.set_velocity(Point(0,5))

        stone.set_position(Point(random.randint(0, 900),50))
        green_gem.set_position(Point(random.randint(0, 900),1))
        light_blue_gem.set_position(Point(random.randint(0, 900),1))
        blue_gem.set_position(Point(random.randint(0, 900),1))
        purple_gem.set_position(Point(random.randint(0, 900),1))

        stone.set_color(gray)
        green_gem.set_color(green)
        light_blue_gem.set_color(light_blue)
        blue_gem.set_color(blue)
        purple_gem.set_color(purple)

        stone.set_font_size(30)
        green_gem.set_font_size(30)
        light_blue_gem.set_font_size(30)
        blue_gem.set_font_size(30)
        purple_gem.set_font_size(30)

        # establishes gems and stones
        cast.add_actor("things", stone)
        cast.add_actor("things", green_gem)
        cast.add_actor("things", light_blue_gem)
        cast.add_actor("things", blue_gem)
        cast.add_actor("things", purple_gem)

        # Move everything        
        score = cast.get_first_actor("score")
        player = cast.get_first_actor("player")
        x_player = player.get_position().get_x()
        y_player = player.get_position().get_y()
        x_max = self._video_service.get_width()
        y_max = self._video_service.get_height()
        player.move_next(y_max, y_max)

        for actor in cast.get_actors("things"):
            actor.move_next(x_max, y_max)

            if actor.get_text() == "*":
                actor_x = actor.get_position().get_x()
                actor_y = actor.get_position().get_y()

                if ((x_player - 10 < actor_x < x_player + 10) and (y_player - 10 < actor_y < y_player + 10)):
                    score.add_points(100)
                if actor_y > y_max - 30 or((x_player - 10 < actor_x < x_player + 10) and (y_player - 10 < actor_y < y_player + 10)):
                    cast.remove_actor("things", actor)

            elif actor.get_text() == "o":
                actor_x = actor.get_position().get_x()
                actor_y = actor.get_position().get_y()

                if ((x_player - 10 < actor_x < x_player + 10) and (y_player - 10 < actor_y <y_player + 10)):
                    score.add_points(-100)
                if actor_y > y_max - 30 or ((x_player - 10 < actor_x < x_player + 10) and (y_player - 10 < actor_y < y_player + 10)):
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