"""
Save/load module for Kevin's Adventure Game.
This module handles saving and loading game state.
"""
import json
import os
from datetime import datetime
from typing import List, Optional, Tuple, Union

from game.exceptions import SaveLoadError
from game.models import Player, World
from game.state import GameState

SAVE_DIRECTORY = "saves"


def ensure_save_directory() -> None:
    """
    Ensure that the save directory exists.
    
    Raises:
        SaveLoadError: If the directory cannot be created
    """
    try:
        if not os.path.exists(SAVE_DIRECTORY):
            os.makedirs(SAVE_DIRECTORY)
    except OSError as e:
        raise SaveLoadError(f"Failed to create save directory: {e}")


def generate_save_filename(player_name: str) -> str:
    """
    Generate a unique filename for the save file.
    
    Args:
        player_name (str): The player's name
    
    Returns:
        str: A unique filename
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"{player_name}_{timestamp}.json"


def save_game(game_state: GameState) -> None:
    """
    Save the current game state to a file.
    
    Args:
        game_state (GameState): The current game state
    
    Raises:
        SaveLoadError: If the game cannot be saved
    """
    ensure_save_directory()
    
    save_data = game_state.to_dict()
    
    filename = generate_save_filename(game_state.player.name)
    filepath = os.path.join(SAVE_DIRECTORY, filename)
    
    try:
        with open(filepath, 'w') as save_file:
            json.dump(save_data, save_file, indent=2)
        print(f"Game saved successfully as {filename}")
    except IOError as e:
        raise SaveLoadError(f"Error saving game: {e}")


def load_game(filename: str) -> Optional[GameState]:
    """
    Load a game state from a file.
    
    Args:
        filename (str): The filename to load
    
    Returns:
        Optional[GameState]: The loaded game state, or None if loading failed
    
    Raises:
        SaveLoadError: If the game cannot be loaded
    """
    filepath = os.path.join(SAVE_DIRECTORY, filename)
    
    try:
        with open(filepath, 'r') as save_file:
            save_data = json.load(save_file)
        print(f"Game loaded successfully from {filename}")
        
        # Handle legacy save format (pre-refactoring)
        if "player" in save_data and "world" in save_data and "flags" not in save_data:
            # Convert legacy format to new format
            player = Player.from_dict(save_data["player"])
            world = World.from_dict(save_data["world"])
            game_state = GameState(player, world)
            return game_state
        
        # Handle new save format
        return GameState.from_dict(save_data)
    except IOError as e:
        raise SaveLoadError(f"Error loading game: {e}")
    except json.JSONDecodeError:
        raise SaveLoadError(f"Error: The save file {filename} is corrupted.")


def list_save_files() -> List[str]:
    """
    List all available save files.
    
    Returns:
        List[str]: A list of save filenames
    """
    ensure_save_directory()
    try:
        save_files = [f for f in os.listdir(SAVE_DIRECTORY) if f.endswith('.json')]
        return save_files
    except OSError as e:
        raise SaveLoadError(f"Error listing save files: {e}")


def delete_save_file(filename: str) -> None:
    """
    Delete a save file.
    
    Args:
        filename (str): The filename to delete
    
    Raises:
        SaveLoadError: If the file cannot be deleted
    """
    filepath = os.path.join(SAVE_DIRECTORY, filename)
    try:
        os.remove(filepath)
        print(f"Save file {filename} deleted successfully.")
    except OSError as e:
        raise SaveLoadError(f"Error deleting save file: {e}")


def load_most_recent_save() -> Optional[GameState]:
    """
    Load the most recent save file.
    
    Returns:
        Optional[GameState]: The loaded game state, or None if no save files exist
    
    Raises:
        SaveLoadError: If the game cannot be loaded
    """
    save_files = list_save_files()
    if not save_files:
        print("No save files found.")
        return None
    
    try:
        most_recent = max(save_files, key=lambda f: os.path.getmtime(os.path.join(SAVE_DIRECTORY, f)))
        return load_game(most_recent)
    except OSError as e:
        raise SaveLoadError(f"Error loading most recent save: {e}")


def save_game_legacy(player: dict, world: dict) -> None:
    """
    Save the current game state to a file using the legacy format.
    This function is provided for backward compatibility.
    
    Args:
        player (dict): The player's current state
        world (dict): The game world state
    """
    ensure_save_directory()
    
    save_data = {
        "player": player,
        "world": world
    }
    
    filename = generate_save_filename(player["name"])
    filepath = os.path.join(SAVE_DIRECTORY, filename)
    
    try:
        with open(filepath, 'w') as save_file:
            json.dump(save_data, save_file, indent=2)
        print(f"Game saved successfully as {filename}")
    except IOError as e:
        print(f"Error saving game: {e}")


def load_game_legacy(filename: str) -> Tuple[Optional[dict], Optional[dict]]:
    """
    Load a game state from a file using the legacy format.
    This function is provided for backward compatibility.
    
    Args:
        filename (str): The filename to load
    
    Returns:
        Tuple[Optional[dict], Optional[dict]]: The player and world dictionaries, or None if loading failed
    """
    filepath = os.path.join(SAVE_DIRECTORY, filename)
    
    try:
        with open(filepath, 'r') as save_file:
            save_data = json.load(save_file)
        print(f"Game loaded successfully from {filename}")
        return save_data["player"], save_data["world"]
    except IOError as e:
        print(f"Error loading game: {e}")
        return None, None
    except json.JSONDecodeError:
        print(f"Error: The save file {filename} is corrupted.")
        return None, None

