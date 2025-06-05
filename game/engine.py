"""
Game Engine - Central coordinator for game state and operations.
Provides a clean interface for game operations and manages state consistency.
"""
from typing import Dict, Any, Optional, Tuple
import logging

from game.player import create_player, get_player_status
from game.world import initialize_world, get_current_location
from game.actions import perform_action
from game.constants import DEFAULT_PLAYER_NAME, Messages, HELP_TEXT
from game.exceptions import (
    GameError, 
    SaveGameError, 
    LoadGameError,
    InvalidInputError
)
from utils.save_load import save_game, load_game, list_save_files
from utils.text_formatting import print_welcome_message, print_colored


class GameEngine:
    """
    Central game engine that manages game state and coordinates between modules.
    """
    
    def __init__(self):
        self.player: Optional[Dict[str, Any]] = None
        self.world: Optional[Dict[str, Any]] = None
        self.running: bool = False
        self.logger = logging.getLogger(__name__)
    
    def initialize_new_game(self, player_name: str = DEFAULT_PLAYER_NAME) -> None:
        """Initialize a new game with default settings."""
        try:
            self.player = create_player(player_name)
            self.world = initialize_world()
            self.logger.info(f"New game initialized for player: {player_name}")
        except Exception as e:
            self.logger.error(f"Failed to initialize new game: {e}")
            raise GameError(f"Failed to initialize new game: {e}")
    
    def load_saved_game(self) -> bool:
        """
        Attempt to load a saved game.
        
        Returns:
            bool: True if game was loaded successfully, False otherwise
        """
        try:
            save_files = list_save_files()
            if not save_files:
                print("No save files found.")
                return False
            
            print("Available save files:")
            for i, file in enumerate(save_files, 1):
                print(f"{i}. {file}")
            
            choice_input = input("Enter the number of the save file to load: ").strip()
            if not choice_input.isdigit():
                raise InvalidInputError("Invalid choice. Please enter a number.")
            
            choice = int(choice_input)
            if not (1 <= choice <= len(save_files)):
                raise InvalidInputError("Invalid choice. Please select a valid save file.")
            
            self.player, self.world = load_game(save_files[choice - 1])
            
            if self.player is None or self.world is None:
                raise LoadGameError("Failed to load game data.")
            
            print(Messages.GAME_LOADED)
            self.logger.info(f"Game loaded from: {save_files[choice - 1]}")
            return True
            
        except (InvalidInputError, LoadGameError) as e:
            print(f"Error loading game: {e}")
            self.logger.error(f"Error loading game: {e}")
            return False
        except Exception as e:
            print(f"Unexpected error loading game: {e}")
            self.logger.error(f"Unexpected error loading game: {e}")
            return False
    
    def save_current_game(self) -> bool:
        """
        Save the current game state.
        
        Returns:
            bool: True if game was saved successfully, False otherwise
        """
        try:
            if self.player is None or self.world is None:
                raise SaveGameError("No game state to save.")
            
            save_game(self.player, self.world)
            print(Messages.GAME_SAVED)
            self.logger.info("Game saved successfully")
            return True
            
        except SaveGameError as e:
            print(f"Error saving game: {e}")
            self.logger.error(f"Error saving game: {e}")
            return False
        except Exception as e:
            print(f"Unexpected error saving game: {e}")
            self.logger.error(f"Unexpected error saving game: {e}")
            return False
    
    def start_game(self) -> None:
        """Start the main game loop."""
        print_welcome_message()
        
        # Ask if player wants to load a saved game
        load_choice = input("Do you want to load a saved game? (y/n): ").lower().strip()
        
        if load_choice == 'y':
            if not self.load_saved_game():
                print("Starting a new game instead.")
                self.initialize_new_game()
        else:
            self.initialize_new_game()
        
        self.running = True
        self.main_game_loop()
    
    def main_game_loop(self) -> None:
        """Main game loop that handles player input and game state."""
        while self.running:
            try:
                self.display_current_state()
                action = self.get_player_input()
                self.process_action(action)
                
            except KeyboardInterrupt:
                print("\nGame interrupted by user.")
                self.quit_game()
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
                self.logger.error(f"Unexpected error in main game loop: {e}")
                # Continue the game loop instead of crashing
    
    def display_current_state(self) -> None:
        """Display the current game state to the player."""
        if self.player is None or self.world is None:
            return
        
        current_location = get_current_location(self.world)
        print(f"\nYou are in the {current_location}.")
        print(get_player_status(self.player))
    
    def get_player_input(self) -> str:
        """Get and validate player input."""
        try:
            action = input("What would you like to do? ").strip()
            if not action:
                raise InvalidInputError("Please enter a command.")
            return action
        except EOFError:
            # Handle Ctrl+D
            print("\nExiting game...")
            self.quit_game()
            return "quit"
    
    def process_action(self, action: str) -> None:
        """Process a player action."""
        if self.player is None or self.world is None:
            return
        
        action_lower = action.lower()
        
        # Handle special commands
        if action_lower == "quit":
            self.quit_game()
        elif action_lower == "help":
            self.show_help()
        elif action_lower == "save":
            self.save_current_game()
        else:
            # Delegate to action system
            try:
                success = perform_action(self.player, self.world, action)
                if not success:
                    print_colored(Messages.INVALID_COMMAND, "yellow")
            except GameError as e:
                print_colored(f"Error: {e}", "red")
                self.logger.error(f"Game error processing action '{action}': {e}")
            except Exception as e:
                print_colored(f"Unexpected error: {e}", "red")
                self.logger.error(f"Unexpected error processing action '{action}': {e}")
    
    def show_help(self) -> None:
        """Display help information."""
        print_colored(HELP_TEXT, "cyan")
    
    def quit_game(self) -> None:
        """Quit the game, saving progress first."""
        if self.player is not None and self.world is not None:
            save_choice = input("Do you want to save your progress? (y/n): ").lower().strip()
            if save_choice == 'y':
                self.save_current_game()
        
        print("Thanks for playing!")
        self.running = False
    
    def get_game_state(self) -> Tuple[Optional[Dict[str, Any]], Optional[Dict[str, Any]]]:
        """
        Get the current game state.
        
        Returns:
            Tuple of (player, world) dictionaries
        """
        return self.player, self.world
    
    def is_running(self) -> bool:
        """Check if the game is currently running."""
        return self.running
    
    def get_player_health(self) -> int:
        """Get the current player health."""
        if self.player is None:
            return 0
        return self.player.get("health", 0)
    
    def get_player_gold(self) -> int:
        """Get the current player gold."""
        if self.player is None:
            return 0
        return self.player.get("gold", 0)
    
    def get_current_location_name(self) -> str:
        """Get the name of the current location."""
        if self.world is None:
            return "Unknown"
        return get_current_location(self.world)


# Global game engine instance
game_engine = GameEngine()

