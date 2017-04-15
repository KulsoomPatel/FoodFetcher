import pygame.font
from pygame.sprite import Sprite


class Instructions(Sprite):
    def __init__(self, screen, settings):

        Sprite.__init__(self)
        self.screen = screen
        self.settings = settings

        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont('Calibri', 24)

        # Store the set of instructions
        self.instr_lines = ["Catch the pizza's in the basket by moving the mouse from right to left"]
        self.instr_lines.append("Ensure your catch rate is at 90% or you're out!")
        self.instr_lines.append("Avoid the poison as 3 catches and you're out!")

        # The instruction message only needs to be prepped once, not on every blit
        self.prep_msg()

    def prep_msg(self):
        y_position = self.settings.screen_height / 2 + self.settings.button_height
        self.msg_images, self.msg_x, self.msg_y = [], [], []
        for index, line in enumerate(self.instr_lines):
            self.msg_images.append(self.font.render(line, True, self.text_color))
            self.msg_x.append(self.settings.screen_width / 2 - self.font.size(line)[0] / 2)
            self.msg_y.append(y_position + index * self.font.size(line)[1])

    def blitme(self):
        for msg_x, msg_y, msg_image in zip(self.msg_x, self.msg_y, self.msg_images):
            self.screen.blit(msg_image, (msg_x, msg_y))