import pygame
from load_image import load_image

class Card(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0, is_in_target=False):
        super().__init__()

        self.is_in_target = is_in_target
        self._images = load_images()
        self.image = self.images["card"]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def _load_images(self):
        return {}