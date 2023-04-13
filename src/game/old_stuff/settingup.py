import pygame
from pygame.locals import *
import os
from startmethod import Start

pygame.init()
dirname = os.path.dirname(__file__)
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill((0, 204, 0))

font = pygame.font.Font('freesansbold.ttf', 32)

def load_image(filename):
    return pygame.image.load(
        os.path.join(dirname, "assets", filename)
    )

running = True
while running:
    
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        Start.start(dirname, screen)
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()
    