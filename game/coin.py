import arcade
from random import randint
from game import constants


class Coin(arcade.Sprite):
    def __init__(self):
        super().__init__(constants.COIN_IMAGE)
        self.center_x = randint(5, constants.MAX_X / 2)
        self.center_y = 300
        self.change_x = constants.COIN_SPEED
        self.change_y = constants.COIN_SPEED * -1 

    def bounce_horizontal(self):
        self.change_y *= -1

    def bounce_vertical(self):
        self.change_x *= -1

class Coin_2(arcade.Sprite):
    def __init__(self):
        super().__init__(constants.COIN_IMAGE)
        self.center_x = randint(400, constants.MAX_X)
        self.center_y = 599
        self.change_x = constants.COIN_SPEED
        self.change_y = constants.COIN_SPEED

    def bounce_horizontal(self):
        self.change_y *= -1

    def bounce_vertical(self):
        self.change_x *= -1




