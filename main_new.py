"""
Main entry point for Kevin's Adventure Game.
Updated to use the new class-based architecture while maintaining backward compatibility.
"""
import sys
from typing import Optional
from game.game_engine import GameEngine, run_game
from game.player_class import Player
from game.world_class import World


def main_class_based() -> None:
    """
    Main function using the new class-based architecture.
    This is the recommended way to run the game.
    """
    try:
        # Create and run the game using the new GameEngine
        engine = GameEngine()
        engine.start_game()
    except KeyboardInterrupt:
        print("\n\nGame interrupted. Goodbye!")
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Please report this issue if it persists.")


def main_legacy() -> None:
    """
    Main function using the legacy function-based approach.
    This maintains backward compatibility with the original code.
    """
    from game.actions import perform_action
    from game.player import create_player, get_player_status
    from game.world import get_current_location, initialize_world
    from utils.save_load import list_save_files, load_game, save_game
    from utils.text_formatting import print_help, print_welcome_message
    
    print_welcome_message()
    
    # Add load game option
    load_option = input("Do you want to load a saved game? (y/n): ").lower()
    if load_option == 'y':
        save_files = list_save_files()
        if save_files:
            print("Available save files:")
            for i, file in enumerate(save_files, 1):
                print(f"{i}. {file}")
            try:
                choice = int(input("Enter the number of the save file to load: "))
                player, world = load_game(save_files[choice - 1])
                if player is None or world is None:
                    print("Failed to load game. Starting a new game.")
                    player = create_player("Kevin")
                    world = initialize_world()
            except (ValueError, IndexError):
                print("Invalid choice. Starting a new game.")
                player = create_player("Kevin")
                world = initialize_world()
        else:
            print("No save files found. Starting a new game.")
            player = create_player("Kevin")
            world = initialize_world()
    else:
        player = create_player("Kevin")
        world = initialize_world()
    
    while True:
        current_location = get_current_location(world)
        print(f"\nYou are in the {current_location}.")
        print(get_player_status(player))
        
        action = input("What would you like to do? ").lower()
        
        if action == "quit":
            save_game(player, world)
            print("Thanks for playing! Your progress has been saved.")
            break
        elif action == "help":
            print_help()
        else:
            perform_action(player, world, action)


def main() -> None:
    """
    Main entry point that allows choosing between architectures.
    """
    print("Kevin's Adventure Game")
    print("=" * 50)
    print("Choose your preferred game mode:")
    print("1. New Class-Based Architecture (Recommended)")
    print("2. Legacy Function-Based Architecture")
    print("3. Auto-detect (tries new, falls back to legacy)")
    
    try:
        choice = input("Enter your choice (1-3, default: 1): ").strip()
        
        if choice == "2":
            print("\nStarting game with legacy architecture...")
            main_legacy()
        elif choice == "3":
            print("\nAuto-detecting best architecture...")
            try:
                main_class_based()
            except ImportError as e:
                print(f"New architecture unavailable ({e}), falling back to legacy...")
                main_legacy()
        else:  # Default to new architecture
            print("\nStarting game with new class-based architecture...")
            main_class_based()
    
    except KeyboardInterrupt:
        print("\n\nGoodbye!")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        print("Please try the legacy mode if problems persist.")


if __name__ == "__main__":
    # Check for command line arguments
    if len(sys.argv) > 1:
        arg = sys.argv[1].lower()
        if arg in ["--legacy", "-l"]:
            print("Starting in legacy mode...")
            main_legacy()
        elif arg in ["--new", "-n"]:
            print("Starting with new architecture...")
            main_class_based()
        elif arg in ["--help", "-h"]:
            print("Kevin's Adventure Game")
            print("Usage: python main_new.py [options]")
            print("Options:")
            print("  --new, -n      Use new class-based architecture")
            print("  --legacy, -l   Use legacy function-based architecture")
            print("  --help, -h     Show this help message")
        else:
            print(f"Unknown argument: {arg}")
            print("Use --help for available options.")
    else:
        main()

