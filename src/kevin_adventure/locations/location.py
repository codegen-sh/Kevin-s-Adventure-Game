"""
Location module for Kevin's Adventure Game.
"""
from typing import Dict, List, Optional

from kevin_adventure.core.entity import Entity


class Location(Entity):
    """
    Base class for all locations in the game.
    """

    def __init__(self, name: str, description: str, connections: List[str] = None, items: List[str] = None):
        """
        Initialize a new location.

        Args:
            name: The location's name
            description: The location's description
            connections: List of connected locations
            items: List of items in the location
        """
        super().__init__(name)
        self.description = description
        self.connections = connections or []
        self.items = items or []

    def interact(self, player, world) -> None:
        """
        Interact with the location.

        Args:
            player: The player interacting with the location
            world: The game world
        """
        print(f"You interact with {self.name}, but nothing special happens.")

    def to_dict(self) -> Dict:
        """
        Convert the location to a dictionary for saving.

        Returns:
            A dictionary representation of the location
        """
        return {
            "name": self.name,
            "description": self.description,
            "connections": self.connections,
            "items": self.items
        }

    def update_from_dict(self, data: Dict) -> None:
        """
        Update the location from a dictionary.

        Args:
            data: The dictionary to update the location from
        """
        self.description = data.get("description", self.description)
        self.connections = data.get("connections", self.connections)
        self.items = data.get("items", self.items)

