"""
Actions module for Kevin's Adventure Game.
This module handles all player actions in the game.
"""
import logging

from kevin_adventure_game.game.items import get_available_items, transfer_item, use_item
from kevin_adventure_game.game.player import (
    add_item_to_inventory,
    damage_player,
    get_player_status,
    move_player,
    remove_item_from_inventory,
)
from kevin_adventure_game.game.world import (
    change_location,
    get_available_locations,
    get_current_location,
    get_location_description,
    interact_with_location,
)
from kevin_adventure_game.utils.random_events import apply_random_event

# Set up logger
logger = logging.getLogger(__name__)


def perform_action(player, world, action):
    """
    Process a player's action and update the game state accordingly.

    Args:
        player (dict): The player's current state
        world (dict): The game world state
        action (str): The action to perform

    Returns:
        bool: True if the action was successful, False otherwise
    """
    # Split the action into command and arguments
    parts = action.strip().lower().split()
    command = parts[0] if parts else ""
    args = parts[1:] if len(parts) > 1 else []

    # Process the command
    if command == "move":
        return handle_move(player, world, args)
    elif command == "look":
        return handle_look(player, world)
    elif command == "inventory":
        return handle_inventory(player)
    elif command == "pickup" or command == "take":
        return handle_pickup(player, world, args)
    elif command == "drop":
        return handle_drop(player, world, args)
    elif command == "use":
        return handle_use(player, world, args)
    elif command == "examine":
        return handle_examine(player, world, args)
    elif command == "status":
        return handle_status(player)
    elif command == "interact":
        return handle_interact(player, world)
    else:
        logger.info(f"Unknown command: {command}")
        print(f"I don't understand '{action}'. Type 'help' for a list of commands.")
        return False


def handle_move(player, world, args):
    """Handle the 'move' command."""
    if not args:
        print("Move where? Available locations:")
        for location in get_available_locations(world):
            print(f"- {location}")
        return False

    destination = " ".join(args).title()
    if change_location(world, destination):
        move_player(player, destination)
        # Random event chance when moving
        if apply_random_event(player, world):
            logger.info(f"Random event triggered when moving to {destination}")
        return True
    else:
        print(f"You can't go to {destination} from here.")
        print("Available locations:")
        for location in get_available_locations(world):
            print(f"- {location}")
        return False


def handle_look(player, world):
    """Handle the 'look' command."""
    current_location = get_current_location(world)
    print(f"You are in the {current_location}.")
    print(get_location_description(world, current_location))
    
    # Show available items
    items = get_available_items(world, current_location)
    if items:
        print("You see the following items:")
        for item in items:
            print(f"- {item}")
    else:
        print("You don't see any items here.")
    
    # Show available exits
    exits = get_available_locations(world)
    print("You can go to:")
    for exit_location in exits:
        print(f"- {exit_location}")
    
    return True


def handle_inventory(player):
    """Handle the 'inventory' command."""
    if not player["inventory"]:
        print("Your inventory is empty.")
    else:
        print("Your inventory contains:")
        for item in player["inventory"]:
            print(f"- {item}")
    return True


def handle_pickup(player, world, args):
    """Handle the 'pickup' or 'take' command."""
    if not args:
        print("Pick up what?")
        return False

    item = " ".join(args).lower()
    current_location = get_current_location(world)
    available_items = get_available_items(world, current_location)
    
    if item in available_items:
        if transfer_item(player, world, item, from_inventory_to_world=False):
            logger.info(f"Player picked up {item} at {current_location}")
            return True
    else:
        print(f"There is no {item} here to pick up.")
        return False


def handle_drop(player, world, args):
    """Handle the 'drop' command."""
    if not args:
        print("Drop what?")
        return False

    item = " ".join(args).lower()
    if item in player["inventory"]:
        if transfer_item(player, world, item, from_inventory_to_world=True):
            logger.info(f"Player dropped {item}")
            return True
    else:
        print(f"You don't have {item} in your inventory.")
        return False


def handle_use(player, world, args):
    """Handle the 'use' command."""
    if not args:
        print("Use what?")
        return False

    item = " ".join(args).lower()
    result = use_item(player, item, world)
    if result:
        logger.info(f"Player used {item}")
    return result


def handle_examine(player, world, args):
    """Handle the 'examine' command."""
    if not args:
        print("Examine what?")
        return False

    item = " ".join(args).lower()
    from kevin_adventure_game.game.items import get_item_description
    
    if item in player["inventory"]:
        print(get_item_description(item))
        return True
    else:
        current_location = get_current_location(world)
        available_items = get_available_items(world, current_location)
        if item in available_items:
            print(get_item_description(item))
            return True
        else:
            print(f"You don't see {item} here.")
            return False


def handle_status(player):
    """Handle the 'status' command."""
    print(get_player_status(player))
    return True


def handle_interact(player, world):
    """Handle the 'interact' command."""
    interact_with_location(world, player)
    return True

