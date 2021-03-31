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
        
        if args["key"] == arcade.key.UP:
            y = 1
        elif args["key"] == arcade.key.DOWN:
            y = -1

        x *= constants.SUBMARINE_MOVE_SCALE
        y *= constants.SUBMARINE_MOVE_SCALE

        submarine = cast["submarine"][0] 
        submarine.change_x = x
        submarine.change_y = y



        a = 0
        b = 0

        if args["key"] == arcade.key.A:
            a = -1
        elif args["key"] == arcade.key.D:
            a = 1
        
        if args["key"] == arcade.key.W:
            b = 1
        elif args["key"] == arcade.key.S:
            b = -1

        a *= constants.SUBMARINE_MOVE_SCALE
        b *= constants.SUBMARINE_MOVE_SCALE

        submarine = cast["submarine_2"][0] 
        submarine.change_x = a
        submarine.change_y = b