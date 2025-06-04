"""
Game actions module for Kevin's Adventure Game.

This module handles all player actions and commands in the game.
"""

from game.items import use_item, get_item_description
from game.player import add_item_to_inventory, move_player
from game.world import get_available_locations, get_current_location, change_location
from locations.village import visit_village
from locations.forest import enter_forest
from locations.mountain import climb_mountain


def perform_action(player, world, action):
    """
    Process and execute a player action.
    
    Args:
        player (dict): The player object containing stats and inventory
        world (dict): The world state object
        action (str): The action command entered by the player
    
    Returns:
        bool: True if action was successful, False otherwise
    """
    action = action.lower().strip()
    
    # Movement actions
    if action in ["go", "move", "travel"]:
        handle_movement(player, world)
        return True
    
    # Check if action is a location name
    available_locations = get_available_locations(world)
    if action in [loc.lower() for loc in available_locations]:
        location_name = next(loc for loc in available_locations if loc.lower() == action)
        move_to_location(player, world, location_name)
        return True
    
    # Item actions
    if action.startswith("use "):
        item = action[4:]  # Remove "use " prefix
        return use_item(player, item, world)
    
    if action.startswith("take ") or action.startswith("pick up "):
        item = action.split(" ", 1)[1] if " " in action else ""
        return take_item(player, world, item)
    
    if action.startswith("examine ") or action.startswith("look at "):
        item = action.split(" ", 1)[1] if " " in action else ""
        return examine_item(item)
    
    # Location-specific actions
    if action in ["explore", "look around", "search"]:
        explore_current_location(player, world)
        return True
    
    if action in ["inventory", "inv", "items"]:
        show_inventory(player)
        return True
    
    if action in ["status", "stats", "health"]:
        show_status(player)
        return True
    
    if action in ["locations", "where can i go", "exits"]:
        show_available_locations(world)
        return True
    
    # Default case
    print(f"I don't understand '{action}'. Type 'help' for available commands.")
    return False


def handle_movement(player, world):
    """Handle movement commands by showing available locations."""
    print("Where would you like to go?")
    show_available_locations(world)


def move_to_location(player, world, location):
    """
    Move player to a specific location.
    
    Args:
        player (dict): The player object
        world (dict): The world state object
        location (str): The target location name
    """
    current_location = get_current_location(world)
    available_locations = get_available_locations(world)
    
    if location not in available_locations:
        print(f"You can't go to {location} from here.")
        return False
    
    # Update player and world state
    move_player(player, location)
    change_location(world, location)
    
    # Trigger location-specific events
    if location == "Village":
        visit_village(player, world)
    elif location == "Forest":
        enter_forest(player, world)
    elif location == "Mountain":
        climb_mountain(player, world)
    
    return True


def take_item(player, world, item):
    """
    Attempt to take an item from the current location.
    
    Args:
        player (dict): The player object
        world (dict): The world state object
        item (str): The item name to take
    
    Returns:
        bool: True if item was taken successfully
    """
    current_location = get_current_location(world)
    location_data = world["locations"].get(current_location, {})
    available_items = location_data.get("items", [])
    
    if item in available_items:
        add_item_to_inventory(player, item)
        available_items.remove(item)
        return True
    else:
        print(f"There is no {item} here.")
        return False


def examine_item(item):
    """
    Examine an item to get its description.
    
    Args:
        item (str): The item name to examine
    
    Returns:
        bool: True if item description was shown
    """
    description = get_item_description(item)
    print(f"{item.title()}: {description}")
    return True


def explore_current_location(player, world):
    """Explore the current location and show available items and exits."""
    current_location = get_current_location(world)
    location_data = world["locations"].get(current_location, {})
    
    print(f"\\nYou look around the {current_location}.")
    print(location_data.get("description", "A mysterious place."))
    
    items = location_data.get("items", [])
    if items:
        print(f"\\nYou see the following items: {', '.join(items)}")
    else:
        print("\\nThere are no items here.")
    
    connections = location_data.get("connections", [])
    if connections:
        print(f"\\nYou can go to: {', '.join(connections)}")


def show_inventory(player):
    """Display the player's inventory."""
    inventory = player.get("inventory", [])
    if inventory:
        print(f"\\nInventory: {', '.join(inventory)}")
    else:
        print("\\nYour inventory is empty.")


def show_status(player):
    """Display the player's current status."""
    print(f"\\nPlayer: {player.get('name', 'Unknown')}")
    print(f"Health: {player.get('health', 0)}")
    print(f"Gold: {player.get('gold', 0)}")
    print(f"Location: {player.get('location', 'Unknown')}")


def show_available_locations(world):
    """Display locations the player can travel to."""
    available_locations = get_available_locations(world)
    if available_locations:
        print(f"\\nYou can go to: {', '.join(available_locations)}")
    else:
        print("\\nThere are no exits from here.")

