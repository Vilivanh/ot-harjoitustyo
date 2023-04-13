import pygame
import os
from pygame.locals import *
from computerturns import ComputerTurn
dirname = os.path.dirname(__file__)
DEFAULT_IMAGE_SIZE = (100, 145)
running  = True
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
class PlayerTurn:
    def players_turn(tabledeck, playerlists, players_number):
        if len(tabledeck) > 0:
            for i in range(len(tabledeck)):
                rank = tabledeck[i][0]
                if rank == "11":
                    rank = "jack"
                if rank == "12":
                    rank = "queen"
                if rank == "13":
                    rank = "king"
                if rank == "14":
                    rank = "ace"
                suit = tabledeck[i][1]
                filename = "{}_of_{}s.png".format(rank, suit)
                image = pygame.image.load(os.path.join(dirname, "assets", filename))
                image_scaled = pygame.transform.scale(image, DEFAULT_IMAGE_SIZE)
                card_position = pygame.Rect(60+i*80, 300, 59, 145)
                
                
                screen.blit(image_scaled, (60+i*80,300))
        players_list = playerlists[0]
        clickhandles = []
        for i in range(len(players_list)):
            rank = players_list[i][0]
            if rank == "11":
                rank = "jack"
            if rank == "12":
                rank = "queen"
            if rank == "13":
                rank = "king"
            if rank == "14":
                rank = "ace"
            suit = players_list[i][1]
            filename = "{}_of_{}s.png".format(rank, suit)
            image = pygame.image.load(os.path.join(dirname, "assets", filename))
            image_scaled = pygame.transform.scale(image, DEFAULT_IMAGE_SIZE)
            card_position = pygame.Rect(60+i*60, 500, 59, 145)
            
            clickhandles.append((card_position, rank, suit))
            screen.blit(image_scaled, (60+i*60,500))
        if len(tabledeck) > 0:
            top_card = tabledeck[-1]
        for event in pygame.event.get():
            if len(tabledeck) >0:
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
            elif len(tabledeck) == 0:
                Freetoplay = True
            if event.type == pygame.QUIT:
                running = False   
            if event.type == pygame.MOUSEBUTTONDOWN:
                clicked = None
                mouse_pos = event.pos
                clickhandles.append(mouse_pos)
                for i in range(len(clickhandles)):
                    if clickhandles[i][0].collidepoint(mouse_pos):
                        clicked = (clickhandles[i][1], clickhandles[i][2])
                        print(clicked)
                        if clicked[0] == "jack":
                            clicked_card_int = int(11)
                        elif clicked[0] == "queen":
                            clicked_card_int = int(12)
                        elif clicked[0] == "king":
                            clicked_card_int = int(13)
                        elif clicked[0] == "ace":
                            clicked_card_int = int(14)
                        else:
                            clicked_card_int = int(clicked[0])
                if Freetoplay == True:
                    tabledeck.append(clicked)
                    print(playerlists[0])
                    playerlists[0].remove(clicked)
                    ComputerTurn.computers_turn(tabledeck, playerlists, players_number, 1)
                if len(tabledeck) > 0:
                    top_card = tabledeck[-1]
                    if top_card[1] == "club":
                        if clicked[1] == "club":
                            
                            if clicked_card_int > top_card_int:
                                tabledeck.append(clicked)
                                playerlists[0].remove(clicked)
                                if len(tabledeck) == players_number:
                                    return PlayerTurn.players_turn([], playerlists, players_number)
                    elif top_card[1] == "spade":
                        if clicked[1] == "spade":
                            if clicked_card_int > top_card_int:
                                tabledeck.append(clicked)
                                playerlists[0].remove(clicked)
                                if len(tabledeck) == players_number:
                                    return PlayerTurn.players_turn([], playerlists, players_number)
                                else:
                                    ComputerTurn.computers_turn(tabledeck, playerlists, players_number, 1)
                        elif clicked[1] == "diamond":
                            tabledeck.append(clicked)
                    elif top_card[1] == "heart":
                        if clicked[1] == "heart":
                            if clicked_card_int > top_card_int:
                                tabledeck.append(clicked)
                                playerlists[0].remove(clicked)
                                if len(tabledeck) == players_number:
                                    PlayerTurn.players_turn([], playerlists, players_number)
                                else:
                                    ComputerTurn.computers_turn(tabledeck, playerlists, players_number, 1)
                        elif clicked[1] == "diamond":
                            tabledeck.append(clicked)
                            playerlists[0].remove(clicked)
                            if len(tabledeck) == players_number:
                                PlayerTurn.players_turn([], playerlists, players_number)
                            else:
                                ComputerTurn.computers_turn(tabledeck, playerlists, players_number, 1)
                    elif top_card[1] == "diamond":
                        if clicked[1] == "diamond":
                            if clicked_card_int > top_card_int:
                                tabledeck.append(clicked)
                                playerlists[0].remove(clicked)
                                if len(tabledeck) == players_number:
                                    PlayerTurn.players_turn([], playerlists, players_number)
                                else:
                                    ComputerTurn.computers_turn(tabledeck, playerlists, players_number, 1)




                    
            


