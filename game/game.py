"""
Game module for the game.
"""
from game.actions import perform_action
from game.player import Player, create_player, get_player_status
from game.world import World, get_current_location, initialize_world
from utils.save_load import list_save_files, load_game, save_game
from utils.text_formatting import print_help, print_welcome_message


class Game:
    """Class representing the game."""
    
    def __init__(self, player_name=None):
        """Initialize the game."""
        self.player = None
        self.world = None
        self.player_name = player_name or "Kevin"
        self.running = False
    
    def start(self):
        """Start the game."""
        print_welcome_message()
        
        # Add load game option
        load_option = input("Do you want to load a saved game? (y/n): ").lower()
        if load_option == 'y':
            save_files = list_save_files()
            if save_files:
                print("Available save files:")
                for i, file in enumerate(save_files, 1):
                    print(f"{i}. {file}")
                choice = int(input("Enter the number of the save file to load: "))
                self.player, self.world = load_game(save_files[choice - 1])
                if self.player is None or self.world is None:
                    print("Failed to load game. Starting a new game.")
                    self._initialize_new_game()
            else:
                print("No save files found. Starting a new game.")
                self._initialize_new_game()
        else:
            self._initialize_new_game()
        
        self.running = True
        self.game_loop()
    
    def _initialize_new_game(self):
        """Initialize a new game."""
        if self.player_name:
            # Use the Player class for new games
            self.player = Player(self.player_name)
            self.world = World()
        else:
            # Use the legacy functions for backward compatibility
            self.player = create_player("Kevin")
            self.world = initialize_world()
    
    def game_loop(self):
        """Run the game loop."""
        while self.running:
            current_location = get_current_location(self.world)
            print(f"\nYou are in the {current_location}.")
            print(get_player_status(self.player))
            
            action = input("What would you like to do? ").lower()
            
            if action == "quit":
                save_game(self.player, self.world)
                print("Thanks for playing! Your progress has been saved.")
                self.running = False
            elif action == "help":
                print_help()
            else:
                result = perform_action(self.player, self.world, action)
                if result == "QUIT":
                    self.running = False
    
    def stop(self):
        """Stop the game."""
        self.running = False

