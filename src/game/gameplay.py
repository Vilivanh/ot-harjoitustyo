import itertools, random
import pygame

players = 4

class Decks:
    def table_deck():
        tabledeck = []
    
    def computer_deck(deck):
        computer_deck = deck

    def player_deck(deck):
        playerdeck = deck

    def play(card):
        chosen_card = card
        tabledeck.append(chosen_card)
        #if len(tabledeck) == players:
            #turn does not change
        #else:
            #turn changes


    def pick(tabledeck):
        if len(tabledeck) == 0:
            return
        picked_card = tabledeck[0]
        playerdeck.append(picked_card)
        tabledeck.pop(0)


