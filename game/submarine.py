from game import constants

import arcade

class Submarine(arcade.Sprite):
    def __init__(self):
        super().__init__(constants.SUBMARINE_IMAGE)
        self.center_x = int(constants.MAX_X / 2)
        self.center_y = int(constants.SUBMARINE_Y)
