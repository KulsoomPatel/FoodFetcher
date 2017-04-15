import pygame
from pygame.sprite import Sprite


class DisplayScore(Sprite):
    def __init__(self, screen, settings, score, pizza, poison):
        Sprite.__init__(self)
        self.screen = screen
        self.settings = settings

        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont('Calibri', 24)
        self.score = str(score)
        self.pizza = str(pizza)
        self.poison = str(poison)
        self.instr_lines = [
            "Game Over!"]

        self.instr_lines.append(
            "You scored " + self.score + " as you caught " + self.pizza + " pizza's and " + self.poison + " poison")

        self.prep_msg()

    def prep_msg(self):
        y_position = self.settings.screen_height / 2 + 50
        self.msg_images, self.msg_x, self.msg_y = [], [], []
        for index, line in enumerate(self.instr_lines):
            self.msg_images.append(self.font.render(line, True, self.text_color))
            self.msg_x.append(self.settings.screen_width / 2 - self.font.size(line)[0] / 2)
            self.msg_y.append(y_position + index * self.font.size(line)[1])

    def blitme(self):
        for msg_x, msg_y, msg_image in zip(self.msg_x, self.msg_y, self.msg_images):
            self.screen.blit(msg_image, (msg_x, msg_y))
