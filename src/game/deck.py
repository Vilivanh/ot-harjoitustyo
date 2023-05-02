import random
import pygame
import os
from constants import ranks, suits
from constants import *

pygame.init()

class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        """
        create a deck
        Args: 
        rank (1-14), suit (club, spade, heart, diamond)
        Returns:
        Deck with 52 cards
        """
        for rank in ranks:
            for suit in suits:
                self.cards.append((rank, suit))
  
    def shuffle(self):
        random.shuffle(self.cards)

class Hand(Deck):
    def __init__(self):
        self.cards = []
        self.card_img = []
        

    def add_card(self, card):
        self.cards.append(card)

    def display_cards(self):
        for card in self.cards:
            rank, suit = card[0], card[1]
            filename = "{}_of_{}s.png".format(rank, suit)
            image = pygame.image.load(os.path.join(dirname, "assets", filename))
            image_scaled = pygame.transform.scale(image, DEFAULT_IMAGE_SIZE)
            
            if image_scaled not in self.card_img:
                self.card_img.append(image_scaled)
        

   