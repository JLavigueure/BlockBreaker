import pygame



class Brick():
    def __init__(self, x, y, width, height, health):
        #dimensions of individual brick
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.health = health
        self.set_color()

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    def set_color(self):
        if(self.health == 5):
            self.color = (0, 0, 0)
        if(self.health == 4):
            self.color = (255, 0, 0)
        if(self.health == 3):
            self.color = (255, 150, 0)
        if(self.health == 2):
            self.color = (255, 255, 0)
        if(self.health == 1):
            self.color = (0, 255, 0)

        


    def collide(self, ball):
        if (ball.y - ball.radius > self.y + self.height) or (ball.y + ball.radius < self.y):
            return False
        if (ball.x + ball.radius < self.x or ball.x - ball.radius > self.x + self.width):
            return False
        self.hit()
        self.brick_collision_angle(ball)
        return 
        
    def hit(self):
        self.health -= 1
        self.set_color()

    def brick_collision_angle(self, ball):
        #check which side collided
        dist_right = abs((ball.x - ball.radius) - (self.x + self.width))
        dist_left = abs(self.x - (ball.x + ball.radius))
        dist_top = abs(self.y - (ball.y + ball.radius))
        dist_bottom = abs((ball.y - ball.radius) - (self.y + self.height))
        if(dist_right < dist_left):
            horizontal_dist = dist_right
        else:
            horizontal_dist = dist_left
        if(dist_top < dist_bottom):
            vertical_dist = dist_top
        else:
            vertical_dist = dist_bottom

        if(horizontal_dist < vertical_dist):
            ball.set_vel(ball.x_vel * -1, ball.y_vel)
        else: 
            ball.set_vel(ball.x_vel, ball.y_vel *- 1)
        
        






    
