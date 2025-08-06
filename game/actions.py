"""
Action system for Kevin's Adventure Game.
Handles all player actions and commands.
"""

from typing import Dict, Any, Callable
from game.player import (
    move_player, add_item_to_inventory, remove_item_from_inventory,
    heal_player, damage_player
)
from game.world import (
    change_location, get_available_locations, get_location_description,
    interact_with_location, is_location_accessible
)
from utils.text_formatting import print_help


def perform_action(player: Dict[str, Any], world: Dict[str, Any], action: str) -> None:
    """
    Process and execute player actions.
    
    Args:
        player: Player data dictionary
        world: World state dictionary  
        action: Action string from user input
    """
    action = action.lower().strip()
    
    # Parse action into command and arguments
    parts = action.split()
    command = parts[0] if parts else ""
    args = parts[1:] if len(parts) > 1 else []
    
    # Action handlers mapping
    action_handlers = {
        'go': _handle_movement,
        'move': _handle_movement,
        'travel': _handle_movement,
        'take': _handle_take_item,
        'pick': _handle_take_item,
        'grab': _handle_take_item,
        'drop': _handle_drop_item,
        'leave': _handle_drop_item,
        'look': _handle_look,
        'examine': _handle_look,
        'explore': _handle_explore,
        'interact': _handle_explore,
        'inventory': _handle_inventory,
        'status': _handle_status,
        'help': _handle_help,
    }
    
    # Execute action if handler exists
    if command in action_handlers:
        action_handlers[command](player, world, args)
    else:
        _handle_unknown_action(player, world, action)


def _handle_movement(player: Dict[str, Any], world: Dict[str, Any], args: list) -> None:
    """Handle movement commands."""
    if not args:
        available = get_available_locations(world)
        print(f"Where would you like to go? Available locations: {', '.join(available)}")
        return
    
    destination = ' '.join(args).title()
    
    if is_location_accessible(world, destination):
        if change_location(world, destination):
            move_player(player, destination)
            print(get_location_description(world, destination))
        else:
            print(f"You cannot go to {destination} from here.")
    else:
        print(f"'{destination}' is not a valid location.")


def _handle_take_item(player: Dict[str, Any], world: Dict[str, Any], args: list) -> None:
    """Handle taking/picking up items."""
    if not args:
        print("What would you like to take?")
        return
    
    item_name = ' '.join(args).lower()
    current_location = world["current_location"]
    location_items = world["locations"][current_location].get("items", [])
    
    if item_name in location_items:
        location_items.remove(item_name)
        add_item_to_inventory(player, item_name)
    else:
        print(f"There is no '{item_name}' here to take.")


def _handle_drop_item(player: Dict[str, Any], world: Dict[str, Any], args: list) -> None:
    """Handle dropping items."""
    if not args:
        print("What would you like to drop?")
        return
    
    item_name = ' '.join(args).lower()
    
    if remove_item_from_inventory(player, item_name):
        current_location = world["current_location"]
        world["locations"][current_location].setdefault("items", []).append(item_name)


def _handle_look(player: Dict[str, Any], world: Dict[str, Any], args: list) -> None:
    """Handle look/examine commands."""
    current_location = world["current_location"]
    
    if not args:
        # Look around current location
        print(get_location_description(world, current_location))
        location_items = world["locations"][current_location].get("items", [])
        if location_items:
            print(f"You can see: {', '.join(location_items)}")
        else:
            print("There are no items here.")
    else:
        # Look at specific item or location
        target = ' '.join(args).lower()
        print(f"You examine the {target}. It looks ordinary.")


def _handle_explore(player: Dict[str, Any], world: Dict[str, Any], args: list) -> None:
    """Handle exploration and interaction with current location."""
    interact_with_location(world, player)


def _handle_inventory(player: Dict[str, Any], world: Dict[str, Any], args: list) -> None:
    """Display player inventory."""
    if player["inventory"]:
        print(f"Inventory: {', '.join(player['inventory'])}")
    else:
        print("Your inventory is empty.")


def _handle_status(player: Dict[str, Any], world: Dict[str, Any], args: list) -> None:
    """Display player status."""
    from game.player import get_player_status
    print(get_player_status(player))


def _handle_help(player: Dict[str, Any], world: Dict[str, Any], args: list) -> None:
    """Display help information."""
    print_help()


def _handle_unknown_action(player: Dict[str, Any], world: Dict[str, Any], action: str) -> None:
    """Handle unknown or invalid actions."""
    print(f"I don't understand '{action}'. Type 'help' for available commands.")
    
    # Suggest similar commands
    suggestions = {
        'walk': 'go',
        'run': 'go', 
        'get': 'take',
        'pickup': 'take',
        'use': 'interact',
        'check': 'look',
        'see': 'look',
        'bag': 'inventory',
        'items': 'inventory'
    }
    
    if action.lower() in suggestions:
        print(f"Did you mean '{suggestions[action.lower()]}'?")

