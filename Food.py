from random import randint

import pygame
from pygame.sprite import Sprite


class Food(Sprite):
    def __init__(self, screen):
        Sprite.__init__(self)
        self.screen = screen
        self.image = pygame.image.load('foodImg.png').convert_alpha()
        self.image_w, self.image_h = self.image.get_size()
        self.speed = 0.1

        self.x_position = self.x_position = randint(self.image_w / 2, self.screen.get_width() - self.image_w / 2)

        # Begin image at the top of the screen
        self.y_position = self.screen.get_height() - self.screen.get_height() -  self.image_h/2

        # redrawing an object to a screen

    def blitme(self):
        draw_pos = self.image.get_rect().move(self.x_position - self.image_w / 2, self.y_position - self.image_h / 2)
        self.screen.blit(self.image, draw_pos)

    def update(self, time_passed):
        self.y_position += self.speed * time_passed
