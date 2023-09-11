import pygame

class Ball: 
    MAXBOUNCEANGLE = 75
    
    def __init__(self, x, y, radius, color):
        self.speed = 5
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.x_vel = 0
        self.y_vel = -5

    def move(self):
        self.y += self.y_vel
        self.x += self.x_vel

    def set_vel(self, x_vel, y_vel):
        self.x_vel = x_vel
        self.y_vel = y_vel

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)