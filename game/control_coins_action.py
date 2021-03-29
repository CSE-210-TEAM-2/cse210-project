import arcade
from game import constants
from game.action import Action
from game.coin import Coin
from random import randint


class ControlCoinsAction(Action):
    """A code template for controlling actors. The responsibility of this
    class of objects is translate user input into some kind of intent.
    
    Stereotype:
        Controller
    """

    def execute(self, cast, args, director):
        spot = randint(0,1000)
        if spot > 990:
            cast["coins"].append(Coin())