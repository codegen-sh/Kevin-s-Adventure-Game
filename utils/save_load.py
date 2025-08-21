"""
Save/load module for Kevin's Adventure Game.
This module handles saving and loading game state.
"""

import json
import os
from datetime import datetime

from game.config import SAVE_CONFIG

# Get save directory from config
SAVE_DIRECTORY = SAVE_CONFIG["SAVE_DIRECTORY"]


class SaveError(Exception):
    """Exception raised for errors in the save/load process."""
    pass


def ensure_save_directory():
    """
    Ensure that the save directory exists.
    
    Raises:
        SaveError: If the directory cannot be created
    """
    try:
        if not os.path.exists(SAVE_DIRECTORY):
            os.makedirs(SAVE_DIRECTORY)
    except OSError as e:
        raise SaveError(f"Could not create save directory: {e}")


def generate_save_filename(player_name):
    """
    Generate a unique filename for the save file.
    
    Args:
        player_name (str): The name of the player
        
    Returns:
        str: A unique filename for the save file
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"{player_name}_{timestamp}.json"


def save_game(player, world):
    """
    Save the current game state to a file.
    
    Args:
        player: The player object or dictionary
        world: The world object or dictionary
        
    Raises:
        SaveError: If the game cannot be saved
    """
    try:
        ensure_save_directory()
        
        # Convert objects to dictionaries if necessary
        player_dict = player.to_dict() if hasattr(player, 'to_dict') else player
        world_dict = world.to_dict() if hasattr(world, 'to_dict') else world
        
        save_data = {
            "player": player_dict,
            "world": world_dict
        }
        
        player_name = player_dict["name"]
        filename = generate_save_filename(player_name)
        filepath = os.path.join(SAVE_DIRECTORY, filename)
        
        with open(filepath, 'w') as save_file:
            json.dump(save_data, save_file, indent=2)
        
        print(f"Game saved successfully as {filename}")
        return filename
    except (IOError, OSError) as e:
        error_msg = f"Error saving game: {e}"
        print(error_msg)
        raise SaveError(error_msg)
    except Exception as e:
        error_msg = f"Unexpected error saving game: {e}"
        print(error_msg)
        raise SaveError(error_msg)


def load_game(filename):
    """
    Load a game state from a file.
    
    Args:
        filename (str): The name of the save file
        
    Returns:
        tuple: A tuple containing (player, world) or (None, None) if loading fails
        
    Raises:
        SaveError: If the game cannot be loaded
    """
    try:
        filepath = os.path.join(SAVE_DIRECTORY, filename)
        
        if not os.path.exists(filepath):
            raise SaveError(f"Save file {filename} does not exist")
        
        with open(filepath, 'r') as save_file:
            save_data = json.load(save_file)
        
        print(f"Game loaded successfully from {filename}")
        return save_data["player"], save_data["world"]
    except IOError as e:
        error_msg = f"Error loading game: {e}"
        print(error_msg)
        return None, None
    except json.JSONDecodeError as e:
        error_msg = f"Error: The save file {filename} is corrupted: {e}"
        print(error_msg)
        return None, None
    except KeyError as e:
        error_msg = f"Error: The save file {filename} has an invalid format: {e}"
        print(error_msg)
        return None, None
    except Exception as e:
        error_msg = f"Unexpected error loading game: {e}"
        print(error_msg)
        return None, None


def list_save_files():
    """
    List all available save files.
    
    Returns:
        list: A list of save file names
        
    Raises:
        SaveError: If the save directory cannot be accessed
    """
    try:
        ensure_save_directory()
        save_files = [f for f in os.listdir(SAVE_DIRECTORY) if f.endswith('.json')]
        return sorted(save_files, key=lambda f: os.path.getmtime(os.path.join(SAVE_DIRECTORY, f)), reverse=True)
    except OSError as e:
        error_msg = f"Error listing save files: {e}"
        print(error_msg)
        raise SaveError(error_msg)


def delete_save_file(filename):
    """
    Delete a save file.
    
    Args:
        filename (str): The name of the save file to delete
        
    Raises:
        SaveError: If the file cannot be deleted
    """
    try:
        filepath = os.path.join(SAVE_DIRECTORY, filename)
        
        if not os.path.exists(filepath):
            raise SaveError(f"Save file {filename} does not exist")
        
        os.remove(filepath)
        print(f"Save file {filename} deleted successfully.")
    except OSError as e:
        error_msg = f"Error deleting save file: {e}"
        print(error_msg)
        raise SaveError(error_msg)


def load_most_recent_save():
    """
    Load the most recent save file.
    
    Returns:
        tuple: A tuple containing (player, world) or (None, None) if loading fails
        
    Raises:
        SaveError: If no save files are found or the file cannot be loaded
    """
    try:
        save_files = list_save_files()
        if not save_files:
            print("No save files found.")
            return None, None
        
        most_recent = save_files[0]  # Already sorted by modification time
        return load_game(most_recent)
    except SaveError as e:
        print(f"Error loading most recent save: {e}")
        return None, None


def get_save_info(filename):
    """
    Get information about a save file.
    
    Args:
        filename (str): The name of the save file
        
    Returns:
        dict: A dictionary containing information about the save file
        
    Raises:
        SaveError: If the file cannot be read
    """
    try:
        filepath = os.path.join(SAVE_DIRECTORY, filename)
        
        if not os.path.exists(filepath):
            raise SaveError(f"Save file {filename} does not exist")
        
        # Get file modification time
        mod_time = datetime.fromtimestamp(os.path.getmtime(filepath))
        
        # Get basic player info without loading the entire file
        with open(filepath, 'r') as save_file:
            save_data = json.load(save_file)
            player_data = save_data.get("player", {})
            world_data = save_data.get("world", {})
        
        return {
            "filename": filename,
            "player_name": player_data.get("name", "Unknown"),
            "player_health": player_data.get("health", 0),
            "player_location": player_data.get("location", "Unknown"),
            "save_date": mod_time.strftime("%Y-%m-%d %H:%M:%S"),
            "file_size": os.path.getsize(filepath)
        }
    except (IOError, json.JSONDecodeError, KeyError, OSError) as e:
        error_msg = f"Error reading save file {filename}: {e}"
        print(error_msg)
        raise SaveError(error_msg)

