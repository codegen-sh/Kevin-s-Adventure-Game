"""
GameEngine class for Kevin's Adventure Game.
Handles the main game loop and coordinates between Player, World, and other systems.
"""
from typing import Dict, List, Any, Optional, Callable
import sys
from game.player_class import Player
from game.world_class import World
from game.items import use_item, get_item_description
from game.weather import apply_weather_effects, describe_weather, weather_forecast
from utils.save_load import save_game, load_game, list_save_files
from utils.text_formatting import print_help, print_welcome_message


class GameEngine:
    """
    Main game engine that coordinates all game systems and handles the game loop.
    
    Attributes:
        player (Player): The current player
        world (World): The game world
        running (bool): Whether the game is currently running
        commands (Dict[str, Callable]): Dictionary of available commands
        debug_mode (bool): Whether debug mode is enabled
    """
    
    def __init__(self, player: Optional[Player] = None, world: Optional[World] = None) -> None:
        """
        Initialize the game engine.
        
        Args:
            player: Optional player object (will create default if None)
            world: Optional world object (will create default if None)
        """
        self.player = player if player is not None else Player("Kevin")
        self.world = world if world is not None else World()
        self.running = False
        self.debug_mode = False
        
        # Initialize command system
        self.commands: Dict[str, Callable] = self._initialize_commands()
        
        # Ensure player is in a valid location
        self._validate_player_location()
    
    def _initialize_commands(self) -> Dict[str, Callable]:
        """
        Initialize the command system with available commands.
        
        Returns:
            Dictionary mapping command names to their handler functions
        """
        return {
            # Movement commands
            "go": self._handle_go,
            "move": self._handle_go,
            "travel": self._handle_go,
            
            # Interaction commands
            "look": self._handle_look,
            "examine": self._handle_examine,
            "take": self._handle_take,
            "drop": self._handle_drop,
            "use": self._handle_use,
            "inventory": self._handle_inventory,
            "inv": self._handle_inventory,
            
            # Information commands
            "status": self._handle_status,
            "help": self._handle_help,
            "weather": self._handle_weather,
            "time": self._handle_time,
            "locations": self._handle_locations,
            
            # Game management commands
            "save": self._handle_save,
            "load": self._handle_load,
            "quit": self._handle_quit,
            "exit": self._handle_quit,
            
            # Location-specific commands
            "explore": self._handle_explore,
            "interact": self._handle_interact,
            
            # Debug commands (only available in debug mode)
            "debug": self._handle_debug,
            "teleport": self._handle_teleport,
            "give": self._handle_give_item,
            "heal": self._handle_heal,
        }
    
    def _validate_player_location(self) -> None:
        """Ensure the player is in a valid location."""
        if self.player.location not in self.world.get_all_location_names():
            print(f"Warning: Player location '{self.player.location}' not found. Moving to Village.")
            self.player.move_to("Village")
            self.world.current_location = "Village"
    
    def start_game(self) -> None:
        """Start the main game loop."""
        print_welcome_message()
        
        # Offer to load a saved game
        if self._offer_load_game():
            return
        
        self.running = True
        
        # Enter the current location
        self.world.interact_with_current_location(self.player)
        
        # Main game loop
        while self.running:
            self._game_loop_iteration()
        
        print("Thanks for playing Kevin's Adventure Game!")
    
    def _offer_load_game(self) -> bool:
        """
        Offer the player to load a saved game.
        
        Returns:
            True if a game was loaded and should continue, False to start new game
        """
        load_option = input("Do you want to load a saved game? (y/n): ").lower().strip()
        if load_option == 'y':
            save_files = list_save_files()
            if save_files:
                print("Available save files:")
                for i, file in enumerate(save_files, 1):
                    print(f"{i}. {file}")
                
                try:
                    choice = int(input("Enter the number of the save file to load: "))
                    if 1 <= choice <= len(save_files):
                        player_data, world_data = load_game(save_files[choice - 1])
                        if player_data and world_data:
                            # Convert loaded data to class instances
                            self.player = Player.from_dict(player_data)
                            self.world = World.from_dict(world_data)
                            self._validate_player_location()
                            print("Game loaded successfully!")
                            self.running = True
                            self.world.interact_with_current_location(self.player)
                            
                            # Continue with loaded game
                            while self.running:
                                self._game_loop_iteration()
                            return True
                        else:
                            print("Failed to load game. Starting a new game.")
                    else:
                        print("Invalid choice. Starting a new game.")
                except (ValueError, IndexError):
                    print("Invalid input. Starting a new game.")
            else:
                print("No save files found. Starting a new game.")
        
        return False
    
    def _game_loop_iteration(self) -> None:
        """Execute one iteration of the game loop."""
        try:
            # Show current location
            current_location = self.world.get_current_location_name()
            print(f"\n=== {current_location} ===")
            
            # Show player status
            print(self.player.get_status())
            
            # Get player input
            action = input("\nWhat would you like to do? ").strip().lower()
            
            if not action:
                print("Please enter a command. Type 'help' for available commands.")
                return
            
            # Process the command
            self._process_command(action)
            
        except KeyboardInterrupt:
            print("\n\nGame interrupted. Saving...")
            self._handle_save()
            self.running = False
        except Exception as e:
            if self.debug_mode:
                print(f"Error: {e}")
                import traceback
                traceback.print_exc()
            else:
                print("Something went wrong. Please try again.")
    
    def _process_command(self, action: str) -> None:
        """
        Process a player command.
        
        Args:
            action: The command string entered by the player
        """
        # Split command into parts
        parts = action.split()
        if not parts:
            return
        
        command = parts[0].lower()
        args = parts[1:] if len(parts) > 1 else []
        
        # Check for direct command match
        if command in self.commands:
            # Check debug commands
            if command in ["debug", "teleport", "give", "heal"] and not self.debug_mode:
                print("Unknown command. Type 'help' for available commands.")
                return
            
            try:
                self.commands[command](args)
            except Exception as e:
                if self.debug_mode:
                    print(f"Command error: {e}")
                else:
                    print("Command failed. Please try again.")
        else:
            # Try location-specific actions
            if self.world.perform_location_action(action, self.player):
                return
            
            # Try partial command matching
            matching_commands = [cmd for cmd in self.commands.keys() if cmd.startswith(command)]
            if len(matching_commands) == 1:
                try:
                    self.commands[matching_commands[0]](args)
                except Exception as e:
                    if self.debug_mode:
                        print(f"Command error: {e}")
                    else:
                        print("Command failed. Please try again.")
            elif len(matching_commands) > 1:
                print(f"Ambiguous command. Did you mean: {', '.join(matching_commands)}?")
            else:
                print("Unknown command. Type 'help' for available commands.")
    
    # Command handlers
    def _handle_go(self, args: List[str]) -> None:
        """Handle movement commands."""
        if not args:
            available = self.world.get_available_locations()
            if available:
                print(f"You can go to: {', '.join(available)}")
            else:
                print("There's nowhere to go from here.")
            return
        
        destination = " ".join(args).title()
        if self.world.change_location(destination, self.player):
            # Apply weather effects when moving
            apply_weather_effects(self.player.to_dict(), self.world.to_dict())
        else:
            print(f"You can't go to '{destination}' from here.")
    
    def _handle_look(self, args: List[str]) -> None:
        """Handle look command."""
        if args:
            # Look at specific item or location
            target = " ".join(args).lower()
            current_loc = self.world.get_current_location_obj()
            if current_loc and current_loc.has_item(target):
                print(get_item_description(target))
            else:
                print(f"You don't see '{target}' here.")
        else:
            # Look around current location
            current_loc = self.world.get_current_location_obj()
            if current_loc:
                print(current_loc.get_full_description())
                print(f"\nWeather: {describe_weather(self.world.to_dict())}")
            else:
                print("You are in an unknown location.")
    
    def _handle_examine(self, args: List[str]) -> None:
        """Handle examine command."""
        if not args:
            print("What would you like to examine?")
            return
        
        item = " ".join(args).lower()
        
        # Check player inventory
        if self.player.has_item(item):
            print(f"In your inventory: {get_item_description(item)}")
            return
        
        # Check current location
        current_loc = self.world.get_current_location_obj()
        if current_loc and current_loc.has_item(item):
            print(get_item_description(item))
        else:
            print(f"You don't see '{item}' here.")
    
    def _handle_take(self, args: List[str]) -> None:
        """Handle take command."""
        if not args:
            current_loc = self.world.get_current_location_obj()
            if current_loc and current_loc.items:
                print(f"Available items: {', '.join(current_loc.items)}")
            else:
                print("There are no items to take here.")
            return
        
        item = " ".join(args).lower()
        current_loc = self.world.get_current_location_obj()
        
        if current_loc and current_loc.has_item(item):
            if current_loc.remove_item(item):
                self.player.add_item(item)
        else:
            print(f"There's no '{item}' here to take.")
    
    def _handle_drop(self, args: List[str]) -> None:
        """Handle drop command."""
        if not args:
            if self.player.inventory:
                print(f"You can drop: {', '.join(self.player.inventory)}")
            else:
                print("Your inventory is empty.")
            return
        
        item = " ".join(args).lower()
        if self.player.remove_item(item):
            current_loc = self.world.get_current_location_obj()
            if current_loc:
                current_loc.add_item(item)
    
    def _handle_use(self, args: List[str]) -> None:
        """Handle use command."""
        if not args:
            if self.player.inventory:
                print(f"You can use: {', '.join(self.player.inventory)}")
            else:
                print("You have no items to use.")
            return
        
        item = " ".join(args).lower()
        if self.player.has_item(item):
            # Use the existing item system
            player_dict = self.player.to_dict()
            world_dict = self.world.to_dict()
            
            if use_item(player_dict, item, world_dict):
                # Update player and world from the modified dictionaries
                self.player = Player.from_dict(player_dict)
                self.world = World.from_dict(world_dict)
        else:
            print(f"You don't have '{item}' in your inventory.")
    
    def _handle_inventory(self, args: List[str]) -> None:
        """Handle inventory command."""
        if self.player.inventory:
            print(f"Inventory: {', '.join(self.player.inventory)}")
            if args and args[0].lower() in ["detail", "details"]:
                print("\nItem details:")
                for item in self.player.inventory:
                    print(f"- {item}: {get_item_description(item)}")
        else:
            print("Your inventory is empty.")
    
    def _handle_status(self, args: List[str]) -> None:
        """Handle status command."""
        print(self.player.get_status())
        print(f"Location: {self.world.get_current_location_name()}")
        print(f"Weather: {self.world.get_current_weather()}")
        print(f"Time: {self.world.get_time_of_day()}")
    
    def _handle_help(self, args: List[str]) -> None:
        """Handle help command."""
        if args and args[0].lower() == "commands":
            print("Available commands:")
            basic_commands = ["go", "look", "take", "drop", "use", "inventory", "status", "help", "save", "quit"]
            for cmd in basic_commands:
                print(f"  {cmd}")
            if self.debug_mode:
                print("Debug commands:")
                debug_commands = ["debug", "teleport", "give", "heal"]
                for cmd in debug_commands:
                    print(f"  {cmd}")
        else:
            print_help()
    
    def _handle_weather(self, args: List[str]) -> None:
        """Handle weather command."""
        if args and args[0].lower() == "forecast":
            print(weather_forecast(self.world.to_dict()))
        else:
            print(describe_weather(self.world.to_dict()))
    
    def _handle_time(self, args: List[str]) -> None:
        """Handle time command."""
        if args and args[0].lower() == "advance":
            if self.debug_mode:
                new_time = self.world.advance_time()
                print(f"Time advanced to: {new_time}")
            else:
                print("You can't control time!")
        else:
            print(f"Current time: {self.world.get_time_of_day()}")
    
    def _handle_locations(self, args: List[str]) -> None:
        """Handle locations command."""
        available = self.world.get_available_locations()
        all_locations = self.world.get_all_location_names()
        
        print(f"Current location: {self.world.get_current_location_name()}")
        print(f"Available destinations: {', '.join(available) if available else 'None'}")
        
        if args and args[0].lower() == "all":
            print(f"All locations: {', '.join(all_locations)}")
    
    def _handle_save(self, args: List[str]) -> None:
        """Handle save command."""
        filename = args[0] if args else None
        if save_game(self.player.to_dict(), self.world.to_dict(), filename):
            print("Game saved successfully!")
        else:
            print("Failed to save game.")
    
    def _handle_load(self, args: List[str]) -> None:
        """Handle load command."""
        if args:
            filename = args[0]
            player_data, world_data = load_game(filename)
            if player_data and world_data:
                self.player = Player.from_dict(player_data)
                self.world = World.from_dict(world_data)
                self._validate_player_location()
                print("Game loaded successfully!")
                self.world.interact_with_current_location(self.player)
            else:
                print("Failed to load game.")
        else:
            save_files = list_save_files()
            if save_files:
                print("Available save files:")
                for i, file in enumerate(save_files, 1):
                    print(f"{i}. {file}")
            else:
                print("No save files found.")
    
    def _handle_quit(self, args: List[str]) -> None:
        """Handle quit command."""
        save_choice = input("Do you want to save before quitting? (y/n): ").lower().strip()
        if save_choice == 'y':
            self._handle_save([])
        
        print("Thanks for playing!")
        self.running = False
    
    def _handle_explore(self, args: List[str]) -> None:
        """Handle explore command."""
        current_loc = self.world.get_current_location_obj()
        if current_loc:
            # Trigger location-specific exploration
            if hasattr(current_loc, 'get_random_event'):
                event = current_loc.get_random_event(self.player, self.world)
                if event:
                    print(event)
                else:
                    print("You explore the area but find nothing of interest.")
            else:
                print("You explore the area but find nothing of interest.")
        else:
            print("There's nothing to explore here.")
    
    def _handle_interact(self, args: List[str]) -> None:
        """Handle interact command."""
        self.world.interact_with_current_location(self.player)
    
    # Debug commands
    def _handle_debug(self, args: List[str]) -> None:
        """Handle debug command."""
        if args and args[0].lower() == "off":
            self.debug_mode = False
            print("Debug mode disabled.")
        else:
            self.debug_mode = True
            print("Debug mode enabled.")
            print("Available debug commands: teleport, give, heal")
    
    def _handle_teleport(self, args: List[str]) -> None:
        """Handle teleport command (debug only)."""
        if not args:
            all_locations = self.world.get_all_location_names()
            print(f"Available locations: {', '.join(all_locations)}")
            return
        
        destination = " ".join(args).title()
        if destination in self.world.get_all_location_names():
            self.world.current_location = destination
            self.player.move_to(destination)
            self.world.interact_with_current_location(self.player)
        else:
            print(f"Location '{destination}' does not exist.")
    
    def _handle_give_item(self, args: List[str]) -> None:
        """Handle give command (debug only)."""
        if not args:
            print("Usage: give <item_name>")
            return
        
        item = " ".join(args).lower()
        self.player.add_item(item)
    
    def _handle_heal(self, args: List[str]) -> None:
        """Handle heal command (debug only)."""
        if args:
            try:
                amount = int(args[0])
                self.player.heal(amount)
            except ValueError:
                print("Usage: heal <amount>")
        else:
            self.player.heal(self.player.max_health - self.player.health)
    
    def stop_game(self) -> None:
        """Stop the game loop."""
        self.running = False
    
    def get_game_state(self) -> Dict[str, Any]:
        """
        Get the current game state.
        
        Returns:
            Dictionary containing current game state
        """
        return {
            "player": self.player.to_dict(),
            "world": self.world.to_dict(),
            "running": self.running,
            "debug_mode": self.debug_mode
        }
    
    def set_game_state(self, state: Dict[str, Any]) -> None:
        """
        Set the game state from a dictionary.
        
        Args:
            state: Dictionary containing game state
            
        Raises:
            ValueError: If state is invalid
        """
        if not isinstance(state, dict):
            raise ValueError("State must be a dictionary")
        
        if "player" in state:
            self.player = Player.from_dict(state["player"])
        if "world" in state:
            self.world = World.from_dict(state["world"])
        if "running" in state:
            self.running = state["running"]
        if "debug_mode" in state:
            self.debug_mode = state["debug_mode"]
        
        self._validate_player_location()


# Convenience function for backward compatibility
def run_game() -> None:
    """
    Run the game using the new GameEngine.
    This function provides backward compatibility.
    """
    engine = GameEngine()
    engine.start_game()


# Function to create and run game with custom player/world
def run_game_with_state(player_data: Optional[Dict[str, Any]] = None, 
                       world_data: Optional[Dict[str, Any]] = None) -> None:
    """
    Run the game with custom player and world state.
    
    Args:
        player_data: Optional player data dictionary
        world_data: Optional world data dictionary
    """
    player = None
    world = None
    
    if player_data:
        player = Player.from_dict(player_data)
    if world_data:
        world = World.from_dict(world_data)
    
    engine = GameEngine(player, world)
    engine.start_game()

