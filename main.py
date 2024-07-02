import pygame
import sys
from game import Game


def main():
    pygame.init()
    config_options = {
        'title': 'Wizard Duel',
        'resolution': (800, 600),
        'full-screen': False
    }
    try:
        game = Game(config_options)  # Pass config options to the Game
        game.run()
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    main()
