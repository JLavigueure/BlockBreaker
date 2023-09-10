import pygame
from sys import exit
from paddle import Paddle;



#init pygame 
pygame.init()
width, height = 900, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Block Breaker")

#define colors
bg = (200,200,200)
red = (255, 0 ,0)
blue = (0, 255, 0)
green = (0, 0, 255)

#define game variables
fps = 60
cols = 12
rows = 5
paddle_width, paddle_height = 70, 15

def draw(screen, paddle):
    screen.fill(bg)
    paddle.draw(screen)
    pygame.display.update()

def main():
    clock = pygame.time.Clock()

    paddle = Paddle(width/2-paddle_width/2, height-paddle_height-3, paddle_width, paddle_height, (0,0,0))


    run = True
    while run: 
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        #refresh display
        draw(screen, paddle)


    pygame.quit()
    quit()

if __name__ == "__main__":
    main()

