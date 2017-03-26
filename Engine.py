import pygame
import sys
from Food import Food
from Poison import Poison
from random import random


class Engine:
    def __init__(self):
        pass

    def release_batch(self, screen, settings, foods, poisons):
        for x in range(0, settings.batch_size):
            self.spawn_foods(screen, settings, foods, poisons)

    def check_foods(self, foods, poisons, basket, scoreboard, screen, settings, time_passed):
        for food in foods:
            food.update(time_passed)
            food.blitme()

            if food.rect.colliderect(basket.rect):
                self.catch_food(scoreboard, settings, food, foods)
                continue

            if food.y_position > screen.get_height():
                self.miss_food(scoreboard, food, foods)
                self.spawn_foods(screen, settings, foods, poisons)
                continue

            if scoreboard.food_caught > 0:
                scoreboard.catch_ratio = float(scoreboard.food_caught) / (
                    scoreboard.food_caught + scoreboard.food_missed)
                if scoreboard.catch_ratio < settings.min_catch_ratio:
                    # Set game_active to false, empty the list of balloons, and increment games_played
                    settings.game_active = False
                    settings.games_played += 1

    def update_basket(self, basket, mouse_x):
        basket.x_position = mouse_x
        basket.update_rect()
        basket.blitme()

    def miss_food(self, scoreboard, food, foods):
        scoreboard.food_missed += 1
        foods.remove(food)

    def catch_food(self, scoreboard, settings, food, foods):
        scoreboard.food_caught += 1
        foods.remove(food)

    def spawn_foods(self, screen, settings, foods, poisons):
        foods.append(Food(screen, settings))
        if random() < settings.poison_ratio:
            self.spawn_poison(screen, settings, poisons)

    def check_events(self, settings, scoreboard, play_button, mouse_x, mouse_y, foods):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.rect.collidepoint(mouse_x, mouse_y):
                    # Play button has been pressed.  Empty list of balloons,
                    #  initialize scoreboard and game parameters, and make game active.
                    del foods[:]
                    scoreboard.initialize_stats()
                    settings.initialize_game_parameters()
                    settings.game_active = True

    def check_poisons(self, poisons, basket, scoreboard, screen, settings, time_passed):
        for poison in poisons:
            poison.update(time_passed)
            poison.blitme()

            if poison.rect.colliderect(basket.rect):
                self.hit_poison(scoreboard, settings, poison, poisons)
                continue

    def spawn_poison(self, screen, settings, poisons):
        poisons.append(Poison(screen, settings))

    def hit_poison(self, scoreboard, settings, poison, poisons):
        scoreboard.poison_hit += 1
        poisons.remove(poison)
