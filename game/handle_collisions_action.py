from game import constants
from game.action import Action
from game.coin import Coin

class HandleCollisionsAction(Action):
    """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.
    
    Stereotype:
        Controller
    """

    def execute(self, cast, args, director):
        submarine = cast["submarine"][0]
        submarine_2 = cast["submarine_2"][0]
        
        coins = cast["coins"]
        coins_2 = cast["coins_2"]
        coins_to_remove = []
        score_1 = cast["score_1"][0]
        score_2 = cast["score_2"][0]

        sharks = cast["sharks"]
            
        for ball in coins:
            self._handle_ball_wall_collision(ball)
            self._handle_ball_submarine_collision(ball, submarine, score_1)
            self._handle_submarine_limit_collision(submarine, submarine_2)
        
        for ball in coins_2:
            self._handle_ball_wall_collision_2(ball)
            self._handle_ball_submarine_collision(ball, submarine_2, score_2)
            self._handle_submarine_limit_collision(submarine, submarine_2)

        for shark in sharks:
            self._handle_shark_submarine_collision(shark, submarine, score_1)
            self._handle_shark_submarine_collision(shark, submarine, score_2)
            
        for ball in coins_to_remove:
            coins.remove(ball)

        self._kill(cast)


    def _kill(self,cast):

        # This will kill the sharks as soon as they get ouyt of the screen
        sharks_to_remove = []
        sharks = cast["sharks"]

        for shark in sharks:
            if shark.bottom <= 0:
                sharks_to_remove.append(shark)

        for shark in sharks_to_remove:
            cast["sharks"].remove(shark)

        # This will kill the coins from the left side as soon as they get ouyt of the screen
        coins_to_remove = []
        coins = cast["coins"]

        for coin in coins:
            if coin.bottom <= 0:
                coins_to_remove.append(coin)

        for coin in coins_to_remove:
            cast["coins"].remove(coin)

        # This will kill the sharks as soon as they get ouyt of the screen

        coins_2_to_remove = []
        coins_2 = cast["coins_2"]

        for coin_2 in coins_2:
            if coin_2.bottom <= 0:
                coins_2_to_remove.append(coin_2)

        for coin_2 in coins_2_to_remove:
            cast["coins_2"].remove(coin_2)

        

    def _handle_ball_wall_collision(self, ball):
        coin_x = ball.center_x
        coin_y = ball.center_y

        # Check for bounce on walls
        if coin_x <= 0 or coin_x >= constants.MAX_X / 2:
            ball.bounce_vertical()

        if coin_y >= constants.MAX_Y:
            ball.bounce_horizontal()
        
        if not constants.COINS_CAN_DIE and coin_y <= 0:
            ball.bounce_horizontal()
        
    def _handle_ball_wall_collision_2(self, ball):
        coin_x = ball.center_x
        coin_y = ball.center_y

        # Check for bounce on walls
        if coin_x <= 400 or coin_x >= constants.MAX_X :
            ball.bounce_vertical()

        if coin_y >= constants.MAX_Y:
            ball.bounce_horizontal()
        
        if not constants.COINS_CAN_DIE and coin_y <= 0:
            ball.bounce_horizontal()

    def _handle_shark_submarine_collision(self, shark, submarine, score):

        # This makes use of the `Sprite` functionality
        if submarine.collides_with_sprite(shark):
            score.hit_shark()
        

    
    def _handle_ball_submarine_collision(self, ball, submarine,score):

        # This makes use of the `Sprite` functionality
        if submarine.collides_with_sprite(ball):
            # Coin and submarine collide!
            ball.bounce_horizontal()
            score.hit_coin()

    def _handle_ball_brick_collision(self, ball, bricks):
        brick_to_remove = None
        for brick in bricks:
            # This makes use of the `Sprite` functionality
            if ball.collides_with_sprite(brick):
                ball.bounce_horizontal()
                brick_to_remove = brick
        if brick_to_remove != None:
            bricks.remove(brick_to_remove)
            

    def _coin_out(self,ball, coins_to_remove):
        if constants.COINS_CAN_DIE and ball.center_y <= 0:
            coins_to_remove.append(ball)
    
    def _handle_submarine_limit_collision(self, submarine, submarine_2):
        if submarine.bottom < 10:
            submarine.bottom = 10
        elif submarine.top > 200:
            submarine.top = 200
        
        if submarine.left < 0:
            submarine.left = 0
        elif submarine.right > constants.SUB_1_MAX_X:
            submarine.right = constants.SUB_1_MAX_X 


        if submarine_2.bottom < 10:
            submarine_2.bottom = 10
        elif submarine_2.top > 200:
            submarine_2.top = 200
        
        if submarine_2.left < 400:
            submarine_2.left = 400
        elif submarine_2.right > constants.SUB_2_MAX_X:
            submarine_2.right = constants.SUB_2_MAX_X 
        
    