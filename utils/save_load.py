import json
import os
import shutil
from datetime import datetime

SAVE_DIRECTORY = "saves"

class SaveError(Exception):
    """Exception raised for errors in the save process."""
    pass

class LoadError(Exception):
    """Exception raised for errors in the load process."""
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
        raise SaveError(f"Failed to create save directory: {e}")

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
        player: The player's current state
        world: The game world state
    
    Raises:
        SaveError: If the game cannot be saved
    """
    try:
        ensure_save_directory()
        
        # Convert player and world to dictionaries if they are objects
        if hasattr(player, 'to_dict'):
            player_dict = player.to_dict()
        else:
            player_dict = player
            
        if hasattr(world, 'to_dict'):
            world_dict = world.to_dict()
        else:
            world_dict = world
        
        save_data = {
            "player": player_dict,
            "world": world_dict
        }
        
        player_name = player_dict.get("name", "Kevin")
        filename = generate_save_filename(player_name)
        filepath = os.path.join(SAVE_DIRECTORY, filename)
        
        # Create a temporary file first to avoid corrupting existing saves
        temp_filepath = filepath + ".tmp"
        with open(temp_filepath, 'w') as save_file:
            json.dump(save_data, save_file, indent=2)
        
        # Rename the temporary file to the actual file
        shutil.move(temp_filepath, filepath)
        
        print(f"Game saved successfully as {filename}")
    except (IOError, OSError, json.JSONEncodeError) as e:
        raise SaveError(f"Error saving game: {e}")

def load_game(filename):
    """
    Load a game state from a file.
    
    Args:
        filename (str): The name of the save file to load
    
    Returns:
        tuple: A tuple containing the player and world states
    
    Raises:
        LoadError: If the game cannot be loaded
    """
    filepath = os.path.join(SAVE_DIRECTORY, filename)
    
    try:
        with open(filepath, 'r') as save_file:
            save_data = json.load(save_file)
        print(f"Game loaded successfully from {filename}")
        
        # Check if we need to convert dictionaries to objects
        from game.player import Player
        from game.world import World
        
        player_dict = save_data.get("player", {})
        world_dict = save_data.get("world", {})
        
        # Try to convert to objects, fall back to dictionaries if it fails
        try:
            player = Player.from_dict(player_dict)
        except (AttributeError, TypeError):
            player = player_dict
            
        try:
            world = World.from_dict(world_dict)
        except (AttributeError, TypeError):
            world = world_dict
            
        return player, world
    except FileNotFoundError:
        raise LoadError(f"Save file {filename} not found")
    except json.JSONDecodeError:
        raise LoadError(f"Save file {filename} is corrupted")
    except IOError as e:
        raise LoadError(f"Error loading game: {e}")

def list_save_files():
    """
    List all available save files.
    
    Returns:
        list: A list of save file names
    """
    try:
        ensure_save_directory()
        save_files = [f for f in os.listdir(SAVE_DIRECTORY) if f.endswith('.json')]
        return save_files
    except OSError as e:
        print(f"Error listing save files: {e}")
        return []

def delete_save_file(filename):
    """
    Delete a save file.
    
    Args:
        filename (str): The name of the save file to delete
    
    Raises:
        SaveError: If the file cannot be deleted
    """
    filepath = os.path.join(SAVE_DIRECTORY, filename)
    try:
        os.remove(filepath)
        print(f"Save file {filename} deleted successfully.")
    except FileNotFoundError:
        raise SaveError(f"Save file {filename} not found")
    except OSError as e:
        raise SaveError(f"Error deleting save file: {e}")

def load_most_recent_save():
    """
    Load the most recent save file.
    
    Returns:
        tuple: A tuple containing the player and world states
    
    Raises:
        LoadError: If no save files are found or the game cannot be loaded
    """
    save_files = list_save_files()
    if not save_files:
        raise LoadError("No save files found")
    
    try:
        most_recent = max(save_files, key=lambda f: os.path.getmtime(os.path.join(SAVE_DIRECTORY, f)))
        return load_game(most_recent)
    except (OSError, ValueError) as e:
        raise LoadError(f"Error loading most recent save: {e}")

