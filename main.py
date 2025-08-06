"""
Kevin's Adventure Game - Main Entry Point

A text-based adventure game featuring Kevin, our adorable pink and green beet mascot!
This refactored version uses modern object-oriented design with proper separation of concerns.
"""

from game.engine import run_interactive_game


def main():
    """
    Main entry point for Kevin's Adventure Game.
    
    This function starts the interactive game session using the new GameEngine.
    The GameEngine handles all game state management, player interactions,
    and coordination between different game systems.
    """
    try:
        run_interactive_game()
    except KeyboardInterrupt:
        print("\n\nThanks for playing Kevin's Adventure Game!")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
        print("Please report this issue if it persists.")


if __name__ == "__main__":
    main()
