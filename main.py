"""
Main module for Kevin's Adventure Game.

This module contains the main game loop and entry point.
"""
import sys
from typing import Dict, Optional, Tuple, Union

from game.actions import perform_action
from game.player import Player, create_player, get_player_status
from game.weather import apply_weather_effects, describe_weather, get_current_weather
from game.world import World, get_current_location, initialize_world
from utils.save_load import (
    list_save_files,
    load_game,
    load_most_recent_save,
    save_game,
)
from utils.text_formatting import print_help, print_separator, print_welcome_message


def handle_load_game() -> Tuple[Optional[Dict], Optional[Dict]]:
    """
    Handle loading a game from a save file.
    
    Returns:
        Tuple[Optional[Dict], Optional[Dict]]: The player and world state, or None if loading failed
    """
    save_files = list_save_files()
    if not save_files:
        print("No save files found. Starting a new game.")
        return None, None
    
    print("Available save files:")
    for i, file in enumerate(save_files, 1):
        print(f"{i}. {file}")
    
    while True:
        try:
            choice_input = input("Enter the number of the save file to load (or 'c' to cancel): ")
            if choice_input.lower() == 'c':
                print("Starting a new game.")
                return None, None
            
            choice = int(choice_input)
            if 1 <= choice <= len(save_files):
                return load_game(save_files[choice - 1])
            else:
                print(f"Please enter a number between 1 and {len(save_files)}.")
        except ValueError:
            print("Please enter a valid number.")
        except KeyboardInterrupt:
            print("\nStarting a new game.")
            return None, None


def main() -> None:
    """
    Main function for the game.
    
    This function contains the main game loop.
    """
    print_welcome_message()
    
    # Add load game option
    load_option = input("Do you want to load a saved game? (y/n): ").lower()
    
    player = None
    world = None
    
    if load_option == 'y':
        player, world = handle_load_game()
    
    # If loading failed or user chose not to load, create a new game
    if player is None or world is None:
        try:
            # Use the new class-based approach
            player = Player("Kevin")
            world = World()
            print("New game started successfully.")
        except Exception as e:
            # Fallback to the old dictionary-based approach if something goes wrong
            print(f"Error creating new game with classes: {e}")
            print("Falling back to dictionary-based game.")
            player = create_player("Kevin")
            world = initialize_world()
    
    # Main game loop
    try:
        while True:
            # Get current location and display info
            if isinstance(world, World):
                current_location = world.get_current_location()
                print(f"\nYou are in the {current_location}.")
                
                # Display weather
                weather = get_current_weather(world.to_dict())
                print(describe_weather(world.to_dict()))
                
                # Apply weather effects
                apply_weather_effects(player, world.to_dict())
            else:
                current_location = get_current_location(world)
                print(f"\nYou are in the {current_location}.")
                
                # Display weather if available
                if "weather" in world:
                    weather = get_current_weather(world)
                    print(describe_weather(world))
                    
                    # Apply weather effects
                    apply_weather_effects(player, world)
            
            # Display player status
            if isinstance(player, Player):
                print(player.get_status())
            else:
                print(get_player_status(player))
            
            # Get player action
            print_separator("-", 40)
            action = input("What would you like to do? ").lower()
            print_separator("-", 40)
            
            # Process action
            if action == "quit":
                save_game(player, world)
                print("Thanks for playing! Your progress has been saved.")
                break
            elif action == "help":
                print_help()
            else:
                try:
                    perform_action(player, world, action)
                except Exception as e:
                    print(f"Error performing action: {e}")
                    print("Please try a different action.")
    
    except KeyboardInterrupt:
        print("\nGame interrupted. Saving progress...")
        save_game(player, world)
        print("Thanks for playing! Your progress has been saved.")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
        print("Attempting to save your progress...")
        try:
            save_game(player, world)
            print("Game saved. Please restart the game.")
        except Exception as save_error:
            print(f"Error saving game: {save_error}")
            print("Unable to save game. Progress may be lost.")
    
    # Exit the game
    sys.exit(0)


if __name__ == "__main__":
    main()

