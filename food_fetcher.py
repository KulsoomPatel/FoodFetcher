import pygame
import sys
from Food import Food
from Basket import Basket


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

        for food in foods:
            food.update(time_passed)
            food.blitme()
            if food.y_position > screen.get_height():
                foods.remove(food)
                foods.append(Food(screen))
        pygame.display.flip()


run_game()
