import pygame, pygame.font
from pygame.sprite import Sprite


class Scoreboard(Sprite):
    def __init__(self, screen):
        Sprite.__init__(self)
        self.screen = screen
        self.initialize_stats()

        # Set dimensions and properties of scoreboard
        self.sb_height, self.sb_width = 60, self.screen.get_width()
        self.rect = pygame.Rect(0, 0, self.sb_width, self.sb_height)
        self.bg_color = (255, 255, 153)
        self.text_color = (0, 0, 0)
        self.font = pygame.font.SysFont('Calibri', 20)

        # Set positions of individual scoring elements on the scoreboard
        self.x_caught_position, self.y_caught_position = 20.0, 10.0
        self.x_missed_position, self.y_missed_position = 150.0, 10.0
        self.x_ratio_position, self.y_ratio_position = 300, 10.0

    def prep_scores(self):
        self.missed_string = "Missed: " + str(self.food_missed)
        self.missed_image = self.font.render(self.missed_string, True, self.text_color)
        self.caught_string = "Caught: " + str(self.food_caught)
        self.caught_image = self.font.render(self.caught_string, True, self.text_color)
        self.set_ratio_string()
        self.caught_ratio_image = self.font.render(self.catch_ratio_string, True, self.ratio_text_color)

    def blitme(self):
        # Turn individual scoring elements into images that can be drawn
        self.prep_scores()
        # Draw blank scoreboard
        self.screen.fill(self.bg_color, self.rect)
        # Draw individual scoring elements
        self.screen.blit(self.caught_image, (self.x_caught_position, self.y_caught_position))
        self.screen.blit(self.missed_image, (self.x_missed_position, self.y_missed_position))
        self.screen.blit(self.caught_ratio_image, (self.x_ratio_position, self.y_ratio_position))

    def initialize_stats(self):
        # Game attributes to track for scoring
        self.food_caught = 0
        self.food_missed = 0
        self.catch_ratio = 1.0

    def set_ratio_string(self):
        if self.catch_ratio == 1.0:
            self.catch_ratio_string = "Pop Rate: 100%"
        else:
            self.catch_ratio_string = "Pop Rate: " + "{0:.3}%".format(self.catch_ratio * 100.0)
        if self.catch_ratio < 0.95:
            self.ratio_text_color = (255, 51, 51)
        else:
            self.ratio_text_color = self.text_color
