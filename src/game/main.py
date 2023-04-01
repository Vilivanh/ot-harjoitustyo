# Import the pygame module
import pygame
import pygame_cards
from shuffle import Methods
from pygame import font
from cards import AceOfSpades

pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700

green = (0, 0, 0)
blue = (255, 255, 255)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
deck,playerlists = Methods.shuffle()
font = pygame.font.Font('freesansbold.ttf', 32)
players_list = playerlists[0]
print(players_list)


print(playerlists[0])
card_list = []

text = font.render(deck, True, green, blue)
textRect = text.get_rect()
textRect.center = (1000 // 2, 700 // 2)
screen.blit(text, textRect)    
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((0, 204, 0))

    
    screen.blit(text, textRect)
    for i in range(len(players_list)):
        text = font.render(players_list[i][1], True, green, blue)
        textRect = text.get_rect()
        textRect.center = (1000//2, 100+(i*50)//2)
        screen.blit(text, textRect)
        
    
    

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()
