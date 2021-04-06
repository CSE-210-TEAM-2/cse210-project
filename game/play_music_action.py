import arcade
from game.action import Action
from game import constants

import arcade

class PlayMusicAction(Action):
    """A code template for drawing actors.
    
    Stereotype:
        Controller
    """

    def execute(self, cast, args, director):
        for sound in cast["sounds"]:
            if not sound.is_playing():
                sound.play()