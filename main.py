"""
Kevin's Adventure Game - Main Entry Point
A text-based adventure game with improved architecture and organization.
"""

from game.controller import create_game_controller


def main():
    """
    Main entry point for Kevin's Adventure Game.
    Uses the new GameController architecture for better organization.
    """
    # Create and initialize the game controller
    game_controller = create_game_controller()
    
    try:
        # Initialize the game (handles new/load game choice)
        game_controller.initialize_game()
        
        # Run the main game loop
        game_controller.run_game_loop()
        
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        print("Please report this issue if it persists.")
    
    finally:
        print("\nGoodbye! 👋")


if __name__ == "__main__":
    main()
