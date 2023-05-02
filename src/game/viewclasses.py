import pygame
from constants import *
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption('Norri')

pygame.init()

class Screens:
    """
    draw start-screen and rule-screen
    """
    def __init__(self):
        self._font = pygame.font.SysFont('freesansbold.ttf', 32)

    def start_screen(self, screen):
        """
        Make the start screen
        """
        self.options = []
        screen.fill((0, 204, 0))
        option_color = (255, 0, 255)
        for i in range(2):
            self.options.append(pygame.draw.rect(screen, option_color, (100*(i+1), 200, 70, 50)))
            
        text1 = self.font.render("start", 1, option_color)
        text2 = self.font.render("rules", 1, option_color)
        screen.blit(text1, (110, 200))
        screen.blit(text2, (210, 200))

    def rules_screen(self, screen):
        """
        show rules
        """
        #To be continued
        return


    