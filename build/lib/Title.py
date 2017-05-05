import pygame
from pygame.sprite import Sprite


class Title(Sprite):
    def __init__(self, screen):
        Sprite.__init__(self)
        self.screen = screen
        self.image = pygame.image.load('foodFetcherImg.png').convert_alpha()
        self.image_w, self.image_h = self.image.get_size()

    def blitme(self, x_pos, y_pos):
        self.screen.blit(self.image, (x_pos, y_pos))
