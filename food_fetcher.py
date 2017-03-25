import pygame
import sys
from Food import Food
from Basket import Basket
from Scoreboard import Scoreboard
from Settings import Settings


def run_game():
    settings = Settings()

    # initialise the game
    pygame.init()
    # returns a pyGame surface
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height), 0, 32)

    clock = pygame.time.Clock()
    scoreboard = Scoreboard(screen)

    foods = []
    spawn_foods(screen, settings, foods)
    basket = Basket(screen)

    # main event loop
    # while True:
    while True:
        time_passed = clock.tick(50)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(settings.bg_color)
        basket.x_position = pygame.mouse.get_pos()[0]
        basket.update_rect()
        basket.blitme()

        for food in foods:
            food.update(time_passed)
            food.blitme()

            if food.rect.colliderect(basket.rect):
                catch_food(scoreboard, settings, food, foods)
                spawn_foods(screen, settings, foods)
                continue

            if food.y_position > screen.get_height():
                miss_food(scoreboard, food, foods)
                spawn_foods(screen, settings, foods)
                continue
        # Display scoreboard
        scoreboard.blitme()
        pygame.display.flip()


def spawn_foods(screen, settings, foods):
    foods.append(Food(screen, settings.food_speed))


def miss_food(scoreboard, food, foods):
    scoreboard.food_missed += 1
    foods.remove(food)


def catch_food(scoreboard, settings, food, foods):
    scoreboard.food_caught += 1
    foods.remove(food)
    settings.food_speed *= 1.05


run_game()
