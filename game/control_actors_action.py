import arcade
from game import constants
from game.action import Action


class ControlActorsAction(Action):
    """A code template for controlling actors. The responsibility of this
    class of objects is translate user input into some kind of intent.
    
    Stereotype:
        Controller
    """

    def execute(self, cast, args, director):
        x = 0
        y = 0

        if args["key"] == arcade.key.LEFT:
            x = -1
        elif args["key"] == arcade.key.RIGHT:
            x = 1
        
        
        x *= constants.PADDLE_MOVE_SCALE
        y *= constants.PADDLE_MOVE_SCALE

        submarine = cast["submarine_1"][0] # there's only one in the cast
        submarine.change_x = x
        submarine.change_y = y