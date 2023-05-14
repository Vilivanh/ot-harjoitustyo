import os
import pygame as pygame
from constants import *
from game_loop import game_loop
from rules import rules_screen
players_number = 6
class StartMethods(object):
    def __init__(self):
        pygame.init()
        self.font = pygame.font.SysFont('freesansbold.ttf', 64)
        pygame.display.set_caption('Norri')
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.screen.fill((0,204,0))
        pygame.display.update()
        self.tableclicks = []
    def addRect(self, position):
        self.rect = pygame.draw.rect(self.screen, (0,0,0), position, 2)
        pygame.display.update()
    def addText(self, text, position):
        self.screen.blit(self.font.render(text, True, (255,0,0), (0,0,0)), position)
        pygame.display.update()
    def create_click_handle(self):
        self.tableclicks = []

    def start_function():
        start_screen = StartMethods()
        tableclicks = []
        start_screen.addRect((200, 175, 150, 100))
        rect1 = pygame.draw.rect(start_screen.screen, (0,0,0), (200, 175, 150, 100), 2)
        tableclicks.append(rect1)
        start_screen.addRect((450, 175, 150, 100))
        start_screen.addRect((200, 175, 150, 100))
        rect2 = pygame.draw.rect(start_screen.screen, (0,0,0), (450, 175, 150, 100), 2)
        tableclicks.append(rect2)
        start_screen.addText("Start", (210, 180))
        start_screen.addText("Rules", (460, 180))    
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    for i in range(len(tableclicks)):
                        if tableclicks[i].collidepoint(mouse_pos):
                            game_loop(True)
                        elif tableclicks[i].collidepoint(mouse_pos):
                            rules_screen(True)
if __name__ == '__main__':
    start_screen = StartMethods()
    tableclicks = []
    start_screen.addRect((200, 175, 150, 100))
    rect1 = pygame.draw.rect(start_screen.screen, (0,0,0), (200, 175, 150, 100), 2)
    tableclicks.append(rect1)
    start_screen.addRect((450, 175, 150, 100))
    rect2 = pygame.draw.rect(start_screen.screen, (0,0,0), (450, 175, 150, 100), 2)
    tableclicks.append(rect2)
    start_screen.addText("Start", (210, 180))
    start_screen.addText("Rules", (460, 180))    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                for i in range(len(tableclicks)):
                    if tableclicks[0].collidepoint(mouse_pos):
                        game_loop(True, [], [], [], 0, players_number, False)
                    elif tableclicks[1].collidepoint(mouse_pos):
                        rules_screen(True)
                        
