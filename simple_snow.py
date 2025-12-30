import pygame
import random

#setup of pygame
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simply Snow")
clock = pygame.time.Clock()


class Snowflake:
    def __init__(self):
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(0, HEIGHT)
        self.speed = random.uniform(1, 3)
        self.radius = random.randint(1, 3)

    def fall(self):
        self.y += self.speed
        if self.y > HEIGHT:
            self.y = 0
            self.x = random.randint(0, WIDTH)

    def draw(self):
        pygame.draw.circle(screen, (255, 255, 255), (int(self.x), int(self.y)), self.radius)

# Initialise Snowflakes
snowflakes = [Snowflake() for _ in range(100)]  # Create 100 snowflakes

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))  # Clear screen with black

    for snowflake in snowflakes:
        snowflake.fall()
        snowflake.draw()
    pygame.display.flip()
    
    clock.tick(60)  # 60 frames per second
pygame.quit()