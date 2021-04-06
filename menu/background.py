import arcade
import arcade.gui

class Background:
       
    def __init__(self, color):
        self._color = color
        self._is_set = False

    def draw(self):
    
            # Draw a filled in rectangle
        
            arcade.draw_rectangle_filled(200, 300, 400, 600, arcade.color.BLUE)
            arcade.draw_rectangle_filled(600, 300, 400, 600, arcade.color.RED)
