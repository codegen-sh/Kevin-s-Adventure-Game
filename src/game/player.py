"""
Player module for Kevin's Adventure Game.
Contains the Player class that manages player state and actions.
"""
from typing import List, Optional


class Player:
    """
    Represents the player in the game.
    Manages player attributes, inventory, and actions.
    """

    def __init__(self, name: str):
        """
        Initialize a new player.

        Args:
            name: The player's name
        """
        self.name = name
        self.health = 100
        self.inventory: List[str] = []
        self.location = "Village"
        self.gold = 100
        self.agility = 10
        self.perception = 10

    def get_status(self) -> str:
        """
        Get a string representation of the player's current status.

        Returns:
            A formatted string with player health, inventory, and gold
        """
        inventory_str = ", ".join(self.inventory) if self.inventory else "empty"
        return f"Health: {self.health} | Inventory: {inventory_str} | Gold: {self.gold}"

    def add_item(self, item: str) -> None:
        """
        Add an item to the player's inventory.

        Args:
            item: The item to add
        """
        self.inventory.append(item)
        print(f"You picked up: {item}")

    def remove_item(self, item: str) -> bool:
        """
        Remove an item from the player's inventory.

        Args:
            item: The item to remove

        Returns:
            True if the item was removed, False otherwise
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
            new_location: The name of the new location
        """
        self.location = new_location
        print(f"You moved to: {new_location}")

    def heal(self, amount: int) -> None:
        """
        Heal the player by a specified amount.

        Args:
            amount: The amount of health to restore
        """
        self.health = min(100, self.health + amount)
        print(f"You healed for {amount} health. Current health: {self.health}")

    def take_damage(self, amount: int) -> bool:
        """
        Damage the player by a specified amount.

        Args:
            amount: The amount of damage to take

        Returns:
            True if the player is still alive, False otherwise
        """
        self.health = max(0, self.health - amount)
        print(f"You took {amount} damage. Current health: {self.health}")
        
        if self.health == 0:
            print("You have been defeated.")
            return False
        return True

    def has_item(self, item: str) -> bool:
        """
        Check if the player has a specific item.

        Args:
            item: The item to check for

        Returns:
            True if the player has the item, False otherwise
        """
        return item in self.inventory

