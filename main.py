"""
Kevin's Adventure Game - Main Entry Point

A text-based adventure game featuring Kevin the beet mascot.
Refactored with improved architecture, error handling, and extensibility.
"""
from game.game import create_game
from utils.input_handler import SafeInput


def main():
    """
    Main entry point for Kevin's Adventure Game.
    """
    try:
        # Create and start the game
        game = create_game()
        game.start()
        
    except KeyboardInterrupt:
        print("\n\nGame interrupted by user. Goodbye!")
    except Exception as e:
        print(f"\nUnexpected error occurred: {e}")
        print("The game will now exit. Sorry for the inconvenience!")
    finally:
        print("\nThanks for playing Kevin's Adventure Game!")


def legacy_main():
    """
    Legacy main function for backward compatibility.
    This maintains the old game loop structure for testing purposes.
    """
    from game.actions import perform_action
    from game.player import create_player, get_player_status
    from game.world import get_current_location, initialize_world
    from utils.save_load import list_save_files, load_game, save_game
    from utils.text_formatting import print_help, print_welcome_message

    print_welcome_message()

    # Add load game option with improved error handling
    try:
        load_option = SafeInput.safe_input("Do you want to load a saved game? (y/n): ", "n").lower()
        
        if load_option == 'y':
            save_files = list_save_files()
            if save_files:
                print("Available save files:")
                for i, file in enumerate(save_files, 1):
                    print(f"{i}. {file}")
                try:
                    choice = int(SafeInput.safe_input("Enter the number of the save file to load: ", "1"))
                    if 1 <= choice <= len(save_files):
                        player, world = load_game(save_files[choice - 1])
                        if player is None or world is None:
                            print("Failed to load game. Starting a new game.")
                            player = create_player("Kevin")
                            world = initialize_world()
                    else:
                        print("Invalid choice. Starting a new game.")
                        player = create_player("Kevin")
                        world = initialize_world()
                except (ValueError, IndexError):
                    print("Invalid input. Starting a new game.")
                    player = create_player("Kevin")
                    world = initialize_world()
            else:
                print("No save files found. Starting a new game.")
                player = create_player("Kevin")
                world = initialize_world()
        else:
            player = create_player("Kevin")
            world = initialize_world()

        # Main game loop with error handling
        while True:
            try:
                current_location = get_current_location(world)
                print(f"\nYou are in the {current_location}.")
                print(get_player_status(player))

                action = SafeInput.safe_input("What would you like to do? ", "help").lower()

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
                print("\n\nGame interrupted. Saving progress...")
                try:
                    save_game(player, world)
                    print("Progress saved. Goodbye!")
                except Exception as e:
                    print(f"Could not save progress: {e}")
                break
            except Exception as e:
                print(f"Error during game loop: {e}")
                print("Continuing game...")
                
    except Exception as e:
        print(f"Critical error: {e}")
        print("Game cannot continue.")


if __name__ == "__main__":
    # Use the new architecture by default
    # To use legacy mode, change this to: legacy_main()
    main()
