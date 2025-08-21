"""
Save/load module for Kevin's Adventure Game.

This module contains functions for saving and loading game state.
"""
import json
import os
import shutil
import tempfile
from datetime import datetime
from typing import Dict, List, Optional, Tuple, Union

# Constants
SAVE_DIRECTORY = "saves"
CURRENT_SAVE_VERSION = 2  # Increment this when save format changes


def ensure_save_directory() -> None:
    """
    Ensure that the save directory exists.
    
    Creates the save directory if it doesn't exist.
    """
    if not os.path.exists(SAVE_DIRECTORY):
        os.makedirs(SAVE_DIRECTORY)


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


def save_game(player, world) -> bool:
    """
    Save the current game state to a file.
    
    Args:
        player: The player's current state
        world: The game world state
        
    Returns:
        bool: True if the save was successful, False otherwise
    """
    ensure_save_directory()
    
    # Convert player and world to dictionaries if they're objects
    if hasattr(player, 'to_dict'):
        player_dict = player.to_dict()
    else:
        player_dict = player
    
    if hasattr(world, 'to_dict'):
        world_dict = world.to_dict()
    else:
        world_dict = world
    
    save_data = {
        "version": CURRENT_SAVE_VERSION,
        "timestamp": datetime.now().isoformat(),
        "player": player_dict,
        "world": world_dict
    }
    
    player_name = player_dict["name"]
    filename = generate_save_filename(player_name)
    filepath = os.path.join(SAVE_DIRECTORY, filename)
    
    # Use atomic write to prevent corruption if the game crashes during save
    try:
        # Write to a temporary file first
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            json.dump(save_data, temp_file, indent=2)
        
        # Replace the original file with the temporary file
        shutil.move(temp_file.name, filepath)
        print(f"Game saved successfully as {filename}")
        return True
    except Exception as e:
        print(f"Error saving game: {e}")
        # Clean up the temporary file if it exists
        if 'temp_file' in locals() and os.path.exists(temp_file.name):
            os.remove(temp_file.name)
        return False


def load_game(filename: str) -> Tuple[Optional[Dict], Optional[Dict]]:
    """
    Load a game state from a file.
    
    Args:
        filename (str): The filename to load
        
    Returns:
        Tuple[Optional[Dict], Optional[Dict]]: The player and world state, or None if loading failed
    """
    filepath = os.path.join(SAVE_DIRECTORY, filename)
    
    try:
        with open(filepath, 'r') as save_file:
            save_data = json.load(save_file)
        
        # Check save version and migrate if necessary
        save_version = save_data.get("version", 1)  # Default to version 1 for old saves
        if save_version < CURRENT_SAVE_VERSION:
            save_data = migrate_save_data(save_data, save_version)
        
        print(f"Game loaded successfully from {filename}")
        return save_data["player"], save_data["world"]
    except FileNotFoundError:
        print(f"Error: Save file {filename} not found.")
        return None, None
    except json.JSONDecodeError:
        print(f"Error: The save file {filename} is corrupted.")
        return None, None
    except KeyError as e:
        print(f"Error: The save file {filename} is missing required data: {e}")
        return None, None
    except Exception as e:
        print(f"Error loading game: {e}")
        return None, None


def migrate_save_data(save_data: Dict, from_version: int) -> Dict:
    """
    Migrate save data from an older version to the current version.
    
    Args:
        save_data (Dict): The save data to migrate
        from_version (int): The version of the save data
        
    Returns:
        Dict: The migrated save data
    """
    # Version 1 to 2 migration
    if from_version == 1 and CURRENT_SAVE_VERSION >= 2:
        # Add missing fields
        if "world" in save_data:
            if "weather" not in save_data["world"]:
                save_data["world"]["weather"] = "clear"
            
            if "state" not in save_data["world"]:
                save_data["world"]["state"] = {
                    "discovered_locations": [],
                    "active_quests": [],
                    "completed_quests": [],
                    "time_of_day": "day",
                    "days_passed": 0,
                    "special_discoveries": []
                }
        
        if "player" in save_data:
            if "stats" not in save_data["player"]:
                save_data["player"]["stats"] = {
                    "strength": 10,
                    "agility": 10,
                    "perception": 10
                }
        
        # Update version
        save_data["version"] = 2
    
    # Add more migrations here as needed for future versions
    
    return save_data


def list_save_files() -> List[str]:
    """
    List all available save files.
    
    Returns:
        List[str]: A list of save filenames
    """
    ensure_save_directory()
    save_files = [f for f in os.listdir(SAVE_DIRECTORY) if f.endswith('.json')]
    return sorted(save_files, key=lambda f: os.path.getmtime(os.path.join(SAVE_DIRECTORY, f)), reverse=True)


def delete_save_file(filename: str) -> bool:
    """
    Delete a save file.
    
    Args:
        filename (str): The filename to delete
        
    Returns:
        bool: True if the file was deleted, False otherwise
    """
    filepath = os.path.join(SAVE_DIRECTORY, filename)
    try:
        os.remove(filepath)
        print(f"Save file {filename} deleted successfully.")
        return True
    except OSError as e:
        print(f"Error deleting save file: {e}")
        return False


def load_most_recent_save() -> Tuple[Optional[Dict], Optional[Dict]]:
    """
    Load the most recent save file.
    
    Returns:
        Tuple[Optional[Dict], Optional[Dict]]: The player and world state, or None if loading failed
    """
    save_files = list_save_files()
    if not save_files:
        print("No save files found.")
        return None, None
    
    most_recent = save_files[0]  # Already sorted by modification time
    return load_game(most_recent)


def get_save_info(filename: str) -> Dict:
    """
    Get information about a save file.
    
    Args:
        filename (str): The filename to get information about
        
    Returns:
        Dict: Information about the save file
    """
    filepath = os.path.join(SAVE_DIRECTORY, filename)
    
    try:
        with open(filepath, 'r') as save_file:
            save_data = json.load(save_file)
        
        # Extract basic info
        player_name = save_data.get("player", {}).get("name", "Unknown")
        player_health = save_data.get("player", {}).get("health", 0)
        player_location = save_data.get("player", {}).get("location", "Unknown")
        timestamp = save_data.get("timestamp", "Unknown")
        version = save_data.get("version", 1)
        
        # Format timestamp if it's a valid ISO format
        try:
            dt = datetime.fromisoformat(timestamp)
            formatted_time = dt.strftime("%Y-%m-%d %H:%M:%S")
        except (ValueError, TypeError):
            formatted_time = timestamp
        
        return {
            "filename": filename,
            "player_name": player_name,
            "player_health": player_health,
            "player_location": player_location,
            "timestamp": formatted_time,
            "version": version
        }
    except Exception as e:
        return {
            "filename": filename,
            "error": str(e)
        }

