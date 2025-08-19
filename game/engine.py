"""
Game engine module for Kevin's Adventure Game.
This module handles the game loop and user input processing.
"""
from game.actions import perform_action
from game.player import Player, get_player_status
from game.world import World, get_current_location, initialize_world
from utils.save_load import list_save_files, load_game, save_game
from utils.text_formatting import print_help, print_welcome_message


class GameEngine:
    """
    Manages the game loop and state.
    
    Attributes:
        player (Player): The player object
        world (World): The world object
        running (bool): Whether the game is running
    """
    
    def __init__(self):
        """
        Initialize a new GameEngine instance.
        """
        self.player = None
        self.world = None
        self.running = False
    
    def start_new_game(self, player_name="Kevin"):
        """
        Start a new game.
        
        Args:
            player_name (str, optional): The player's name. Defaults to "Kevin".
        """
        self.player = Player(player_name)
        self.world = initialize_world()
        self.running = True
    
    def load_saved_game(self, save_file):
        """
        Load a saved game.
        
        Args:
            save_file (str): The name of the save file
        
        Returns:
            bool: True if the game was loaded successfully, False otherwise
        """
        player_data, world_data = load_game(save_file)
        
        if player_data is None or world_data is None:
            print("Failed to load game.")
            return False
        
        if isinstance(player_data, dict):
            # Convert dictionary to Player object
            self.player = Player(
                name=player_data.get("name", "Kevin"),
                health=player_data.get("health", 100),
                inventory=player_data.get("inventory", []),
                location=player_data.get("location", "Village"),
                gold=player_data.get("gold", 100)
            )
        else:
            self.player = player_data
        
        if isinstance(world_data, dict):
            # Convert dictionary to World object
            self.world = World.from_dict(world_data)
        else:
            self.world = world_data
        
        self.running = True
        return True
    
    def save_current_game(self):
        """
        Save the current game.
        
        Returns:
            bool: True if the game was saved successfully, False otherwise
        """
        if self.player and self.world:
            # Convert objects to dictionaries if needed
            player_data = self.player
            world_data = self.world
            
            if isinstance(self.player, Player):
                player_data = {
                    "name": self.player.name,
                    "health": self.player.health,
                    "inventory": self.player.inventory,
                    "location": self.player.location,
                    "gold": self.player.gold
                }
            
            if isinstance(self.world, World):
                world_data = self.world.to_dict()
            
            return save_game(player_data, world_data)
        
        return False
    
    def process_input(self, user_input):
        """
        Process user input.
        
        Args:
            user_input (str): The user's input
        
        Returns:
            bool: True if the game should continue, False if it should end
        """
        action = user_input.lower()
        
        if action == "quit":
            self.save_current_game()
            print("Thanks for playing! Your progress has been saved.")
            self.running = False
            return False
        elif action == "help":
            print_help()
        else:
            perform_action(self.player, self.world, action)
        
        return True
    
    def run(self):
        """
        Run the game loop.
        """
        print_welcome_message()
        
        # Add load game option
        load_option = input("Do you want to load a saved game? (y/n): ").lower()
        if load_option == 'y':
            save_files = list_save_files()
            if save_files:
                print("Available save files:")
                for i, file in enumerate(save_files, 1):
                    print(f"{i}. {file}")
                
                try:
                    choice = int(input("Enter the number of the save file to load: "))
                    if 1 <= choice <= len(save_files):
                        if not self.load_saved_game(save_files[choice - 1]):
                            print("Starting a new game.")
                            self.start_new_game()
                    else:
                        print("Invalid choice. Starting a new game.")
                        self.start_new_game()
                except ValueError:
                    print("Invalid input. Starting a new game.")
                    self.start_new_game()
            else:
                print("No save files found. Starting a new game.")
                self.start_new_game()
        else:
            self.start_new_game()
        
        # Main game loop
        while self.running:
            try:
                current_location = get_current_location(self.world)
                print(f"\nYou are in the {current_location}.")
                print(get_player_status(self.player))
                
                action = input("What would you like to do? ")
                self.process_input(action)
            except KeyboardInterrupt:
                print("\nGame interrupted. Saving progress...")
                self.save_current_game()
                print("Thanks for playing! Your progress has been saved.")
                self.running = False
            except Exception as e:
                print(f"An error occurred: {e}")
                print("The game will continue, but some data may be lost.")
                # Optionally, save the game here to prevent data loss

