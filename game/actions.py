"""
Game actions module - handles user input and delegates to appropriate game systems.
"""

from game.items import use_item
from game.player import move_player
from game.world import (
    change_location,
    get_available_locations,
    get_location_description,
    interact_with_location,
    is_location_accessible
)


def perform_action(player, world, action):
    """
    Process user actions and delegate to appropriate game systems.
    
    Args:
        player (dict): Player data
        world (dict): World state
        action (str): User input action
    """
    action = action.lower().strip()
    
    # Handle movement actions
    if action.startswith("go to ") or action.startswith("move to "):
        location = action.replace("go to ", "").replace("move to ", "").title()
        handle_movement(player, world, location)
    
    elif action in ["go", "move", "travel"]:
        show_available_locations(world)
    
    # Handle item usage
    elif action.startswith("use "):
        item = action.replace("use ", "")
        handle_item_usage(player, world, item)
    
    # Handle inventory actions
    elif action in ["inventory", "inv", "items"]:
        show_inventory(player)
    
    # Handle location interaction
    elif action in ["look", "examine", "explore"]:
        handle_location_interaction(player, world)
    
    # Handle location-specific actions
    elif action in ["interact", "enter", "visit"]:
        interact_with_location(world, player)
    
    # Handle status check
    elif action in ["status", "health", "stats"]:
        show_player_status(player)
    
    else:
        print(f"I don't understand '{action}'. Type 'help' for available commands.")


def handle_movement(player, world, location):
    """Handle player movement to a new location."""
    if is_location_accessible(world, location):
        if change_location(world, location):
            move_player(player, location)
            print(f"\n{get_location_description(world, location)}")
        else:
            print(f"You cannot go to {location} from here.")
    else:
        print(f"'{location}' is not a valid location or is not accessible from here.")


def show_available_locations(world):
    """Show locations the player can travel to."""
    available = get_available_locations(world)
    if available:
        print("You can travel to:")
        for location in available:
            print(f"  - {location}")
        print("Use 'go to [location]' to travel.")
    else:
        print("There are no available locations to travel to.")


def handle_item_usage(player, world, item):
    """Handle using an item from inventory."""
    if item in player.get("inventory", []):
        use_item(player, item, world)
    else:
        print(f"You don't have '{item}' in your inventory.")


def show_inventory(player):
    """Display player's inventory."""
    inventory = player.get("inventory", [])
    if inventory:
        print("Your inventory contains:")
        for item in inventory:
            print(f"  - {item}")
    else:
        print("Your inventory is empty.")


def handle_location_interaction(player, world):
    """Handle examining the current location."""
    current_location = world.get("current_location", "Unknown")
    description = get_location_description(world, current_location)
    print(f"\n{description}")
    
    # Show available items in location
    location_data = world.get("locations", {}).get(current_location, {})
    items = location_data.get("items", [])
    if items:
        print(f"\nYou can see: {', '.join(items)}")


def show_player_status(player):
    """Display detailed player status."""
    print(f"\n=== Player Status ===")
    print(f"Name: {player.get('name', 'Unknown')}")
    print(f"Health: {player.get('health', 0)}/100")
    print(f"Gold: {player.get('gold', 0)}")
    print(f"Location: {player.get('location', 'Unknown')}")
    
    inventory = player.get("inventory", [])
    if inventory:
        print(f"Inventory: {', '.join(inventory)}")
    else:
        print("Inventory: Empty")
