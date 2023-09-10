import pygame
from sys import exit
from paddle import Paddle;

#define colors
bg = (200,200,200)
red = (255, 0 ,0)
blue = (0, 255, 0)
green = (0, 0, 255)

#define game variables
width, height = 900, 600
fps = 60
cols = 12
rows = 5
paddle_width, paddle_height = 110, 20

def draw(screen, paddle):
    screen.fill(bg)
    paddle.draw(screen)
    pygame.display.update()

def main():
    #init pygame
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Block Breaker")
    clock = pygame.time.Clock()

    #init objects
    paddle = Paddle(width/2-paddle_width/2, height-paddle_height-8, paddle_width, paddle_height, (0,0,0))

    #pygame loop
    run = True
    while run: 
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if(keys[pygame.K_LEFT]):
            paddle.move(-1)
        if(keys[pygame.K_RIGHT]):
            paddle.move(1)
            
        #refresh display
        draw(screen, paddle)


    pygame.quit()
    quit()

if __name__ == "__main__":
    main()

