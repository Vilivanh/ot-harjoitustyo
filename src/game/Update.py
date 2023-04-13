import pygame
from constants import *
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption('Norri')
screen.fill((0, 204, 0))
clickhandles = []
tablehandles = []
class UpdateScreen:
    def update_screen(PlayerHand, ComputerHands, tabledeck):
        
        screen.fill((0, 204, 0))
        clickhandles = []
        tablehandles = []

        if len(tabledeck)>0:
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
            screen.blit(image_scaled, (60+i*60,500))

        if len(ComputerHands) == 3:
            for i in range(len(ComputerHands)):
                for j in range(len(ComputerHands[i])):
                    
                    filename = "BACK.png"
                    image = pygame.image.load(os.path.join(dirname, "assets", filename))
                    image_scaled2 = pygame.transform.scale(image, ANOTHER_IMAGE_SIZE)
                    image_scaled = pygame.transform.rotate(image_scaled2, (i+1)*90)
                    if i == 0:
                        screen.blit(image_scaled, (i*40,200+10*j))
                    if i == 1:
                        screen.blit(image_scaled, (200+j*30,20))
                    if i == 2:
                        screen.blit(image_scaled, (i*450,200+10*j))
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
                        screen.blit(image_scaled, (10+i*40,200+10*j))
                    if i == 1:
                        screen.blit(image_scaled, (20+j*30,10))
                    if i == 2:
                        screen.blit(image_scaled, (450+(j-1)*30,10))
                    if i == 3:
                        screen.blit(image_scaled, (i*275,200+10*j))

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
                        screen.blit(image_scaled, (10+i*40,200+10*j))
                    if i == 1:
                        screen.blit(image_scaled, (0+j*20,10))
                    if i == 2:
                        screen.blit(image_scaled, (350+(j-1)*20,10))
                    if i == 3:
                        screen.blit(image_scaled, (650+(j-2)*20,10))
                    if i == 4:
                        screen.blit(image_scaled, (i*225,200+10*j))

            if len(tabledeck) > 0: 
                for i in range(len(tabledeck)):
                    rank, suit = tabledeck[i][0], tabledeck[i][1]
                    filename = "{}_of_{}s.png".format(rank, suit)
                    image = pygame.image.load(os.path.join(dirname, "assets", filename))
                    image_scaled = pygame.transform.scale(image, DEFAULT_IMAGE_SIZE)
                    card_position = pygame.Rect(100+i*60, 200, 59, 145)
                    screen.blit(image_scaled, (100+i*60,200))