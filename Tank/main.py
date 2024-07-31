import pygame
import sys
from settings import *
from game import Game
from menu import Menu


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Tank Game")

    game = Game()
    menu = Menu(screen, WORLD_MAPS, game)

    while True:
        selected_level = menu.run()
        if selected_level is not None:
            game.run_level(selected_level)
        else:
            pygame.quit()
            sys.exit()


if __name__ == '__main__':
    main()
