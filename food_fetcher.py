import pygame
import sys
from Food import Food
from Basket import Basket
from Scoreboard import Scoreboard
from Settings import Settings
from Button import Button


def run_game():
    settings = Settings()

    # initialise the game
    pygame.init()
    # returns a pyGame surface
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height), 0, 32)
    clock = pygame.time.Clock()
    scoreboard = Scoreboard(screen)
    play_button = Button(screen, settings.screen_width / 2 - settings.button_width / 2,
                         settings.screen_height / 2 - settings.button_height / 2, settings, "Play Food Fetcher")

    foods = []
    spawn_foods(screen, settings, foods)
    basket = Basket(screen)

    # main event loop
    # while True:
    while True:
        time_passed = clock.tick(50)
        mouse_x = pygame.mouse.get_pos()[0]
        mouse_y = pygame.mouse.get_pos()[1]
        check_events(settings, play_button, mouse_x, mouse_y)

        screen.fill(settings.bg_color)

        if settings.game_active:
            update_basket(basket, mouse_x)
            check_foods(foods, basket, scoreboard, screen, settings, time_passed)

            if len(foods) == 0:
                settings.food_speed *= settings.speed_increase_factor
                release_batch(screen, settings, foods)
        else:
            play_button.blitme()

            # Display scoreboard
        scoreboard.blitme()
        play_button.blitme()
        pygame.display.flip()


def spawn_foods(screen, settings, foods):
    foods.append(Food(screen, settings))


def miss_food(scoreboard, food, foods):
    scoreboard.food_missed += 1
    foods.remove(food)


def catch_food(scoreboard, settings, food, foods):
    scoreboard.food_caught += 1
    foods.remove(food)
    settings.food_speed *= settings.speed_increase_factor

    if scoreboard.food_caught % settings.catch_needed == 0:
        settings.batch_size += 1


def update_basket(basket, mouse_x):
    basket.x_position = mouse_x
    basket.update_rect()
    basket.blitme()


def release_batch(screen, settings, foods):
    for x in range(0, settings.batch_size):
        spawn_foods(screen, settings, foods)


def check_foods(foods, basket, scoreboard, screen, settings, time_passed):
    for food in foods:
        food.update(time_passed)
        food.blitme()

        if food.rect.colliderect(basket.rect):
            catch_food(scoreboard, settings, food, foods)
            continue

        if food.y_position > screen.get_height():
            miss_food(scoreboard, food, foods)
            spawn_foods(screen, settings, foods)
            continue


def check_events(settings, play_button, mouse_x, mouse_y):
    if play_button.rect.collidepoint(mouse_x, mouse_y):
        settings.game_active = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


run_game()
