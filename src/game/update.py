"""
This file is used to update the visible screen
"""
import pygame
from constants import *
from handlers import Handlers
from cardhandlers import CardHandlers
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption('Norri')
screen.fill((0, 204, 0))
#clickhandles = []
#tablehandles = []
class UpdateScreen:
    def __init__(self):
        self.Player_Hand = []
        self.Computer_Hands = []
        self.tabledeck = []
    def update_screen(self, Player_Hand, Computer_Hands, tabledeck):
        """
        Args: Player_Hand, Computer_Hands, tabledeck
        Returns: updates screen based on hands and tabledeck
        """
        screen.fill((0, 204, 0))
        clickhandles = []
        tablehandles = []

        if len(tabledeck) > 0:
            for i, tabledeck in enumerate(tabledeck):
                rank = Handlers.rank_fixer(tabledeck[i][0])
                suit = tabledeck[i][1]
                card_position = pygame.Rect(100+i*60, 200, 59, 145)
                tablehandles.append((card_position, rank, suit))
        for i, PlayerHand in enumerate(PlayerHand):
            rank = Handlers.rank_fixer(Player_Hand[i][0])
            suit = Player_Hand[i][1]
            image_scaled = CardHandlers.card_image_scaler(rank, suit)
            card_position = pygame.Rect(60+i*60, 500, 59, 145)
            clickhandles.append((card_position, rank, suit))
            screen.blit(image_scaled, (60+i*60, 500))

        if len(Computer_Hands) == 3:
            for i, Computer_Hands in enumerate(Computer_Hands):
                for j in range(len(Computer_Hands[i])):
                    image_scaled2 = CardHandlers.back_image_scaler()
                    image_scaled = pygame.transform.rotate(image_scaled2, (i+1)*90)
                    if i == 0:
                        screen.blit(image_scaled, (i*40, 200+10*j))
                    if i == 1:
                        screen.blit(image_scaled, (200+j*30, 20))
                    if i == 2:
                        screen.blit(image_scaled, (i*450, 200+10*j))
        elif len(Computer_Hands) == 4:
            for i, Computer_Hands in enumerate(Computer_Hands):
                for j in range(len(Computer_Hands[i])):
                    image_scaled2 = CardHandlers.back_image_scaler()
                    if i == 0:
                        image_scaled = pygame.transform.rotate(image_scaled2, (i+1)*90)
                    elif i == 1:
                        image_scaled = pygame.transform.rotate(image_scaled2, (i+1)*90)
                    elif i == 2:
                        image_scaled = pygame.transform.rotate(image_scaled2, (i)*90)
                    elif i == 3:
                        image_scaled = pygame.transform.rotate(image_scaled2, (i)*90)
                    if i == 0:
                        screen.blit(image_scaled, (10+i*40, 200+10*j))
                    if i == 1:
                        screen.blit(image_scaled, (20+j*30, 10))
                    if i == 2:
                        screen.blit(image_scaled, (450+(j-1)*30, 10))
                    if i == 3:
                        screen.blit(image_scaled, (i*275, 200+10*j))

        elif len(Computer_Hands) == 5:
            for i, Computer_Hands in enumerate(Computer_Hands):
                for j in range(len(Computer_Hands[i])):
                    image_scaled2 = CardHandlers.back_image_scaler()
                    if i == 0:
                        image_scaled = pygame.transform.rotate(image_scaled2, (i+1)*90)
                    elif i == 1:
                        image_scaled = pygame.transform.rotate(image_scaled2, (i+1)*90)
                    elif i == 2:
                        image_scaled = pygame.transform.rotate(image_scaled2, (i)*90)
                    elif i == 3:
                        image_scaled = pygame.transform.rotate(image_scaled2, (i-1)*90)
                    elif i == 4:
                        image_scaled = pygame.transform.rotate(image_scaled2, (i-1)*90)
                    if i == 0:
                        screen.blit(image_scaled, (10+i*40, 200+10*j))
                    if i == 1:
                        screen.blit(image_scaled, (0+j*20, 10))
                    if i == 2:
                        screen.blit(image_scaled, (350+(j-1)*20, 10))
                    if i == 3:
                        screen.blit(image_scaled, (650+(j-2)*20, 10))
                    if i == 4:
                        screen.blit(image_scaled, (i*225, 200+10*j))
            if len(tabledeck) > 0:
                for i in range(len(tabledeck)):
                    rank, suit = tabledeck[i][0], tabledeck[i][1]
                    image_scaled = CardHandlers.card_image_scaler(rank, suit)
                    card_position = pygame.Rect(100+i*60, 200, 59, 145)
                    screen.blit(image_scaled, (100+i*60, 200))