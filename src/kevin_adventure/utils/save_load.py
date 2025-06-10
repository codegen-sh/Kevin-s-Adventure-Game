"""
Save and load utilities for Kevin's Adventure Game.
"""
import json
import os
from datetime import datetime
from typing import Dict, List, Optional, Tuple

from kevin_adventure.core.player import Player
from kevin_adventure.core.world import World

SAVE_DIRECTORY = "saves"


def ensure_save_directory() -> None:
    """
    Ensure that the save directory exists.
    """
    if not os.path.exists(SAVE_DIRECTORY):
        os.makedirs(SAVE_DIRECTORY)


def generate_save_filename(player_name: str) -> str:
    """
    Generate a unique filename for the save file.

    Args:
        player_name: The player's name

    Returns:
        A unique filename for the save file
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"{player_name}_{timestamp}.json"


def save_game(player: Player, world: World) -> None:
    """
    Save the current game state to a file.

    Args:
        player: The player to save
        world: The world to save
    """
    ensure_save_directory()

    save_data = {
        "player": player.to_dict(),
        "world": world.to_dict()
    }

    filename = generate_save_filename(player.name)
    filepath = os.path.join(SAVE_DIRECTORY, filename)

    try:
        with open(filepath, 'w') as save_file:
            json.dump(save_data, save_file, indent=2)
        print(f"Game saved successfully as {filename}")
    except IOError as e:
        print(f"Error saving game: {e}")


def load_game(filename: str) -> Tuple[Optional[Player], Optional[World]]:
    """
    Load a game state from a file.

    Args:
        filename: The filename to load from

    Returns:
        A tuple containing the player and world, or None if loading failed
    """
    filepath = os.path.join(SAVE_DIRECTORY, filename)

    try:
        with open(filepath, 'r') as save_file:
            save_data = json.load(save_file)
        print(f"Game loaded successfully from {filename}")
        
        player = Player.from_dict(save_data["player"])
        world = World.from_dict(save_data["world"])
        
        return player, world
    except IOError as e:
        print(f"Error loading game: {e}")
        return None, None
    except json.JSONDecodeError:
        print(f"Error: The save file {filename} is corrupted.")
        return None, None


def list_save_files() -> List[str]:
    """
    List all available save files.

    Returns:
        A list of save filenames
    """
    ensure_save_directory()
    save_files = [f for f in os.listdir(SAVE_DIRECTORY) if f.endswith('.json')]
    return save_files


def delete_save_file(filename: str) -> None:
    """
    Delete a save file.

    Args:
        filename: The filename to delete
    """
    filepath = os.path.join(SAVE_DIRECTORY, filename)
    try:
        os.remove(filepath)
        print(f"Save file {filename} deleted successfully.")
    except OSError as e:
        print(f"Error deleting save file: {e}")


def load_most_recent_save() -> Tuple[Optional[Player], Optional[World]]:
    """
    Load the most recent save file.

    Returns:
        A tuple containing the player and world, or None if loading failed
    """
    save_files = list_save_files()
    if not save_files:
        print("No save files found.")
        return None, None

    most_recent = max(save_files, key=lambda f: os.path.getmtime(os.path.join(SAVE_DIRECTORY, f)))
    return load_game(most_recent)

