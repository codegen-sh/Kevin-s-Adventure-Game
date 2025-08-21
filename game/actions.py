"""
Actions module for Kevin's Adventure Game.

This module contains functions for handling player actions in the game.
"""
from game.items import get_available_items, get_item_description, transfer_item, use_item
from game.player import get_player_status, move_player
from game.world import (
    change_location,
    get_available_locations,
    get_current_location,
    get_location_description,
    interact_with_location,
    is_location_accessible,
)
from utils.random_events import apply_random_event
from utils.text_formatting import print_help


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
    parts = action.strip().split(" ", 1)
    command = parts[0].lower()
    args = parts[1].lower() if len(parts) > 1 else ""

    # Process the command
    if command == "move" or command == "go":
        handle_move(player, world, args)
    elif command == "look":
        handle_look(player, world)
    elif command == "inventory" or command == "inv":
        handle_inventory(player)
    elif command == "pickup" or command == "take" or command == "get":
        handle_pickup(player, world, args)
    elif command == "drop":
        handle_drop(player, world, args)
    elif command == "use":
        handle_use(player, world, args)
    elif command == "examine" or command == "inspect":
        handle_examine(player, world, args)
    elif command == "status":
        handle_status(player)
    elif command == "interact":
        handle_interact(player, world)
    else:
        print(f"I don't understand '{action}'. Type 'help' for a list of commands.")

    # Random events have a chance to occur after any action
    apply_random_event(player, world)


def handle_move(player, world, location):
    """Handle the 'move' or 'go' command."""
    if not location:
        print("Where do you want to go? Available locations:")
        for loc in get_available_locations(world):
            print(f"- {loc}")
        return

    if is_location_accessible(world, location):
        if change_location(world, location):
            move_player(player, location)
            print(get_location_description(world, location))
        else:
            print(f"You can't go to {location} from here.")
    else:
        print(f"You can't go to {location} from here. Available locations:")
        for loc in get_available_locations(world):
            print(f"- {loc}")


def handle_look(player, world):
    """Handle the 'look' command."""
    current_location = get_current_location(world)
    print(get_location_description(world, current_location))
    
    # Show available items
    items = get_available_items(world, current_location)
    if items:
        print("You can see the following items:")
        for item in items:
            print(f"- {item}")
    else:
        print("There are no items of interest here.")
    
    # Show available exits
    exits = get_available_locations(world)
    print("You can go to the following locations:")
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
    """Handle the 'pickup', 'take', or 'get' command."""
    if not item:
        print("What do you want to pick up?")
        return

    current_location = get_current_location(world)
    items = get_available_items(world, current_location)
    
    if item in items:
        transfer_item(player, world, item, from_inventory_to_world=False)
    else:
        print(f"There is no {item} here to pick up.")


def handle_drop(player, world, item):
    """Handle the 'drop' command."""
    if not item:
        print("What do you want to drop?")
        return

    if item in player["inventory"]:
        transfer_item(player, world, item, from_inventory_to_world=True)
    else:
        print(f"You don't have {item} in your inventory.")


def handle_use(player, world, item):
    """Handle the 'use' command."""
    if not item:
        print("What do you want to use?")
        return

    use_item(player, item, world)


def handle_examine(player, world, item):
    """Handle the 'examine' or 'inspect' command."""
    if not item:
        print("What do you want to examine?")
        return

    if item in player["inventory"]:
        print(get_item_description(item))
    else:
        current_location = get_current_location(world)
        items = get_available_items(world, current_location)
        
        if item in items:
            print(get_item_description(item))
        else:
            print(f"You don't see {item} here.")


def handle_status(player):
    """Handle the 'status' command."""
    print(get_player_status(player))


def handle_interact(player, world):
    """Handle the 'interact' command."""
    interact_with_location(world, player)

