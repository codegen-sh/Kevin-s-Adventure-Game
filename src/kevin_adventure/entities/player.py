"""
Player class for the Kevin's Adventure Game.
"""
from typing import Dict, List, Optional, Any

from kevin_adventure.entities.item import Item


class Player:
    """Represents the player character in the game."""

    def __init__(self, name: str = "Kevin", health: int = 100, gold: int = 100, location: str = "Village"):
        """Initialize a new player with default values."""
        self.name = name
        self.health = health
        self.inventory: List[Item] = []
        self.location = location
        self.gold = gold
        self.max_health = 100
        # Additional attributes that might be used in the future
        self.attributes = {
            "agility": 10,
            "perception": 10,
            "strength": 10,
        }

    def get_status(self) -> str:
        """Get a string representation of the player's status."""
        return f"Health: {self.health} | Inventory: {self.format_inventory()} | Gold: {self.gold}"

    def format_inventory(self) -> str:
        """Format the player's inventory for display."""
        if not self.inventory:
            return "empty"
        return ", ".join(item.name for item in self.inventory)

    def add_item(self, item: Item) -> None:
        """Add an item to the player's inventory."""
        self.inventory.append(item)

    def remove_item(self, item_name: str) -> Optional[Item]:
        """
        Remove an item from the player's inventory.
        
        Args:
            item_name: The name of the item to remove
            
        Returns:
            The removed item, or None if the item was not found
        """
        for i, item in enumerate(self.inventory):
            if item.name.lower() == item_name.lower():
                return self.inventory.pop(i)
        return None

    def get_item(self, item_name: str) -> Optional[Item]:
        """
        Get an item from the player's inventory without removing it.
        
        Args:
            item_name: The name of the item to get
            
        Returns:
            The item, or None if the item was not found
        """
        for item in self.inventory:
            if item.name.lower() == item_name.lower():
                return item
        return None

    def has_item(self, item_name: str) -> bool:
        """Check if the player has an item in their inventory."""
        return any(item.name.lower() == item_name.lower() for item in self.inventory)

    def move(self, new_location: str) -> None:
        """Move the player to a new location."""
        self.location = new_location

    def heal(self, amount: int) -> None:
        """Heal the player by a specified amount."""
        self.health = min(self.max_health, self.health + amount)

    def damage(self, amount: int) -> bool:
        """
        Damage the player by a specified amount.
        
        Args:
            amount: The amount of damage to deal
            
        Returns:
            True if the player is still alive, False if the player has died
        """
        self.health = max(0, self.health - amount)
        return self.health > 0

    def is_alive(self) -> bool:
        """Check if the player is alive."""
        return self.health > 0

    def modify_attribute(self, attribute: str, amount: int) -> None:
        """Modify a player attribute by a specified amount."""
        if attribute in self.attributes:
            self.attributes[attribute] = max(1, self.attributes[attribute] + amount)

    def get_attribute(self, attribute: str) -> int:
        """Get the value of a player attribute."""
        return self.attributes.get(attribute, 0)

    def to_dict(self) -> Dict[str, Any]:
        """Convert the player to a dictionary for saving."""
        return {
            "name": self.name,
            "health": self.health,
            "inventory": [item.to_dict() for item in self.inventory],
            "location": self.location,
            "gold": self.gold,
            "attributes": self.attributes.copy(),
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Player':
        """Create a player from a dictionary (for loading)."""
        from kevin_adventure.entities.item import Item
        
        player = cls(
            name=data["name"],
            health=data["health"],
            gold=data["gold"],
            location=data["location"]
        )
        
        player.inventory = [Item.from_dict(item_data) for item_data in data["inventory"]]
        player.attributes = data.get("attributes", {
            "agility": 10,
            "perception": 10,
            "strength": 10,
        })
        
        return player

