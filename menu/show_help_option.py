from action import Action


class ShowHelpAction(Action):
    
    def __init__(self, factory):
        self._factory = factory

    def execute(self, cast, args, director):
        if "help_button" in cast.keys():
            help_button = cast["help_button"][0]
            point = (args["x"], args["y"])
            
            if help_button.collides_with_point(point):
                cast = self._factory.create_cast("help_scene")
                script = self._factory.create_script("help_scene")
                director.direct_scene(cast, script)
