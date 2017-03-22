import pygame
import sys
from Food import Food
from Basket import Basket
from Scoreboard import Scoreboard


def run_game():
    # screen height and width are variables to store details
    screen_width, screen_height = 800, 600
    # RGB color
    bg_color = 179, 204, 255
    # initialise the game
    pygame.init()
    # returns a pyGame surface
    screen = pygame.display.set_mode((screen_width, screen_height), 0, 32)

    clock = pygame.time.Clock()
    scoreboard = Scoreboard(screen)
    foods = [Food(screen)]
    basket = Basket(screen)

    # main event loop
    # while True:
    while True:
        time_passed = clock.tick(50)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(bg_color)
        basket.x_position = pygame.mouse.get_pos()[0]
        basket.update_rect()
        basket.blitme()

        for food in foods:
            food.update(time_passed)
            food.blitme()

            if food.rect.colliderect(basket.rect):
                scoreboard.food_caught += 1
                foods.remove(food)
                foods.append(Food(screen))
                continue

            if food.y_position > screen.get_height():
                scoreboard.food_missed += 1
                foods.remove(food)
                foods.append(Food(screen))
                continue

        # Display scoreboard
        scoreboard.blitme()
        pygame.display.flip()


run_game()
