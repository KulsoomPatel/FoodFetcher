import pygame
from Basket import Basket
from Scoreboard import Scoreboard
from Settings import Settings
from Button import Button
from Engine import Engine


def run_game():
    settings = Settings()
    engine = Engine()

    # initialise the game
    pygame.init()
    # returns a pyGame surface
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height), 0, 32)
    clock = pygame.time.Clock()
    scoreboard = Scoreboard(screen)
    play_button = Button(screen, settings.screen_width / 2 - settings.button_width / 2,
                         settings.screen_height / 2 - settings.button_height / 2, settings, "Play Food Fetcher")

    game_over_button = Button(screen, play_button.x_position, play_button.y_position - 2 * settings.button_height,
                              settings, "Game Over")

    foods = []
    basket = Basket(screen)

    # main event loop
    # while True:
    while True:
        time_passed = clock.tick(50)
        mouse_x = pygame.mouse.get_pos()[0]
        mouse_y = pygame.mouse.get_pos()[1]
        engine.check_events(settings, scoreboard, play_button, mouse_x, mouse_y, foods)

        screen.fill(settings.bg_color)

        if settings.game_active:
            engine.update_basket(basket, mouse_x)
            engine.check_foods(foods, basket, scoreboard, screen, settings, time_passed)

            if len(foods) == 0:
                settings.food_speed *= settings.speed_increase_factor
                engine.release_batch(screen, settings, foods)
        else:
            play_button.blitme()
            # If a game has just ended, show Game Over button
            if settings.games_played > 0:
                game_over_button.blitme()

        # Display scoreboard
        scoreboard.blitme()
        pygame.display.flip()


run_game()
