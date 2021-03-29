import arcade
from random import randint
from game import constants


class Coin(arcade.Sprite):
    def __init__(self):
        super().__init__(constants.BALL_IMAGE)
        self.center_x = randint(5, constants.MAX_X - 5)
        self.center_y = 600#constants.BALL_Y
        self.change_x = 0
        self.change_y = -1

    def bounce_horizontal(self):
        self.change_y *= -1

    def bounce_vertical(self):
        self.change_x *= -1

    def go_faster(self):
        self.change_y -= .1

