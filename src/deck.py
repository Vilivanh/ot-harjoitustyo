"""
Set up a deck of cards for the game
"""
import random
import pygame
import os
from constants import *
from cardhandlers import CardHandlers
pygame.init()

class Deck:
    """
    Class to create the deck and needed methods
    """
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
            image_scaled = CardHandlers.card_image_scaler(rank, suit)           
            if image_scaled not in self.card_img:
                self.card_img.append(image_scaled)
        