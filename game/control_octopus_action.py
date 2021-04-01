import arcade
from game import constants
from game.action import Action
from game.octopus import Octopus
from random import randint


class Octopus_action(Action):
    """A code template for controlling actors. The responsibility of this
    class of objects is translate user input into some kind of intent.
    
    Stereotype:
        Controller
    """

    def execute(self, cast, args, director):
        spot = randint(0,1000)

        list_of_octopi = []

        for key, val in cast.items():
            if isinstance(val, int):
                list_of_octopi[key] = 1
        
        if spot > 990:
            cast["octopi"].append(Octopus())