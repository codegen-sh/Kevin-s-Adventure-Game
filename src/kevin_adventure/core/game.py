"""
Core Game class that manages the game state and main loop.
"""
from typing import Dict, List, Optional

from kevin_adventure.core.command_processor import CommandProcessor
from kevin_adventure.entities.player import Player
from kevin_adventure.entities.world import World
from kevin_adventure.ui.text_ui import TextUI
from kevin_adventure.utils.save_load import SaveManager


class Game:
    """Main game class that manages the game state and main loop."""

    def __init__(self):
        """Initialize the game with default values."""
        self.player: Optional[Player] = None
        self.world: Optional[World] = None
        self.ui = TextUI()
        self.command_processor = CommandProcessor(self)
        self.save_manager = SaveManager()
        self.running = False

    def initialize(self, player_name: str = "Kevin") -> None:
        """Initialize a new game with a new player and world."""
        self.player = Player(name=player_name)
        self.world = World()
        self.world.initialize()
        self.running = True

    def load_game(self, save_file: str) -> bool:
        """Load a game from a save file."""
        try:
            game_data = self.save_manager.load_game(save_file)
            if game_data:
                self.player = game_data["player"]
                self.world = game_data["world"]
                self.running = True
                return True
            return False
        except Exception as e:
            self.ui.display_error(f"Error loading game: {e}")
            return False

    def save_game(self) -> bool:
        """Save the current game state."""
        if not self.player or not self.world:
            self.ui.display_error("No game in progress to save.")
            return False

        try:
            self.save_manager.save_game(self.player, self.world)
            return True
        except Exception as e:
            self.ui.display_error(f"Error saving game: {e}")
            return False

    def process_command(self, command: str) -> bool:
        """Process a player command."""
        return self.command_processor.process(command)

    def quit(self) -> None:
        """Quit the game, saving the current state."""
        self.save_game()
        self.running = False
        self.ui.display_message("Thanks for playing! Your progress has been saved.")

    def run(self) -> None:
        """Run the main game loop."""
        self.ui.display_welcome()

        # Handle game loading or initialization
        load_option = self.ui.get_input("Do you want to load a saved game? (y/n): ").lower()
        if load_option == 'y':
            save_files = self.save_manager.list_save_files()
            if save_files:
                self.ui.display_message("Available save files:")
                for i, file in enumerate(save_files, 1):
                    self.ui.display_message(f"{i}. {file}")
                choice = int(self.ui.get_input("Enter the number of the save file to load: "))
                if not self.load_game(save_files[choice - 1]):
                    self.ui.display_message("Failed to load game. Starting a new game.")
                    self.initialize()
            else:
                self.ui.display_message("No save files found. Starting a new game.")
                self.initialize()
        else:
            self.initialize()

        # Main game loop
        while self.running:
            current_location = self.world.get_current_location()
            self.ui.display_message(f"\nYou are in the {current_location.name}.")
            self.ui.display_message(self.player.get_status())

            command = self.ui.get_input("What would you like to do? ").lower()
            self.process_command(command)

        self.ui.display_message("Game ended. Goodbye!")

