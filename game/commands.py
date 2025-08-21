"""
Commands module for Kevin's Adventure Game.
Contains the Command class hierarchy and command registry.
"""
from game.exceptions import InvalidCommandError, InvalidItemError, InvalidLocationError
from game.player import add_item_to_inventory, get_player_status, remove_item_from_inventory
from game.world import (
    change_location,
    get_available_locations,
    get_current_location,
    get_location_description,
    interact_with_location
)
from utils.text_formatting import print_help


class Command:
    """
    Base class for all commands.
    
    Attributes:
        name (str): The name of the command
        aliases (list): List of alternative names for the command
        help_text (str): Help text for the command
    """
    
    def __init__(self, name, aliases=None, help_text=""):
        """
        Initialize a new Command instance.
        
        Args:
            name (str): The name of the command
            aliases (list, optional): List of alternative names for the command. Defaults to None.
            help_text (str, optional): Help text for the command. Defaults to "".
        """
        self.name = name
        self.aliases = aliases or []
        self.help_text = help_text
    
    def matches(self, command_name):
        """
        Check if the command matches a given name.
        
        Args:
            command_name (str): The name to check
            
        Returns:
            bool: True if the command matches, False otherwise
        """
        return command_name.lower() == self.name.lower() or command_name.lower() in [alias.lower() for alias in self.aliases]
    
    def execute(self, game_state, args):
        """
        Execute the command.
        
        Args:
            game_state: The current game state
            args (list): List of command arguments
            
        Returns:
            bool: True if the command was executed successfully, False otherwise
        """
        raise NotImplementedError("Subclasses must implement execute()")


class MoveCommand(Command):
    """Command for moving to a new location."""
    
    def __init__(self):
        super().__init__(
            name="move",
            aliases=["go", "travel"],
            help_text="Move to a new location. Usage: move [location]"
        )
    
    def execute(self, game_state, args):
        if not args:
            print("Move where? Available locations:")
            for location in get_available_locations(game_state.world):
                print(f"- {location}")
            return True
        
        new_location = args[0].capitalize()
        available_locations = get_available_locations(game_state.world)
        
        if new_location in available_locations:
            if change_location(game_state.world, new_location):
                game_state.player.move_to(new_location)
                return True
        else:
            print(f"You can't go to {new_location} from here.")
            print("Available locations:")
            for location in available_locations:
                print(f"- {location}")
        
        return False


class LookCommand(Command):
    """Command for looking around the current location."""
    
    def __init__(self):
        super().__init__(
            name="look",
            aliases=["examine", "observe"],
            help_text="Look around the current location. Usage: look"
        )
    
    def execute(self, game_state, args):
        current_location = get_current_location(game_state.world)
        description = get_location_description(game_state.world, current_location)
        print(description)
        
        # Show available exits
        print("\nAvailable exits:")
        for location in get_available_locations(game_state.world):
            print(f"- {location}")
        
        # Show items in the location
        items = game_state.world.to_dict()["locations"][current_location].get("items", [])
        if items:
            print("\nYou can see:")
            for item in items:
                print(f"- {item}")
        
        return True


class InventoryCommand(Command):
    """Command for checking the player's inventory."""
    
    def __init__(self):
        super().__init__(
            name="inventory",
            aliases=["inv", "items"],
            help_text="Check your inventory. Usage: inventory"
        )
    
    def execute(self, game_state, args):
        if not game_state.player.inventory:
            print("Your inventory is empty.")
        else:
            print("Your inventory contains:")
            for item in game_state.player.inventory:
                print(f"- {item}")
        
        return True


class PickupCommand(Command):
    """Command for picking up an item."""
    
    def __init__(self):
        super().__init__(
            name="pickup",
            aliases=["take", "get"],
            help_text="Pick up an item. Usage: pickup [item]"
        )
    
    def execute(self, game_state, args):
        if not args:
            print("Pick up what?")
            return False
        
        item = args[0].lower()
        current_location = get_current_location(game_state.world)
        location_items = game_state.world.to_dict()["locations"][current_location].get("items", [])
        
        if item in location_items:
            add_item_to_inventory(game_state.player, item)
            location_items.remove(item)
            return True
        else:
            print(f"There is no {item} here.")
            return False


class DropCommand(Command):
    """Command for dropping an item."""
    
    def __init__(self):
        super().__init__(
            name="drop",
            aliases=["discard", "remove"],
            help_text="Drop an item from your inventory. Usage: drop [item]"
        )
    
    def execute(self, game_state, args):
        if not args:
            print("Drop what?")
            return False
        
        item = args[0].lower()
        return remove_item_from_inventory(game_state.player, item)


class UseCommand(Command):
    """Command for using an item."""
    
    def __init__(self):
        super().__init__(
            name="use",
            aliases=["utilize", "employ"],
            help_text="Use an item from your inventory. Usage: use [item]"
        )
    
    def execute(self, game_state, args):
        if not args:
            print("Use what?")
            return False
        
        item = args[0].lower()
        if item not in game_state.player.inventory:
            print(f"You don't have {item} in your inventory.")
            return False
        
        # Handle different items
        if item == "bread" or item == "berries" or item == "mushrooms":
            from game.player import heal_player
            heal_player(game_state.player, 10)
            game_state.player.inventory.remove(item)
            print(f"You ate the {item} and recovered some health.")
            return True
        elif item == "map":
            print("You look at the map. It shows your current location and nearby areas.")
            print("Available locations:")
            for location in game_state.world.get_all_location_names():
                print(f"- {location}")
            return True
        elif item == "torch":
            print("You light the torch. It illuminates the area around you.")
            return True
        else:
            print(f"You're not sure how to use the {item}.")
            return False


