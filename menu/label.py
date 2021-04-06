import arcade.gui


class Label(arcade.gui.UILabel):

    def __init__(self, text, center_x, center_y):
        super().__init__(text, center_x, center_y)
        