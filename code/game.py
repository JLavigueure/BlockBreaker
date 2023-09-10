import pygame
from math import sin, cos, radians
from sys import exit
from paddle import Paddle
from ball import Ball
from brick import Brick

#define colors
bg = (200,200,200)
red = (255, 0 ,0)
green = (0, 255, 0)
blue = (0, 0, 255)

#define game variables
width, height = 900, 600
fps = 60
cols = 9
rows = 5
paddle_width, paddle_height, paddle_padding = 110, 20, 8
ball_radius = 10
brick_height = 40
brick_gap = 2

def draw(screen, paddle, ball, bricks):
    screen.fill(bg)
    paddle.draw(screen)
    ball.draw(screen)
    for brick in bricks:
        brick.draw(screen)

    pygame.display.update()

def ball_collision(ball):
    # collide with walls
    if(ball.x-ball_radius <= 0 or ball.x + ball_radius >= width):
        ball.set_vel(ball.x_vel * - 1, ball.y_vel)
    # collide with roof
    if(ball.y-ball_radius <= 0):
        ball.set_vel(ball.x_vel, ball.y_vel * -1)

    # collide will floor
    if(ball.y + ball_radius >= height):
        ball.set_vel(ball.x_vel, ball.y_vel *-1)

def ball_paddle_collision(ball, paddle):
    #check collision
    if (ball.y + ball_radius < paddle.y) or not(ball.x + ball_radius > paddle.x and ball.x - ball_radius < paddle.x + paddle_width):
        return

    #determine new angle, disregards old angle
    paddle_center = paddle.x + paddle_width/2
    distance_to_center = ball.x - paddle_center
    percent_width = distance_to_center/(paddle_width/2)
    angle = radians(percent_width * ball.MAXBOUNCEANGLE)

    #set new velocity
    x_vel = ball.SPEED*sin(angle)
    y_vel = ball.SPEED*-cos(angle)
    ball.set_vel(x_vel, y_vel)

def generate_bricks(rows, cols):
    total_gap = (cols+1)*brick_gap
    brick_width = (width - total_gap) / cols
    bricks = []

    for row in range(rows):
        for col in range(cols):
            x = (brick_width + brick_gap) * col + brick_gap
            y = (brick_height + brick_gap) * row + brick_gap
            brick = Brick(x, y, brick_width, brick_height, rows - row)
            bricks.append(brick)
        
    return bricks


def main():
    #init pygame
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Block Breaker")
    clock = pygame.time.Clock()

    #init objects
    paddle = Paddle(width/2-paddle_width/2, height-paddle_height-paddle_padding, paddle_width, paddle_height, (0,0,0))
    ball = Ball(width/2, height - paddle_height - paddle_padding - ball_radius, ball_radius, blue)
    bricks = generate_bricks(rows, cols)

    #pygame loop
    run = True
    while run: 
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        #paddle movement
        keys = pygame.key.get_pressed()
        if(keys[pygame.K_LEFT]) and paddle.x > 0:
            paddle.move(-1)
        if(keys[pygame.K_RIGHT]) and paddle.x + paddle_width < width:
            paddle.move(1)
        
        #ball movenent and collisions
        ball.move()
        ball_paddle_collision(ball, paddle)
        ball_collision(ball)
        for brick in bricks:
            brick.collide(ball)
            if(brick.health <= 0):
                bricks.remove(brick)                
            

        #refresh display
        draw(screen, paddle, ball, bricks)


    pygame.quit()
    quit()

if __name__ == "__main__":
    main()

