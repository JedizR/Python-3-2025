import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("flying_circle")

class Circle:
    def __init__(self, x, y, speed_x, speed_y, radius, color):
        self.x = x
        self.y = y
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
        if self.x - self.radius < 0 or self.x + self.radius > 800:
            return "x_hit"
        if self.y - self.radius < 0 or self.y + self.radius > 600:
            return "y_hit"
        return False

if __name__ == "__main__":
    clock = pygame.time.Clock()
    circle_1 = Circle(400, 300, 8, 4, 20, (255, 0, 0))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        circle_1.update()
        screen.fill((255,255,255))
        circle_1.draw(screen)
        pygame.display.flip()
        clock.tick(60)
