import pygame
from Food import Food


class Poison(Food):
    def __init__(self, screen, settings):
        Food.__init__(self, screen, settings)
        self.image = pygame.image.load('poisonImg.png').convert_alpha()
