import pygame
from shuffle import Methods
from pygame import font
from cards import AceofSpades

pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
font = pygame.font.Font('freesansbold.ttf', 32)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
running = True
choose_start = "START"
choose_stats = "STATISTICS"
while running:
            

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Fill the background with white
    screen.fill((0, 204, 0))

    text1 = font.render(choose_start, True, (0,0,0), (255,255,255))
    text2 = font.render(choose_stats, True, (0,0,0), (255,255,255))
    text1Rect = text1.get_rect()
    text1Rect.center = (300, 500)
    text2Rect = text2.get_rect()
    text2Rect.center = (700, 500)
    screen.blit(text1, text1Rect)
    screen.blit(text2, text2Rect)
    screen.display()

    pygame.display.flip()
pygame.quit()