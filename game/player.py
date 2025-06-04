"""
Player management module for Kevin's Adventure Game.
Handles all player-related operations including creation, status, inventory, and health.
"""

from typing import Dict, List, Any, Optional
from config import PLAYER_DEFAULTS
from utils.text_formatting import format_inventory, print_game_over


def create_player(name: str) -> Dict[str, Any]:
    """
    Create a new player with default values.
    
    Args:
        name (str): The player's name
        
    Returns:
        Dict[str, Any]: Player state dictionary containing name, health, gold, inventory, etc.
    """
    return {
        "name": name,
        "health": PLAYER_DEFAULTS["health"],
        "inventory": PLAYER_DEFAULTS["inventory"].copy(),
        "location": PLAYER_DEFAULTS["location"],
        "gold": PLAYER_DEFAULTS["gold"]
    }


def get_player_status(player: Dict[str, Any]) -> str:
    """
    Get a formatted string of the player's current status.
    
    Args:
        player (Dict[str, Any]): Player state dictionary
        
    Returns:
        str: Formatted status string showing health, inventory, and gold
    """
    return f"Health: {player['health']} | Inventory: {format_inventory(player['inventory'])} | Gold: {player['gold']}"


def add_item_to_inventory(player: Dict[str, Any], item: str) -> None:
    """
    Add an item to the player's inventory.
    
    Args:
        player (Dict[str, Any]): Player state dictionary
        item (str): Name of the item to add
    """
    player['inventory'].append(item)
    print(f"You picked up: {item}")


def remove_item_from_inventory(player: Dict[str, Any], item: str) -> bool:
    """
    Remove an item from the player's inventory.
    
    Args:
        player (Dict[str, Any]): Player state dictionary
        item (str): Name of the item to remove
        
    Returns:
        bool: True if item was removed successfully, False if item not found
    """
    if item in player['inventory']:
        player['inventory'].remove(item)
        print(f"You dropped: {item}")
        return True
    else:
        print(f"You don't have {item} in your inventory.")
        return False


def move_player(player: Dict[str, Any], new_location: str) -> None:
    """
    Update the player's current location.
    
    Args:
        player (Dict[str, Any]): Player state dictionary
        new_location (str): Name of the new location
    """
    player['location'] = new_location
    print(f"You moved to: {new_location}")


def heal_player(player: Dict[str, Any], amount: int) -> None:
    """
    Heal the player by a specified amount.
    
    Args:
        player (Dict[str, Any]): Player state dictionary
        amount (int): Amount of health to restore
    """
    max_health = 200  # Could be moved to config
    player['health'] = min(max_health, player['health'] + amount)
    print(f"You healed for {amount} health. Current health: {player['health']}")


def damage_player(player: Dict[str, Any], amount: int) -> None:
    """
    Damage the player by a specified amount.
    
    Args:
        player (Dict[str, Any]): Player state dictionary
        amount (int): Amount of damage to deal
    """
    player['health'] = max(0, player['health'] - amount)
    print(f"You took {amount} damage. Current health: {player['health']}")
    if player['health'] == 0:
        print("You have been defeated.")
        print_game_over()

