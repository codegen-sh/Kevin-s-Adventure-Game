"""
Save and load functionality for Kevin's Adventure Game.
Handles game state persistence with support for both old dictionary format and new class-based format.
"""

import json
import os
from datetime import datetime
from typing import Tuple, Optional, Union, Any

SAVE_DIRECTORY = "saves"


def ensure_save_directory() -> None:
    """Ensure that the save directory exists."""
    if not os.path.exists(SAVE_DIRECTORY):
        os.makedirs(SAVE_DIRECTORY)


def generate_save_filename(player_name: str, custom_name: str = None) -> str:
    """
    Generate a unique filename for the save file.
    
    Args:
        player_name: Name of the player
        custom_name: Optional custom save name
        
    Returns:
        Generated filename
    """
    if custom_name:
        # Sanitize custom name
        safe_name = "".join(c for c in custom_name if c.isalnum() or c in (' ', '-', '_')).rstrip()
        safe_name = safe_name.replace(' ', '_')
        return f"{safe_name}.json"
    else:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        return f"{player_name}_{timestamp}.json"


def save_game(player, world, custom_filename: str = None) -> bool:
    """
    Save the current game state to a file.
    
    Args:
        player: Player instance or dictionary
        world: World instance or dictionary
        custom_filename: Optional custom filename
        
    Returns:
        True if save was successful, False otherwise
    """
    ensure_save_directory()

    try:
        # Convert objects to dictionaries for JSON serialization
        from game.player import Player
        from game.world import World
        
        if isinstance(player, Player):
            player_data = player.to_dict()
            player_name = player.name
        else:
            player_data = player
            player_name = player.get("name", "Unknown")
        
        if isinstance(world, World):
            world_data = world.to_dict()
        else:
            world_data = world

        save_data = {
            "version": "2.0",  # Version for backward compatibility
            "player": player_data,
            "world": world_data,
            "save_timestamp": datetime.now().isoformat()
        }

        filename = custom_filename or generate_save_filename(player_name)
        filepath = os.path.join(SAVE_DIRECTORY, filename)

        with open(filepath, 'w') as save_file:
            json.dump(save_data, save_file, indent=2)
        
        print(f"Game saved successfully as {filename}")
        return True
        
    except Exception as e:
        print(f"Error saving game: {e}")
        return False


def load_game(filename: str) -> Tuple[Optional[Any], Optional[Any]]:
    """
    Load a game state from a file.
    
    Args:
        filename: Name of the save file to load
        
    Returns:
        Tuple of (player_data, world_data) or (None, None) if failed
    """
    filepath = os.path.join(SAVE_DIRECTORY, filename)

    try:
        with open(filepath, 'r') as save_file:
            save_data = json.load(save_file)
        
        print(f"Game loaded successfully from {filename}")
        
        # Handle different save file versions
        version = save_data.get("version", "1.0")
        
        if version == "2.0":
            # New format with class support
            return save_data["player"], save_data["world"]
        else:
            # Legacy format
            return save_data["player"], save_data["world"]
            
    except FileNotFoundError:
        print(f"Error: Save file {filename} not found.")
        return None, None
    except json.JSONDecodeError:
        print(f"Error: The save file {filename} is corrupted.")
        return None, None
    except KeyError as e:
        print(f"Error: Save file {filename} is missing required data: {e}")
        return None, None
    except Exception as e:
        print(f"Error loading game: {e}")
        return None, None

def list_save_files():
    """List all available save files. Use load_most_recent_save() to load the most recent save."""
    ensure_save_directory()
    save_files = [f for f in os.listdir(SAVE_DIRECTORY) if f.endswith('.json')]
    return save_files

def delete_save_file(filename):
    """Delete a save file. Use list_save_files() to list all available save files."""
    filepath = os.path.join(SAVE_DIRECTORY, filename)
    try:
        os.remove(filepath)
        print(f"Save file {filename} deleted successfully.")
    except OSError as e:
        print(f"Error deleting save file: {e}")

def load_most_recent_save():
    """Load the most recent save file. Use list_save_files() to list all available save files."""
    save_files = list_save_files()
    if not save_files:
        print("No save files found.")
        return None, None

    most_recent = max(save_files, key=lambda f: os.path.getmtime(os.path.join(SAVE_DIRECTORY, f)))
    return load_game(most_recent)
