import os
import pygame as pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
def rules_screen(RULES):
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    font = pygame.font.Font('freesansbold.ttf', 20)
    pygame.display.set_caption('Norri - rules')
    while RULES == True:
        
        text1 = font.render("The goal of the game is to get rid of all the cards dealt to you", True, (255,255,255), (0, 204, 0))
        text2 = font.render("Every time when you play, you choose to play card or pick the smallest card from the table", True, (255,255,255), (0, 204, 0)) 
        text3 = font.render("Clubs can only be played on another club", True, (255,255,255), (0, 204, 0))
        text4 = font.render("Diamonds can be played on top of hearts or spades so that smallest", True, (255,255,255), (0, 204, 0))  
        text4a = font.render("diamond is higher than highest spade or heart", True, (255,255,255), (0, 204, 0))
        text5 = font.render("If highest card in table is a diamond, only diamonds can be played", True, (255,255,255), (0, 204, 0))
        text6 = font.render("When there are as much cards on the table as there", True, (255,255,255), (0, 204, 0))
        text6a = font.render("are players, table cards are removed from the game and", True, (255,255,255), (0, 204, 0))
        text6b = font.render("the player who played the last card gets to continue the game", True, (255,255,255), (0, 204, 0))
        text7 = font.render("Winner is the first player who does not have any cards", True, (255,255,255), (0, 204, 0))
        screen.fill((0, 204, 0))
        screen.fill((0, 204, 0))
        screen.blit(text1, (10,10))
        screen.blit(text2, (10,70))
        screen.blit(text3, (10,130))
        screen.blit(text4, (10,190))
        screen.blit(text4a, (10,220))
        screen.blit(text5, (10,280))
        screen.blit(text6, (10,340))
        screen.blit(text6a, (10,370))
        screen.blit(text6b, (10,400))
        screen.blit(text7, (10,460))
        text_back = font.render("Exit", True, (0, 0, 0), (0, 204, 0))
        rect2 = pygame.draw.rect(screen, (0,0,0), (450, 500, 150, 100), 2)
        text_rect = text_back.get_rect()
        text_rect.center = (500, 550)
        screen.blit(text_back, text_rect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RULES = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if rect2.collidepoint(mouse_pos):
                    exit()
            pygame.display.flip()

