"""
Kevin's Adventure Game - Main Entry Point
A text-based adventure game with improved architecture and maintainability.
"""
import logging
from game.engine import game_engine


def setup_logging():
    """Set up logging for the game."""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('game.log'),
            logging.StreamHandler()
        ]
    )


def main():
    """Main entry point for the game."""
    setup_logging()
    
    try:
        game_engine.start_game()
    except Exception as e:
        logging.error(f"Fatal error in main: {e}")
        print(f"A fatal error occurred: {e}")
        print("Please check the game.log file for more details.")


if __name__ == "__main__":
    main()
