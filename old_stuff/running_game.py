import pygame
import os
from pygame.locals import *
from shuffle import Methods
from turns import PlayerTurn
from computerturns import ComputerTurn

pygame.init()
dirname = os.path.dirname(__file__)
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
clickhandles = []

green = (0, 0, 0)
blue = (255, 255, 255)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
DEFAULT_IMAGE_SIZE = (100, 145)
screen.fill((0, 204, 0))
running = True
starter, playerlists = Methods.shuffling(4)

while running:
    screen.fill((0, 204, 0))
    players_list = playerlists[0]
    for i in range(len(players_list)):
        rank = players_list[i][0]
        if rank == "11":
            rank = "jack"
        if rank == "12":
            rank = "queen"
        if rank == "13":
            rank = "king"
        if rank == "14":
            rank = "ace"
        suit = players_list[i][1]
        filename = "{}_of_{}s.png".format(rank, suit)
        image = pygame.image.load(os.path.join(dirname, "assets", filename))
        image_scaled = pygame.transform.scale(image, DEFAULT_IMAGE_SIZE)
        card_position = pygame.Rect(60+i*60, 500, 59, 145)
        
        clickhandles.append((card_position, rank, suit))
        screen.blit(image_scaled, (60+i*60,500))
    PlayerTurn.players_turn([], playerlists, 4)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False   
        
            
            
            


    pygame.display.flip()

pygame.quit()
    
