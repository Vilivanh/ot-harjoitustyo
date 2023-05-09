import pygame
import os
from constants import *
from cardhandlers import CardHandlers

class Handlers:
    """
    class to use for repeated commands
    """
    def computer_handler(Computer_Hands, screen, dirname):
        if len(Computer_Hands) == 1:
            for i in range(len(Computer_Hands)):
                for j in range(len(Computer_Hands[i])):
                    image_scaled2 = CardHandlers.back_image_scaler()
                    image_scaled = pygame.transform.rotate(image_scaled2, (i+1)*90)
                    if i == 0:
                        screen.blit(image_scaled, (200+j*30, 20))
        elif len(Computer_Hands) == 2:
            for i in range(len(Computer_Hands)):
                for j in range(len(Computer_Hands[i])):
                    image_scaled2 = CardHandlers.back_image_scaler()
                    image_scaled = pygame.transform.rotate(image_scaled2, (i+1)*90)
                    if i == 0:
                        screen.blit(image_scaled, (i*40, 200+10*j))
                    if i == 1:
                        screen.blit(image_scaled, (200+j*30, 20))
        elif len(Computer_Hands) == 3:
            for i in range(len(Computer_Hands)):
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
            for i in range(len(Computer_Hands)):
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
            for i in range(len(Computer_Hands)):
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
    def rank_fixer(givenrank):
        if givenrank == "11":
            rank = "jack"
        elif givenrank == "12":
            rank = "queen"
        elif givenrank == "13":
            rank = "king"
        elif givenrank == "14":
            rank = "ace"
        else:
            rank = givenrank
        return rank
    def rank_integer(givenrank):
        if givenrank == "jack":
            rank = "11"
        elif givenrank == "queen":
            rank = "12"
        elif givenrank == "king":
            rank = "13"
        elif givenrank == "ace":
            rank = "14"
        else:
            rank = givenrank
        return rank
    