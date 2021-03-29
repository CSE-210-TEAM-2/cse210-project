from game import constants
from game.action import Action

class HandleCollisionsAction(Action):
    """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.
    
    Stereotype:
        Controller
    """

    def execute(self, cast, args, director):
        submarine = cast["submarine_1"][0]
        coins = cast["coins"]
#        bricks = cast["bricks"]
#        balls_to_remove = []   
        for coin in coins:
#            self._handle_ball_wall_collision(ball)
            self._handle_coin_submarine_collision(coin, submarine)
#            self._handle_ball_brick_collision(ball, bricks)
#            self._handle_ball_base_collision(ball, balls_to_remove)
#            self._handle_paddle_limit_collision(paddle)
            
#        for ball in balls_to_remove:
#            balls.remove(ball)
#
#    def _handle_ball_wall_collision(self, ball):
#        ball_x = ball.center_x
#        ball_y = ball.center_y
#
#        # Check for bounce on walls
#        if ball_x <= 0 or ball_x >= constants.MAX_X:
#            ball.bounce_vertical()
#
#        if ball_y >= constants.MAX_Y:
#            ball.bounce_horizontal()
#        
#        if not constants.BALLS_CAN_DIE and ball_y <= 0:
#            ball.bounce_horizontal()
    
    def _handle_coin_submarine_collision(self, coin, submarine):
        # This makes use of the `Sprite` functionality
        if submarine.collides_with_sprite(coin):
            # Ball and paddle collide!
#            ball.bounce_horizontal()
            coins.go_faster()

#    def _handle_ball_brick_collision(self, ball, bricks):
#        brick_to_remove = None
#        for brick in bricks:
#            # This makes use of the `Sprite` functionality
#            if ball.collides_with_sprite(brick):
#                ball.bounce_horizontal()
#                brick_to_remove = brick
#        if brick_to_remove != None:
#            bricks.remove(brick_to_remove)
#
#    def _handle_ball_base_collision(self, ball, balls_to_remove):
#        if constants.BALLS_CAN_DIE and ball.center_y < 0:
#            balls_to_remove.append(ball)
#    
#    def _handle_paddle_limit_collision(self, paddle):
#        if paddle.bottom < 10:
#            paddle.bottom = 10
#        elif paddle.top > 200:
#            paddle.top = 200
#        
#        if paddle.left < 0:
#            paddle.left = 0
#        elif paddle.right > constants.MAX_X:
#            paddle.right = constants.MAX_X 
#    