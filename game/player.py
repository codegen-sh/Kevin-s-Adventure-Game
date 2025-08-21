"""
Player module for Kevin's Adventure Game.

This module contains the Player class and related functions for managing the player.
"""
from typing import Dict, List, Optional, Union

from utils.text_formatting import format_inventory, print_game_over


class Player:
    """
    Class representing a player in the game.
    
    Attributes:
        name (str): The player's name
        health (int): The player's current health
        inventory (List[str]): The player's inventory
        location (str): The player's current location
        gold (int): The player's gold
        stats (Dict[str, int]): The player's stats (strength, agility, etc.)
    """
    
    def __init__(self, name: str):
        """
        Initialize a new Player.
        
        Args:
            name (str): The player's name
        """
        self.name = name
        self.health = 100
        self.inventory: List[str] = []
        self.location = "Village"
        self.gold = 100
        self.stats = {
            "strength": 10,
            "agility": 10,
            "perception": 10
        }
    
    def get_status(self) -> str:
        """
        Get the player's current status.
        
        Returns:
            str: A string describing the player's current status
        """
        return f"Health: {self.health} | Inventory: {format_inventory(self.inventory)} | Gold: {self.gold}"
    
    def add_item(self, item: str) -> None:
        """
        Add an item to the player's inventory.
        
        Args:
            item (str): The item to add
        """
        self.inventory.append(item)
        print(f"You picked up: {item}")
    
    def remove_item(self, item: str) -> bool:
        """
        Remove an item from the player's inventory.
        
        Args:
            item (str): The item to remove
            
        Returns:
            bool: True if the item was removed, False otherwise
        """
        if item in self.inventory:
            self.inventory.remove(item)
            print(f"You dropped: {item}")
            return True
        else:
            print(f"You don't have {item} in your inventory.")
            return False
    
    def move(self, new_location: str) -> None:
        """
        Move the player to a new location.
        
        Args:
            new_location (str): The new location
        """
        self.location = new_location
        print(f"You moved to: {new_location}")
    
    def heal(self, amount: int) -> None:
        """
        Heal the player.
        
        Args:
            amount (int): The amount to heal
        """
        self.health = min(100, self.health + amount)
        print(f"You healed for {amount} health. Current health: {self.health}")
    
    def damage(self, amount: int) -> None:
        """
        Damage the player.
        
        Args:
            amount (int): The amount of damage
        """
        self.health = max(0, self.health - amount)
        print(f"You took {amount} damage. Current health: {self.health}")
        if self.health == 0:
            print("You have been defeated.")
            print_game_over()
    
    def add_gold(self, amount: int) -> None:
        """
        Add gold to the player.
        
        Args:
            amount (int): The amount of gold to add
        """
        self.gold += amount
        print(f"You gained {amount} gold. Current gold: {self.gold}")
    
    def remove_gold(self, amount: int) -> bool:
        """
        Remove gold from the player.
        
        Args:
            amount (int): The amount of gold to remove
            
        Returns:
            bool: True if the gold was removed, False if the player doesn't have enough
        """
        if self.gold >= amount:
            self.gold -= amount
            print(f"You spent {amount} gold. Current gold: {self.gold}")
            return True
        else:
            print(f"You don't have enough gold. Current gold: {self.gold}")
            return False
    
    def to_dict(self) -> Dict[str, Union[str, int, List[str], Dict[str, int]]]:
        """
        Convert the player to a dictionary for saving.
        
        Returns:
            dict: A dictionary representation of the player
        """
        return {
            "name": self.name,
            "health": self.health,
            "inventory": self.inventory,
            "location": self.location,
            "gold": self.gold,
            "stats": self.stats
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Union[str, int, List[str], Dict[str, int]]]) -> 'Player':
        """
        Create a player from a dictionary.
        
        Args:
            data (dict): A dictionary representation of a player
            
        Returns:
            Player: A new Player instance
        """
        player = cls(data["name"])
        player.health = data["health"]
        player.inventory = data["inventory"]
        player.location = data["location"]
        player.gold = data["gold"]
        player.stats = data.get("stats", {
            "strength": 10,
            "agility": 10,
            "perception": 10
        })
        return player


# Legacy functions for backward compatibility
def create_player(name: str) -> Dict[str, Union[str, int, List[str]]]:
    """
    Create a new player.
    
    Args:
        name (str): The player's name
        
    Returns:
        dict: A dictionary representing the player
    """
    return {
        "name": name,
        "health": 100,
        "inventory": [],
        "location": "Village",
        "gold": 100
    }

def get_player_status(player: Dict[str, Union[str, int, List[str]]]) -> str:
    """
    Get the player's current status.
    
    Args:
        player (dict): The player's current state
        
    Returns:
        str: A string describing the player's current status
    """
    return f"Health: {player['health']} | Inventory: {format_inventory(player['inventory'])} | Gold: {player['gold']}"

def add_item_to_inventory(player: Dict[str, Union[str, int, List[str]]], item: str) -> None:
    """
    Add an item to the player's inventory.
    
    Args:
        player (dict): The player's current state
        item (str): The item to add
    """
    player['inventory'].append(item)
    print(f"You picked up: {item}")

def remove_item_from_inventory(player: Dict[str, Union[str, int, List[str]]], item: str) -> bool:
    """
    Remove an item from the player's inventory.
    
    Args:
        player (dict): The player's current state
        item (str): The item to remove
        
    Returns:
        bool: True if the item was removed, False otherwise
    """
    if item in player['inventory']:
        player['inventory'].remove(item)
        print(f"You dropped: {item}")
        return True
    else:
        print(f"You don't have {item} in your inventory.")
        return False

def move_player(player: Dict[str, Union[str, int, List[str]]], new_location: str) -> None:
    """
    Move the player to a new location.
    
    Args:
        player (dict): The player's current state
        new_location (str): The new location
    """
    player['location'] = new_location
    print(f"You moved to: {new_location}")

def heal_player(player: Dict[str, Union[str, int, List[str]]], amount: int) -> None:
    """
    Heal the player.
    
    Args:
        player (dict): The player's current state
        amount (int): The amount to heal
    """
    player['health'] = min(100, player['health'] + amount)
    print(f"You healed for {amount} health. Current health: {player['health']}")

def damage_player(player: Dict[str, Union[str, int, List[str]]], amount: int) -> None:
    """
    Damage the player.
    
    Args:
        player (dict): The player's current state
        amount (int): The amount of damage
    """
    player['health'] = max(0, player['health'] - amount)
    print(f"You took {amount} damage. Current health: {player['health']}")
    if player['health'] == 0:
        print("You have been defeated.")
        print_game_over()

