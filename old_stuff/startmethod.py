import pygame
from pygame.locals import *
import os
from player_decision import Decisions

pygame.init()

class Start:
    def start(dirname, screen):
        running = True
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
                        #Decisions.player_decision()
                    if stats_position.collidepoint(mouse_pos):
                        print("stats")
                    start_position.collidepoint(mouse_pos)
                    stats_position.collidepoint(mouse_pos)
                    
            start_img = pygame.image.load(os.path.join(dirname, "assets", "START.png")).convert()
            stats_img = pygame.image.load(os.path.join(dirname, "assets", "STATISTICS.png")).convert()
            screen.blit(start_img, (200,200))
            screen.blit(stats_img, (500,200))
        pygame.display.flip()

        
    
    
    

    
    
        
    
    
