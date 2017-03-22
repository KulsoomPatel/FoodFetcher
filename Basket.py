import pygame
from pygame.sprite import Sprite


class Basket(Sprite):
    def __init__(self,screen):
        Sprite.__init__(self)
        self.screen = screen
        self.image = pygame.image.load('basketImg.png').convert_alpha()
        self.image_w, self.image_h = self.image.get_size()

        self.x_position = self.screen.get_width() / 2
        self.y_position = self.image_h / 2

    def blitme(self):
        draw_pos = self.image.get_rect().move(self.x_position - self.image_w / 2, self.y_position - self.image_h / 2)
        self.screen.blit(self.image, draw_pos)
