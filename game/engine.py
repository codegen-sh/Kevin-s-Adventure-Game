"""
Game engine module for Kevin's Adventure Game.
This module provides the main game engine that manages game state and flow.
"""

from game.actions import perform_action
from game.config import SAVE_CONFIG
from game.player import Player
from game.world import World, initialize_world
from utils.save_load import (SaveError, list_save_files, load_game,
                            load_most_recent_save, save_game)
from utils.text_formatting import print_help, print_welcome_message


class GameEngine:
    """
    Main game engine class that manages game state and flow.
    """
    
    def __init__(self):
        """Initialize a new GameEngine instance."""
        self.player = None
        self.world = None
        self.action_count = 0
        self.running = False
    
    def start(self):
        """
        Start the game.
        
        This method initializes the game, loads or creates a new game state,
        and starts the main game loop.
        """
        print_welcome_message()
        
        # Initialize game state
        self._initialize_game_state()
        
        # Start the main game loop
        self.running = True
        self._main_loop()
    
    def _initialize_game_state(self):
        """
        Initialize the game state by loading a saved game or creating a new one.
        """
        # Ask if the player wants to load a saved game
        load_option = input("Do you want to load a saved game? (y/n): ").lower()
        
        if load_option == 'y':
            self._load_game()
        else:
            self._new_game()
    
    def _load_game(self):
        """
        Load a saved game.
        """
        try:
            save_files = list_save_files()
            
            if save_files:
                print("Available save files:")
                for i, file in enumerate(save_files, 1):
                    print(f"{i}. {file}")
                
                choice = input("Enter the number of the save file to load (or 'r' for most recent): ")
                
                if choice.lower() == 'r':
                    player_dict, world_dict = load_most_recent_save()
                else:
                    try:
                        choice_index = int(choice) - 1
                        if 0 <= choice_index < len(save_files):
                            player_dict, world_dict = load_game(save_files[choice_index])
                        else:
                            print("Invalid choice. Starting a new game.")
                            self._new_game()
                            return
                    except ValueError:
                        print("Invalid input. Starting a new game.")
                        self._new_game()
                        return
                
                if player_dict is None or world_dict is None:
                    print("Failed to load game. Starting a new game.")
                    self._new_game()
                else:
                    # Convert dictionaries to objects
                    self.player = Player.from_dict(player_dict)
                    self.world = World.from_dict(world_dict)
            else:
                print("No save files found. Starting a new game.")
                self._new_game()
        except SaveError as e:
            print(f"Error loading game: {e}")
            print("Starting a new game.")
            self._new_game()
    
    def _new_game(self):
        """
        Create a new game.
        """
        name = input("Enter your character's name (default: Kevin): ") or "Kevin"
        self.player = Player(name)
        
        # Initialize world from dictionary for now
        world_dict = initialize_world()
        self.world = World.from_dict(world_dict)
    
    def _main_loop(self):
        """
        Main game loop.
        """
        while self.running:
            # Display current location and player status
            current_location = self.world.get_current_location_name()
            print(f"\nYou are in the {current_location}.")
            print(self.player.get_status())
            
            # Get player action
            action = input("What would you like to do? ").lower()
            
            # Process action
            if action == "quit":
                self._handle_quit()
                break
            elif action == "help":
                print_help()
            else:
                perform_action(self.player, self.world, action)
                self.action_count += 1
                
                # Autosave if enabled
                if (SAVE_CONFIG["AUTOSAVE_ENABLED"] and 
                    self.action_count % SAVE_CONFIG["AUTOSAVE_FREQUENCY"] == 0):
                    try:
                        save_game(self.player, self.world)
                        print("Game autosaved.")
                    except SaveError as e:
                        print(f"Autosave failed: {e}")
    
    def _handle_quit(self):
        """
        Handle the quit command.
        """
        try:
            save_game(self.player, self.world)
            print("Thanks for playing! Your progress has been saved.")
        except SaveError as e:
            print(f"Error saving game: {e}")
            print("Thanks for playing! Your progress could not be saved.")
        
        self.running = False


def run_game():
    """
    Run the game.
    
    This function creates a new GameEngine instance and starts the game.
    """
    engine = GameEngine()
    engine.start()

