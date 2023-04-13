import pygame
import os

# polku tämän tiedoston hakemistoon
dirname = os.path.dirname(__file__)

card_images = {}
suits = ["club", "heart", "spade", "diamond"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king", "ace"]
for suit in suits:
    for rank in ranks:
        filename = "cards/{}_of_{}s.png".format(rank, suit)
        card_images[(rank, suit)] = pygame.image.load(f"/assets/{filename}")

