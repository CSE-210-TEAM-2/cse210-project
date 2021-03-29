import arcade


from game import constants
from game.control_actors_action import ControlActorsAction
from game.control_coins_action import ControlCoinsAction
from game.draw_actors_action import DrawActorsAction
from game.handle_collisions_action import HandleCollisionsAction
from game.move_actors_action import MoveActorsAction

from game.coin import Coin
from game.brick import Brick
from game.director import Director
from game.submarine import Submarine


def main():

    # create the cast {key: tag, value: list}
    cast = {}

    cast["submarine_1"] = []
    cast["submarine_1"].append(Submarine())

    cast["submarine_2"] = []
    cast["submarine_2"].append(Submarine())

    cast["coins"] = []
    

    # create the script {key: tag, value: list}
    script = {}

    control_actors_action = ControlActorsAction()
    control_coins_action = ControlCoinsAction()
    move_actors_action = MoveActorsAction()
    handle_collisions_action = HandleCollisionsAction()
    draw_actors_action = DrawActorsAction()
    
    script[Director.ON_KEY_PRESS] = [control_actors_action]
    script[Director.ON_UPDATE] = [control_coins_action,move_actors_action,handle_collisions_action]
    script[Director.ON_DRAW] = [draw_actors_action]

    # start the game
    director = Director(constants.MAX_X, constants.MAX_Y)
    director.direct_scene(cast, script)
    arcade.run()


if __name__ == "__main__":
    main()