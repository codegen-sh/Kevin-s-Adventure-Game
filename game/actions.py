"""
Actions module for Kevin's Adventure Game.
This module handles all player actions and commands.
"""
from game.items import get_item_description, transfer_item, use_item
from game.player import damage_player, get_player_status, move_player
from game.world import (
    change_location,
    get_available_locations,
    get_current_location,
    get_location_description,
    interact_with_location,
)
from utils.random_events import apply_random_event
from utils.text_formatting import print_event


def perform_action(player, world, action):
    """
    Process a player action and update the game state accordingly.
    
    Args:
        player (dict): The player's current state
        world (dict): The game world state
        action (str): The action to perform
    
    Returns:
        None
    """
    # Split the action into command and arguments
    parts = action.split()
    command = parts[0] if parts else ""
    args = parts[1:] if len(parts) > 1 else []
    arg = " ".join(args) if args else ""
    
    # Process the command
    if command == "move":
        handle_move(player, world, arg)
    elif command == "look":
        handle_look(player, world)
    elif command == "inventory":
        handle_inventory(player)
    elif command == "pickup" or command == "take":
        handle_pickup(player, world, arg)
    elif command == "drop":
        handle_drop(player, world, arg)
    elif command == "use":
        handle_use(player, world, arg)
    elif command == "examine":
        handle_examine(player, world, arg)
    elif command == "status":
        handle_status(player)
    elif command == "interact":
        handle_interact(player, world)
    else:
        print(f"I don't understand '{action}'. Type 'help' for a list of commands.")
    
    # Random events have a chance to occur after any action
    if command not in ["help", "quit", "status", "inventory", "examine"]:
        if random_event_should_occur():
            apply_random_event(player, world)


def random_event_should_occur():
    """
    Determine if a random event should occur.
    
    Returns:
        bool: True if a random event should occur, False otherwise
    """
    import random
    return random.random() < 0.1  # 10% chance of a random event


def handle_move(player, world, location):
    """Handle the 'move' command."""
    if not location:
        print("Move where? Available locations:")
        for loc in get_available_locations(world):
            print(f"- {loc}")
        return
    
    if change_location(world, location):
        move_player(player, location)
    else:
        print(f"You can't go to {location} from here.")
        print("Available locations:")
        for loc in get_available_locations(world):
            print(f"- {loc}")


def handle_look(player, world):
    """Handle the 'look' command."""
    current_location = get_current_location(world)
    description = get_location_description(world, current_location)
    print(description)
    
    # Show available items in the location
    items = world["locations"][current_location]["items"]
    if items:
        print("You see the following items:")
        for item in items:
            print(f"- {item}")
    else:
        print("You don't see any items here.")
    
    # Show available exits
    exits = get_available_locations(world)
    print("You can go to:")
    for exit in exits:
        print(f"- {exit}")


def handle_inventory(player):
    """Handle the 'inventory' command."""
    if not player["inventory"]:
        print("Your inventory is empty.")
    else:
        print("Your inventory contains:")
        for item in player["inventory"]:
            print(f"- {item}")


def handle_pickup(player, world, item):
    """Handle the 'pickup' or 'take' command."""
    if not item:
        print("Pick up what?")
        return
    
    current_location = get_current_location(world)
    location_items = world["locations"][current_location]["items"]
    
    if item in location_items:
        transfer_item(player, world, item, from_inventory_to_world=False)
    else:
        print(f"There is no {item} here to pick up.")


def handle_drop(player, world, item):
    """Handle the 'drop' command."""
    if not item:
        print("Drop what?")
        return
    
    if item in player["inventory"]:
        transfer_item(player, world, item, from_inventory_to_world=True)
    else:
        print(f"You don't have {item} in your inventory.")


def handle_use(player, world, item):
    """Handle the 'use' command."""
    if not item:
        print("Use what?")
        return
    
    use_item(player, item, world)


def handle_examine(player, world, item):
    """Handle the 'examine' command."""
    if not item:
        print("Examine what?")
        return
    
    if item in player["inventory"]:
        print(get_item_description(item))
    else:
        current_location = get_current_location(world)
        location_items = world["locations"][current_location]["items"]
        
        if item in location_items:
            print(get_item_description(item))
        else:
            print(f"You don't see {item} here.")


def handle_status(player):
    """Handle the 'status' command."""
    print(get_player_status(player))


def handle_interact(player, world):
    """Handle the 'interact' command."""
    interact_with_location(world, player)

