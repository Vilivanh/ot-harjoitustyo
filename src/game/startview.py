import os
import pygame as pygame
from constants import *
from play import Play
from Computerchoose import ComputerChoose
from update import UpdateScreen
from handlers import Handlers
from cardhandlers import CardHandlers
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Norri')
screen.fill((0, 204, 0))