from random import random
from game.casting.actor import Actor
from game.casting.cast import Cast
from game.casting.score import Score

from game.directing.director import Director

from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService

from game.shared.color import Color
from game.shared.point import Point
from game.casting.rock_gem import RockGem

FRAME_RATE = 12
MAX_X = 900
MAX_Y = 600
CELL_SIZE = 10
FONT_SIZE = 20
COLS = 60
ROWS = 40
CAPTION = "GREED"
WHITE = Color(255, 255, 255)


def main():
    
    # create the cast
    cast = Cast()

    # create the robot and its initial position
    x = int(MAX_X / 2)
    y = int(580)
    position = Point(x, y)

    # Displaying the Score
    score = Score()
    cast.add_actor("score", score)
    score.set_position(Point(MAX_X // 20, 15))
    score.set_color(WHITE)

    """
    # create the banner
    banner = Actor()
    banner.set_text("Score: ")
    banner.set_font_size(FONT_SIZE)
    banner.set_color(WHITE)
    banner.set_position(Point(CELL_SIZE, 0))
    cast.add_actor("banners", banner)
    """

    #create the player Setting the values for each property
    #Creating and instance to use the properties and methods from Actor
    player = Actor()
    player.set_text("#")
    cast.add_actor("player", player)
    player.set_font_size(FONT_SIZE)
    player.set_position(position)
    player.set_color(WHITE)

    
    
    #creating Rocks & Gems Kevin's Personal Branch

    # artifacts_list = {"0":-1, "*": 1}
    # text = random.choice(list(artifacts_list))
    # value = artifacts_list[text]

    # artifact = Artifact(value)
    # artifact.set_text(text)
    # artifact.set_font_size(FONT_SIZE)




    #Kevin Was setting the color in here as well
    # artifact.set_color(color)

    # artifact.set_position(position)
    # artifact.set_velocity(Point(0,2))
    # cast.add_actor("artifacts", artifact)





    # start the game
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director(keyboard_service, video_service)
    director.start_game(cast)

if __name__ == "__main__":
    main()
