import pygame

class Paddle:
    velocity = 5

    def __init__(self,x,y,width,height,color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    #-1 moves left, 1 moves right
    def move(self, direction):
        self.x += self.velocity * direction
    