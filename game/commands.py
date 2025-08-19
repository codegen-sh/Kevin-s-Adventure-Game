"""
Commands module for Kevin's Adventure Game.
This module implements the command pattern for handling player actions.
"""
from abc import ABC, abstractmethod
from game.items import get_item, get_item_description, use_item
from game.player import add_item_to_inventory, remove_item_from_inventory
from game.world import get_available_locations, get_current_location, change_location, interact_with_location


class Command(ABC):
    """
    Abstract base class for commands.
    """
    
    @abstractmethod
    def execute(self, player, world, args):
        """
        Execute the command.
        
        Args:
            player: The player object
            world: The world object
            args (list): Command arguments
        
        Returns:
            bool: True if the command was executed successfully, False otherwise
        """
        pass


class MoveCommand(Command):
    """
    Command for moving to a new location.
    """
    
    def execute(self, player, world, args):
        """
        Execute the move command.
        
        Args:
            player: The player object
            world: The world object
            args (list): Command arguments
        
        Returns:
            bool: True if the command was executed successfully, False otherwise
        """
        if not args:
            print("Move where? Try 'move [location]'")
            return False
        
        new_location = args[0].capitalize()
        available_locations = get_available_locations(world)
        
        if new_location in available_locations:
            if change_location(world, new_location):
                player.move(new_location)
                return True
        else:
            print(f"You can't go to {new_location} from here.")
            print(f"Available locations: {', '.join(available_locations)}")
        
        return False


class LookCommand(Command):
    """
    Command for examining surroundings.
    """
    
    def execute(self, player, world, args):
        """
        Execute the look command.
        
        Args:
            player: The player object
            world: The world object
            args (list): Command arguments
        
        Returns:
            bool: True if the command was executed successfully, False otherwise
        """
        current_location = get_current_location(world)
        
        if isinstance(world, dict):
            # For backward compatibility with dictionary-based world
            location_data = world["locations"][current_location]
            print(location_data["description"])
            
            if location_data["items"]:
                print(f"You see: {', '.join(location_data['items'])}")
            
            print(f"From here, you can go to: {', '.join(location_data['connections'])}")
        else:
            # For class-based world
            location = world.get_location(current_location)
            print(location.description)
            
            if location.items:
                print(f"You see: {', '.join(location.items)}")
            
            print(f"From here, you can go to: {', '.join(location.connections)}")
        
        return True


class InventoryCommand(Command):
    """
    Command for checking inventory.
    """
    
    def execute(self, player, world, args):
        """
        Execute the inventory command.
        
        Args:
            player: The player object
            world: The world object
            args (list): Command arguments
        
        Returns:
            bool: True if the command was executed successfully, False otherwise
        """
        if isinstance(player, dict):
            # For backward compatibility with dictionary-based player
            if not player["inventory"]:
                print("Your inventory is empty.")
            else:
                print(f"Inventory: {', '.join(player['inventory'])}")
        else:
            # For class-based player
            if not player.inventory:
                print("Your inventory is empty.")
            else:
                print(f"Inventory: {', '.join(player.inventory)}")
        
        return True


class PickupCommand(Command):
    """
    Command for picking up items.
    """
    
    def execute(self, player, world, args):
        """
        Execute the pickup command.
        
        Args:
            player: The player object
            world: The world object
            args (list): Command arguments
        
        Returns:
            bool: True if the command was executed successfully, False otherwise
        """
        if not args:
            print("Pick up what? Try 'pickup [item]'")
            return False
        
        item = args[0].lower()
        current_location = get_current_location(world)
        
        if isinstance(world, dict):
            # For backward compatibility with dictionary-based world
            location_data = world["locations"][current_location]
            
            if item in location_data["items"]:
                location_data["items"].remove(item)
                add_item_to_inventory(player, item)
                return True
        else:
            # For class-based world
            location = world.get_location(current_location)
            
            if item in location.items:
                location.remove_item(item)
                add_item_to_inventory(player, item)
                return True
        
        print(f"There is no {item} here to pick up.")
        return False


class DropCommand(Command):
    """
    Command for dropping items.
    """
    
    def execute(self, player, world, args):
        """
        Execute the drop command.
        
        Args:
            player: The player object
            world: The world object
            args (list): Command arguments
        
        Returns:
            bool: True if the command was executed successfully, False otherwise
        """
        if not args:
            print("Drop what? Try 'drop [item]'")
            return False
        
        item = args[0].lower()
        current_location = get_current_location(world)
        
        if remove_item_from_inventory(player, item):
            if isinstance(world, dict):
                # For backward compatibility with dictionary-based world
                world["locations"][current_location]["items"].append(item)
            else:
                # For class-based world
                location = world.get_location(current_location)
                location.add_item(item)
            
            return True
        
        return False


