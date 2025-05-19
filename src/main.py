"""
Main entry point for Kevin's Adventure Game.
"""
from kevin_adventure.core.game import Game


def main():
    """
    Main entry point for the game.
    """
    game = Game()
    game.start()


if __name__ == "__main__":
    main()

