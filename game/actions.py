"""
Game actions module for Kevin's Adventure Game.
Handles all player actions and commands.
"""

from game.player import move_player, add_item_to_inventory, remove_item_from_inventory
from game.world import (
    get_available_locations, change_location, interact_with_location,
    get_location_description, get_current_location
)
from game.items import get_available_items, transfer_item, use_item
from utils.random_events import apply_random_event
from utils.text_formatting import print_separator


def perform_action(player, world, action):
    """
    Process and execute player actions.
    
    Args:
        player (dict): Player state dictionary
        world (dict): World state dictionary  
        action (str): Action command from player
    """
    action = action.lower().strip()
    
    # Movement actions
    if action.startswith("go ") or action.startswith("move "):
        location = action.split(" ", 1)[1] if " " in action else ""
        handle_movement(player, world, location)
    
    # Inventory actions
    elif action.startswith("take ") or action.startswith("pick up "):
        item = action.split(" ", 1)[1] if " " in action else ""
        handle_take_item(player, world, item)
    
    elif action.startswith("drop "):
        item = action.split(" ", 1)[1] if " " in action else ""
        handle_drop_item(player, world, item)
    
    elif action.startswith("use "):
        item = action.split(" ", 1)[1] if " " in action else ""
        handle_use_item(player, world, item)
    
    # Information actions
    elif action in ["look", "examine", "observe"]:
        handle_look(player, world)
    
    elif action in ["inventory", "inv", "items"]:
        handle_inventory(player)
    
    elif action in ["status", "stats"]:
        handle_status(player)
    
    # Interaction actions
    elif action in ["interact", "explore", "search"]:
        interact_with_location(world, player)
    
    # Random event trigger
    elif action in ["wait", "rest"]:
        handle_wait(player, world)
    
    else:
        print(f"I don't understand '{action}'. Type 'help' for available commands.")


def handle_movement(player, world, location):
    """Handle player movement between locations."""
    if not location:
        print("Where would you like to go?")
        available = get_available_locations(world)
        print(f"Available locations: {', '.join(available)}")
        return
    
    location = location.title()  # Capitalize first letter
    available_locations = get_available_locations(world)
    
    if location in available_locations:
        if change_location(world, location):
            move_player(player, location)
            print(f"\n{get_location_description(world, location)}")
        else:
            print(f"You cannot go to {location} from here.")
    else:
        print(f"'{location}' is not a valid location.")
        print(f"Available locations: {', '.join(available_locations)}")


def handle_take_item(player, world, item):
    """Handle taking items from the current location."""
    if not item:
        print("What would you like to take?")
        current_location = get_current_location(world)
        available_items = get_available_items(world, current_location)
        if available_items:
            print(f"Available items: {', '.join(available_items)}")
        else:
            print("There are no items here to take.")
        return
    
    current_location = get_current_location(world)
    available_items = get_available_items(world, current_location)
    
    if item in available_items:
        transfer_item(player, world, item, from_inventory_to_world=False)
    else:
        print(f"There is no '{item}' here to take.")
        if available_items:
            print(f"Available items: {', '.join(available_items)}")


def handle_drop_item(player, world, item):
    """Handle dropping items from inventory."""
    if not item:
        print("What would you like to drop?")
        if player['inventory']:
            print(f"Your inventory: {', '.join(player['inventory'])}")
        else:
            print("Your inventory is empty.")
        return
    
    if item in player['inventory']:
        transfer_item(player, world, item, from_inventory_to_world=True)
    else:
        print(f"You don't have '{item}' in your inventory.")


def handle_use_item(player, world, item):
    """Handle using items from inventory."""
    if not item:
        print("What would you like to use?")
        if player['inventory']:
            print(f"Your inventory: {', '.join(player['inventory'])}")
        else:
            print("Your inventory is empty.")
        return
    
    if item in player['inventory']:
        use_item(player, item, world)
    else:
        print(f"You don't have '{item}' in your inventory.")


def handle_look(player, world):
    """Handle looking around the current location."""
    current_location = get_current_location(world)
    print(f"\n{get_location_description(world, current_location)}")
    
    # Show available items
    available_items = get_available_items(world, current_location)
    if available_items:
        print(f"Items here: {', '.join(available_items)}")
    
    # Show available exits
    available_locations = get_available_locations(world)
    print(f"Exits: {', '.join(available_locations)}")


def handle_inventory(player):
    """Display player inventory."""
    if player['inventory']:
        print(f"Inventory: {', '.join(player['inventory'])}")
    else:
        print("Your inventory is empty.")


def handle_status(player):
    """Display detailed player status."""
    print_separator()
    print(f"Player: {player['name']}")
    print(f"Health: {player['health']}/100")
    print(f"Gold: {player['gold']}")
    print(f"Location: {player['location']}")
    if player['inventory']:
        print(f"Inventory: {', '.join(player['inventory'])}")
    else:
        print("Inventory: Empty")
    print_separator()


def handle_wait(player, world):
    """Handle waiting/resting action."""
    print("You wait and rest for a moment...")
    apply_random_event(player, world)

