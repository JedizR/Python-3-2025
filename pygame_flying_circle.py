import pygame
import sys
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("flying_circle")

class Circle:
    def __init__(self, start_x, start_y, speed_x, speed_y, radius, color):
        self.x = start_x
        self.y = start_y
        self.radius = radius
        self.color = color
        self.speed_x = speed_x
        self.speed_y = speed_y
        
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
        
    def update(self):
        if self.wall_hit() == "x_hit":
            self.speed_x = -self.speed_x
        if self.wall_hit() == "y_hit":
            self.speed_y = -self.speed_y
        self.x += self.speed_x
        self.y += self.speed_y
        
    def wall_hit(self):
        if self.x - self.radius < 0 or self.x + self.radius > SCREEN_WIDTH:
            return "x_hit"
        if self.y - self.radius < 0 or self.y + self.radius > SCREEN_HEIGHT:
            return "y_hit"
        return False

if __name__ == "__main__":
    running = True
    clock = pygame.time.Clock()
    circle_list = []
    
    circle_1 = Circle(start_x=random.randint(100,SCREEN_WIDTH-100), 
                    start_y=random.randint(100,SCREEN_HEIGHT-100), 
                    speed_x=random.randint(4,7), 
                    speed_y=random.randint(4,7), 
                    radius=20, 
                    color=(255, 0, 0))

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break

        circle_1.update()
        screen.fill((255,255,255))
        circle_1.draw(screen)
        pygame.display.flip()
        clock.tick(60)
