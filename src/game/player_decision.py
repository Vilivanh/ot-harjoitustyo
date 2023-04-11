import pygame
from pygame.locals import *
import os
from shuffle import Methods
class Decisions:

    def player_decision():
        pygame.init()
        dirname = os.path.dirname(__file__)
        SCREEN_WIDTH = 1000
        SCREEN_HEIGHT = 700

        green = (0, 0, 0)
        blue = (255, 255, 255)

        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

        font = pygame.font.Font('freesansbold.ttf', 32)

        #def load_image(filename):
            #return pygame.image.load(
                #os.path.join(dirname, "assets", filename))
        #card_list = []

        pygame.display.flip()
        running = True
        while running:

            # Did the user click the window close button?
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    four_position = Rect(200,150,171,140)
                    five_position = Rect(200,300,171, 140)
                    six_position = Rect(200,450, 171, 140)
                    if four_position.collidepoint(mouse_pos):
                        Methods.shuffling(4)
                    if five_position.collidepoint(mouse_pos):
                        Methods.shuffling(5)
                    if six_position.collidepoint(mouse_pos):
                        Methods.shuffling(6)
                    
                    
            four_img = pygame.image.load(os.path.join(dirname, "assets", "4players.png")).convert()
            five_img = pygame.image.load(os.path.join(dirname, "assets", "5players.png")).convert()
            six_img = pygame.image.load(os.path.join(dirname, "assets", "6players.png")).convert()
            screen.fill((0, 204, 0))
            font = pygame.font.Font('freesansbold.ttf', 32)
            text = font.render("Choose the number of players", True, green, blue)
            textRect = text.get_rect()
            textRect.center = (250, 50)
            screen.blit(text, textRect) 

            screen.blit(four_img, (200,150))
            screen.blit(five_img, (200,300))
            screen.blit(six_img, (200,450))
            pygame.display.flip()

        # Done! Time to quit.
        pygame.quit()