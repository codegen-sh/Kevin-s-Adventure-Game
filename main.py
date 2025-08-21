"""
Main module for Kevin's Adventure Game.
This module contains the main game loop.
"""
import sys
from typing import Optional

from game.actions import perform_action
from game.exceptions import GameError, SaveLoadError
from game.models import Player, World
from game.state import GameState
from utils.save_load import (
    list_save_files,
    load_game,
    load_game_legacy,
    save_game,
    save_game_legacy,
)
from utils.text_formatting import print_help, print_welcome_message


def initialize_world() -> World:
    """
    Initialize the game world.
    
    Returns:
        World: The initialized game world
    """
    world = World(current_location="Village")
    world.locations = {
        "Village": {
            "description": "A small, peaceful village with thatched-roof houses and friendly inhabitants.",
            "connections": ["Forest", "Mountain"],
            "items": ["map", "bread"]
        },
        "Forest": {
            "description": "A dense, mysterious forest with towering trees and the sound of rustling leaves.",
            "connections": ["Village", "Cave"],
            "items": ["stick", "berries"]
        },
        "Cave": {
            "description": "A dark, damp cave with echoing sounds and glittering minerals on the walls.",
            "connections": ["Forest"],
            "items": ["torch", "gemstone"]
        },
        "Mountain": {
            "description": "A tall, snow-capped mountain with treacherous paths and breathtaking views.",
            "connections": ["Village"],
            "items": ["rope", "pickaxe"]
        }
    }
    return world


def create_player(name: str) -> Player:
    """
    Create a new player.
    
    Args:
        name (str): The player's name
    
    Returns:
        Player: The created player
    """
    return Player(name=name)


def main() -> None:
    """
    Main game loop.
    """
    print_welcome_message()
    
    try:
        # Add load game option
        load_option = input("Do you want to load a saved game? (y/n): ").lower()
        game_state = None
        
        if load_option == 'y':
            save_files = list_save_files()
            if save_files:
                print("Available save files:")
                for i, file in enumerate(save_files, 1):
                    print(f"{i}. {file}")
                choice = int(input("Enter the number of the save file to load: "))
                
                try:
                    # Try to load with new format first
                    game_state = load_game(save_files[choice - 1])
                except SaveLoadError:
                    # If that fails, try legacy format
                    player_dict, world_dict = load_game_legacy(save_files[choice - 1])
                    if player_dict is not None and world_dict is not None:
                        player = Player.from_dict(player_dict)
                        world = World.from_dict(world_dict)
                        game_state = GameState(player, world)
                    else:
                        print("Failed to load game. Starting a new game.")
                        player = create_player("Kevin")
                        world = initialize_world()
                        game_state = GameState(player, world)
            else:
                print("No save files found. Starting a new game.")
                player = create_player("Kevin")
                world = initialize_world()
                game_state = GameState(player, world)
        else:
            player = create_player("Kevin")
            world = initialize_world()
            game_state = GameState(player, world)
        
        # Main game loop
        while True:
            current_location = game_state.world.get_current_location()
            print(f"\nYou are in the {current_location}.")
            print(game_state.player.get_status())
            
            action = input("What would you like to do? ").lower()
            
            if action == "quit":
                save_game(game_state)
                print("Thanks for playing! Your progress has been saved.")
                break
            elif action == "help":
                print_help()
            else:
                try:
                    # For backward compatibility, we still use the old perform_action function
                    # In a future update, this should be replaced with a new implementation
                    # that uses the GameState class
                    perform_action(game_state.player.to_dict(), game_state.world.to_dict(), action)
                    
                    # Update the player and world in the game state
                    # This is a temporary solution until perform_action is updated
                    # to work with the GameState class
                    game_state.player = Player.from_dict(game_state.player.to_dict())
                    game_state.world = World.from_dict(game_state.world.to_dict())
                except GameError as e:
                    print(f"Error: {e}")
    except KeyboardInterrupt:
        print("\nGame interrupted. Exiting without saving.")
        sys.exit(0)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        print("The game will now exit.")
        sys.exit(1)


if __name__ == "__main__":
    main()

