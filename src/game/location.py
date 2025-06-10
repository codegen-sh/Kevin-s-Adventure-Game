"""
Location module for Kevin's Adventure Game.
Contains the Location base class that all specific locations inherit from.
"""
from typing import Dict, List, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from src.game.player import Player
    from src.game.world import World


class Location:
    """
    Base class for all locations in the game.
    """

    def __init__(self, name: str, description: str):
        """
        Initialize a new location.

        Args:
            name: The name of the location
            description: A description of the location
        """
        self.name = name
        self.description = description
        self.connections: List[str] = []
        self.items: List[str] = []

    def enter(self, player: 'Player', world: 'World') -> None:
        """
        Called when a player enters this location.
        Should be overridden by subclasses to provide location-specific behavior.

        Args:
            player: The player entering the location
            world: The game world
        """
        print(f"You are in {self.name}. {self.description}")

    def get_available_actions(self) -> Dict[str, str]:
        """
        Get a dictionary of available actions at this location.

        Returns:
            A dictionary mapping action numbers to descriptions
        """
        return {
            "1": "Look around",
            "2": "Check inventory",
            "3": "Leave"
        }

    def handle_action(self, action: str, player: 'Player', world: 'World') -> bool:
        """
        Handle a player action at this location.

        Args:
            action: The action to handle
            player: The player performing the action
            world: The game world

        Returns:
            True if the player wants to leave the location, False otherwise
        """
        if action == "1":  # Look around
            print(self.description)
            if self.items:
                print(f"You can see: {', '.join(self.items)}")
            return False
        elif action == "2":  # Check inventory
            print(f"Inventory: {', '.join(player.inventory) if player.inventory else 'empty'}")
            return False
        elif action == "3":  # Leave
            return True
        else:
            print("Invalid action. Try again.")
            return False

    def add_item(self, item: str) -> None:
        """
        Add an item to this location.

        Args:
            item: The item to add
        """
        if item not in self.items:
            self.items.append(item)

    def remove_item(self, item: str) -> bool:
        """
        Remove an item from this location.

        Args:
            item: The item to remove

        Returns:
            True if the item was removed, False otherwise
        """
        if item in self.items:
            self.items.remove(item)
            return True
        return False

