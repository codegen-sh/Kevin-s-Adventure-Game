"""
Module for saving and loading game state.
"""
import json
import os
from datetime import datetime


def save_game(player, world, filename=None):
    """
    Save the current game state to a file.
    
    Args:
        player (dict): The player's state
        world (dict): The world state
        filename (str, optional): Custom filename for the save. If None, a timestamp is used.
    
    Returns:
        str: The filename of the saved game
    """
    # Create saves directory if it doesn't exist
    if not os.path.exists("saves"):
        os.makedirs("saves")
    
    # Generate filename with timestamp if not provided
    if filename is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        player_name = player.get("name", "player")
        filename = f"{player_name}_{timestamp}.json"
    
    # Ensure filename has .json extension
    if not filename.endswith(".json"):
        filename += ".json"
    
    # Create full path
    filepath = os.path.join("saves", filename)
    
    # Create save data
    save_data = {
        "player": player,
        "world": world,
        "timestamp": datetime.now().isoformat(),
        "version": "1.0.0"  # Game version
    }
    
    # Write to file
    try:
        with open(filepath, "w") as f:
            json.dump(save_data, f, indent=2)
        print(f"Game saved successfully as '{filename}'.")
        return filename
    except Exception as e:
        print(f"Error saving game: {e}")
        return None


def load_game(filename):
    """
    Load a game from a save file.
    
    Args:
        filename (str): The filename of the save to load
    
    Returns:
        tuple: (player, world) if successful, (None, None) if failed
    """
    # Ensure filename has .json extension
    if not filename.endswith(".json"):
        filename += ".json"
    
    # Create full path
    filepath = os.path.join("saves", filename)
    
    # Read from file
    try:
        with open(filepath, "r") as f:
            save_data = json.load(f)
        
        print(f"Game loaded successfully from '{filename}'.")
        return save_data["player"], save_data["world"]
    except FileNotFoundError:
        print(f"Save file '{filename}' not found.")
        return None, None
    except json.JSONDecodeError:
        print(f"Save file '{filename}' is corrupted.")
        return None, None
    except Exception as e:
        print(f"Error loading game: {e}")
        return None, None


def list_save_files():
    """
    List all available save files.
    
    Returns:
        list: List of save filenames
    """
    # Create saves directory if it doesn't exist
    if not os.path.exists("saves"):
        os.makedirs("saves")
        return []
    
    # Get all .json files in the saves directory
    save_files = [f for f in os.listdir("saves") if f.endswith(".json")]
    
    # Sort by modification time (newest first)
    save_files.sort(key=lambda x: os.path.getmtime(os.path.join("saves", x)), reverse=True)
    
    return save_files


def delete_save_file(filename):
    """
    Delete a save file.
    
    Args:
        filename (str): The filename of the save to delete
    
    Returns:
        bool: True if successful, False if failed
    """
    # Ensure filename has .json extension
    if not filename.endswith(".json"):
        filename += ".json"
    
    # Create full path
    filepath = os.path.join("saves", filename)
    
    # Delete file
    try:
        os.remove(filepath)
        print(f"Save file '{filename}' deleted successfully.")
        return True
    except FileNotFoundError:
        print(f"Save file '{filename}' not found.")
        return False
    except Exception as e:
        print(f"Error deleting save file: {e}")
        return False

