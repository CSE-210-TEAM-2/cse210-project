import arcade
from game import constants
from game.action import Action
from game.shark import Shark
from random import randint


class Shark_action(Action):
    """A code template for controlling actors. The responsibility of this
    class of objects is translate user input into some kind of intent.
    
    Stereotype:
        Controller
    """

    def execute(self, cast, args, director):
        spot = randint(0,1000)

        list_of_sharks = []

        for key, val in cast.items():
            if isinstance(val, int):
                list_of_sharks[key] = 1
        
        if spot > 800:
            cast["sharks"].append(Shark())