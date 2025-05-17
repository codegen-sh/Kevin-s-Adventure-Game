import json
import os
import shutil
from datetime import datetime
from utils.text_formatting import print_error, print_success, print_warning

SAVE_DIRECTORY = "saves"
MAX_SAVES_PER_PLAYER = 5  # Maximum number of save files per player


def ensure_save_directory():
    """
    Ensure that the save directory exists.
    
    Returns:
        bool: True if directory exists or was created successfully, False otherwise
    """
    try:
        if not os.path.exists(SAVE_DIRECTORY):
            os.makedirs(SAVE_DIRECTORY)
        return True
    except OSError as e:
        print_error(f"Failed to create save directory: {e}")
        return False


def generate_save_filename(player_name, custom_name=None):
    """
    Generate a unique filename for the save file.
    
    Args:
        player_name (str): The name of the player
        custom_name (str, optional): Custom save name provided by the player
    
    Returns:
        str: The generated filename
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    if custom_name:
        # Replace spaces and special characters with underscores
        custom_name = ''.join(c if c.isalnum() else '_' for c in custom_name)
        return f"{player_name}_{custom_name}_{timestamp}.json"
    
    return f"{player_name}_{timestamp}.json"


def save_game(player, world, custom_name=None):
    """
    Save the current game state to a file.
    
    Args:
        player (dict): The player's state
        world (dict): The game world state
        custom_name (str, optional): Custom save name provided by the player
    
    Returns:
        bool: True if save was successful, False otherwise
    """
    if not ensure_save_directory():
        return False

    save_data = {
        "player": player,
        "world": world,
        "save_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "game_version": "1.0.0"  # Add version tracking for compatibility
    }

    filename = generate_save_filename(player["name"], custom_name)
    filepath = os.path.join(SAVE_DIRECTORY, filename)

    try:
        with open(filepath, 'w') as save_file:
            json.dump(save_data, save_file, indent=2)
        print_success(f"Game saved successfully as {filename}")
        
        # Clean up old saves if there are too many
        cleanup_old_saves(player["name"])
        return True
    except IOError as e:
        print_error(f"Error saving game: {e}")
        return False
    except Exception as e:
        print_error(f"Unexpected error while saving game: {e}")
        return False


def load_game(filename):
    """
    Load a game state from a file.
    
    Args:
        filename (str): The name of the save file to load
    
    Returns:
        tuple: (player, world) - The loaded player and world state, or (None, None) if loading fails
    """
    filepath = os.path.join(SAVE_DIRECTORY, filename)

    if not os.path.exists(filepath):
        print_error(f"Save file {filename} does not exist.")
        return None, None

    try:
        with open(filepath, 'r') as save_file:
            save_data = json.load(save_file)
        
        # Check for version compatibility (future-proofing)
        if "game_version" in save_data:
            game_version = save_data.get("game_version")
            # Here you could add version compatibility checks
        
        print_success(f"Game loaded successfully from {filename}")
        
        # Create backup of the save file before loading
        backup_save_file(filepath)
        
        return save_data["player"], save_data["world"]
    except IOError as e:
        print_error(f"Error loading game: {e}")
        return None, None
    except json.JSONDecodeError:
        print_error(f"The save file {filename} is corrupted.")
        return None, None
    except KeyError as e:
        print_error(f"The save file {filename} is missing required data: {e}")
        return None, None
    except Exception as e:
        print_error(f"Unexpected error while loading game: {e}")
        return None, None


def list_save_files():
    """
    List all available save files.
    
    Returns:
        list: List of save filenames
    """
    if not ensure_save_directory():
        return []
    
    try:
        save_files = [f for f in os.listdir(SAVE_DIRECTORY) if f.endswith('.json')]
        save_files.sort(key=lambda f: os.path.getmtime(os.path.join(SAVE_DIRECTORY, f)), reverse=True)
        return save_files
    except OSError as e:
        print_error(f"Error listing save files: {e}")
        return []


def delete_save_file(filename):
    """
    Delete a save file.
    
    Args:
        filename (str): The name of the save file to delete
    
    Returns:
        bool: True if deletion was successful, False otherwise
    """
    filepath = os.path.join(SAVE_DIRECTORY, filename)
    
    if not os.path.exists(filepath):
        print_warning(f"Save file {filename} does not exist.")
        return False
    
    try:
        os.remove(filepath)
        print_success(f"Save file {filename} deleted successfully.")
        return True
    except OSError as e:
        print_error(f"Error deleting save file: {e}")
        return False


def load_most_recent_save():
    """
    Load the most recent save file.
    
    Returns:
        tuple: (player, world) - The loaded player and world state, or (None, None) if loading fails
    """
    save_files = list_save_files()
    
    if not save_files:
        print_warning("No save files found.")
        return None, None

    most_recent = save_files[0]  # Already sorted by modification time in list_save_files()
    return load_game(most_recent)


def backup_save_file(filepath):
    """
    Create a backup of a save file before loading it.
    
    Args:
        filepath (str): Path to the save file
    
    Returns:
        bool: True if backup was successful, False otherwise
    """
    try:
        backup_path = f"{filepath}.bak"
        shutil.copy2(filepath, backup_path)
        return True
    except OSError:
        # Silently fail - backup is nice to have but not critical
        return False


def cleanup_old_saves(player_name):
    """
    Remove old save files if a player has too many saves.
    
    Args:
        player_name (str): The name of the player
    """
    save_files = list_save_files()
    
    # Filter saves for this player
    player_saves = [f for f in save_files if f.startswith(f"{player_name}_")]
    
    # If player has more than the maximum allowed saves, delete the oldest ones
    if len(player_saves) > MAX_SAVES_PER_PLAYER:
        # Sort by modification time (oldest first)
        player_saves.sort(key=lambda f: os.path.getmtime(os.path.join(SAVE_DIRECTORY, f)))
        
        # Delete oldest saves
        for old_save in player_saves[:len(player_saves) - MAX_SAVES_PER_PLAYER]:
            delete_save_file(old_save)
