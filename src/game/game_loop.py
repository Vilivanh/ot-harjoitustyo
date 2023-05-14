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
players_number = 6
played_cards = 0
player_hand, Computer_Hands = Play().deal(players_number)
clickhandles = []
tablehandles = []
tabledeck = []
TURNTOPLAY = None
RUNNING = True
NEWTURN = False
def game_loop(RUNNING, tabledeck, clickhandles, tablehandles, played_cards, players_number, NEWTURN):
    while RUNNING:
        if len(tabledeck) > 0:
            for i in range(len(tabledeck)):
                print(tabledeck)
                rank2 = tabledeck[i][0]
                rank = Handlers().rank_fixer(rank2)
                suit = tabledeck[i][1]
                card_position = pygame.Rect(100+i*60, 200, 59, 145)
                tablehandles.append((card_position, rank, suit))
        for i in range(len(player_hand)):
            rank2 = player_hand[i][0]
            rank = Handlers().rank_fixer(rank2)
            suit = player_hand[i][1]
            image_scaled = CardHandlers().card_image_scaler(rank, suit)
            card_position = pygame.Rect(60+i*60, 500, 59, 145)
            clickhandles.append((card_position, rank, suit))
            screen.blit(image_scaled, (60+i*60, 500))
        Handlers().computer_handler(Computer_Hands, screen, dirname)
        if len(tabledeck) > 0: 
            for i in range(len(tabledeck)):
                rank, suit = tabledeck[i][0], tabledeck[i][1]
                image_scaled = CardHandlers().card_image_scaler(rank, suit)
                card_position = pygame.Rect(100+i*60, 200, 59, 145)
                screen.blit(image_scaled, (100+i*60, 200))
        if played_cards == 0:
            for i in range(len(Computer_Hands)):
                for j in range(len(Computer_Hands[i])):
                    if Computer_Hands[i][j] == ("2", "club"):
                        TURNTOPLAY = f"Computer {i}"
            for i in range(len(player_hand)):
                if player_hand[i] == ("2", "club"):
                    TURNTOPLAY = "Player"
            if TURNTOPLAY != "Player":
                PlayingComputer = int(TURNTOPLAY[-1])
                CHOSEN_card = ("2", "club")
                tabledeck.append(CHOSEN_card)
                played_cards += 1
                Computer_Hands[PlayingComputer].remove(CHOSEN_card)
                UpdateScreen().update_screen(player_hand, Computer_Hands, tabledeck)
                PlayingComputer += 1
                TURNTOPLAY = f"Computer {PlayingComputer}"
                if PlayingComputer == len(Computer_Hands):
                    PlayingComputer = None
                    TURNTOPLAY = "Player"
        elif played_cards > 0:
            if TURNTOPLAY != "Player":
                PlayingComputer = int(TURNTOPLAY[-1])
                print(PlayingComputer)
                if len(tabledeck) > 0:
                    PLAYEDHAND = Computer_Hands[PlayingComputer]
                    print(PLAYEDHAND)
                    CHOSEN = ComputerChoose().nonempty(tabledeck, PLAYEDHAND, players_number)
                    print(Computer_Hands)
                    if CHOSEN is not None:
                        tabledeck.append(CHOSEN)
                        Computer_Hands[PlayingComputer].remove(CHOSEN)
                        UpdateScreen().update_screen(player_hand, Computer_Hands, tabledeck)
                        if len(Computer_Hands[PlayingComputer]) == 0:
                            Computer_Hands.pop(PlayingComputer)
                            players_number -= 1
                            if PlayingComputer == len(Computer_Hands):
                                TURNTOPLAY == "Player"
                        pygame.time.wait(150)
                        played_cards += 1
                        if len(tabledeck) == players_number:
                            TURNTOPLAY = f"Computer {PlayingComputer}"
                            tabledeck = []
                            UpdateScreen().update_screen(player_hand, Computer_Hands, tabledeck)
                        else:
                            UpdateScreen().update_screen(player_hand, Computer_Hands, tabledeck)
                            NEXTTURN = PlayingComputer + 1
                            if NEXTTURN == len(Computer_Hands):
                                TURNTOPLAY = "Player"
                            else:
                                TURNTOPLAY = f"Computer {NEXTTURN}"
                    if CHOSEN is None:
                        Computer_Hands[PlayingComputer].append(tabledeck[0])
                        tabledeck.pop(0)
                        UpdateScreen().update_screen(player_hand, Computer_Hands, tabledeck)
                        played_cards += 1
                        NEXTTURN = PlayingComputer + 1
                        if NEXTTURN == len(Computer_Hands):
                            TURNTOPLAY = "Player"
                        else:
                            TURNTOPLAY = f"Computer {NEXTTURN}"

                else:
                    PLAYEDHAND = Computer_Hands[PlayingComputer]
                    CHOSEN = ComputerChoose().emptytable(PLAYEDHAND)
                    print(f"this is {CHOSEN}")
                    if CHOSEN is not None:
                        tabledeck.append(CHOSEN)
                        Computer_Hands[PlayingComputer].remove(CHOSEN)
                        if len(Computer_Hands[PlayingComputer]) == 0:
                            Computer_Hands.pop(PlayingComputer)
                            players_number -= 1
                        NEXTTURN = PlayingComputer + 1
                        if NEXTTURN == len(Computer_Hands):
                            TURNTOPLAY = "Player"
                        else:
                            TURNTOPLAY = f"Computer {NEXTTURN}"
                        UpdateScreen().update_screen(player_hand, Computer_Hands, tabledeck)
                        played_cards += 1
                    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUNNING = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if TURNTOPLAY == "Player":
                    clicked = None
                    tableclicked = None
                    mouse_pos = event.pos
                    for i in range(len(tablehandles)):
                        if tablehandles[0][0].collidepoint(mouse_pos):
                            tableclicked = (tablehandles[0][1], tablehandles[0][2])                
                    for i in range(len(clickhandles)):
                        if clickhandles[i][0].collidepoint(mouse_pos):
                            clicked = (clickhandles[i][1], clickhandles[i][2])
                            clicked_card_int = int(Handlers().rank_integer(clicked[0]))
                            clicked_card_suit = clicked[1]
                    if played_cards == 0:
                        if clicked == ("2", "club"):
                            tabledeck.append(clicked)
                            player_hand.remove(clicked)
                            UpdateScreen().update_screen(player_hand, Computer_Hands, tabledeck)
                            played_cards += 1
                            clickhandles = []
                            TURNTOPLAY = "Computer 0"
                    else:
                        if len(tabledeck) > 0:
                            top_card = tabledeck[-1]
                            toprank = Handlers().rank_integer(top_card[0])
                            topsuit = top_card[1]
                            if clicked is not None:
                                rank = Handlers().rank_integer(clicked[0])
                                if clicked[1] == topsuit:
                                    if int(rank) > int(toprank):
                                        tabledeck.append(clicked)
                                        player_hand.remove(clicked)
                                        clickhandles = []
                                        UpdateScreen().update_screen(player_hand, Computer_Hands, tabledeck)
                                        if len(tabledeck) == players_number:
                                            TURNTOPLAY = "Player"
                                            tabledeck = []
                                            UpdateScreen().update_screen(player_hand, Computer_Hands, tabledeck)
                                        else:
                                            TURNTOPLAY = "Computer 0"
                                else:
                                    if topsuit == "spade":
                                        if clicked[1] == "diamond":
                                            tabledeck.append(clicked)
                                            player_hand.remove(clicked)
                                            clickhandles = []
                                            UpdateScreen().update_screen(player_hand, Computer_Hands, tabledeck)
                                            if len(tabledeck) == players_number:
                                                TURNTOPLAY = "Player"
                                                tabledeck = []
                                                NEWTURN = True
                                            else:
                                                TURNTOPLAY = "Computer 0"
                                    if topsuit == "heart":
                                        if clicked[1] == "diamond":
                                            tabledeck.append(clicked)
                                            player_hand.remove(clicked)
                                            clickhandles = []
                                            UpdateScreen().update_screen(player_hand, Computer_Hands, tabledeck)
                                            if len(tabledeck) == players_number:
                                                TURNTOPLAY = "Player"
                                                tabledeck = []
                                            else:
                                                TURNTOPLAY = "Computer 0"
                            elif clicked == None:
                                if tableclicked is not None:
                                    player_hand.append(tabledeck[0])
                                    tabledeck.pop(0)
                                    UpdateScreen().update_screen(player_hand, Computer_Hands, tabledeck)
                                    TURNTOPLAY = "Computer 0"
                        elif len(tabledeck) == 0:
                            if NEWTURN is True:
                                UpdateScreen().update_screen(player_hand, Computer_Hands, tabledeck)
                                if clicked != None:
                                    tabledeck.append(clicked)
                                    player_hand.remove(clicked)
                                    if len(player_hand) == 0:
                                        score = 7-players_number
                                        if score == 1:
                                            text = font.render(f"You finished{score}st", True, (255, 255, 255), (0, 0, 0))
                                        elif score == 2:
                                            text = font.render(f"You finished{score}nd", True, (255, 255, 255), (0, 0, 0))
                                        elif score == 3:
                                            text = font.render(f"You finished{score}rd", True, (255, 255, 255), (0, 0, 0))
                                        else:
                                            text = font.render(f"You finished{score}st", True, (255, 255, 255), (0, 0, 0))
                                        text_rect = text.get_rect()
                                        text_rect.center = (500, 350)
                                        screen.blit(text, text_rect)
                                        pygame.time.wait(30000)
                                    clickhandles = []
                                    UpdateScreen().update_screen(player_hand, Computer_Hands, tabledeck)
                                    TURNTOPLAY = "Computer 0"
                                    NEWTURN = False
                            else:
                                if clicked is not None:
                                    tabledeck.append(clicked)
                                    player_hand.remove(clicked)
                                    if len(player_hand) == 0:
                                        score = 7-players_number
                                        if score == 1:
                                            text = font.render(f"You finished{score}st", True, (255, 255, 255), (0, 0, 0))
                                        elif score == 2:
                                            text = font.render(f"You finished{score}nd", True, (255, 255, 255), (0, 0, 0))
                                        elif score == 3:
                                            text = font.render(f"You finished{score}rd", True, (255, 255, 255), (0, 0, 0))
                                        else:
                                            text = font.render(f"You finished{score}st", True, (255, 255, 255), (0, 0, 0))
                                        text_rect = text.get_rect()
                                        text_rect.center = (500, 350)
                                        screen.blit(text, text_rect)
                                        pygame.time.wait(30000)
                                    UpdateScreen().update_screen(player_hand, Computer_Hands, tabledeck)
                                    TURNTOPLAY = "Computer 0"
                                    
        pygame.display.flip()