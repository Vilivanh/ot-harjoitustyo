import itertools, random
import pygame
import os
from views import Views
from startmethod import Start
players = 4
DEFAULT_IMAGE_SIZE = (100, 145)

pygame.init()
dirname = os.path.dirname(__file__)
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
font = pygame.font.Font('freesansbold.ttf', 32)
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



