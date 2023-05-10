"""
Module that constructs card for the ui
"""
import os
import pygame
from constants import ANOTHER_IMAGE_SIZE, DEFAULT_IMAGE_SIZE

class CardHandlers:
    def __init__(self):
        self.dirname = os.path.dirname(__file__)
    def back_image_scaler(self):
        """
        No args, returns back of card
        """
        filename = "BACK.png"
        image = pygame.image.load(os.path.join(self.dirname, "assets", filename))
        image_scaled2 = pygame.transform.scale(image, ANOTHER_IMAGE_SIZE)
        return image_scaled2
    def card_image_scaler(self, rank, suit):
        """
        Args: rank, suit
        Returns: card
        """
        self.rank = rank
        self.suit = suit
        filename = "{}_of_{}s.png".format(rank, suit)
        image = pygame.image.load(os.path.join(self.dirname, "assets", filename))
        image_scaled = pygame.transform.scale(image, DEFAULT_IMAGE_SIZE)
        return image_scaled
    