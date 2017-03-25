from random import randint, uniform
import pygame
from pygame.sprite import Sprite


class Food(Sprite):
    def __init__(self, screen, settings):
        Sprite.__init__(self)
        self.screen = screen
        self.image = pygame.image.load('foodImg.png').convert_alpha()
        self.image_w, self.image_h = self.image.get_size()
        self.speed = uniform(0.75, 1.25) * settings.food_speed

        self.x_position = randint(self.image_w / 2, self.screen.get_width() - self.image_w / 2)
        max_offset = min(settings.batch_size * self.image_h, self.screen.get_height())

        # Begin image at the top of the screen
        self.y_position = self.screen.get_height() - self.screen.get_height() - self.image_h / 2 + randint(0,
                                                                                                           self.screen.get_height())
        self.update_rect()

        # redrawing an object to a screen

    def blitme(self):
        draw_pos = self.image.get_rect().move(self.x_position - self.image_w / 2, self.y_position - self.image_h / 2)
        self.screen.blit(self.image, draw_pos)

    def update(self, time_passed):
        self.y_position += self.speed * time_passed
        self.update_rect()

    def update_rect(self):
        self.rect = pygame.Rect(self.x_position - self.image_w / 2, self.y_position - self.image_h / 2,
                                self.image_w, self.image_h)
