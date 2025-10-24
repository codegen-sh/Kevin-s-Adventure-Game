"""
Game actions module for Kevin's Adventure Game.
Handles all player actions and commands.
"""

from typing import Dict, Any, Tuple
from game.items import (
    get_available_items, 
    get_item_description, 
    transfer_item, 
    use_item
)
from game.player import get_player_status, move_player
from game.world import (
    change_location, 
    get_available_locations, 
    get_current_location,
    get_location_description,
    interact_with_location
)
from utils.random_events import apply_random_event


def perform_action(player: Dict[str, Any], world: Dict[str, Any], action: str) -> bool:
    """
    Perform a player action based on the input command.
    
    Args:
        player: Player state dictionary
        world: World state dictionary  
        action: Action string from user input
        
    Returns:
        bool: True if action was successful, False otherwise
    """
    action_parts = action.split()
    command = action_parts[0] if action_parts else ""
    
    # Handle movement commands
    if command == "move" or command == "go":
        if len(action_parts) > 1:
            destination = action_parts[1].title()
            return handle_move(player, world, destination)
        else:
            print("Move where? Available locations:")
            available_locations = get_available_locations(world)
            for location in available_locations:
                print(f"- {location}")
            return False
    
    # Handle look/examine commands
    elif command == "look" or command == "examine":
        if len(action_parts) > 1:
            target = " ".join(action_parts[1:])
            return handle_examine(player, world, target)
        else:
            return handle_look(player, world)
    
    # Handle inventory commands
    elif command == "inventory" or command == "inv":
        return handle_inventory(player)
    
    # Handle pickup commands
    elif command == "pickup" or command == "take" or command == "get":
        if len(action_parts) > 1:
            item = " ".join(action_parts[1:])
            return handle_pickup(player, world, item)
        else:
            print("Pick up what?")
            return False
    
    # Handle drop commands
    elif command == "drop":
        if len(action_parts) > 1:
            item = " ".join(action_parts[1:])
            return handle_drop(player, world, item)
        else:
            print("Drop what?")
            return False
    
    # Handle use commands
    elif command == "use":
        if len(action_parts) > 1:
            item = " ".join(action_parts[1:])
            return handle_use(player, world, item)
        else:
            print("Use what?")
            return False
    
    # Handle status command
    elif command == "status":
        return handle_status(player)
    
    # Handle interact command
    elif command == "interact":
        return handle_interact(player, world)
    
    # Handle random exploration
    elif command == "explore":
        return handle_explore(player, world)
    
    # Unknown command
    else:
        print(f"Unknown command: {action}")
        print("Type 'help' for available commands.")
        return False


def handle_move(player: Dict[str, Any], world: Dict[str, Any], destination: str) -> bool:
    """Handle player movement to a new location."""
    if change_location(world, destination):
        move_player(player, destination)
        current_location = get_current_location(world)
        description = get_location_description(world, current_location)
        print(f"\n{description}")
        
        # Show available items in the new location
        available_items = get_available_items(world, current_location)
        if available_items:
            print(f"You see: {', '.join(available_items)}")
        
        # Random chance of an event occurring when moving
        apply_random_event(player, world)
        return True
    else:
        print(f"You can't go to {destination} from here.")
        available_locations = get_available_locations(world)
        print(f"Available locations: {', '.join(available_locations)}")
        return False


def handle_look(player: Dict[str, Any], world: Dict[str, Any]) -> bool:
    """Handle looking around the current location."""
    current_location = get_current_location(world)
    description = get_location_description(world, current_location)
    print(f"\n{description}")
    
    # Show available items
    available_items = get_available_items(world, current_location)
    if available_items:
        print(f"You see: {', '.join(available_items)}")
    else:
        print("There are no items here.")
    
    # Show available exits
    available_locations = get_available_locations(world)
    print(f"Exits: {', '.join(available_locations)}")
    return True


def handle_examine(player: Dict[str, Any], world: Dict[str, Any], target: str) -> bool:
    """Handle examining a specific item or location feature."""
    current_location = get_current_location(world)
    available_items = get_available_items(world, current_location)
    
    # Check if target is an item in the current location
    if target in available_items:
        description = get_item_description(target)
        print(f"{target}: {description}")
        return True
    
    # Check if target is an item in inventory
    elif target in player["inventory"]:
        description = get_item_description(target)
        print(f"{target}: {description}")
        return True
    
    else:
        print(f"You don't see a {target} here.")
        return False


def handle_inventory(player: Dict[str, Any]) -> bool:
    """Handle displaying player inventory."""
    if player["inventory"]:
        print("Inventory:")
        for item in player["inventory"]:
            description = get_item_description(item)
            print(f"- {item}: {description}")
    else:
        print("Your inventory is empty.")
    return True


def handle_pickup(player: Dict[str, Any], world: Dict[str, Any], item: str) -> bool:
    """Handle picking up an item."""
    current_location = get_current_location(world)
    available_items = get_available_items(world, current_location)
    
    if item in available_items:
        return transfer_item(player, world, item, from_inventory_to_world=False)
    else:
        print(f"There is no {item} here.")
        return False


def handle_drop(player: Dict[str, Any], world: Dict[str, Any], item: str) -> bool:
    """Handle dropping an item."""
    if item in player["inventory"]:
        return transfer_item(player, world, item, from_inventory_to_world=True)
    else:
        print(f"You don't have {item} in your inventory.")
        return False


def handle_use(player: Dict[str, Any], world: Dict[str, Any], item: str) -> bool:
    """Handle using an item."""
    return use_item(player, item, world)


def handle_status(player: Dict[str, Any]) -> bool:
    """Handle displaying player status."""
    print(get_player_status(player))
    return True


def handle_interact(player: Dict[str, Any], world: Dict[str, Any]) -> bool:
    """Handle interacting with the current location."""
    interact_with_location(world, player)
    return True


def handle_explore(player: Dict[str, Any], world: Dict[str, Any]) -> bool:
    """Handle exploring the current location for random events."""
    current_location = get_current_location(world)
    print(f"You explore the {current_location} more thoroughly...")
    apply_random_event(player, world)
    return True

