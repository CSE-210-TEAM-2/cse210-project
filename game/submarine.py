from game import constants

import arcade

class Submarine(arcade.Sprite):
    def __init__(self):
        super().__init__(constants.BRICK_IMAGE)
        self.center_x = 300
        self.center_y = 100
