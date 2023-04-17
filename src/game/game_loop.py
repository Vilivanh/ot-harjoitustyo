import pygame as pygame
import os
from deck import *
from constants import *
from play import Play
from Computerchoose import ComputerChoose
from Update import UpdateScreen
import sys
import time
pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption('Norri')
screen.fill((0, 204, 0))
players_number = 6
PlayerHand, ComputerHands = Play().deal(players_number)
clickhandles = []
tablehandles = []

running = True
newturn = False
while running:
    if len(tabledeck) > 0:
        for i in range(len(tabledeck)):
            rank = tabledeck[i][0]
            if rank == "11":
                rank = "jack"
            elif rank == "12":
                rank = "queen"
            elif rank == "13":
                rank = "king"
            elif rank == "14":
                rank = "ace"
            else:
                rank = tabledeck[i][0]
            suit = tabledeck[i][1]
            card_position = pygame.Rect(100+i*60, 200, 59, 145)
            
            tablehandles.append((card_position, rank, suit))
    for i in range(len(PlayerHand)):

        
        rank = PlayerHand[i][0]
        if rank == "11":
            rank = "jack"
        if rank == "12":
            rank = "queen"
        if rank == "13":
            rank = "king"
        if rank == "14":
            rank = "ace"
        suit = PlayerHand[i][1]
        filename = "{}_of_{}s.png".format(rank, suit)
        image = pygame.image.load(os.path.join(dirname, "assets", filename))
        image_scaled = pygame.transform.scale(image, DEFAULT_IMAGE_SIZE)
        card_position = pygame.Rect(60+i*60, 500, 59, 145)
        
        clickhandles.append((card_position, rank, suit))
        screen.blit(image_scaled, (60+i*60, 500))
    if len(ComputerHands) == 1:
        for i in range(len(ComputerHands)):
            for j in range(len(ComputerHands[i])):
                
                filename = "BACK.png"
                image = pygame.image.load(os.path.join(dirname, "assets", filename))
                image_scaled2 = pygame.transform.scale(image, ANOTHER_IMAGE_SIZE)
                image_scaled = pygame.transform.rotate(image_scaled2, (i+1)*90)
                if i == 0:
                    screen.blit(image_scaled, (200+j*30, 20))
    elif len(ComputerHands) == 2:
        for i in range(len(ComputerHands)):
            for j in range(len(ComputerHands[i])):
                
                filename = "BACK.png"
                image = pygame.image.load(os.path.join(dirname, "assets", filename))
                image_scaled2 = pygame.transform.scale(image, ANOTHER_IMAGE_SIZE)
                image_scaled = pygame.transform.rotate(image_scaled2, (i+1)*90)
                if i == 0:
                    screen.blit(image_scaled, (i*40, 200+10*j))
                if i == 1:
                    screen.blit(image_scaled, (200+j*30, 20))
                     
    elif len(ComputerHands) == 3:
        for i in range(len(ComputerHands)):
            for j in range(len(ComputerHands[i])):
                
                filename = "BACK.png"
                image = pygame.image.load(os.path.join(dirname, "assets", filename))
                image_scaled2 = pygame.transform.scale(image, ANOTHER_IMAGE_SIZE)
                image_scaled = pygame.transform.rotate(image_scaled2, (i+1)*90)
                if i == 0:
                    screen.blit(image_scaled, (i*40, 200+10*j))
                if i == 1:
                    screen.blit(image_scaled, (200+j*30, 20))
                if i == 2:
                    screen.blit(image_scaled, (i*450, 200+10*j))
    elif len(ComputerHands) == 4:
        for i in range(len(ComputerHands)):
            for j in range(len(ComputerHands[i])):
                
                filename = "BACK.png"
                image = pygame.image.load(os.path.join(dirname, "assets", filename))
                image_scaled2 = pygame.transform.scale(image, ANOTHER_IMAGE_SIZE)
                if i == 0:
                    image_scaled = pygame.transform.rotate(image_scaled2, (i+1)*90)
                elif i == 1:
                    image_scaled = pygame.transform.rotate(image_scaled2, (i+1)*90)
                elif i == 2:
                    image_scaled = pygame.transform.rotate(image_scaled2, (i)*90)
                elif i == 3:
                    image_scaled = pygame.transform.rotate(image_scaled2, (i)*90)
                if i == 0:
                    screen.blit(image_scaled, (10+i*40, 200+10*j))
                if i == 1:
                    screen.blit(image_scaled, (20+j*30, 10))
                if i == 2:
                    screen.blit(image_scaled, (450+(j-1)*30, 10))
                if i == 3:
                    screen.blit(image_scaled, (i*275, 200+10*j))

    elif len(ComputerHands) == 5:
        for i in range(len(ComputerHands)):
            for j in range(len(ComputerHands[i])):
                
                filename = "BACK.png"
                image = pygame.image.load(os.path.join(dirname, "assets", filename))
                image_scaled2 = pygame.transform.scale(image, ANOTHER_IMAGE_SIZE)
                if i == 0:
                    image_scaled = pygame.transform.rotate(image_scaled2, (i+1)*90)
                elif i == 1:
                    image_scaled = pygame.transform.rotate(image_scaled2, (i+1)*90)
                elif i == 2:
                    image_scaled = pygame.transform.rotate(image_scaled2, (i)*90)
                elif i == 3:
                    image_scaled = pygame.transform.rotate(image_scaled2, (i-1)*90)
                elif i == 4:
                    image_scaled = pygame.transform.rotate(image_scaled2, (i-1)*90)
                if i == 0:
                    screen.blit(image_scaled, (10+i*40, 200+10*j))
                if i == 1:
                    screen.blit(image_scaled, (0+j*20, 10))
                if i == 2:
                    screen.blit(image_scaled, (350+(j-1)*20, 10))
                if i == 3:
                    screen.blit(image_scaled, (650+(j-2)*20, 10))
                if i == 4:
                    screen.blit(image_scaled, (i*225, 200+10*j))

    if len(tabledeck) > 0: 
        for i in range(len(tabledeck)):
            rank, suit = tabledeck[i][0], tabledeck[i][1]
            filename = "{}_of_{}s.png".format(rank, suit)
            image = pygame.image.load(os.path.join(dirname, "assets", filename))
            image_scaled = pygame.transform.scale(image, DEFAULT_IMAGE_SIZE)
            card_position = pygame.Rect(100+i*60, 200, 59, 145)
            screen.blit(image_scaled, (100+i*60, 200))


    if played_cards == 0:
        for i in range(len(ComputerHands)):
            for j in range(len(ComputerHands[i])):
                if ComputerHands[i][j] == ("2", "club"):
                    TurnToPlay = f"Computer {i}"
        for i in range(len(PlayerHand)):
            if PlayerHand[i] == ("2", "club"):
                TurnToPlay = "Player"
        if TurnToPlay != "Player":
            PlayingComputer = int(TurnToPlay[-1])
            chosen_card = ("2", "club")
            tabledeck.append(chosen_card)
            played_cards +=1
            ComputerHands[PlayingComputer].remove(chosen_card)
            UpdateScreen.update_screen(PlayerHand, ComputerHands, tabledeck)
            PlayingComputer += 1
            TurnToPlay = f"Computer {PlayingComputer}"
            if PlayingComputer == len(ComputerHands):
                PlayingComputer = None
                TurnToPlay = "Player"

    
    if played_cards > 0:
        if TurnToPlay != "Player":
            PlayingComputer = int(TurnToPlay[-1])
            if len(tabledeck) > 0:
                playedhand = ComputerHands[PlayingComputer]
                chosen = ComputerChoose.nonempty(tabledeck, playedhand)
                if chosen != None:
                    tabledeck.append(chosen)
                    ComputerHands[PlayingComputer].remove(chosen)
                    UpdateScreen.update_screen(PlayerHand, ComputerHands, tabledeck)
                    if len(ComputerHands[PlayingComputer]) == 0:
                        ComputerHands.pop(PlayingComputer)
                        players_number -=1
                    pygame.time.wait(900)
                    played_cards += 1
                    if len(tabledeck) == players_number:
                        TurnToPlay = f"Computer {PlayingComputer}"
                        tabledeck = []
                        UpdateScreen.update_screen(PlayerHand, ComputerHands, tabledeck)
                    else:
                        UpdateScreen.update_screen(PlayerHand, ComputerHands, tabledeck)
                        nextturn = PlayingComputer + 1
                        if nextturn == len(ComputerHands):
                            TurnToPlay = "Player"
                        else:
                            TurnToPlay = f"Computer {nextturn}"

                if chosen == None:
                    ComputerHands[PlayingComputer].append(tabledeck[0])
                    tabledeck.pop(0)
                    UpdateScreen.update_screen(PlayerHand, ComputerHands, tabledeck)
                    played_cards += 1
                    nextturn = PlayingComputer + 1
                    if nextturn == len(ComputerHands):
                        TurnToPlay = "Player"
                    else:
                        TurnToPlay = f"Computer {nextturn}"

            else:
                playedhand = ComputerHands[PlayingComputer]
                chosen = ComputerChoose.emptytable(playedhand)
                if chosen != None:
                    tabledeck.append(chosen)
                    ComputerHands[PlayingComputer].remove(chosen)
                    if len(ComputerHands[PlayingComputer]) == 0:
                        ComputerHands.pop(PlayingComputer)
                        players_number -= 1
                    nextturn = PlayingComputer + 1
                    if nextturn == len(ComputerHands):
                        TurnToPlay = "Player"
                    else:
                        TurnToPlay = f"Computer {nextturn}"
                    UpdateScreen.update_screen(PlayerHand, ComputerHands, tabledeck)
                    played_cards += 1
                

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if TurnToPlay == "Player":
                clicked = None
                tableclicked = None
                mouse_pos = event.pos
                for i in range(len(tablehandles)):
                    if tablehandles[0][0].collidepoint(mouse_pos):
                        tableclicked = (tablehandles[0][1], tablehandles[0][2])
                
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
                        clicked_card_suit = clicked[1]
                if played_cards == 0:
                    if clicked == ("2", "club"):
                        tabledeck.append(clicked)
                        PlayerHand.remove(clicked)
                        UpdateScreen.update_screen(PlayerHand, ComputerHands, tabledeck)
                        played_cards += 1
                        clickhandles = []
                        TurnToPlay = "Computer 0"
                else:
                    if len(tabledeck) > 0:
                        top_card = tabledeck[-1]
                        toprank = top_card[0]
                        if toprank == "jack":
                            toprank = "11"
                        if toprank == "queen":
                            toprank = "12"
                        if toprank == "king":
                            toprank = "13"
                        if toprank == "ace":
                            toprank = "14"
                        topsuit = top_card[1]
                        if clicked != None:
                            rank = clicked[0]
                            if rank == "jack":
                                rank = "11"
                            elif rank == "queen":
                                rank = "12"
                            elif rank == "king":
                                rank = "13"
                            elif rank == "ace":
                                rank = "14"
                            else:
                                rank = clicked[0]
                            if clicked[1] == topsuit:
                                if int(rank) > int(toprank):
                                    tabledeck.append(clicked)
                                    PlayerHand.remove(clicked)
                                    clickhandles = []
                                    UpdateScreen.update_screen(PlayerHand, ComputerHands, tabledeck)
                                    if len(tabledeck) == players_number:
                                        TurnToPlay = "Player"
                                        tabledeck = []
                                    else:
                                        TurnToPlay = "Computer 0"
                            else:
                                if topsuit == "spade":
                                    if clicked[1] == "diamond":
                                        tabledeck.append(clicked)
                                        PlayerHand.remove(clicked)
                                        clickhandles = []
                                        UpdateScreen.update_screen(PlayerHand, ComputerHands, tabledeck)
                                        if len(tabledeck) == players_number:
                                            TurnToPlay = "Player"
                                            tabledeck = []
                                            newturn = True
                                        else:
                                            TurnToPlay = "Computer 0"
                                if topsuit == "heart":
                                    if clicked[1] == "diamond":
                                        tabledeck.append(clicked)
                                        PlayerHand.remove(clicked)
                                        clickhandles = []
                                        UpdateScreen.update_screen(PlayerHand, ComputerHands, tabledeck)
                                        if len(tabledeck) == players_number:
                                            TurnToPlay = "Player"
                                            tabledeck = []
                                        else:
                                            TurnToPlay = "Computer 0"
                        elif clicked == None:
                            if tableclicked != None:
                                PlayerHand.append(tabledeck[0])
                                tabledeck.pop(0)
                                
                                UpdateScreen.update_screen(PlayerHand, ComputerHands, tabledeck)
                                TurnToPlay = "Computer 0"
                    elif len(tabledeck) == 0:
                        if newturn == True:
                            UpdateScreen.update_screen(PlayerHand, ComputerHands, tabledeck)
                            if clicked != None:
                                tabledeck.append(clicked)
                                PlayerHand.remove(clicked)
                                clickhandles = []
                                UpdateScreen.update_screen(PlayerHand, ComputerHands, tabledeck)
                                TurnToPlay = "Computer 0"
                                newturn = False
                        else:
                            if clicked != None:
                                tabledeck.append(clicked)
                                PlayerHand.remove(clicked)
                                UpdateScreen.update_screen(PlayerHand, ComputerHands, tabledeck)
                                TurnToPlay = "Computer 0"
                                



    
    pygame.display.flip()