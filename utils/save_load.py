import json
import os
from datetime import datetime
from game.player import Player
from game.world import World
from game.exceptions import SaveLoadError, InvalidSaveFileError

SAVE_DIRECTORY = "saves"

def ensure_save_directory():
    """Ensure that the save directory exists. Use save_game() to actually save the game."""
    if not os.path.exists(SAVE_DIRECTORY):
        os.makedirs(SAVE_DIRECTORY)

def generate_save_filename(player_name):
    """Generate a unique filename for the save file. Use save_game() to actually save the game."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"{player_name}_{timestamp}.json"

def save_game(player, world):
    """
    Save the current game state to a file.
    
    Args:
        player: Player object or dictionary
        world: World object or dictionary
    """
    ensure_save_directory()

    # Convert objects to dictionaries for JSON serialization
    if isinstance(player, Player):
        player_data = player.to_dict()
        player_name = player.name
    else:
        # Handle old dictionary format
        player_data = player
        player_name = player["name"]
    
    if isinstance(world, World):
        world_data = world.to_dict()
    else:
        # Handle old dictionary format
        world_data = world

    save_data = {
        "version": "2.0",  # Version for new class-based format
        "player": player_data,
        "world": world_data,
        "saved_at": datetime.now().isoformat()
    }

    filename = generate_save_filename(player_name)
    filepath = os.path.join(SAVE_DIRECTORY, filename)

    try:
        with open(filepath, 'w') as save_file:
            json.dump(save_data, save_file, indent=2)
        print(f"Game saved successfully as {filename}")
        return filename
    except IOError as e:
        error_msg = f"Error saving game: {e}"
        print(error_msg)
        raise SaveLoadError(error_msg)

def load_game(filename):
    """
    Load a game state from a file.
    
    Args:
        filename (str): Name of the save file
        
    Returns:
        tuple: (Player object, World object) or (None, None) on error
    """
    filepath = os.path.join(SAVE_DIRECTORY, filename)

    try:
        with open(filepath, 'r') as save_file:
            save_data = json.load(save_file)
        
        # Check save file version
        version = save_data.get("version", "1.0")
        
        if version == "2.0":
            # New class-based format
            player = Player.from_dict(save_data["player"])
            world = World.from_dict(save_data["world"])
        else:
            # Old dictionary format - convert to classes
            player_data = save_data["player"]
            world_data = save_data["world"]
            
            # Convert old format to new classes
            player = Player.from_dict(player_data)
            world = World.from_dict(world_data)
        
        print(f"Game loaded successfully from {filename}")
        return player, world
        
    except IOError as e:
        error_msg = f"Error loading game: {e}"
        print(error_msg)
        return None, None
    except json.JSONDecodeError as e:
        error_msg = f"The save file {filename} is corrupted: {e}"
        print(f"Error: {error_msg}")
        return None, None
    except KeyError as e:
        error_msg = f"Invalid save file format: missing {e}"
        print(f"Error: {error_msg}")
        return None, None
    except Exception as e:
        error_msg = f"Unexpected error loading save file: {e}"
        print(f"Error: {error_msg}")
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