class UseCommand(Command):
    """
    Command for using items.
    """
    
    def execute(self, player, world, args):
        """
        Execute the use command.
        
        Args:
            player: The player object
            world: The world object
            args (list): Command arguments
        
        Returns:
            bool: True if the command was executed successfully, False otherwise
        """
        if not args:
            print("Use what? Try 'use [item]'")
            return False
        
        item = args[0].lower()
        
        if isinstance(player, dict):
            # For backward compatibility with dictionary-based player
            if item in player["inventory"]:
                return use_item(player, world, item)
        else:
            # For class-based player
            if item in player.inventory:
                return use_item(player, world, item)
        
        print(f"You don't have {item} in your inventory.")
        return False


class ExamineCommand(Command):
    """
    Command for examining items.
    """
    
    def execute(self, player, world, args):
        """
        Execute the examine command.
        
        Args:
            player: The player object
            world: The world object
            args (list): Command arguments
        
        Returns:
            bool: True if the command was executed successfully, False otherwise
        """
        if not args:
            print("Examine what? Try 'examine [item]'")
            return False
        
        item = args[0].lower()
        
        if isinstance(player, dict):
            # For backward compatibility with dictionary-based player
            if item in player["inventory"]:
                print(get_item_description(item))
                return True
        else:
            # For class-based player
            if item in player.inventory:
                print(get_item_description(item))
                return True
        
        current_location = get_current_location(world)
        
        if isinstance(world, dict):
            # For backward compatibility with dictionary-based world
            location_data = world["locations"][current_location]
            
            if item in location_data["items"]:
                print(get_item_description(item))
                return True
        else:
            # For class-based world
            location = world.get_location(current_location)
            
            if item in location.items:
                print(get_item_description(item))
                return True
        
        print(f"There is no {item} here to examine.")
        return False


class StatusCommand(Command):
    """
    Command for checking player status.
    """
    
    def execute(self, player, world, args):
        """
        Execute the status command.
        
        Args:
            player: The player object
            world: The world object
            args (list): Command arguments
        
        Returns:
            bool: True if the command was executed successfully, False otherwise
        """
        if isinstance(player, dict):
            # For backward compatibility with dictionary-based player
            print(f"Health: {player['health']} | Gold: {player['gold']}")
            print(f"Location: {player['location']}")
            print(f"Inventory: {', '.join(player['inventory']) if player['inventory'] else 'empty'}")
        else:
            # For class-based player
            print(f"Health: {player.health} | Gold: {player.gold}")
            print(f"Location: {player.location}")
            print(f"Inventory: {', '.join(player.inventory) if player.inventory else 'empty'}")
        
        return True


class InteractCommand(Command):
    """
    Command for interacting with the current location.
    """
    
    def execute(self, player, world, args):
        """
        Execute the interact command.
        
        Args:
            player: The player object
            world: The world object
            args (list): Command arguments
        
        Returns:
            bool: True if the command was executed successfully, False otherwise
        """
        interact_with_location(world, player)
        return True


class HelpCommand(Command):
    """
    Command for showing help.
    """
    
    def execute(self, player, world, args):
        """
        Execute the help command.
        
        Args:
            player: The player object
            world: The world object
            args (list): Command arguments
        
        Returns:
            bool: True if the command was executed successfully, False otherwise
        """
        from utils.text_formatting import print_help
        print_help()
        return True


# Command registry
COMMANDS = {
    "move": MoveCommand(),
    "look": LookCommand(),
    "inventory": InventoryCommand(),
    "pickup": PickupCommand(),
    "take": PickupCommand(),  # Alias for pickup
    "drop": DropCommand(),
    "use": UseCommand(),
    "examine": ExamineCommand(),
    "status": StatusCommand(),
    "interact": InteractCommand(),
    "help": HelpCommand()
}


def get_command(command_name):
    """
    Get a command by name.
    
    Args:
        command_name (str): The name of the command
    
    Returns:
        Command: The command with the given name, or None if not found
    """
    return COMMANDS.get(command_name.lower())


def execute_command(player, world, command_string):
    """
    Execute a command.
    
    Args:
        player: The player object
        world: The world object
        command_string (str): The command string
    
    Returns:
        bool: True if the command was executed successfully, False otherwise
    """
    parts = command_string.split()
    command_name = parts[0].lower() if parts else ""
    args = parts[1:] if len(parts) > 1 else []
    
    command = get_command(command_name)
    if command:
        return command.execute(player, world, args)
    
    print(f"I don't understand '{command_string}'. Type 'help' for a list of commands.")
    return False

