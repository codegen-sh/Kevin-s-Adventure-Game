"""
Game Engine for Kevin's Adventure Game.
Central coordinator for game state and flow.
"""

from typing import Optional, Union, Dict, Any
from game.player import Player, create_player
from game.world import World, initialize_world, get_current_location
from game.actions import perform_action
from utils.save_load import list_save_files, load_game, save_game
from utils.text_formatting import print_help, print_welcome_message


class GameEngine:
    """
    Central game engine that manages game state and coordinates between components.
    
    Attributes:
        player: Current player instance
        world: Current world instance
        running: Whether the game is currently running
        auto_save: Whether to automatically save on quit
    """
    
    def __init__(self, auto_save: bool = True):
        """
        Initialize the game engine.
        
        Args:
            auto_save: Whether to automatically save when quitting
        """
        self.player: Optional[Player] = None
        self.world: Optional[World] = None
        self.running = False
        self.auto_save = auto_save
    
    def start_new_game(self, player_name: str = "Kevin") -> None:
        """
        Start a new game with a fresh player and world.
        
        Args:
            player_name: Name for the new player
        """
        self.player = create_player(player_name)
        self.world = initialize_world()
        self.running = True
        print(f"Started new game with player: {player_name}")
    
    def load_game_from_file(self, save_file: str) -> bool:
        """
        Load a game from a save file.
        
        Args:
            save_file: Name of the save file to load
            
        Returns:
            True if game was loaded successfully, False otherwise
        """
        try:
            player_data, world_data = load_game(save_file)
            if player_data is None or world_data is None:
                return False
            
            # Convert loaded data to proper instances
            if isinstance(player_data, Player):
                self.player = player_data
            else:
                self.player = Player.from_dict(player_data)
            
            if isinstance(world_data, World):
                self.world = world_data
            else:
                self.world = World.from_dict(world_data)
            
            self.running = True
            print(f"Game loaded successfully from {save_file}")
            return True
            
        except Exception as e:
            print(f"Failed to load game: {e}")
            return False
    
    def save_current_game(self, save_file: str = None) -> bool:
        """
        Save the current game state.
        
        Args:
            save_file: Optional save file name, defaults to auto-generated name
            
        Returns:
            True if game was saved successfully, False otherwise
        """
        if not self.player or not self.world:
            print("No game to save!")
            return False
        
        try:
            save_game(self.player, self.world, save_file)
            return True
        except Exception as e:
            print(f"Failed to save game: {e}")
            return False
    
    def run_game_loop(self) -> None:
        """Run the main game loop."""
        if not self.player or not self.world:
            print("Game not initialized! Call start_new_game() or load_game_from_file() first.")
            return
        
        print_welcome_message()
        
        while self.running:
            try:
                self._display_current_state()
                action = self._get_player_input()
                self._process_action(action)
                
                # Check if player is still alive
                if not self.player.is_alive():
                    print("Game Over!")
                    self.running = False
                    
            except KeyboardInterrupt:
                print("\nGame interrupted by user.")
                self._handle_quit()
                break
            except Exception as e:
                print(f"An error occurred: {e}")
                print("Type 'help' for available commands.")
    
    def _display_current_state(self) -> None:
        """Display the current game state to the player."""
        if isinstance(self.world, World):
            current_location = self.world.get_current_location()
        else:
            current_location = get_current_location(self.world)
        
        print(f"\nYou are in the {current_location}.")
        print(self.player.get_status())
    
    def _get_player_input(self) -> str:
        """Get input from the player."""
        return input("What would you like to do? ").strip()
    
    def _process_action(self, action: str) -> None:
        """
        Process a player action.
        
        Args:
            action: Action string from player input
        """
        action_lower = action.lower()
        
        # Handle engine-level commands
        if action_lower == "quit" or action_lower == "exit":
            self._handle_quit()
        elif action_lower == "help":
            print_help()
        elif action_lower == "save":
            self._handle_save()
        elif action_lower.startswith("save "):
            save_name = action[5:].strip()
            self._handle_save(save_name)
        elif action_lower == "status":
            self._handle_status()
        else:
            # Delegate to action system
            perform_action(self.player, self.world, action)
    
    def _handle_quit(self) -> None:
        """Handle quit command."""
        if self.auto_save:
            if self.save_current_game():
                print("Game saved automatically.")
        
        print("Thanks for playing Kevin's Adventure Game!")
        self.running = False
    
    def _handle_save(self, save_name: str = None) -> None:
        """Handle save command."""
        if self.save_current_game(save_name):
            print("Game saved successfully!")
        else:
            print("Failed to save game.")
    
    def _handle_status(self) -> None:
        """Handle status command."""
        print("\n=== Game Status ===")
        print(f"Player: {self.player.name}")
        print(self.player.get_status())
        
        if isinstance(self.world, World):
            current_location = self.world.get_current_location()
            available_locations = self.world.get_available_locations()
        else:
            current_location = get_current_location(self.world)
            from game.world import get_available_locations
            available_locations = get_available_locations(self.world)
        
        print(f"Current Location: {current_location}")
        print(f"Available Exits: {', '.join(available_locations)}")
    
    def quit_game(self) -> None:
        """Quit the game (can be called externally)."""
        self._handle_quit()
    
    def is_running(self) -> bool:
        """Check if the game is currently running."""
        return self.running
    
    def get_player(self) -> Optional[Player]:
        """Get the current player instance."""
        return self.player
    
    def get_world(self) -> Optional[World]:
        """Get the current world instance."""
        return self.world


def run_interactive_game() -> None:
    """
    Run an interactive game session with load/new game options.
    This is the main entry point for the game.
    """
    print_welcome_message()
    
    # Ask if player wants to load a saved game
    load_option = input("Do you want to load a saved game? (y/n): ").lower()
    
    engine = GameEngine()
    
    if load_option == 'y':
        save_files = list_save_files()
        if save_files:
            print("Available save files:")
            for i, file in enumerate(save_files, 1):
                print(f"{i}. {file}")
            
            try:
                choice = int(input("Enter the number of the save file to load: "))
                if 1 <= choice <= len(save_files):
                    if engine.load_game_from_file(save_files[choice - 1]):
                        print("Game loaded successfully!")
                    else:
                        print("Failed to load game. Starting a new game.")
                        engine.start_new_game()
                else:
                    print("Invalid choice. Starting a new game.")
                    engine.start_new_game()
            except (ValueError, IndexError):
                print("Invalid input. Starting a new game.")
                engine.start_new_game()
        else:
            print("No save files found. Starting a new game.")
            engine.start_new_game()
    else:
        engine.start_new_game()
    
    # Run the main game loop
    engine.run_game_loop()

