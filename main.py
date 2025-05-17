from game.actions import perform_action
from game.player import create_player, get_player_status
from game.world import get_current_location, initialize_world
from utils.save_load import list_save_files, load_game, save_game
from utils.text_formatting import print_help, print_welcome_message


def main():
    """
    Main game loop and entry point for Kevin's Adventure Game.
    """
    print_welcome_message()
    
    # Initialize game state (player and world)
    player, world = initialize_game()
    
    # Main game loop
    game_loop(player, world)


def initialize_game():
    """
    Initialize the game by either loading a saved game or creating a new one.
    
    Returns:
        tuple: (player, world) - The player and world state dictionaries
    """
    # Add load game option
    load_option = input("Do you want to load a saved game? (y/n): ").lower()
    
    if load_option == 'y':
        try:
            player, world = load_saved_game()
            if player is None or world is None:
                print("Failed to load game. Starting a new game.")
                player = create_player(input("Enter your character name: ") or "Kevin")
                world = initialize_world()
        except Exception as e:
            print(f"Error loading game: {e}")
            print("Starting a new game.")
            player = create_player(input("Enter your character name: ") or "Kevin")
            world = initialize_world()
    else:
        player = create_player(input("Enter your character name: ") or "Kevin")
        world = initialize_world()
    
    return player, world


def load_saved_game():
    """
    Load a saved game file selected by the user.
    
    Returns:
        tuple: (player, world) - The loaded player and world state, or (None, None) if loading fails
    """
    save_files = list_save_files()
    
    if not save_files:
        print("No save files found.")
        return None, None
    
    print("Available save files:")
    for i, file in enumerate(save_files, 1):
        print(f"{i}. {file}")
    
    try:
        choice = int(input("Enter the number of the save file to load (0 to cancel): "))
        if choice == 0:
            return None, None
        if 1 <= choice <= len(save_files):
            return load_game(save_files[choice - 1])
        else:
            print("Invalid choice.")
            return None, None
    except ValueError:
        print("Please enter a valid number.")
        return None, None


def game_loop(player, world):
    """
    Main game loop that handles player input and game state updates.
    
    Args:
        player (dict): The player's state
        world (dict): The game world state
    """
    while True:
        try:
            # Display current game state
            current_location = get_current_location(world)
            print(f"\nYou are in the {current_location}.")
            print(get_player_status(player))
            
            # Get and process player action
            action = input("What would you like to do? ").lower()
            
            if action == "quit":
                handle_quit(player, world)
                break
            elif action == "help":
                print_help()
            else:
                perform_action(player, world, action)
                
            # Check if player is defeated
            if player["health"] <= 0:
                print("Game over! Your health reached zero.")
                if input("Would you like to start a new game? (y/n): ").lower() == 'y':
                    player = create_player(input("Enter your character name: ") or "Kevin")
                    world = initialize_world()
                else:
                    break
        
        except KeyboardInterrupt:
            print("\nGame interrupted. Saving progress...")
            save_game(player, world)
            print("Progress saved. Goodbye!")
            break
        except Exception as e:
            print(f"An error occurred: {e}")
            print("The game will continue, but some data may have been lost.")


def handle_quit(player, world):
    """
    Handle the quit command, saving the game before exiting.
    
    Args:
        player (dict): The player's state
        world (dict): The game world state
    """
    save_option = input("Would you like to save your progress? (y/n): ").lower()
    
    if save_option == 'y':
        save_name = input("Enter a name for your save file (or press Enter for default): ")
        if save_name:
            save_game(player, world, save_name)
        else:
            save_game(player, world)
        print("Your progress has been saved.")
    
    print("Thanks for playing!")


if __name__ == "__main__":
    main()
