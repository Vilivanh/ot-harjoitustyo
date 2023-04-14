import pygame
import os
from pygame.locals import *

pygame.init()

dirname = os.path.dirname(__file__)
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
DEFAULT_IMAGE_SIZE = (100, 145)
ANOTHER_IMAGE_SIZE = (50, 73)
screen.fill((0, 204, 0))
font = pygame.font.Font('freesansbold.ttf', 32)
suits = ["club", "heart", "spade", "diamond"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king", "ace"]
tabledeck = []
played_cards = 0
