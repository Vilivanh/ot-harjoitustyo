import pygame
import os
from pygame.locals import *

DEFAULT_IMAGE_SIZE = (100, 145)

pygame.init()
dirname = os.path.dirname(__file__)
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
font = pygame.font.Font('freesansbold.ttf', 32)
def load_image(filename):
    return pygame.image.load(
        os.path.join(dirname, "assets", filename)
    )
start_img = pygame.image.load(os.path.join(dirname, "assets", "START.png")).convert()
stats_img = pygame.image.load(os.path.join(dirname, "assets", "STATISTICS.png")).convert()
screen.fill((0, 204, 0))
screen.blit(start_img, (200,200))
screen.blit(stats_img, (500,200))

pygame.display.flip()
running = True
class Views:
    def startview():
        
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    start_position = pygame.Rect(200,200,280,91)
                    stats_position = pygame.Rect(500,200,280,91)
                    if start_position.collidepoint(mouse_pos):
                        print("start")
                    if stats_position.collidepoint(mouse_pos):
                        print("stats")
                    
                    
            start_img = pygame.image.load(os.path.join(dirname, "assets", "START.png")).convert()
            stats_img = pygame.image.load(os.path.join(dirname, "assets", "STATISTICS.png")).convert()
            screen.fill((0, 204, 0))
            screen.blit(start_img, (200,200))
            screen.blit(stats_img, (500,200))

    pygame.quit()
    def chooseview():
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    four_position = pygame.Rect(200,150,171,140)
                    five_position = pygame.Rect(200,300,171, 140)
                    six_position = pygame.Rect(200,450, 171, 140)
                    if four_position.collidepoint(mouse_pos):
                        print("4")
                    if five_position.collidepoint(mouse_pos):
                        print("5")
                    if six_position.collidepoint(mouse_pos):
                        print("6")
                    
                    
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

    def gameplayview(playerlists, starter):
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
            #card_position = pygame.Rect(60+i*60, 500, 59, 145)
            
            #clickhandles.append((card_position, rank, suit))
            screen.blit(image_scaled, (60+i*60,500))
