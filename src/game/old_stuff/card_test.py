import pygame
import os
from pygame.locals import *

handdeck = [(4, 'club'), (14, 'spade'), (11, 'heart'), (13, 'spade'), (14, 'heart'), (11, 'spade'), (11, 'club'), (13, 'diamond'), (13, 'heart'), (2, 'heart')]

pygame.init()
dirname = os.path.dirname(__file__)
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700

green = (0, 0, 0)
blue = (255, 255, 255)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
card_images = {}
suits = ["club", "heart", "spade", "diamond"]
oldranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king", "ace"]

DEFAULT_IMAGE_SIZE = (100, 145)
ranks = [] 
card_images = []
for i in range(len(oldranks)):
    if oldranks[i] == "11":
        rank = "jack"
    elif oldranks[i] == "12":
        rank = "queen"
    elif oldranks[i] == "13":
        rank = "king"
    elif oldranks[i] == "14":
        rank = "ace"
    else:
        rank = oldranks[i]
    ranks.append(ranks)    

clickhandles = []


running = True
while running:
    
        
    screen.fill((0, 204, 0))
    for i in range(len(handdeck)):
        rank = str(handdeck[i][0])
        if rank == "11":
            rank = "jack"
        if rank == "12":
            rank = "queen"
        if rank == "13":
            rank = "king"
        if rank == "14":
            rank = "ace"
        suit = handdeck[i][1]
        filename = "{}_of_{}s.png".format(rank, suit)
        image = pygame.image.load(os.path.join(dirname, "assets", filename))
        image_scaled = pygame.transform.scale(image, DEFAULT_IMAGE_SIZE)
        card_position = Rect(60+i*60, 500, 59, 145)
        
        clickhandles.append((card_position, rank, suit))
        screen.blit(image_scaled, (60+i*60,500))
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False    
        elif event.type == pygame.MOUSEBUTTONDOWN:
            clicked = None
            mouse_pos = event.pos
            for i in range(len(clickhandles)):
                if clickhandles[i][0].collidepoint(mouse_pos):
                    clicked = (clickhandles[i][1], clickhandles[i][2])
            
            
            print(clicked)

    pygame.display.flip()

# Done! Time to quit.
pygame.quit()
    