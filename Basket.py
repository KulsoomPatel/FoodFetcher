import pygame
from pygame.sprite import Sprite


class Basket(Sprite):
    def __init__(self,screen):
        Sprite.__init__(self)
        self.screen = screen
        self.image = pygame.image.load('images\\basketImg.png').convert_alpha()
        self.image_w, self.image_h = self.image.get_size()

        self.x_position = self.screen.get_width() / 2
        self.y_position = self.screen.get_height() - self.image_h/2

        self.update_rect()

    def blitme(self):
        draw_pos = self.image.get_rect().move(self.x_position - self.image_w / 2, self.y_position - self.image_h / 2)
        self.screen.blit(self.image, draw_pos)

    def update_rect(self):
        self.rect = pygame.Rect(self.x_position - self.image_w / 2, self.y_position - self.image_h / 2,
                                self.image_w, self.image_h)

