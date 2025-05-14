from game.actions import perform_action
from game.player import Player, create_player, get_player_status
from game.state import GameState
from game.weather import Weather
from game.world import World, create_world, get_current_location, initialize_world
from utils.save_load import list_save_files, load_game, save_game
from utils.text_formatting import print_help, print_welcome_message


class Game:
    """
    Main game class that manages the game loop and state.
    
    This class handles the game initialization, loading/saving,
    and the main game loop.
    """
    
    def __init__(self):
        """Initialize a new Game."""
        self.player = None
        self.world = None
        self.game_state = None
        self.weather = None
    
    def initialize_new_game(self, player_name="Kevin"):
        """
        Initialize a new game.
        
        Args:
            player_name (str, optional): The name of the player
        """
        self.player = Player(player_name)
        self.world = create_world()
        self.game_state = GameState()
        self.weather = Weather()
        
        # Add the weather to the world for easy access
        self.world.weather = self.weather
        self.world.game_state = self.game_state
    
    def load_saved_game(self, save_file):
        """
        Load a saved game.
        
        Args:
            save_file (str): The name of the save file
            
        Returns:
            bool: True if the game was loaded successfully, False otherwise
        """
        player_dict, world_dict = load_game(save_file)
        
        if player_dict is None or world_dict is None:
            return False
        
        # Convert the dictionaries to objects
        self.player = Player(player_dict["name"])
        self.player.health = player_dict["health"]
        self.player.inventory = player_dict["inventory"]
        self.player.location = player_dict["location"]
        self.player.gold = player_dict["gold"]
        
        self.world = create_world()
        self.world.current_location = world_dict["current_location"]
        
        # Initialize game state and weather
        self.game_state = GameState()
        self.weather = Weather()
        
        # Add the weather and game state to the world for easy access
        self.world.weather = self.weather
        self.world.game_state = self.game_state
        
        return True
    
    def save_current_game(self):
        """Save the current game."""
        # Convert objects to dictionaries for saving
        player_dict = {
            "name": self.player.name,
            "health": self.player.health,
            "inventory": self.player.inventory,
            "location": self.player.location,
            "gold": self.player.gold
        }
        
        world_dict = {
            "current_location": self.world.current_location,
            "locations": {}
        }
        
        for name, location in self.world.locations.items():
            world_dict["locations"][name] = {
                "description": location.description,
                "connections": location.connections,
                "items": location.items
            }
        
        save_game(player_dict, world_dict)
    
    def run(self):
        """Run the main game loop."""
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
                if not self.load_saved_game(save_files[choice - 1]):
                    print("Failed to load game. Starting a new game.")
                    self.initialize_new_game()
            else:
                print("No save files found. Starting a new game.")
                self.initialize_new_game()
        else:
            self.initialize_new_game()
        
        # Main game loop
        while True:
            current_location = self.world.get_current_location()
            print(f"\nYou are in the {current_location}.")
            print(self.player.get_status())
            
            action = input("What would you like to do? ").lower()
            
            if action == "quit":
                self.save_current_game()
                print("Thanks for playing! Your progress has been saved.")
                break
            elif action == "help":
                print_help()
            else:
                perform_action(self.player, self.world, action)


def main():
    """Main function to start the game."""
    game = Game()
    game.run()


# Legacy main function for backward compatibility
def legacy_main():
    """Legacy main function for backward compatibility."""
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
            player, world = load_game(save_files[choice - 1])
            if player is None or world is None:
                print("Failed to load game. Starting a new game.")
                player = create_player("Kevin")
                world = initialize_world()
        else:
            print("No save files found. Starting a new game.")
            player = create_player("Kevin")
            world = initialize_world()
    else:
        player = create_player("Kevin")
        world = initialize_world()

    while True:
        current_location = get_current_location(world)
        print(f"\nYou are in the {current_location}.")
        print(get_player_status(player))

        action = input("What would you like to do? ").lower()

        if action == "quit":
            save_game(player, world)
            print("Thanks for playing! Your progress has been saved.")
            break
        elif action == "help":
            print_help()
        else:
            perform_action(player, world, action)


if __name__ == "__main__":
    main()
