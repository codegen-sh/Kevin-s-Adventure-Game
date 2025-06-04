from game.actions import perform_action
from game.player import create_player, get_player_status
from game.world import get_current_location, initialize_world
from utils.save_load import list_save_files, load_game, save_game
from utils.text_formatting import print_help, print_welcome_message
from utils.validation import safe_input, validate_numeric_input, ValidationError


def main():
    print_welcome_message()

    # Add load game option with error handling
    try:
        load_option = safe_input("Do you want to load a saved game? (y/n): ")
        if load_option and load_option.lower() == 'y':
            player, world = handle_load_game()
            if player is None or world is None:
                print("Starting a new game.")
                player = create_player("Kevin")
                world = initialize_world()
        else:
            player = create_player("Kevin")
            world = initialize_world()
    except Exception as e:
        print(f"Error during game initialization: {e}")
        print("Starting a new game.")
        player = create_player("Kevin")
        world = initialize_world()

    # Main game loop with error handling
    while True:
        try:
            current_location = get_current_location(world)
            print(f"\nYou are in the {current_location}.")
            print(get_player_status(player))

            action = safe_input("What would you like to do? ")
            if action is None:
                print("Exiting game...")
                break

            action = action.lower()

            if action == "quit":
                try:
                    save_game(player, world)
                    print("Thanks for playing! Your progress has been saved.")
                except Exception as e:
                    print(f"Error saving game: {e}")
                    print("Thanks for playing!")
                break
            elif action == "help":
                print_help()
            else:
                perform_action(player, world, action)
                
        except KeyboardInterrupt:
            print("\nGame interrupted. Saving progress...")
            try:
                save_game(player, world)
                print("Progress saved. Thanks for playing!")
            except Exception as e:
                print(f"Error saving game: {e}")
                print("Thanks for playing!")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            print("The game will continue, but you may want to save and restart.")


def handle_load_game():
    """Handle the load game process with proper error handling."""
    try:
        save_files = list_save_files()
        if not save_files:
            print("No save files found.")
            return None, None
            
        print("Available save files:")
        for i, file in enumerate(save_files, 1):
            print(f"{i}. {file}")
        
        choice_input = safe_input("Enter the number of the save file to load: ")
        if choice_input is None:
            return None, None
            
        choice = validate_numeric_input(choice_input, 1, len(save_files))
        player, world = load_game(save_files[choice - 1])
        
        if player is None or world is None:
            print("Failed to load game.")
            return None, None
            
        return player, world
        
    except ValidationError as e:
        print(f"Invalid input: {e}")
        return None, None
    except Exception as e:
        print(f"Error loading game: {e}")
        return None, None


if __name__ == "__main__":
    main()
