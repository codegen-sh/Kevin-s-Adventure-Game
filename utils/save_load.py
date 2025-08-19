"""
Save/load module for Kevin's Adventure Game.
This module handles saving and loading game state.
"""
import json
import os
from datetime import datetime


SAVE_DIRECTORY = "saves"


def ensure_save_directory():
    """
    Ensure that the save directory exists.
    """
    if not os.path.exists(SAVE_DIRECTORY):
        os.makedirs(SAVE_DIRECTORY)


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


def save_game(player, world):
    """
    Save the current game state to a file.
    
    Args:
        player: The player object
        world: The world object
    
    Returns:
        bool: True if the game was saved successfully, False otherwise
    """
    ensure_save_directory()
    
    # Convert objects to dictionaries if needed
    if hasattr(player, '__dict__'):
        player_data = {
            "name": player.name,
            "health": player.health,
            "inventory": player.inventory,
            "location": player.location,
            "gold": player.gold
        }
    else:
        player_data = player
    
    if hasattr(world, 'to_dict'):
        world_data = world.to_dict()
    else:
        world_data = world
    
    save_data = {
        "player": player_data,
        "world": world_data
    }
    
    player_name = player_data.get("name", "Player")
    filename = generate_save_filename(player_name)
    filepath = os.path.join(SAVE_DIRECTORY, filename)
    
    try:
        with open(filepath, 'w') as save_file:
            json.dump(save_data, save_file, indent=2)
        print(f"Game saved successfully as {filename}")
        return True
    except IOError as e:
        print(f"Error saving game: {e}")
        return False


def load_game(filename):
    """
    Load a game state from a file.
    
    Args:
        filename (str): The name of the save file
    
    Returns:
        tuple: A tuple containing (player, world), or (None, None) if loading failed
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
    except KeyError:
        print(f"Error: The save file {filename} has an invalid format.")
        return None, None


def list_save_files():
    """
    List all available save files.
    
    Returns:
        list: A list of save file names
    """
    ensure_save_directory()
    save_files = [f for f in os.listdir(SAVE_DIRECTORY) if f.endswith('.json')]
    return save_files


def delete_save_file(filename):
    """
    Delete a save file.
    
    Args:
        filename (str): The name of the save file
    
    Returns:
        bool: True if the file was deleted successfully, False otherwise
    """
    filepath = os.path.join(SAVE_DIRECTORY, filename)
    try:
        os.remove(filepath)
        print(f"Save file {filename} deleted successfully.")
        return True
    except OSError as e:
        print(f"Error deleting save file: {e}")
        return False


def load_most_recent_save():
    """
    Load the most recent save file.
    
    Returns:
        tuple: A tuple containing (player, world), or (None, None) if loading failed
    """
    save_files = list_save_files()
    if not save_files:
        print("No save files found.")
        return None, None
    
    most_recent = max(save_files, key=lambda f: os.path.getmtime(os.path.join(SAVE_DIRECTORY, f)))
    return load_game(most_recent)

