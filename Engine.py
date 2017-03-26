import pygame
import sys
from Food import Food
from Poison import Poison
from random import random


class Engine:
    def __init__(self, screen, settings, scoreboard, foods, poisons, basket):
        self.screen = screen
        self.settings = settings
        self.scoreboard = scoreboard
        self.foods = foods
        self.poisons = poisons
        self.basket = basket

    def release_batch(self):
        for x in range(0, self.settings.batch_size):
            self.spawn_foods()

    def check_foods(self, time_passed):
        for food in self.foods:
            food.update(time_passed)
            food.blitme()

            if food.rect.colliderect(self.basket.rect):
                self.catch_food(food)
                continue

            if food.y_position > self.screen.get_height():
                self.miss_food(food)
                self.spawn_foods()
                continue

            if self.scoreboard.food_caught > 0:
                self.scoreboard.catch_ratio = float(self.scoreboard.food_caught) / (
                    self.scoreboard.food_caught + self.scoreboard.food_missed)
                if self.scoreboard.catch_ratio < self.settings.min_catch_ratio:
                    # Set game_active to false, empty the list of balloons, and increment games_played
                    self.settings.game_active = False
                    self.settings.games_played += 1

    def update_basket(self, mouse_x):
        self.basket.x_position = mouse_x
        self.basket.update_rect()
        self.basket.blitme()

    def miss_food(self, food):
        self.scoreboard.food_missed += 1
        self.foods.remove(food)

    def catch_food(self, food):
        self.scoreboard.food_caught += 1
        self.foods.remove(food)

    def spawn_foods(self):
        self.foods.append(Food(self.screen, self.settings))
        if random() < self.settings.poison_ratio:
            self.spawn_poison()

    def check_events(self, play_button, mouse_x, mouse_y):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.rect.collidepoint(mouse_x, mouse_y):
                    # Play button has been pressed.  Empty list of balloons,
                    #  initialize scoreboard and game parameters, and make game active.
                    del self.foods[:]
                    self.scoreboard.initialize_stats()
                    self.settings.initialize_game_parameters()
                    self.settings.game_active = True

    def check_poisons(self, time_passed):
        for poison in self.poisons:
            poison.update(time_passed)
            poison.blitme()

            if poison.rect.colliderect(self.basket.rect):
                self.hit_poison(poison)
                continue

    def spawn_poison(self):
        self.poisons.append(Poison(self.screen, self.settings))

    def hit_poison(self, poison):
        self.scoreboard.poison_hit += 1
        self.poisons.remove(poison)
