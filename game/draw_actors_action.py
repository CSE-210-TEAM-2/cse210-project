from game.action import Action
from game import constants

import arcade

class DrawActorsAction(Action):
    """A code template for drawing actors.
    
    Stereotype:
        Controller
    """

    def execute(self, cast, args, director):
        for submarine in cast["submarine_1"]:
            submarine.draw()
        
        for submarine in cast["submarine_2"]:
            submarine.draw()
        
        for coin in cast["coins"]:
            coin.draw()