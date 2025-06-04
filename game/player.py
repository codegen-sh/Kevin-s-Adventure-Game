"""
Player management module for Kevin's Adventure Game.

This module handles all player-related functionality including player creation,
status management, inventory operations, and player state modifications.
"""

from utils.text_formatting import format_inventory, print_game_over


def create_player(name):
    """
    Create a new player with default stats and inventory.
    
    Args:
        name (str): The player's name
        
    Returns:
        dict: A dictionary containing player data with the following keys:
            - name (str): Player's name
            - health (int): Current health points (default: 100)
            - inventory (list): List of items in player's inventory
            - location (str): Current location (default: "Village")
            - gold (int): Amount of gold coins (default: 100)
    
    Example:
        >>> player = create_player("Kevin")
        >>> print(player["name"])
        Kevin
        >>> print(player["health"])
        100
    """
    return {
        "name": name,
        "health": 100,
        "inventory": [],
        "location": "Village",
        "gold": 100
    }

def get_player_status(player):
    """
    Get a formatted string representation of the player's current status.
    
    Args:
        player (dict): The player object containing stats and inventory
        
    Returns:
        str: Formatted status string showing health, inventory, and gold
        
    Example:
        >>> player = create_player("Kevin")
        >>> status = get_player_status(player)
        >>> print(status)
        Health: 100 | Inventory: empty | Gold: 100
    """
    return f"Health: {player['health']} | Inventory: {format_inventory(player['inventory'])} | Gold: {player['gold']}"

def add_item_to_inventory(player, item):
    """
    Add an item to the player's inventory.
    
    Args:
        player (dict): The player object to modify
        item (str): The name of the item to add
        
    Side Effects:
        - Modifies the player's inventory list
        - Prints a confirmation message
        
    Example:
        >>> player = create_player("Kevin")
        >>> add_item_to_inventory(player, "sword")
        You picked up: sword
        >>> print(player["inventory"])
        ['sword']
    """
    player['inventory'].append(item)
    print(f"You picked up: {item}")

def remove_item_from_inventory(player, item):
    """
    Remove an item from the player's inventory.
    
    Args:
        player (dict): The player object to modify
        item (str): The name of the item to remove
        
    Returns:
        bool: True if item was successfully removed, False if item not found
        
    Side Effects:
        - Modifies the player's inventory list if item exists
        - Prints a confirmation or error message
        
    Example:
        >>> player = create_player("Kevin")
        >>> add_item_to_inventory(player, "sword")
        >>> success = remove_item_from_inventory(player, "sword")
        You dropped: sword
        >>> print(success)
        True
    """
    if item in player['inventory']:
        player['inventory'].remove(item)
        print(f"You dropped: {item}")
        return True
    else:
        print(f"You don't have {item} in your inventory.")

def move_player(player, new_location):
    """
    Move the player to a new location.
    
    Args:
        player (dict): The player object to modify
        new_location (str): The name of the destination location
        
    Side Effects:
        - Updates the player's location
        - Prints a movement confirmation message
        
    Example:
        >>> player = create_player("Kevin")
        >>> move_player(player, "Forest")
        You moved to: Forest
        >>> print(player["location"])
        Forest
    """
    player['location'] = new_location
    print(f"You moved to: {new_location}")

def heal_player(player, amount):
    """
    Heal the player by a specified amount.
    
    Args:
        player (dict): The player object to modify
        amount (int): The amount of health to heal
        
    Side Effects:
        - Updates the player's health
        - Prints a healing confirmation message
        
    Example:
        >>> player = create_player("Kevin")
        >>> heal_player(player, 20)
        You healed for 20 health. Current health: 120
    """
    player['health'] = min(100, player['health'] + amount)
    print(f"You healed for {amount} health. Current health: {player['health']}")

def damage_player(player, amount):
    """
    Damage the player by a specified amount.
    
    Args:
        player (dict): The player object to modify
        amount (int): The amount of damage to take
        
    Side Effects:
        - Updates the player's health
        - Prints a damage confirmation message
        - Checks if the player is defeated and prints game over message if so
        
    Example:
        >>> player = create_player("Kevin")
        >>> damage_player(player, 30)
        You took 30 damage. Current health: 70
    """
    player['health'] = max(0, player['health'] - amount)
    print(f"You took {amount} damage. Current health: {player['health']}")
    if player['health'] == 0:
        print("You have been defeated.")
        print_game_over()
