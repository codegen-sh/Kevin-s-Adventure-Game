"""
Module for the game engine.
"""

from game.actions import perform_action
from game.player import Player, get_player_status
from game.state import GameState
from game.world import World, get_current_location
from ui.display import print_help, print_welcome_message
from ui.input_handler import get_input, get_yes_no
from utils.save_load import (
    LoadError,
    SaveError,
    list_save_files,
    load_game,
    load_most_recent_save,
    save_game,
)


class GameEngine:
    """
    A class to manage the game loop and game state.
    
    Attributes:
        player: The player
        world: The world
        game_state: The game state
        running (bool): Whether the game is running
    """
    
    def __init__(self, player=None, world=None, game_state=None):
        """
        Initialize a new GameEngine.
        
        Args:
            player: The player. Defaults to None.
            world: The world. Defaults to None.
            game_state: The game state. Defaults to None.
        """
        self.player = player
        self.world = world
        self.game_state = game_state
        self.running = False
    
    def initialize_new_game(self, player_name="Kevin"):
        """
        Initialize a new game.
        
        Args:
            player_name (str, optional): The player's name. Defaults to "Kevin".
        """
        self.player = Player(player_name)
        self.world = World()
        self.game_state = GameState(self.player.to_dict(), self.world.to_dict())
    
    def load_game(self, save_file=None):
        """
        Load a game from a save file.
        
        Args:
            save_file (str, optional): The save file to load. Defaults to None.
        
        Returns:
            bool: True if the game was loaded successfully, False otherwise
        """
        try:
            if save_file:
                self.player, self.world = load_game(save_file)
            else:
                self.player, self.world = load_most_recent_save()
            
            # Convert dictionaries to objects if needed
            if isinstance(self.player, dict):
                self.player = Player.from_dict(self.player)
            if isinstance(self.world, dict):
                self.world = World.from_dict(self.world)
            
            self.game_state = GameState(self.player.to_dict(), self.world.to_dict())
            return True
        except LoadError as e:
            print(f"Error loading game: {e}")
            return False
    
    def save_game(self):
        """
        Save the current game state.
        
        Returns:
            bool: True if the game was saved successfully, False otherwise
        """
        try:
            save_game(self.player, self.world)
            return True
        except SaveError as e:
            print(f"Error saving game: {e}")
            return False
    
    def start(self):
        """
        Start the game.
        """
        print_welcome_message()
        
        # Add load game option
        load_option = get_yes_no("Do you want to load a saved game? (y/n): ")
        if load_option:
            save_files = list_save_files()
            if save_files:
                print("Available save files:")
                for i, file in enumerate(save_files, 1):
                    print(f"{i}. {file}")
                
                while True:
                    try:
                        choice = int(get_input("Enter the number of the save file to load (or 0 to start a new game): "))
                        if choice == 0:
                            self.initialize_new_game()
                            break
                        elif 1 <= choice <= len(save_files):
                            if not self.load_game(save_files[choice - 1]):
                                print("Failed to load game. Starting a new game.")
                                self.initialize_new_game()
                            break
                        else:
                            print(f"Please enter a number between 0 and {len(save_files)}.")
                    except ValueError:
                        print("Please enter a valid number.")
            else:
                print("No save files found. Starting a new game.")
                self.initialize_new_game()
        else:
            self.initialize_new_game()
        
        self.running = True
        self.game_loop()
    
    def game_loop(self):
        """
        Run the main game loop.
        """
        while self.running:
            current_location = get_current_location(self.world)
            print(f"\nYou are in the {current_location}.")
            print(get_player_status(self.player))
            
            action = get_input("What would you like to do? ").lower()
            
            if action == "quit":
                self.save_game()
                print("Thanks for playing! Your progress has been saved.")
                self.running = False
            elif action == "help":
                print_help()
            else:
                perform_action(self.player, self.world, action)
    
    def stop(self):
        """
        Stop the game.
        """
        self.running = False

