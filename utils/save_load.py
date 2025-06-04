"""
Save and load functionality for Kevin's Adventure Game.

This module provides utilities for saving and loading game state to/from JSON files.
It handles player data, world state, and save file management.
"""

import json
import os
from datetime import datetime


def save_game(player, world, filename=None):
    """
    Save the current game state to a JSON file.
    
    Args:
        player (dict): The player object containing stats and inventory
        world (dict): The world state object
        filename (str, optional): Custom filename for the save file.
                                 If None, generates a timestamp-based filename.
    
    Returns:
        bool: True if save was successful, False otherwise
        
    Side Effects:
        - Creates a save file in the 'saves' directory
        - Prints confirmation or error messages
        
    Example:
        >>> player = create_player("Kevin")
        >>> world = initialize_world()
        >>> success = save_game(player, world, "test_save.json")
        Game saved successfully as test_save.json
        >>> print(success)
        True
    """
    if not os.path.exists("saves"):
        os.makedirs("saves")
    
    if filename is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"save_{timestamp}.json"
    
    save_data = {
        "player": player,
        "world": world,
        "timestamp": datetime.now().isoformat(),
        "version": "1.0"
    }
    
    try:
        filepath = os.path.join("saves", filename)
        with open(filepath, 'w') as f:
            json.dump(save_data, f, indent=2)
        print(f"Game saved successfully as {filename}")
        return True
    except Exception as e:
        print(f"Error saving game: {e}")
        return False

def load_game(filename):
    """
    Load a game state from a JSON file.
    
    Args:
        filename (str): The name of the save file to load
        
    Returns:
        tuple: A tuple containing (player, world) if successful,
               or (None, None) if loading failed
               
    Side Effects:
        - Prints confirmation or error messages
        
    Example:
        >>> player, world = load_game("test_save.json")
        Game loaded successfully from test_save.json
        >>> print(player is not None)
        True
    """
    filepath = os.path.join("saves", filename)
    
    if not os.path.exists(filepath):
        print(f"Save file {filename} not found.")
        return None, None
    
    try:
        with open(filepath, 'r') as f:
            save_data = json.load(f)
        
        player = save_data.get("player")
        world = save_data.get("world")
        
        if player is None or world is None:
            print(f"Invalid save file format: {filename}")
            return None, None
            
        print(f"Game loaded successfully from {filename}")
        return player, world
        
    except json.JSONDecodeError:
        print(f"Error: Save file {filename} is corrupted.")
        return None, None
    except Exception as e:
        print(f"Error loading game: {e}")
        return None, None

def list_save_files():
    """
    Get a list of all available save files.
    
    Returns:
        list: List of save file names (without directory path)
        
    Example:
        >>> save_files = list_save_files()
        >>> print(type(save_files))
        <class 'list'>
    """
    if not os.path.exists("saves"):
        return []
    
    save_files = []
    for filename in os.listdir("saves"):
        if filename.endswith(".json"):
            save_files.append(filename)
    
    return sorted(save_files)

def delete_save_file(filename):
    """
    Delete a specific save file.
    
    Args:
        filename (str): The name of the save file to delete
        
    Returns:
        bool: True if deletion was successful, False otherwise
        
    Side Effects:
        - Removes the save file from disk
        - Prints confirmation or error messages
        
    Example:
        >>> success = delete_save_file("old_save.json")
        Save file old_save.json deleted successfully.
        >>> print(success)
        True
    """
    filepath = os.path.join("saves", filename)
    
    if not os.path.exists(filepath):
        print(f"Save file {filename} not found.")
        return False
    
    try:
        os.remove(filepath)
        print(f"Save file {filename} deleted successfully.")
        return True
    except Exception as e:
        print(f"Error deleting save file: {e}")
        return False

def get_save_file_info(filename):
    """
    Get information about a save file without fully loading it.
    
    Args:
        filename (str): The name of the save file
        
    Returns:
        dict: Dictionary containing save file metadata, or None if file not found
              Keys include: timestamp, version, player_name, player_location
              
    Example:
        >>> info = get_save_file_info("test_save.json")
        >>> print(info["player_name"])
        Kevin
    """
    filepath = os.path.join("saves", filename)
    
    if not os.path.exists(filepath):
        return None
    
    try:
        with open(filepath, 'r') as f:
            save_data = json.load(f)
        
        player = save_data.get("player", {})
        
        return {
            "timestamp": save_data.get("timestamp", "Unknown"),
            "version": save_data.get("version", "Unknown"),
            "player_name": player.get("name", "Unknown"),
            "player_location": player.get("location", "Unknown"),
            "player_health": player.get("health", 0),
            "player_gold": player.get("gold", 0)
        }
        
    except Exception as e:
        print(f"Error reading save file info: {e}")
        return None

def load_most_recent_save():
    """
    Load the most recent save file.
    
    Returns:
        tuple: A tuple containing (player, world) if successful,
               or (None, None) if no save files are found
               
    Side Effects:
        - Prints confirmation or error messages
        
    Example:
        >>> player, world = load_most_recent_save()
        Game loaded successfully from most_recent_save.json
        >>> print(player is not None)
        True
    """
    save_files = list_save_files()
    if not save_files:
        print("No save files found.")
        return None, None

    most_recent = max(save_files, key=lambda f: os.path.getmtime(os.path.join("saves", f)))
    return load_game(most_recent)
