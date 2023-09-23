import random as r

class Ai:

    def __init__(self):
        pass
    
    def get_move(self, paddle, ball, bricks, screen_width):
        #While ball moves up, just track ball
        if(ball.y_vel < 0):
            if(ball.x < paddle.x + paddle.width/5):
                return -1
            if(ball.x > paddle.x + paddle.width/5 * 4):
                return 1
            return 0
        #Predict ball 
        preidcted_x = self.get_ball_trajectory(ball, paddle, screen_width)
        #Move paddle to predicted spot
        if(preidcted_x < paddle.x + paddle.width/5):
            return -1
        if(preidcted_x > paddle.x + paddle.width/5 * 4):
            return 1
        #Aim for majority of bricks once paddle is in predicted spot
        brick_avg_x = self.getBricksAvgX(bricks)
        if(brick_avg_x < preidcted_x):
            #aim for 1/5 width mark of paddle
            if(preidcted_x < paddle.x + paddle.width/5):
                return -1
            else: 
                return 1
        #if bricks are mostly to the right of the ball
        if(brick_avg_x > preidcted_x):
            #aim for 4/5 width mark of paddle
            if(preidcted_x < paddle.x + paddle.width/5 * 4):
                return -1
            else: 
                return 1
        # random int if perfectly center to avoid stagnating 
        return r.randint(-1, 1)


    def get_ball_trajectory(self, ball, paddle, screen_width):
        #Get y distance
        y_dist = (paddle.y - ball.y) / ball.y_vel
        #Predict x position
        x = y_dist * ball.x_vel + ball.x
        #Adjust for wall bounces
        while(x < 0 or x > screen_width):
            if(x < 0):
                x = abs(x)
            elif(x > screen_width):
                x = screen_width - (x - screen_width)
        return x
    
        

    #returns avg x value of all bricks that currently exist
    def getBricksAvgX(self, bricks):
        qty = len(bricks)
        if(qty == 0):
            return 0
        sumx = 0
        for b in bricks:
            sumx+=b.x
        return sumx/qty
    
