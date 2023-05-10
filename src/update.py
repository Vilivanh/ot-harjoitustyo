"""
This file is used to update the visible screen
"""
import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, suits, ranks
from handlers import Handlers
from cardhandlers import CardHandlers
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption('Norri')
screen.fill((0, 204, 0))
#clickhandles = []
#tablehandles = []
class UpdateScreen:
    def __init__(self):
        self.suits = suits
        self.ranks = ranks
    def update_screen(self, player_hand, computer_hands, tabledeck):
        """
        Args: player_hand, computer_hands, tabledeck
        Returns: updates screen based on hands and tabledeck
        """
        screen.fill((0, 204, 0))
        clickhandles = []
        tablehandles = []
        if len(tabledeck) > 0:
            for i in range(len(tabledeck)):
                rank = Handlers().rank_fixer(tabledeck[i][0])
                suit = tabledeck[i][1]
                card_position = pygame.Rect(100+i*60, 200, 59, 145)
                tablehandles.append((card_position, rank, suit))
        for i in range(len(player_hand)):
            rank = Handlers().rank_fixer(player_hand[i][0])
            suit = player_hand[i][1]
            image_scaled = CardHandlers().card_image_scaler(rank, suit)
            card_position = pygame.Rect(60+i*60, 500, 59, 145)
            clickhandles.append((card_position, rank, suit))
            screen.blit(image_scaled, (60+i*60, 500))

        if len(computer_hands) == 3:
            for i, computer_hands in enumerate(computer_hands):
                for j in range(len(computer_hands[i])):
                    image_scaled2 = CardHandlers().back_image_scaler()
                    image_scaled = pygame.transform.rotate(image_scaled2, (i+1)*90)
                    if i == 0:
                        screen.blit(image_scaled, (10+i*40, 200+10*j))
                    if i == 1:
                        screen.blit(image_scaled, (200+j*30, 20))
                    if i == 2:
                        screen.blit(image_scaled, (i*450, 200+10*j))
        elif len(computer_hands) == 4:
            for i, computer_hands in enumerate(computer_hands):
                for j in range(len(computer_hands[i])):
                    image_scaled2 = CardHandlers().back_image_scaler()
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

        elif len(computer_hands) == 5:
            for i in range(len(computer_hands)):
                for j in range(len(computer_hands[i])):
                    image_scaled2 = CardHandlers().back_image_scaler()
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
                    image_scaled = CardHandlers().card_image_scaler(rank, suit)
                    card_position = pygame.Rect(100+i*60, 200, 59, 145)
                    screen.blit(image_scaled, (100+i*60, 200))