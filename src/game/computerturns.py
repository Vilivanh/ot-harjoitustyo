import pygame
import os
from pygame.locals import *

dirname = os.path.dirname(__file__)
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
DEFAULT_IMAGE_SIZE = (100, 145)

class ComputerTurn:
    
    def computers_turn(tabledeck, playerlists, players_number, computer_number):
        #if len(tabledeck) > 0:
            #for i in range(len(tabledeck)):
                #rank = tabledeck[i][0]
                #if rank == "11":
                    #rank = "jack"
                #if rank == "12":
                    #rank = "queen"
                #if rank == "13":
                    #rank = "king"
                #if rank == "14":
                    #rank = "ace"
                #suit = tabledeck[i][1]
                #filename = "{}_of_{}s.png".format(rank, suit)
                #image = pygame.image.load(os.path.join(dirname, "assets", filename))
                #image_scaled = pygame.transform.scale(image, DEFAULT_IMAGE_SIZE)
                #card_position = pygame.Rect(60+i*80, 300, 59, 145)
                
                
                #screen.blit(image_scaled, (60+i*80,300))
        computers_deck = playerlists[computer_number]
        
        chosen = None
        if len(tabledeck) == 0:
            for i in range(len(computers_deck)):
                chosen = computers_deck[i]
                if computers_deck[i][1] == "heart" or "spade":
                    if computers_deck[i][0] == "jack":
                        comp_int = int(11)
                    elif computers_deck[i][0] == "queen":
                        comp_int = int(12)
                    elif computers_deck[i][0] == "king":
                        comp_int = int(13)
                    elif computers_deck[i][0] == "ace":
                        comp_int = int(14)
                    else:
                        comp_int = int(computers_deck[i][0])
                    if computers_deck[i][0] == "jack":
                        if comp_int > 11:
                            chosen = (computers_deck[i][0], computers_deck[i][1])
                    elif computers_deck[i][0] == "queen":
                        if comp_int > 12:
                            chosen = (computers_deck[i][0], computers_deck[i][1])
                    elif computers_deck[i][0] == "king":
                        if comp_int > 13:
                            chosen = (computers_deck[i][0], computers_deck[i][1])
                    elif computers_deck[i][0] == "ace":
                        if comp_int > 14:
                            chosen = (computers_deck[i][0], computers_deck[i][1])
                    else:
                        if int(computers_deck[i][0]) < comp_int:
                            chosen = (computers_deck[i][0], computers_deck[i][1])
                if computers_deck[i][1] == "club":
                    if computers_deck[i][0] == "jack":
                        comp_int = int(11)
                    elif computers_deck[i][0] == "queen":
                        comp_int = int(12)
                    elif computers_deck[i][0] == "king":
                        comp_int = int(13)
                    elif computers_deck[i][0] == "ace":
                        comp_int = int(14)
                    else:
                        comp_int = int(computers_deck[i][0])
                        if chosen[1] == "club" and comp_int < int(chosen[0]):
                            chosen = (computers_deck[i][0], computers_deck[i][1])
                    if chosen[1] == "diamond":
                        chosen = (computers_deck[i][0], computers_deck[i][1])
        else:
            top_card = tabledeck[-1]
            if top_card[0] == "jack":
                top_card_int = int(11)
            elif top_card[0] == "queen":
                top_card_int = int(12)
            elif top_card[0] == "king":
                top_card_int = int(13)
            elif top_card[0] == "ace":
                top_card_int = int(14)
            else:
                top_card_int = int(top_card[0])
            chosen = None
            for i in range(len(computers_deck)):
                if top_card[1] == computers_deck[i][1]:
                    if computers_deck[i][0] == "jack":
                        comp_int = 11
                    elif computers_deck[i][0] == "queen":
                        comp_int = 12
                    elif computers_deck[i][0] == "king":
                        comp_int = 13
                    elif computers_deck[i][0] == "ace":
                        comp_int = 14
                    else:
                        comp_int = int(computers_deck[i][0])
                    if top_card_int < comp_int:
                        if chosen != None:
                            if chosen[0] == "jack":
                                if comp_int < 11:
                                    chosen = computers_deck[i]
                            elif chosen[0] == "queen":
                                if comp_int < 12:
                                    chosen = computers_deck[i]
                            elif chosen[0] == "king":
                                if comp_int < 13:
                                    chosen = computers_deck[i]
                            elif chosen[0] == "ace":
                                if comp_int < 14:
                                    chosen = computers_deck[i]
                            else:
                                if comp_int < int(chosen[0]):
                                    chosen = computers_deck[i] 
                        elif chosen == None:
                            chosen = computers_deck[i]
                elif top_card[1] == "spade" or top_card[1] == "heart":
                    if chosen == None:
                        if computers_deck[i][0] == "jack":
                            comp_int = 11
                        elif computers_deck[i][0] == "queen":
                            comp_int = 12
                        elif computers_deck[i][0] == "king":
                            comp_int = 13
                        elif computers_deck[i][0] == "ace":
                            comp_int = 14
                        else:
                            comp_int = int(computers_deck[i][0])
                        if top_card_int > 11 and comp_int < 5:
                            chosen = computers_deck[i]
            if len(tabledeck) == 1:
                if top_card_int > 5 and top_card[1] == "diamond":
                    chosen = None

        if chosen == None:
            playerlists[computer_number].append(tabledeck[0])
            tabledeck.pop(0)
            computer_number += 1
            if computer_number == players_number:
                starting = "0"
                return starting
            else:
                starting = f"{computer_number}"
                return starting
        elif chosen != None:
            tabledeck.append(chosen)
            playerlists[computer_number].remove(chosen)
            if len(tabledeck) == players_number:
                tabledeck = []
                starting = f"{computer_number}"
                return starting
            elif len(tabledeck) < players_number:
                computer_number +=1
                if computer_number == players_number:
                    starting = "0"
                    return starting
                else:
                    
                    starting = f"{computer_number}"
                    return starting
                    computer_number += 1
                    ComputerTurn.computers_turn(tabledeck, playerlists, players_number, computer_number)