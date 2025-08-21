"""
Main module for Kevin's Adventure Game.
"""

from game.engine import GameEngine


def main():
    """
    Main function to start the game.
    """
    engine = GameEngine()
    try:
        engine.start()
    except KeyboardInterrupt:
        print("\nGame interrupted. Saving and exiting...")
        engine.save_game()
    except Exception as e:
        print(f"\nAn error occurred: {e}")
        print("Attempting to save the game...")
        engine.save_game()
        raise


if __name__ == "__main__":
    main()

