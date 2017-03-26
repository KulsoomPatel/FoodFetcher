import pygame
import sys

from Food import Food


class Engine:
    def __init__(self):
        pass

    def release_batch(self, screen, settings, foods):
        for x in range(0, settings.batch_size):
            self.spawn_foods(screen, settings, foods)

    def check_foods(self, foods, basket, scoreboard, screen, settings, time_passed):
        for food in foods:
            food.update(time_passed)
            food.blitme()

            if food.rect.colliderect(basket.rect):
                self.catch_food(scoreboard, settings, food, foods)
                continue

            if food.y_position > screen.get_height():
                self.miss_food(scoreboard, food, foods)
                self.spawn_foods(screen, settings, foods)
                continue

            if scoreboard.food_caught > 0:
                scoreboard.catch_ratio = float(scoreboard.food_caught) / (scoreboard.food_caught + scoreboard.food_missed)
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
        settings.food_speed *= settings.speed_increase_factor

        if scoreboard.food_caught % settings.catch_needed == 0:
            settings.batch_size += 1

    def spawn_foods(self, screen, settings, foods):
        foods.append(Food(screen, settings))

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
