import arcade

from game.director import Director
from menu.check_over_action import CheckOverAction
from menu.show_menu_action import ShowMenuAction
from menu.show_help_action import ShowHelpAction
from menu.start_game_action import StartGameAction
from menu.background import Background
from menu.button import Button
from menu.draw_actors_action import DrawActorsAction
from menu.label import Label

class Factory:

    def create_cast(self, scene):
        cast = {}
        
        if scene == "menu_scene":
            cast["background"] = [ Background(arcade.color.WHITE) ]
            cast["start_button"] = [ Button("Start Game", 400, 350, 200, 50) ]
            cast["help_button"] = [ Button("Instructions", 400, 250, 200, 50) ]
            cast["title_label"] = [ Label("Menu Scene", 400, 550) ]
            
        elif scene == "help_scene":
            cast["background"] = [ Background(arcade.color.LIGHT_BLUE) ]
            cast["back_button"] = [ Button("Back to Menu", 400, 100, 200, 50) ]
            cast["title_label"] = [ Label("Help Scene", 400, 550) ]
            cast["instructions"] = [ Label("this is a game", 400, 300)]

        elif scene == "game_scene":
            cast["background"] = [ Background(arcade.color.LIGHT_GRAY) ]
            cast["title_label"] = [ Label("Game Scene", 400, 550) ]
            cast["instructions_label"] = [ Label("Wait 5 seconds!", 400, 350) ]
            cast["time_label"] = [ Label("", 400, 300) ]
            
        return cast
            

    def create_script(self, scene):
        script = {}

        if scene == "menu_scene":
            script[Director.ON_MOUSE_RELEASE] = []
            script[Director.ON_MOUSE_RELEASE].append(ShowHelpAction(self))
            script[Director.ON_MOUSE_RELEASE].append(StartGameAction(self))
            script[Director.ON_DRAW] = []
            script[Director.ON_DRAW].append(DrawActorsAction())
            
        elif scene == "help_scene":
            script[Director.ON_MOUSE_RELEASE] = []
            script[Director.ON_MOUSE_RELEASE].append(ShowMenuAction(self))
            script[Director.ON_DRAW] = []
            script[Director.ON_DRAW].append(DrawActorsAction())

        elif scene == "game_scene":
            script[Director.ON_UPDATE] = []
            script[Director.ON_UPDATE].append(CheckOverAction(self))
            script[Director.ON_DRAW] = []
            script[Director.ON_DRAW].append(DrawActorsAction())
           
        return script
            