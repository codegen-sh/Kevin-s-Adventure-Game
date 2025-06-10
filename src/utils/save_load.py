"""
Save/Load module for Kevin's Adventure Game.
Contains the SaveManager class for saving and loading game state.
"""
import json
import os
import pickle
from datetime import datetime
from typing import List, Optional, Tuple, TYPE_CHECKING

if TYPE_CHECKING:
    from src.game.player import Player
    from src.game.weather import Weather
    from src.game.world import World


class SaveManager:
    """
    Manages saving and loading game state.
    """

    def __init__(self, save_directory: str = "saves"):
        """
        Initialize the save manager.

        Args:
            save_directory: The directory to store save files in
        """
        self.save_directory = save_directory
        self._ensure_save_directory()

    def _ensure_save_directory(self) -> None:
        """Ensure that the save directory exists."""
        if not os.path.exists(self.save_directory):
            os.makedirs(self.save_directory)

    def _generate_save_filename(self, player_name: str) -> str:
        """
        Generate a unique filename for the save file.

        Args:
            player_name: The name of the player

        Returns:
            A unique filename for the save file
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        return f"{player_name}_{timestamp}.pickle"

    def save_game(self, player: 'Player', world: 'World', weather: 'Weather') -> bool:
        """
        Save the current game state to a file.

        Args:
            player: The player object
            world: The world object
            weather: The weather object

        Returns:
            True if the save was successful, False otherwise
        """
        self._ensure_save_directory()

        filename = self._generate_save_filename(player.name)
        filepath = os.path.join(self.save_directory, filename)

        try:
            with open(filepath, 'wb') as save_file:
                pickle.dump((player, world, weather), save_file)
            print(f"Game saved successfully as {filename}")
            return True
        except (IOError, pickle.PickleError) as e:
            print(f"Error saving game: {e}")
            return False

    def load_game(self, filename: str) -> Optional[Tuple['Player', 'World', 'Weather']]:
        """
        Load a game state from a file.

        Args:
            filename: The name of the save file

        Returns:
            A tuple of (player, world, weather) if successful, None otherwise
        """
        filepath = os.path.join(self.save_directory, filename)

        try:
            with open(filepath, 'rb') as save_file:
                data = pickle.load(save_file)
            print(f"Game loaded successfully from {filename}")
            return data
        except (IOError, pickle.UnpickleError) as e:
            print(f"Error loading game: {e}")
            return None

    def list_save_files(self) -> List[str]:
        """
        List all available save files.

        Returns:
            A list of save file names
        """
        self._ensure_save_directory()
        save_files = [f for f in os.listdir(self.save_directory) if f.endswith('.pickle')]
        return save_files

    def delete_save_file(self, filename: str) -> bool:
        """
        Delete a save file.

        Args:
            filename: The name of the save file

        Returns:
            True if the file was deleted successfully, False otherwise
        """
        filepath = os.path.join(self.save_directory, filename)
        try:
            os.remove(filepath)
            print(f"Save file {filename} deleted successfully.")
            return True
        except OSError as e:
            print(f"Error deleting save file: {e}")
            return False

    def load_most_recent_save(self) -> Optional[Tuple['Player', 'World', 'Weather']]:
        """
        Load the most recent save file.

        Returns:
            A tuple of (player, world, weather) if successful, None otherwise
        """
        save_files = self.list_save_files()
        if not save_files:
            print("No save files found.")
            return None

        most_recent = max(
            save_files, 
            key=lambda f: os.path.getmtime(os.path.join(self.save_directory, f))
        )
        return self.load_game(most_recent)

