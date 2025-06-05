import random

from game.player import (
    add_item_to_inventory,
    damage_player,
    heal_player,
    move_player,
    remove_item_from_inventory,
)
from game.world import change_location, get_all_locations, get_available_locations
from utils.random_events import generate_random_event
from game.constants import ITEM_DESCRIPTIONS
from game.item_handlers import item_registry


def get_item_description(item):
    """Get the description of an item."""
    return ITEM_DESCRIPTIONS.get(item, "A mysterious item.")


def use_item(player, item, world):
    """
    Use an item from the player's inventory.
    Now delegates to the item handler system for better maintainability.
    """
    if item not in player["inventory"]:
        print(f"You don't have {item} in your inventory.")
        return False
    
    return item_registry.use_item(player, world, item)

def get_available_items(world, location):
    return world["locations"][location]["items"]

def add_item_to_world(world, location, item):
    if item not in world["locations"][location]["items"]:
        world["locations"][location]["items"].append(item)
        print(f"A {item} has been added to {location}.")
    else:
        print(f"There's already a {item} in {location}.")

def remove_item_from_world(world, location, item):
    if item in world["locations"][location]["items"]:
        world["locations"][location]["items"].remove(item)
        return True
    return False

def transfer_item(player, world, item, from_inventory_to_world=True):
    current_location = world["current_location"]

    if from_inventory_to_world:
        if remove_item_from_inventory(player, item):
            add_item_to_world(world, current_location, item)
            return True
    else:
        if remove_item_from_world(world, current_location, item):
            add_item_to_inventory(player, item)
            return True

    return False
