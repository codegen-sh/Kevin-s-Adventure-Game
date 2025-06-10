"""
Player module for Kevin's Adventure Game.
"""
from typing import Dict, List, Optional

from kevin_adventure.core.entity import Entity


class Player(Entity):
    """
    Player class representing the game's protagonist.
    """

    def __init__(self, name: str):
        """
        Initialize a new player.

        Args:
            name: The player's name
        """
        super().__init__(name)
        self.health: int = 100
        self.inventory: List[str] = []
        self.location: str = "Village"
        self.gold: int = 100
        self.agility: int = 10
        self.perception: int = 10

    def get_status(self) -> str:
        """
        Get the player's current status.

        Returns:
            A string representation of the player's status
        """
        from kevin_adventure.utils.text_formatting import format_inventory
        return f"Health: {self.health} | Inventory: {format_inventory(self.inventory)} | Gold: {self.gold}"

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
            new_location: The location to move to
        """
        self.location = new_location
        print(f"You moved to: {new_location}")

    def heal(self, amount: int) -> None:
        """
        Heal the player.

        Args:
            amount: The amount to heal
        """
        self.health = min(100, self.health + amount)
        print(f"You healed for {amount} health. Current health: {self.health}")

    def damage(self, amount: int) -> None:
        """
        Damage the player.

        Args:
            amount: The amount of damage to take
        """
        self.health = max(0, self.health - amount)
        print(f"You took {amount} damage. Current health: {self.health}")
        if self.health == 0:
            print("You have been defeated.")
            from kevin_adventure.utils.text_formatting import print_game_over
            print_game_over()

    def to_dict(self) -> Dict:
        """
        Convert the player to a dictionary for saving.

        Returns:
            A dictionary representation of the player
        """
        return {
            "name": self.name,
            "health": self.health,
            "inventory": self.inventory,
            "location": self.location,
            "gold": self.gold,
            "agility": self.agility,
            "perception": self.perception
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'Player':
        """
        Create a player from a dictionary.

        Args:
            data: The dictionary to create the player from

        Returns:
            A new Player instance
        """
        player = cls(data["name"])
        player.health = data["health"]
        player.inventory = data["inventory"]
        player.location = data["location"]
        player.gold = data["gold"]
        player.agility = data.get("agility", 10)
        player.perception = data.get("perception", 10)
        return player

