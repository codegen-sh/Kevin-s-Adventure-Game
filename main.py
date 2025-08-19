"""
Main module for Kevin's Adventure Game.
This is the entry point for the game.
"""
from game.engine import GameEngine


def main():
    """
    Main function to start the game.
    """
    engine = GameEngine()
    engine.run()


if __name__ == "__main__":
    main()

