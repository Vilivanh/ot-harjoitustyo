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
tabledeck = []
green = (0, 0, 0)
blue = (255, 255, 255)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
DEFAULT_IMAGE_SIZE = (100, 145)
ANOTHER_IMAGE_SIZE = (50, 73)
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
    for i in range(1, len(playerlists)):
        for j in range(len(playerlists[i])):
            
            filename = "BACK.png"
            image = pygame.image.load(os.path.join(dirname, "assets", filename))
            image_scaled2 = pygame.transform.scale(image, ANOTHER_IMAGE_SIZE)
            image_scaled = pygame.transform.rotate(image_scaled2, i*90)
            if i == 1:
                screen.blit(image_scaled, (i*40,200+10*j))
            if i == 2:
                screen.blit(image_scaled, (100+j*40,20))
            if i == 3:
                screen.blit(image_scaled, (i*280,200+10*j))
    if len(tabledeck) > 0:
        clickhandles = []
        for i in range(len(tabledeck)):
            rank = tabledeck[i][0]
            if rank == "11":
                rank = "jack"
            if rank == "12":
                rank = "queen"
            if rank == "13":
                rank = "king"
            if rank == "14":
                rank = "ace"
            suit = tabledeck[i][1]
            filename = "{}_of_{}s.png".format(rank, suit)
            image = pygame.image.load(os.path.join(dirname, "assets", filename))
            image_scaled = pygame.transform.scale(image, DEFAULT_IMAGE_SIZE)
            card_position = pygame.Rect(150+i*60, 250, 59, 145)
            
            clickhandles.append((card_position, rank, suit))
            screen.blit(image_scaled, (150+i*60,250))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False   
        
    pygame.display.flip()

pygame.quit()