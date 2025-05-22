"""
Main module for Kevin's Adventure Game.
This is the entry point for the game.
"""
import argparse
import logging
import sys
from pathlib import Path

from kevin_adventure_game.game.actions import perform_action
from kevin_adventure_game.game.player import create_player, get_player_status
from kevin_adventure_game.game.world import get_current_location, initialize_world
from kevin_adventure_game.utils.save_load import (
    list_save_files,
    load_game,
    load_most_recent_save,
    save_game,
)
from kevin_adventure_game.utils.text_formatting import print_help, print_welcome_message

# Set up logging
def setup_logging(debug=False):
    """Set up logging configuration."""
    log_level = logging.DEBUG if debug else logging.INFO
    log_dir = Path.home() / ".kevin_adventure_game" / "logs"
    log_dir.mkdir(parents=True, exist_ok=True)
    log_file = log_dir / "game.log"
    
    logging.basicConfig(
        level=log_level,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler() if debug else logging.NullHandler(),
        ],
    )
    
    # Create a logger for this module
    logger = logging.getLogger(__name__)
    logger.info("Logging initialized")
    return logger


def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description="Kevin's Adventure Game")
    parser.add_argument(
        "--debug", action="store_true", help="Enable debug mode"
    )
    parser.add_argument(
        "--load", action="store_true", help="Load the most recent save game"
    )
    parser.add_argument(
        "--new", action="store_true", help="Start a new game, ignoring any saves"
    )
    parser.add_argument(
        "--player-name", type=str, default="Kevin", help="Set the player name"
    )
    return parser.parse_args()


def main():
    """Main entry point for the game."""
    # Parse command line arguments
    args = parse_args()
    
    # Set up logging
    logger = setup_logging(args.debug)
    logger.info("Starting game")
    
    try:
        # Display welcome message
        print_welcome_message()
        
        # Handle game loading or creation
        if args.new:
            logger.info("Starting new game")
            player = create_player(args.player_name)
            world = initialize_world()
        elif args.load:
            logger.info("Loading most recent save")
            player, world = load_most_recent_save()
            if player is None or world is None:
                logger.warning("Failed to load save, starting new game")
                print("Failed to load game. Starting a new game.")
                player = create_player(args.player_name)
                world = initialize_world()
        else:
            # Ask if the player wants to load a saved game
            load_option = input("Do you want to load a saved game? (y/n): ").lower()
            if load_option == 'y':
                save_files = list_save_files()
                if save_files:
                    print("Available save files:")
                    for i, file in enumerate(save_files, 1):
                        print(f"{i}. {file}")
                    try:
                        choice = int(input("Enter the number of the save file to load (or 0 to start new): "))
                        if choice == 0:
                            logger.info("User chose to start new game")
                            player = create_player(args.player_name)
                            world = initialize_world()
                        else:
                            logger.info(f"Loading save file: {save_files[choice - 1]}")
                            player, world = load_game(save_files[choice - 1])
                            if player is None or world is None:
                                logger.warning("Failed to load save, starting new game")
                                print("Failed to load game. Starting a new game.")
                                player = create_player(args.player_name)
                                world = initialize_world()
                    except (ValueError, IndexError) as e:
                        logger.error(f"Error loading save: {e}")
                        print("Invalid choice. Starting a new game.")
                        player = create_player(args.player_name)
                        world = initialize_world()
                else:
                    logger.info("No save files found, starting new game")
                    print("No save files found. Starting a new game.")
                    player = create_player(args.player_name)
                    world = initialize_world()
            else:
                logger.info("Starting new game")
                player = create_player(args.player_name)
                world = initialize_world()
        
        # Main game loop
        logger.info("Entering main game loop")
        while True:
            try:
                current_location = get_current_location(world)
                print(f"\nYou are in the {current_location}.")
                print(get_player_status(player))
                
                action = input("What would you like to do? ").lower()
                
                if action == "quit":
                    logger.info("Player quit the game")
                    save_game(player, world)
                    print("Thanks for playing! Your progress has been saved.")
                    break
                elif action == "help":
                    print_help()
                else:
                    perform_action(player, world, action)
                
                # Check if player is defeated
                if player["health"] <= 0:
                    logger.info("Player was defeated")
                    print("Game over! You have been defeated.")
                    restart = input("Would you like to restart? (y/n): ").lower()
                    if restart == 'y':
                        logger.info("Player chose to restart")
                        player = create_player(args.player_name)
                        world = initialize_world()
                    else:
                        logger.info("Player chose not to restart")
                        print("Thanks for playing!")
                        break
            
            except KeyboardInterrupt:
                logger.info("Game interrupted by user")
                print("\nGame interrupted. Saving progress...")
                save_game(player, world)
                print("Progress saved. Thanks for playing!")
                break
            
            except Exception as e:
                logger.error(f"Unexpected error: {e}", exc_info=True)
                print(f"An error occurred: {e}")
                print("The game will try to continue.")
    
    except Exception as e:
        logger.critical(f"Fatal error: {e}", exc_info=True)
        print(f"A fatal error occurred: {e}")
        print("The game cannot continue. Please check the logs for details.")
        return 1
    
    logger.info("Game ended normally")
    return 0


if __name__ == "__main__":
    sys.exit(main())

