from game.action import Action


class DrawActorsAction(Action):
    
    def execute(self, cast, args, director):
        for group in cast:
            for actor in cast[group]:
                actor.draw()

        