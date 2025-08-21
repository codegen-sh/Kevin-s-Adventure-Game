"""
Main module for Kevin's Adventure Game.
Contains the main game loop and entry point.
"""
from game.commands import create_command_registry
from game.exceptions import GameError, SaveLoadError
from game.game_state import create_game_state, load_game_state
from game.player import Player
from game.world import World, get_current_location
from utils.save_load import list_save_files
from utils.text_formatting import print_help, print_welcome_message


def main():
    """Main function for the game."""
    print_welcome_message()
    
    # Create command registry
    command_registry = create_command_registry()
    
    # Add load game option
    load_option = input("Do you want to load a saved game? (y/n): ").lower()
    if load_option == 'y':
        try:
            save_files = list_save_files()
            if save_files:
                print("Available save files:")
                for i, file in enumerate(save_files, 1):
                    print(f"{i}. {file}")
                choice = int(input("Enter the number of the save file to load: "))
                game_state = load_game_state(save_files[choice - 1])
                if game_state is None:
                    print("Failed to load game. Starting a new game.")
                    game_state = create_game_state("Kevin")
            else:
                print("No save files found. Starting a new game.")
                game_state = create_game_state("Kevin")
        except (ValueError, IndexError, SaveLoadError) as e:
            print(f"Error loading game: {e}")
            print("Starting a new game.")
            game_state = create_game_state("Kevin")
    else:
        game_state = create_game_state("Kevin")
    
    # Main game loop
    while True:
        try:
            current_location = get_current_location(game_state.world)
            print(f"\nYou are in the {current_location}.")
            print(game_state.player.get_status())
            
            action = input("What would you like to do? ").lower()
            
            if action == "quit":
                from game.game_state import save_game_state
                save_game_state(game_state)
                print("Thanks for playing! Your progress has been saved.")
                break
            
            command_registry.execute_command(game_state, action)
        except GameError as e:
            print(f"Game error: {e}")
        except KeyboardInterrupt:
            print("\nGame interrupted. Saving and exiting...")
            from game.game_state import save_game_state
            save_game_state(game_state)
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            print("The game will continue, but some functionality may be affected.")


if __name__ == "__main__":
    main()