class ExamineItemCommand(Command):
    """Command for examining an item."""
    
    def __init__(self):
        super().__init__(
            name="examine",
            aliases=["inspect", "look at"],
            help_text="Examine an item. Usage: examine [item]"
        )
    
    def execute(self, game_state, args):
        if not args:
            print("Examine what?")
            return False
        
        item = args[0].lower()
        
        # Check if the item is in the player's inventory
        if item in game_state.player.inventory:
            # Item descriptions
            descriptions = {
                "map": "A weathered map showing the village, forest, cave, and mountain.",
                "bread": "A fresh loaf of bread. It smells delicious.",
                "stick": "A sturdy wooden stick. Could be useful for various tasks.",
                "berries": "Plump, juicy berries. They look safe to eat.",
                "torch": "A wooden torch that can be lit to provide light in dark areas.",
                "gemstone": "A sparkling gemstone that catches the light beautifully.",
                "rope": "A coil of strong rope. Useful for climbing or tying things.",
                "pickaxe": "A sturdy pickaxe for mining or breaking rocks.",
                "sword": "A sharp, well-crafted sword. Useful for protection.",
                "mushrooms": "Edible mushrooms that can restore some health.",
                "mysterious_package": "A sealed package addressed to the mountain hermit.",
                "unicorn_hair": "A shimmering strand of unicorn hair. It seems magical.",
                "dragon_scale": "A tough, iridescent dragon scale. It's warm to the touch."
            }
            
            if item in descriptions:
                print(descriptions[item])
                return True
            else:
                print(f"It's a {item}. Nothing special about it.")
                return True
        else:
            # Check if the item is in the current location
            current_location = get_current_location(game_state.world)
            location_items = game_state.world.to_dict()["locations"][current_location].get("items", [])
            
            if item in location_items:
                print(f"You see a {item}. You can pick it up with 'pickup {item}'.")
                return True
            else:
                print(f"You don't see any {item} here.")
                return False


class StatusCommand(Command):
    """Command for checking the player's status."""
    
    def __init__(self):
        super().__init__(
            name="status",
            aliases=["stats", "health"],
            help_text="Check your current status. Usage: status"
        )
    
    def execute(self, game_state, args):
        print(get_player_status(game_state.player))
        return True


class InteractCommand(Command):
    """Command for interacting with the current location."""
    
    def __init__(self):
        super().__init__(
            name="interact",
            aliases=["engage", "explore"],
            help_text="Interact with your current location. Usage: interact"
        )
    
    def execute(self, game_state, args):
        interact_with_location(game_state.world, game_state.player)
        return True


class HelpCommand(Command):
    """Command for displaying help information."""
    
    def __init__(self):
        super().__init__(
            name="help",
            aliases=["?", "commands"],
            help_text="Display help information. Usage: help"
        )
    
    def execute(self, game_state, args):
        print_help()
        return True


class QuitCommand(Command):
    """Command for quitting the game."""
    
    def __init__(self):
        super().__init__(
            name="quit",
            aliases=["exit", "bye"],
            help_text="Save and quit the game. Usage: quit"
        )
    
    def execute(self, game_state, args):
        from game.game_state import save_game_state
        save_game_state(game_state)
        print("Thanks for playing! Your progress has been saved.")
        return True


# Command registry
class CommandRegistry:
    """
    Registry for all available commands.
    
    Attributes:
        commands (list): List of Command instances
    """
    
    def __init__(self):
        """Initialize a new CommandRegistry instance."""
        self.commands = []
    
    def register_command(self, command):
        """
        Register a command.
        
        Args:
            command (Command): The command to register
        """
        self.commands.append(command)
    
    def get_command(self, command_name):
        """
        Get a command by name.
        
        Args:
            command_name (str): The name of the command
            
        Returns:
            Command: The command instance, or None if not found
        """
        for command in self.commands:
            if command.matches(command_name):
                return command
        return None
    
    def execute_command(self, game_state, command_str):
        """
        Execute a command.
        
        Args:
            game_state: The current game state
            command_str (str): The command string to execute
            
        Returns:
            bool: True if the command was executed successfully, False otherwise
        """
        parts = command_str.split()
        command_name = parts[0] if parts else ""
        args = parts[1:] if len(parts) > 1 else []
        
        command = self.get_command(command_name)
        if command:
            try:
                return command.execute(game_state, args)
            except InvalidCommandError as e:
                print(e.message)
                return False
            except InvalidLocationError as e:
                print(e.message)
                return False
            except InvalidItemError as e:
                print(e.message)
                return False
            except Exception as e:
                print(f"An error occurred: {str(e)}")
                return False
        else:
            print(f"Unknown command: {command_name}. Type 'help' for a list of commands.")
            return False


# Create and initialize the command registry
def create_command_registry():
    """
    Create and initialize the command registry.
    
    Returns:
        CommandRegistry: The initialized command registry
    """
    registry = CommandRegistry()
    
    # Register commands
    registry.register_command(MoveCommand())
    registry.register_command(LookCommand())
    registry.register_command(InventoryCommand())
    registry.register_command(PickupCommand())
    registry.register_command(DropCommand())
    registry.register_command(UseCommand())
    registry.register_command(ExamineItemCommand())
    registry.register_command(StatusCommand())
    registry.register_command(InteractCommand())
    registry.register_command(HelpCommand())
    registry.register_command(QuitCommand())
    
    return registry

