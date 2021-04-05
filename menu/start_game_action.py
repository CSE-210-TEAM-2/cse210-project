from action import Action


class StartGameAction(Action):
    
    def __init__(self, factory):
        self._factory = factory

    def execute(self, cast, args, director):
        if "start_button" in cast.keys():
            start_button = cast["start_button"][0]
            point = (args["x"], args["y"])
            
            if start_button.collides_with_point(point):
                cast = self._factory.create_cast("game_scene")
                script = self._factory.create_script("game_scene")
                director.direct_scene(cast, script)