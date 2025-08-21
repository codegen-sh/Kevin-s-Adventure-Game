"""
Save/load module for Kevin's Adventure Game.
Contains functions for saving and loading game state.
"""
import json
import os
from datetime import datetime

from game.exceptions import SaveLoadError

SAVE_DIRECTORY = "saves"


def ensure_save_directory():
    """
    Ensure that the save directory exists.
    
    Raises:
        SaveLoadError: If the directory could not be created
    """
    try:
        if not os.path.exists(SAVE_DIRECTORY):
            os.makedirs(SAVE_DIRECTORY)
    except OSError as e:
        raise SaveLoadError(f"Could not create save directory: {e}")


def generate_save_filename(player_name):
    """
    Generate a unique filename for the save file.
    
    Args:
        player_name (str): The player's name
        
    Returns:
        str: A unique filename
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"{player_name}_{timestamp}.json"


def save_game(player, world, filename=None):
    """
    Save the current game state to a file.
    
    Args:
        player (dict): The player's current state
        world (dict): The game world state
        filename (str, optional): The filename to save to. Defaults to None.
        
    Returns:
        str: The filename the game was saved to
        
    Raises:
        SaveLoadError: If the game could not be saved
    """
    ensure_save_directory()
    
    save_data = {
        "player": player,
        "world": world
    }
    
    if filename is None:
        player_name = player["name"] if isinstance(player, dict) else player.name
        filename = generate_save_filename(player_name)
    
    filepath = os.path.join(SAVE_DIRECTORY, filename)
    
    try:
        with open(filepath, 'w') as save_file:
            json.dump(save_data, save_file, indent=2)
        print(f"Game saved successfully as {filename}")
        return filename
    except IOError as e:
        raise SaveLoadError(f"Error saving game: {e}")


def load_game(filename):
    """
    Load a game state from a file.
    
    Args:
        filename (str): The filename to load from
        
    Returns:
        tuple: A tuple containing (player_dict, world_dict), or (None, None) if loading failed
        
    Raises:
        SaveLoadError: If the game could not be loaded
    """
    filepath = os.path.join(SAVE_DIRECTORY, filename)
    
    try:
        with open(filepath, 'r') as save_file:
            save_data = json.load(save_file)
        print(f"Game loaded successfully from {filename}")
        return save_data["player"], save_data["world"]
    except IOError as e:
        raise SaveLoadError(f"Error loading game: {e}")
    except json.JSONDecodeError:
        raise SaveLoadError(f"Error: The save file {filename} is corrupted.")


def list_save_files():
    """
    List all available save files.
    
    Returns:
        list: List of save filenames
    """
    ensure_save_directory()
    save_files = [f for f in os.listdir(SAVE_DIRECTORY) if f.endswith('.json')]
    return save_files


def delete_save_file(filename):
    """
    Delete a save file.
    
    Args:
        filename (str): The filename to delete
        
    Raises:
        SaveLoadError: If the file could not be deleted
    """
    filepath = os.path.join(SAVE_DIRECTORY, filename)
    try:
        os.remove(filepath)
        print(f"Save file {filename} deleted successfully.")
    except OSError as e:
        raise SaveLoadError(f"Error deleting save file: {e}")


def load_most_recent_save():
    """
    Load the most recent save file.
    
    Returns:
        tuple: A tuple containing (player_dict, world_dict), or (None, None) if loading failed
        
    Raises:
        SaveLoadError: If no save files were found or the game could not be loaded
    """
    save_files = list_save_files()
    if not save_files:
        raise SaveLoadError("No save files found.")
    
    try:
        most_recent = max(save_files, key=lambda f: os.path.getmtime(os.path.join(SAVE_DIRECTORY, f)))
        return load_game(most_recent)
    except Exception as e:
        raise SaveLoadError(f"Error loading most recent save: {e}")

