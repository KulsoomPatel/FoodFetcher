import pygame
from Basket import Basket
from DisplayScore import DisplayScore
from Scoreboard import Scoreboard
from Settings import Settings
from Button import Button
from Engine import Engine
from Instructions import Instructions
from Title import Title


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

    game_over_button = Button(screen, play_button.x_position, play_button.y_position + 1.5 * settings.button_height,
                              settings, "Game Over!")
    instructions = Instructions(screen, settings)
    draw_title = Title(screen)

    displayScore = DisplayScore(screen, settings, 5, 3)

    foods = []
    poisons = []
    basket = Basket(screen)
    engine = Engine(screen, settings, scoreboard, foods, poisons, basket)

    # main event loop
    # while True:
    while True:
        time_passed = clock.tick(50)
        mouse_x = pygame.mouse.get_pos()[0]
        mouse_y = pygame.mouse.get_pos()[1]
        engine.check_events(play_button, mouse_x, mouse_y)

        screen.fill(settings.bg_color)

        if settings.game_active:
            engine.update_basket(mouse_x)
            engine.check_foods(time_passed)
            engine.check_poisons(time_passed)

            if len(foods) == 0:
                if scoreboard.food_caught > 0:
                    #  Increase the balloon speed for each new batch of balloons.
                    settings.food_speed *= settings.speed_increase_factor
                    settings.poison_ratio *= settings.speed_increase_factor
                    scoreboard.batches_finished += 1
                    # If player has completed required batches, increase batch_size

                if scoreboard.batches_finished % settings.batches_needed == 0 and scoreboard.batches_finished > 0:
                    settings.batch_size += 1
                engine.release_batch()
        else:
            play_button.blitme()
            draw_title.blitme(settings.screen_width / 2 - settings.button_width / 2,
                              settings.screen_height / 2 - settings.button_height * 4)
            # If a game has just ended, show Game Over button
            if settings.games_played > 0:
                game_over_button.blitme()
                displayScore.blitme()

            if settings.games_played < 1:
                instructions.blitme()

        # Display scoreboard
        scoreboard.blitme()
        pygame.display.flip()


run_game()
