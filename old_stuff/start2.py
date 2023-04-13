import pygame
from pygame.locals import *
import os
from player_decision import Decisions

pygame.init()
dirname = os.path.dirname(__file__)
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700

green = (0, 0, 0)
blue = (255, 255, 255)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

font = pygame.font.Font('freesansbold.ttf', 32)

def load_image(filename):
    return pygame.image.load(
        os.path.join(dirname, "assets", filename)
    )
card_list = []

pygame.display.flip()
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            start_position = Rect(200,200,280,91)
            stats_position = Rect(500,200,280,91)
            if start_position.collidepoint(mouse_pos):
                Decisions.player_decision()
            if stats_position.collidepoint(mouse_pos):
                print("stats")
            start_position.collidepoint(mouse_pos)
            stats_position.collidepoint(mouse_pos)
            
    start_img = pygame.image.load(os.path.join(dirname, "assets", "START.png")).convert()
    stats_img = pygame.image.load(os.path.join(dirname, "assets", "STATISTICS.png")).convert()
    screen.fill((0, 204, 0))
    screen.blit(start_img, (200,200))
    screen.blit(stats_img, (500,200))
    
    
    
    

    
    
        
    
    

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()