import arcade
from game import constants


class Score(arcade.Sprite):
    def __init__(self):
        super().__init__(constants.TORPEDO_IMAGE)
        self.score = 100

    def hit_shark(self):
        self.score -= 10
    
    def hit_coin(self):
        self.score += 50

    def draw(self):
        score = str(self.score)
        arcade.draw_text(score, 50, 550, arcade.color.WHITE, 25)



class Score_2(arcade.Sprite):
    def __init__(self):
        super().__init__(constants.TORPEDO_IMAGE)
        self.score = 10
    
    def hit_shark(self):
        self.score -= 10

    def hit_coin(self):
        self.score += 50

    def draw(self):
        score = str(self.score)
        arcade.draw_text(score, 725, 550, arcade.color.WHITE, 25)



    
    

