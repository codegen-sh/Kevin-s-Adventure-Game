"""
Game actions module - handles all player actions and commands.
"""
from typing import Dict, Any
from game.player import (
    move_player, add_item_to_inventory, remove_item_from_inventory,
    heal_player, damage_player
)
from game.world import (
    change_location, get_available_locations, interact_with_location,
    get_location_description, get_current_location
)
from game.items import use_item, get_location_items
from utils.random_events import apply_random_event


def perform_action(player: Dict[str, Any], world: Dict[str, Any], action: str) -> None:
    """
    Process and execute player actions.
    
    Args:
        player: Player data dictionary
        world: World state dictionary
        action: Action string from user input
    """
    action = action.lower().strip()
    
    # Movement commands
    if action in ['go', 'move', 'travel']:
        handle_movement(player, world)
    elif action.startswith('go ') or action.startswith('move ') or action.startswith('travel '):
        destination = action.split(' ', 1)[1]
        handle_movement_to(player, world, destination)
    
    # Interaction commands
    elif action in ['look', 'examine', 'observe']:
        handle_look(player, world)
    elif action in ['interact', 'explore', 'search']:
        interact_with_location(world, player)
    
    # Inventory commands
    elif action in ['inventory', 'inv', 'items']:
        show_inventory(player)
    elif action.startswith('take ') or action.startswith('get ') or action.startswith('pick up '):
        item = action.split(' ', 1)[1] if ' ' in action else ''
        handle_take_item(player, world, item)
    elif action.startswith('drop ') or action.startswith('leave '):
        item = action.split(' ', 1)[1] if ' ' in action else ''
        handle_drop_item(player, world, item)
    elif action.startswith('use '):
        item = action.split(' ', 1)[1] if ' ' in action else ''
        handle_use_item(player, world, item)
    
    # Status commands
    elif action in ['status', 'stats', 'health']:
        show_status(player)
    elif action in ['map', 'locations']:
        show_map(world)
    
    # Random event trigger
    elif action in ['wait', 'rest']:
        print("You take a moment to rest...")
        apply_random_event(player, world)
    
    else:
        print(f"I don't understand '{action}'. Type 'help' for available commands.")


def handle_movement(player: Dict[str, Any], world: Dict[str, Any]) -> None:
    """Handle generic movement command - show available locations."""
    available_locations = get_available_locations(world)
    if available_locations:
        print("You can travel to:")
        for i, location in enumerate(available_locations, 1):
            print(f"{i}. {location}")
        print("Type 'go [location name]' to travel there.")
    else:
        print("There are no available locations to travel to from here.")


def handle_movement_to(player: Dict[str, Any], world: Dict[str, Any], destination: str) -> None:
    """Handle movement to a specific location."""
    destination = destination.title()  # Capitalize first letter
    available_locations = get_available_locations(world)
    
    if destination in available_locations:
        if change_location(world, destination):
            move_player(player, destination)
            current_location = get_current_location(world)
            print(f"\n{get_location_description(world, current_location)}")
            apply_random_event(player, world)
        else:
            print(f"You cannot travel to {destination} right now.")
    else:
        print(f"You cannot reach {destination} from here.")
        print(f"Available locations: {', '.join(available_locations)}")


def handle_look(player: Dict[str, Any], world: Dict[str, Any]) -> None:
    """Handle look/examine command."""
    current_location = get_current_location(world)
    print(f"\n{get_location_description(world, current_location)}")
    
    # Show available items
    items = get_location_items(world, current_location)
    if items:
        print(f"You can see: {', '.join(items)}")
    
    # Show available exits
    available_locations = get_available_locations(world)
    if available_locations:
        print(f"Exits: {', '.join(available_locations)}")


def handle_take_item(player: Dict[str, Any], world: Dict[str, Any], item: str) -> None:
    """Handle taking an item from the current location."""
    if not item:
        print("What do you want to take?")
        return
    
    current_location = get_current_location(world)
    location_items = world["locations"][current_location].get("items", [])
    
    if item in location_items:
        location_items.remove(item)
        add_item_to_inventory(player, item)
    else:
        print(f"There is no {item} here.")


def handle_drop_item(player: Dict[str, Any], world: Dict[str, Any], item: str) -> None:
    """Handle dropping an item at the current location."""
    if not item:
        print("What do you want to drop?")
        return
    
    if remove_item_from_inventory(player, item):
        current_location = get_current_location(world)
        world["locations"][current_location]["items"].append(item)


def handle_use_item(player: Dict[str, Any], world: Dict[str, Any], item: str) -> None:
    """Handle using an item from inventory."""
    if not item:
        print("What do you want to use?")
        return
    
    if item in player["inventory"]:
        use_item(player, world, item)
    else:
        print(f"You don't have {item} in your inventory.")


def show_inventory(player: Dict[str, Any]) -> None:
    """Display player's inventory."""
    if player["inventory"]:
        print("Your inventory contains:")
        for item in player["inventory"]:
            print(f"  - {item}")
    else:
        print("Your inventory is empty.")


def show_status(player: Dict[str, Any]) -> None:
    """Display player's current status."""
    print(f"Name: {player['name']}")
    print(f"Health: {player['health']}/100")
    print(f"Gold: {player['gold']}")
    print(f"Location: {player['location']}")


def show_map(world: Dict[str, Any]) -> None:
    """Display available locations and their connections."""
    print("World Map:")
    for location, data in world["locations"].items():
        connections = ", ".join(data["connections"])
        print(f"  {location}: connects to {connections}")
