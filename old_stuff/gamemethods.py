import pygame

class Turns:
    def __init__(self, TableDeck):
        tabledeck_length = len(TableDeck)
        top_card = TableDeck[tabledeck_length - 1]
        bottom_card = TableDeck[0]

    def _pick(self):
        PlayerDeck.append(bottom_card)
        TableDeck.pop(0)


    def _play(self, chosen_card):
        TableDeck.append(chosen_card)
        PlayerDeck.pop(chosen_card)

        if len(TableDeck) == players:
            while len(TableDeck)>0:
                TableDeck.pop(0)

    def _choose(self, chosen_option):
        if chosen_option == card:
            if card > top_card:
                _play(card)
            else:
                print("can't play")
        if chosen_option == pick:
            _pick()


class ComputerTurns:
    def ():
        