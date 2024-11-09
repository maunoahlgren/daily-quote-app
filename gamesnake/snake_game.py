import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 640, 480
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Game logic goes here

    # Refresh game screen
    pygame.display.update()

# Quit Pygame
pygame.quit()
sys.exit()

testi
