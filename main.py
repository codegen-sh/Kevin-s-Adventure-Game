import sys
import argparse
from game.actions import perform_action
from game.player import create_player, get_player_status
from game.world import get_current_location, initialize_world
from utils.save_load import list_save_files, load_game, save_game
from utils.text_formatting import print_help, print_welcome_message
from utils.logging_config import initialize_logging, get_logger, log_player_action, log_game_event
from utils.debug import (
    setup_debug_from_args, debug_command_handler, is_debug_mode, 
    print_debug_status, enable_debug_mode
)
from utils.error_recovery import handle_error_with_recovery, create_checkpoint
from utils.validation import validate_choice_input, validate_numeric_input
from exceptions import GameError, SaveError, LoadError, PlayerError, ValidationError

# Initialize logging and get logger
loggers = initialize_logging()
logger = loggers['main']

def parse_arguments():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description="Kevin's Adventure Game")
    parser.add_argument('--debug', action='store_true', help='Enable debug mode')
    parser.add_argument('--verbose', '-v', action='store_true', help='Enable verbose logging')
    parser.add_argument('--performance', '-p', action='store_true', help='Enable performance monitoring')
    parser.add_argument('--debug-commands', '-c', action='store_true', help='Enable debug commands')
    parser.add_argument('--log-level', choices=['DEBUG', 'INFO', 'WARNING', 'ERROR'], 
                       default='INFO', help='Set logging level')
    
    return parser.parse_args()

def safe_input(prompt: str, default: str = "") -> str:
    """
    Safe input function with error handling.
    
    Args:
        prompt (str): Input prompt
        default (str): Default value if input fails
    
    Returns:
        str: User input or default value
    """
    try:
        return input(prompt).strip()
    except (KeyboardInterrupt, EOFError):
        logger.info("User interrupted input")
        return default
    except Exception as e:
        logger.error(f"Input error: {e}")
        return default

def handle_load_game_choice():
    """
    Handle the load game choice with comprehensive error handling.
    
    Returns:
        tuple: (player, world) or (None, None) if load failed
    """
    try:
        load_option = safe_input("Do you want to load a saved game? (y/n): ").lower()
        
        if load_option not in ['y', 'yes']:
            return None, None
        
        save_files = list_save_files()
        if not save_files:
            print("No save files found. Starting a new game.")
            logger.info("No save files available")
            return None, None
        
        print("Available save files:")
        for i, file in enumerate(save_files, 1):
            print(f"{i}. {file}")
        
        # Get user choice with validation
        while True:
            try:
                choice_input = safe_input("Enter the number of the save file to load: ")
                if not choice_input:
                    print("No selection made. Starting a new game.")
                    return None, None
                
                choice = validate_numeric_input(choice_input, min_value=1, max_value=len(save_files), integer_only=True)
                selected_file = save_files[choice - 1]
                break
                
            except ValidationError as e:
                print(f"Invalid choice: {e.message}")
                print(f"Please enter a number between 1 and {len(save_files)}")
                continue
            except Exception as e:
                logger.error(f"Error processing save file choice: {e}")
                print("Error processing choice. Starting a new game.")
                return None, None
        
        # Attempt to load the selected file
        try:
            player, world = load_game(selected_file)
            if player is None or world is None:
                raise LoadError(f"Failed to load game data from {selected_file}")
            
            logger.info(f"Successfully loaded game: {selected_file}")
            log_game_event("game_loaded", f"Loaded save file: {selected_file}")
            return player, world
            
        except (LoadError, GameError) as e:
            logger.error(f"Load error: {e}")
            print(f"Failed to load game: {e}")
            
            # Attempt recovery
            success, recovered_data = handle_error_with_recovery(e, action="load_game")
            if success and recovered_data:
                player, world = recovered_data
                print("✅ Game loaded from recovery backup.")
                return player, world
            else:
                print("❌ Could not recover save file. Starting a new game.")
                return None, None
                
    except Exception as e:
        logger.error(f"Unexpected error in load game choice: {e}")
        print("An error occurred while loading. Starting a new game.")
        return None, None

