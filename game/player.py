"""
Player module for Kevin's Adventure Game.
Contains the Player class and related functionality.
"""

from typing import List, Optional
from utils.text_formatting import format_inventory, print_game_over


class Player:
    """
    Represents a player in Kevin's Adventure Game.
    
    Attributes:
        name: Player's name
        health: Current health points (0-100)
        max_health: Maximum health points
        inventory: List of items in player's inventory
        location: Current location name
        gold: Amount of gold the player has
    """
    
    def __init__(self, name: str, health: int = 100, max_health: int = 100, 
                 location: str = "Village", gold: int = 100):
        """
        Initialize a new player.
        
        Args:
            name: Player's name
            health: Starting health points
            max_health: Maximum health points
            location: Starting location
            gold: Starting gold amount
        """
        self.name = name
        self.health = health
        self.max_health = max_health
        self.inventory: List[str] = []
        self.location = location
        self.gold = gold
    
    def get_status(self) -> str:
        """
        Get formatted player status string.
        
        Returns:
            Formatted status string with health, inventory, and gold
        """
        return f"Health: {self.health}/{self.max_health} | Inventory: {format_inventory(self.inventory)} | Gold: {self.gold}"
    
    def add_item(self, item: str) -> None:
        """
        Add an item to the player's inventory.
        
        Args:
            item: Item name to add
        """
        self.inventory.append(item)
        print(f"You picked up: {item}")
    
    def remove_item(self, item: str) -> bool:
        """
        Remove an item from the player's inventory.
        
        Args:
            item: Item name to remove
            
        Returns:
            True if item was removed, False if not found
        """
        if item in self.inventory:
            self.inventory.remove(item)
            print(f"You dropped: {item}")
            return True
        else:
            print(f"You don't have {item} in your inventory.")
            return False
    
    def has_item(self, item: str) -> bool:
        """
        Check if player has a specific item.
        
        Args:
            item: Item name to check
            
        Returns:
            True if player has the item, False otherwise
        """
        return item in self.inventory
    
    def move_to(self, new_location: str) -> None:
        """
        Move player to a new location.
        
        Args:
            new_location: Name of the new location
        """
        self.location = new_location
        print(f"You moved to: {new_location}")
    
    def heal(self, amount: int) -> None:
        """
        Heal the player by a specified amount.
        
        Args:
            amount: Amount of health to restore
        """
        old_health = self.health
        self.health = min(self.max_health, self.health + amount)
        actual_healing = self.health - old_health
        print(f"You healed for {actual_healing} health. Current health: {self.health}/{self.max_health}")
    
    def take_damage(self, amount: int) -> None:
        """
        Deal damage to the player.
        
        Args:
            amount: Amount of damage to deal
        """
        self.health = max(0, self.health - amount)
        print(f"You took {amount} damage. Current health: {self.health}/{self.max_health}")
        
        if self.health == 0:
            print("You have been defeated.")
            print_game_over()
    
    def is_alive(self) -> bool:
        """
        Check if the player is still alive.
        
        Returns:
            True if player has health > 0, False otherwise
        """
        return self.health > 0
    
    def add_gold(self, amount: int) -> None:
        """
        Add gold to the player's purse.
        
        Args:
            amount: Amount of gold to add
        """
        self.gold += amount
        print(f"You gained {amount} gold. Total gold: {self.gold}")
    
    def spend_gold(self, amount: int) -> bool:
        """
        Spend gold if the player has enough.
        
        Args:
            amount: Amount of gold to spend
            
        Returns:
            True if transaction successful, False if insufficient funds
        """
        if self.gold >= amount:
            self.gold -= amount
            print(f"You spent {amount} gold. Remaining gold: {self.gold}")
            return True
        else:
            print(f"You don't have enough gold. You need {amount} but only have {self.gold}.")
            return False
    
    def to_dict(self) -> dict:
        """
        Convert player to dictionary for saving.
        
        Returns:
            Dictionary representation of the player
        """
        return {
            "name": self.name,
            "health": self.health,
            "max_health": self.max_health,
            "inventory": self.inventory.copy(),
            "location": self.location,
            "gold": self.gold
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> 'Player':
        """
        Create player from dictionary data.
        
        Args:
            data: Dictionary containing player data
            
        Returns:
            Player instance created from the data
        """
        player = cls(
            name=data.get("name", "Kevin"),
            health=data.get("health", 100),
            max_health=data.get("max_health", 100),
            location=data.get("location", "Village"),
            gold=data.get("gold", 100)
        )
        player.inventory = data.get("inventory", []).copy()
        return player


# Backward compatibility functions for existing code
def create_player(name: str) -> Player:
    """
    Create a new player (backward compatibility function).
    
    Args:
        name: Player's name
        
    Returns:
        New Player instance
    """
    return Player(name)


def get_player_status(player) -> str:
    """
    Get player status (backward compatibility function).
    
    Args:
        player: Player instance or dictionary
        
    Returns:
        Formatted status string
    """
    if isinstance(player, Player):
        return player.get_status()
    else:
        # Handle old dictionary format
        return f"Health: {player['health']} | Inventory: {format_inventory(player['inventory'])} | Gold: {player['gold']}"


def add_item_to_inventory(player, item: str) -> None:
    """Add item to inventory (backward compatibility function)."""
    if isinstance(player, Player):
        player.add_item(item)
    else:
        player['inventory'].append(item)
        print(f"You picked up: {item}")


def remove_item_from_inventory(player, item: str) -> bool:
    """Remove item from inventory (backward compatibility function)."""
    if isinstance(player, Player):
        return player.remove_item(item)
    else:
        if item in player['inventory']:
            player['inventory'].remove(item)
            print(f"You dropped: {item}")
            return True
        else:
            print(f"You don't have {item} in your inventory.")
            return False


def move_player(player, new_location: str) -> None:
    """Move player (backward compatibility function)."""
    if isinstance(player, Player):
        player.move_to(new_location)
    else:
        player['location'] = new_location
        print(f"You moved to: {new_location}")


def heal_player(player, amount: int) -> None:
    """Heal player (backward compatibility function)."""
    if isinstance(player, Player):
        player.heal(amount)
    else:
        player['health'] = min(100, player['health'] + amount)
        print(f"You healed for {amount} health. Current health: {player['health']}")


def damage_player(player, amount: int) -> None:
    """Damage player (backward compatibility function)."""
    if isinstance(player, Player):
        player.take_damage(amount)
    else:
        player['health'] = max(0, player['health'] - amount)
        print(f"You took {amount} damage. Current health: {player['health']}")
        if player['health'] == 0:
            print("You have been defeated.")
            print_game_over()
