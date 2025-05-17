"""
Game module for Kevin's Adventure Game.
Contains the Game class that serves as the main controller.
"""
import random
from typing import Dict, List, Optional, Tuple

from src.game.item import ItemRegistry
from src.game.player import Player
from src.game.weather import Weather
from src.game.world import World
from src.utils.save_load import SaveManager


class Game:
    """
    Main game controller class.
    Manages the game loop and coordinates between player, world, and other systems.
    """

    def __init__(self):
        """Initialize a new game."""
        self.player = None
        self.world = World()
        self.weather = Weather()
        self.item_registry = ItemRegistry()
        self.save_manager = SaveManager()
        self.running = False

    def initialize(self) -> None:
        """Initialize the game world and systems."""
        self._initialize_items()
        self.world.initialize_default_world()

    def start_new_game(self, player_name: str) -> None:
        """
        Start a new game with a new player.

        Args:
            player_name: The name of the player
        """
        self.player = Player(player_name)
        self.world = World()
        self.weather = Weather()
        self.initialize()
        self.running = True

    def load_game(self, save_file: str) -> bool:
        """
        Load a game from a save file.

        Args:
            save_file: The name of the save file

        Returns:
            True if the game was loaded successfully, False otherwise
        """
        result = self.save_manager.load_game(save_file)
        if result:
            self.player, self.world, self.weather = result
            self.running = True
            return True
        return False

    def save_game(self) -> bool:
        """
        Save the current game state.

        Returns:
            True if the game was saved successfully, False otherwise
        """
        if not self.player:
            return False
        return self.save_manager.save_game(self.player, self.world, self.weather)

    def quit_game(self) -> None:
        """Quit the game, saving the current state."""
        self.save_game()
        self.running = False

    def process_command(self, command: str) -> None:
        """
        Process a player command.

        Args:
            command: The command to process
        """
        command = command.lower().strip()
        
        if command == "quit":
            self.quit_game()
        elif command == "help":
            self._print_help()
        elif command.startswith("move "):
            self._handle_move_command(command[5:])
        elif command == "look":
            self._handle_look_command()
        elif command == "inventory":
            self._handle_inventory_command()
        elif command.startswith("pickup "):
            self._handle_pickup_command(command[7:])
        elif command.startswith("drop "):
            self._handle_drop_command(command[5:])
        elif command.startswith("use "):
            self._handle_use_command(command[4:])
        elif command.startswith("examine "):
            self._handle_examine_command(command[8:])
        elif command == "status":
            self._handle_status_command()
        elif command == "interact":
            self._handle_interact_command()
        elif command == "weather":
            self._handle_weather_command()
        else:
            print("Unknown command. Type 'help' for a list of commands.")

    def _print_help(self) -> None:
        """Print the help message with available commands."""
        help_text = """
Available commands:
- move [location]: Move to a new location
- look: Examine your surroundings
- inventory: Check your inventory
- pickup [item]: Pick up an item
- drop [item]: Drop an item from your inventory
- use [item]: Use an item
- examine [item]: Get a description of an item
- status: Check your current status
- interact: Interact with your current location
- weather: Check the current weather
- help: Show this help message
- quit: Save and exit the game
        """
        print(help_text.strip())

    def _handle_move_command(self, location: str) -> None:
        """
        Handle the 'move' command.

        Args:
            location: The location to move to
        """
        if not location:
            print("Move where? Type 'move [location]'.")
            return
            
        if self.world.change_location(location):
            self.player.move(location)
            current_location = self.world.get_current_location()
            print(f"You are now in {current_location.name}.")
            print(current_location.description)
        else:
            print(f"You can't go to {location} from here.")
            print(f"Available locations: {', '.join(self.world.get_available_locations())}")

    def _handle_look_command(self) -> None:
        """Handle the 'look' command."""
        current_location = self.world.get_current_location()
        print(current_location.description)
        
        # Show items in the location
        if current_location.items:
            print(f"You can see: {', '.join(current_location.items)}")
        else:
            print("There's nothing of interest here.")
            
        # Show available exits
        if current_location.connections:
            print(f"Exits: {', '.join(current_location.connections)}")
        else:
            print("There are no obvious exits.")

    def _handle_inventory_command(self) -> None:
        """Handle the 'inventory' command."""
        if self.player.inventory:
            print(f"Inventory: {', '.join(self.player.inventory)}")
        else:
            print("Your inventory is empty.")

    def _handle_pickup_command(self, item: str) -> None:
        """
        Handle the 'pickup' command.

        Args:
            item: The item to pick up
        """
        if not item:
            print("Pick up what? Type 'pickup [item]'.")
            return
            
        current_location = self.world.get_current_location()
        if item in current_location.items:
            current_location.remove_item(item)
            self.player.add_item(item)
        else:
            print(f"There's no {item} here to pick up.")

    def _handle_drop_command(self, item: str) -> None:
        """
        Handle the 'drop' command.

        Args:
            item: The item to drop
        """
        if not item:
            print("Drop what? Type 'drop [item]'.")
            return
            
        if self.player.remove_item(item):
            current_location = self.world.get_current_location()
            current_location.add_item(item)

    def _handle_use_command(self, item: str) -> None:
        """
        Handle the 'use' command.

        Args:
            item: The item to use
        """
        if not item:
            print("Use what? Type 'use [item]'.")
            return
            
        if not self.player.has_item(item):
            print(f"You don't have {item} in your inventory.")
            return
            
        item_obj = self.item_registry.get_item(item)
        if item_obj:
            item_obj.use(self.player, self.world)
        else:
            print(f"You're not sure how to use the {item}.")

    def _handle_examine_command(self, item: str) -> None:
        """
        Handle the 'examine' command.

        Args:
            item: The item to examine
        """
        if not item:
            print("Examine what? Type 'examine [item]'.")
            return
            
        description = self.item_registry.get_description(item)
        print(description)

    def _handle_status_command(self) -> None:
        """Handle the 'status' command."""
        print(self.player.get_status())

    def _handle_interact_command(self) -> None:
        """Handle the 'interact' command."""
        current_location = self.world.get_current_location()
        current_location.enter(self.player, self.world)

    def _handle_weather_command(self) -> None:
        """Handle the 'weather' command."""
        print(self.weather.describe_weather())
        self.weather.apply_weather_effects(self.player)
        print(self.weather.forecast())

    def _initialize_items(self) -> None:
        """Initialize the item registry with all game items."""
        # This will be implemented after we create the specific item classes
        pass

