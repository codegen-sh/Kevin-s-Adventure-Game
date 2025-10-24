import json
import os
from datetime import datetime
from game.config import GAME_SETTINGS, MESSAGES

SAVE_DIRECTORY = GAME_SETTINGS["save_directory"]

def ensure_save_directory():
    """Ensure that the save directory exists. Use save_game() to actually save the game."""
    if not os.path.exists(SAVE_DIRECTORY):
        os.makedirs(SAVE_DIRECTORY)

def generate_save_filename(player_name):
    """Generate a unique filename for the save file. Use save_game() to actually save the game."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"{player_name}_{timestamp}.json"

def save_game(player, world):
    """Save the current game state to a file."""
    ensure_save_directory()

    save_data = {
        "player": player,
        "world": world
    }

    filename = generate_save_filename(player["name"])
    filepath = os.path.join(SAVE_DIRECTORY, filename)

    try:
        with open(filepath, 'w') as save_file:
            json.dump(save_data, save_file, indent=2)
        print(f"Game saved successfully as {filename}")
    except IOError as e:
        print(f"Error saving game: {e}")

def load_game(filename):
    """Load a game state from a file."""
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
