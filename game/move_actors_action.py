from game.action import Action


class MoveActorsAction(Action):
    """A code template for moving actors. The responsibility of this class of
    objects is move any actor that has a velocity more than zero.
    
    Stereotype:
        Controller
    """

    def execute(self, cast, args, director):
        for group in cast.values():
            for actor in group:
                if actor.change_x != 0 or actor.change_y != 0:
                    actor.center_x = actor.center_x + actor.change_x
                    actor.center_y = actor.center_y + actor.change_y