"""
Game actions module - handles all player actions and commands.
"""

from game.items import get_item_description, use_item
from game.player import (add_item_to_inventory, damage_player, heal_player,
                         move_player, remove_item_from_inventory)
from game.world import (change_location, get_available_locations,
                        get_current_location, get_location_description,
                        interact_with_location, is_location_accessible)
from utils.text_formatting import print_invalid_action


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
        location = action.split(" ", 1)[1].title()
        handle_movement(player, world, location)

    # Inventory actions
    elif action.startswith("take "):
        item = action.split(" ", 1)[1] if " " in action else ""
        handle_take_item(player, world, item)
    
    elif action.startswith("pick up "):
        item = action[8:]  # Remove "pick up " prefix
        handle_take_item(player, world, item)

    elif action.startswith("drop "):
        item = action.split(" ", 1)[1] if " " in action else ""
        handle_drop_item(player, world, item)

    elif action.startswith("use "):
        item = action.split(" ", 1)[1] if " " in action else ""
        handle_use_item(player, world, item)

    # Information actions
    elif action in ["look", "examine", "describe"]:
        handle_look(player, world)

    elif action in ["inventory", "inv", "items"]:
        handle_inventory(player)

    elif action in ["status", "health", "stats"]:
        handle_status(player)

    # Location interaction
    elif action in ["interact", "explore", "search"]:
        interact_with_location(world, player)

    # Default case
    else:
        print_invalid_action(action)


def handle_movement(player, world, location):
    """Handle player movement between locations."""
    current_location = get_current_location(world)
    available_locations = get_available_locations(world)

    if location in available_locations:
        if change_location(world, location):
            move_player(player, location)
            print(f"\n{get_location_description(world, location)}")
        else:
            print(f"You cannot go to {location} from here.")
    else:
        print(f"You cannot go to {location} from {current_location}.")
        print(f"Available locations: {', '.join(available_locations)}")


def handle_take_item(player, world, item):
    """Handle taking items from the current location."""
    current_location = get_current_location(world)
    location_items = world["locations"][current_location].get("items", [])

    if item in location_items:
        add_item_to_inventory(player, item)
        world["locations"][current_location]["items"].remove(item)
    else:
        print(f"There is no {item} here to take.")
        if location_items:
            print(f"Available items: {', '.join(location_items)}")


def handle_drop_item(player, world, item):
    """Handle dropping items at the current location."""
    if remove_item_from_inventory(player, item):
        current_location = get_current_location(world)
        world["locations"][current_location]["items"].append(item)


def handle_use_item(player, world, item):
    """Handle using items from inventory."""
    if item in player["inventory"]:
        use_item(player, item, world)
    else:
        print(f"You don't have {item} in your inventory.")


def handle_look(player, world):
    """Handle looking around the current location."""
    current_location = get_current_location(world)
    description = get_location_description(world, current_location)
    items = world["locations"][current_location].get("items", [])
    connections = get_available_locations(world)

    print(f"\n{description}")

    if items:
        print(f"Items here: {', '.join(items)}")

    print(f"You can go to: {', '.join(connections)}")


def handle_inventory(player):
    """Handle displaying player inventory."""
    inventory = player["inventory"]
    if inventory:
        print(f"Inventory: {', '.join(inventory)}")
    else:
        print("Your inventory is empty.")


def handle_status(player):
    """Handle displaying player status."""
    print(f"Name: {player['name']}")
    print(f"Health: {player['health']}/100")
    print(f"Gold: {player['gold']}")
    print(f"Location: {player['location']}")
    handle_inventory(player)