def main():
    """Main game loop with comprehensive error handling."""
    try:
        # Parse command line arguments
        args = parse_arguments()
        
        # Setup debug mode from arguments
        if args.debug:
            enable_debug_mode(
                verbose=args.verbose,
                performance=args.performance,
                commands=args.debug_commands
            )
        
        # Initialize logging with appropriate level
        log_level = getattr(__import__('logging'), args.log_level)
        initialize_logging(debug_mode=args.debug, verbose=args.verbose, log_level=log_level)
        
        logger.info("Starting Kevin's Adventure Game")
        log_game_event("game_started", "Game application started")
        
        # Print welcome message
        print_welcome_message()

        # Add load game option
        player, world = handle_load_game_choice()

        if player is None or world is None:
            player = create_player("Kevin")
            world = initialize_world()

        while True:
            try:
                current_location = get_current_location(world)
                print(f"\nYou are in the {current_location}.")
                print(get_player_status(player))

                action = safe_input("What would you like to do? ")
                
                if not action:
                    continue  # Skip empty input

                # Check for debug commands first
                if is_debug_mode() and debug_command_handler(action, player, world):
                    continue

                if action.lower() == "quit":
                    try:
                        save_game(player, world)
                        logger.info("Game saved successfully on quit")
                        log_game_event("game_quit", "Player quit game", player=player)
                        print("Thanks for playing! Your progress has been saved.")
                        break
                    except SaveError as e:
                        logger.error(f"Save error on quit: {e}")
                        print(f"Warning: Could not save game: {e}")
                        
                        # Attempt emergency save
                        success, emergency_file = handle_error_with_recovery(e, player, world, "quit_save")
                        if success and emergency_file:
                            print(f"✅ Emergency save created: {emergency_file}")
                        else:
                            print("❌ Could not create emergency save.")
                            
                        quit_anyway = safe_input("Quit without saving? (y/n): ").lower()
                        if quit_anyway in ['y', 'yes']:
                            break
                        else:
                            continue
                            
                elif action.lower() == "help":
                    print_help()
                elif action.lower() == "debug" and is_debug_mode():
                    print_debug_status()
                else:
                    try:
                        perform_action(player, world, action.lower())
                        
                        # Log the action
                        log_player_action(player, action, result="completed")
                        
                        # Create periodic checkpoints
                        if hash(action) % 10 == 0:  # Every ~10th action
                            create_checkpoint(player, world)
                            
                    except GameError as e:
                        logger.error(f"Game error during action '{action}': {e}")
                        print(f"Game error: {e}")
                        
                        # Attempt recovery
                        success, recovered_data = handle_error_with_recovery(e, player, world, action)
                        if success:
                            if recovered_data and isinstance(recovered_data, tuple) and len(recovered_data) == 2:
                                player.update(recovered_data[0])
                                world.update(recovered_data[1])
                            print("✅ Recovered from error. Continuing game.")
                        else:
                            print("❌ Could not recover from error.")
                            
                    except Exception as e:
                        logger.error(f"Unexpected error during action '{action}': {e}")
                        print(f"An unexpected error occurred: {e}")
                        
                        # Attempt recovery
                        success, _ = handle_error_with_recovery(e, player, world, action)
                        if success:
                            print("✅ Recovered from unexpected error. Continuing game.")
                        else:
                            print("❌ Could not recover from error.")
                            
            except KeyboardInterrupt:
                logger.info("Game interrupted by user")
                print("\n\nGame interrupted. Saving...")
                
                try:
                    save_game(player, world)
                    print("Game saved. Goodbye!")
                except Exception as save_error:
                    logger.error(f"Error saving on interrupt: {save_error}")
                    print("Could not save game. Exiting anyway.")
                
                break
                
            except Exception as e:
                logger.error(f"Unexpected error in main game loop: {e}")
                print(f"An unexpected error occurred: {e}")
                
                # Attempt to continue
                continue_anyway = safe_input("Try to continue? (y/n): ").lower()
                if continue_anyway not in ['y', 'yes']:
                    print("Exiting game...")
                    break
        
        logger.info("Game ended")
        log_game_event("game_ended", "Game application ended")
        
    except Exception as fatal_error:
        logger.critical(f"Fatal error in main: {fatal_error}")
        print(f"Fatal error: {fatal_error}")
        print("The game encountered a critical error and must exit.")
        sys.exit(1)

if __name__ == "__main__":
    main()
