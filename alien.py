import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Class representing one alien."""

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen

        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = 0
        self.rect.y = 0

        self.x = float(self.rect.x)

