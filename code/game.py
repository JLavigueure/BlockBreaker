import pygame
from numpy import random, arange
from math import sin, cos, radians
from sys import exit
from paddle import Paddle
from ball import Ball
from brick import Brick
from ai import Ai

#define game variables
AI = True
width, height = 900, 600
fps = 500
cols = 9
rows = 5
hit_points = 25
break_points = 175
paddle_width, paddle_height, paddle_padding = 110, 20, 8
ball_radius = 10
brick_height = 40
brick_gap = 2
gameover_screen = 400
bg = (53, 59, 240)
paddle_color = (90, 170, 176)
ball_color = (240, 182, 7)
ball_speed_increase = 1.15
# bg_surf = pygame.image.load('BlockBreaker/graphics/bg.png')

pygame.init()
GAME_FONT = pygame.font.SysFont("Fixedsys", 40)

#draws game assets
def draw(screen, paddle, ball, bricks, points):
    screen.fill(bg)
    # screen.blit(bg_surf, (0,0))
    paddle.draw(screen)
    ball.draw(screen)
    for brick in bricks:
        brick.draw(screen)
    
    score_text = GAME_FONT.render(f"Score: {points}", 1, "black")
    screen.blit(score_text, (10, height - score_text.get_height()-10))

    pygame.display.update()

#returns true if ball collides with floor, else false and change ball velocity
def ball_collision(ball):
    # collide with walls
    if(ball.x-ball_radius <= 0 or ball.x + ball_radius >= width):
        ball.set_vel(ball.x_vel * - 1, ball.y_vel)
        return False
    # collide with roof
    if(ball.y-ball_radius <= 0):
        ball.set_vel(ball.x_vel, ball.y_vel * -1)
        return False

    # collide will floor
    if(ball.y + ball_radius >= height):
        return True

#changes ball velocity determined by position hit on paddle
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
    x_vel = ball.speed*sin(angle)
    y_vel = ball.speed*-cos(angle)
    ball.set_vel(x_vel, y_vel)

#generates bricks
def generate_bricks(rows, cols, level):
    total_gap = (cols+1)*brick_gap
    brick_width = (width - total_gap) / cols
    bricks = []


    for row in range(rows):
        for col in range(cols):
            health = generate_random_health(level)
            x = (brick_width + brick_gap) * col + brick_gap
            y = (brick_height + brick_gap) * row + brick_gap
            brick = Brick(x, y, brick_width, brick_height, health)
            bricks.append(brick)
        
    return bricks

def generate_random_health(level):
    if(level == 1):
        return random.choice(arange(1,6), p=[.4, .4, .1, .1, 0])
    if(level == 2):
        return random.choice(arange(1,6), p=[.4, .3, .2, .1, 0])
    if(level == 3):
        return random.choice(arange(1,6), p=[.3, .2, .3, .1, .1])
    if(level == 4):
        return random.choice(arange(1,6), p=[.2, .2, .3, .2, .1])
    if(level == 5):
        return random.choice(arange(1,6), p=[.1, .2, .3, .2, .2])
    if(level == 6):
        return random.choice(arange(1,6), p=[0, .2, .4, .2, .2])
    if(level == 7):
        return random.choice(arange(1,6), p=[0, .1, .3, .4, .2])
    if(level == 8):
        return random.choice(arange(1,6), p=[0, .1, .2, .4, .3])
    if(level == 9):
        return random.choice(arange(1,6), p=[0, 0, .2, .4, .4])
    if(level == 10):
        return random.choice(arange(1,6), p=[0, 0, .1, .5, .4])
    return random.choice(arange(1,6), p=[0, 0, 0, .5, .5])

def game_over(screen, points):
    lose_text = GAME_FONT.render("Game over", 1, "black")
    final_score_text = GAME_FONT.render(f"Score: {points}", 1, "black")
    screen.blit(final_score_text, (width/2 - lose_text.get_width()/2, height/2 + 50))
    screen.blit(lose_text, (width/2 - lose_text.get_width()/2, height/2))
    pygame.display.update()

def main():
    if(AI):
        ai = Ai()

    level = 1
    lives = 1
    points = 0
    #init pygame
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Block Breaker")
    clock = pygame.time.Clock()
    #init objects
    paddle = Paddle(width/2-paddle_width/2, height-paddle_height-paddle_padding, paddle_width, paddle_height, paddle_color)
    ball = Ball(width/2, height - paddle_height - paddle_padding - ball_radius, ball_radius, ball_color)
    bricks = generate_bricks(rows, cols, level)


    #pygame loop
    run = True
    while run: 
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        #paddle movement
        if(lives > 0):
            if not(AI):
                keys = pygame.key.get_pressed()
                if(keys[pygame.K_LEFT]) and paddle.x > 0:
                    paddle.move(-1)
                if(keys[pygame.K_RIGHT]) and paddle.x + paddle_width < width:
                    paddle.move(1)
            else:
                ai_move = ai.get_move(paddle, ball, bricks, width)
                if(ai_move == 1 and paddle.x + paddle.width < width):
                    paddle.move(ai_move)
                elif(ai_move == -1 and paddle.x > 0):
                    paddle.move(ai_move)
        

        
                
        #ball movenent and collisions
        ball.move()
        ball_paddle_collision(ball, paddle)
        ball_collision(ball)
        
        for brick in bricks:
            if(brick.collide(ball) and lives > 0):
                points += hit_points
            if(brick.health <= 0 and lives > 0):
                bricks.remove(brick)  
                points += break_points             

        if not(bricks) and ball.y > brick_height*rows + 15:
            level+=1
            bricks = generate_bricks(rows, cols, level)
            ball.speed *= ball_speed_increase
            


        #refresh display
        draw(screen, paddle, ball, bricks, points)
        if(ball.y + ball_radius >= height):
            lives-=1
        if(lives <= 0):
            game_over(screen, points)
        

    pygame.quit()
    quit()

if __name__ == "__main__":
    main()
