import random as r

class Ai:

    def __init__(self):
        pass

    def get_move(self, paddle, ball, bricks):
        #move paddle to under ball
        if(ball.x < paddle.x + paddle.width/5):
            return -1
        if(ball.x > paddle.x + paddle.width/5 * 4):
            return 1

        brickAvgX = self.getBricksAvgX(bricks)

        #aim paddle
        #if bricks are mostly to the left of the ball
        if(brickAvgX < ball.x):
            #aim for 1/5 width mark of paddle
            if(ball.x < paddle.x + paddle.width/5):
                return -1
            else: 
                return 1
        #if bricks are mostly to the right of the ball
        if(brickAvgX > ball.x):
            #aim for 4/5 width mark of paddle
            if(ball.x < paddle.x + paddle.width/5 * 4):
                return -1
            else: 
                return 1
        #random int if perfectly center to avoid stagnating 
        return r.randint(-1, 1)
    
    #returns avg x value of all bricks that currently exist
    def getBricksAvgX(self, bricks):
        qty = len(bricks)
        sumx = 0
        for b in bricks:
            sumx+=b.x
        return sumx/qty
    
