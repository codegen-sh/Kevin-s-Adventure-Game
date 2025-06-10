"""
Utility functions for saving and loading game state.
"""
import json
import os
from datetime import datetime
from typing import Dict, List, Optional, Tuple, Any


class SaveManager:
    """Manages saving and loading game state."""

    def __init__(self, save_directory: str = "saves"):
        """
        Initialize the save manager.
        
        Args:
            save_directory: The directory to save games in
        """
        self.save_directory = save_directory
        self.ensure_save_directory()

    def ensure_save_directory(self) -> None:
        """Ensure that the save directory exists."""
        if not os.path.exists(self.save_directory):
            os.makedirs(self.save_directory)

    def generate_save_filename(self, player_name: str) -> str:
        """
        Generate a unique filename for the save file.
        
        Args:
            player_name: The name of the player
            
        Returns:
            A unique filename for the save file
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        return f"{player_name}_{timestamp}.json"

    def save_game(self, player: Any, world: Any) -> str:
        """
        Save the current game state to a file.
        
        Args:
            player: The player object
            world: The world object
            
        Returns:
            The filename of the saved game
        """
        self.ensure_save_directory()

        # Convert objects to dictionaries
        save_data = {
            "player": player.to_dict(),
            "world": world.to_dict(),
            "timestamp": datetime.now().isoformat()
        }

        filename = self.generate_save_filename(player.name)
        filepath = os.path.join(self.save_directory, filename)

        try:
            with open(filepath, 'w') as save_file:
                json.dump(save_data, save_file, indent=2)
            print(f"Game saved successfully as {filename}")
            return filename
        except IOError as e:
            print(f"Error saving game: {e}")
            raise

    def load_game(self, filename: str) -> Optional[Dict[str, Any]]:
        """
        Load a game state from a file.
        
        Args:
            filename: The name of the save file
            
        Returns:
            A dictionary containing the player and world objects, or None if loading failed
        """
        from kevin_adventure.entities.player import Player
        from kevin_adventure.entities.world import World
        
        filepath = os.path.join(self.save_directory, filename)

        try:
            with open(filepath, 'r') as save_file:
                save_data = json.load(save_file)
            print(f"Game loaded successfully from {filename}")
            
            # Convert dictionaries back to objects
            player = Player.from_dict(save_data["player"])
            world = World.from_dict(save_data["world"])
            
            return {
                "player": player,
                "world": world
            }
        except IOError as e:
            print(f"Error loading game: {e}")
            return None
        except json.JSONDecodeError:
            print(f"Error: The save file {filename} is corrupted.")
            return None

    def list_save_files(self) -> List[str]:
        """
        List all available save files.
        
        Returns:
            A list of save filenames
        """
        self.ensure_save_directory()
        save_files = [f for f in os.listdir(self.save_directory) if f.endswith('.json')]
        return save_files

    def delete_save_file(self, filename: str) -> bool:
        """
        Delete a save file.
        
        Args:
            filename: The name of the save file
            
        Returns:
            True if the file was deleted, False otherwise
        """
        filepath = os.path.join(self.save_directory, filename)
        try:
            os.remove(filepath)
            print(f"Save file {filename} deleted successfully.")
            return True
        except OSError as e:
            print(f"Error deleting save file: {e}")
            return False

    def load_most_recent_save(self) -> Optional[Dict[str, Any]]:
        """
        Load the most recent save file.
        
        Returns:
            A dictionary containing the player and world objects, or None if loading failed
        """
        save_files = self.list_save_files()
        if not save_files:
            print("No save files found.")
            return None

        most_recent = max(save_files, key=lambda f: os.path.getmtime(os.path.join(self.save_directory, f)))
        return self.load_game(most_recent)

