"""
Item module for Kevin's Adventure Game.
Contains the Item class and item-related functionality.
"""
from typing import Callable, Dict, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from src.game.player import Player
    from src.game.world import World


class Item:
    """
    Represents an item in the game.
    """

    def __init__(self, name: str, description: str):
        """
        Initialize a new item.

        Args:
            name: The name of the item
            description: A description of the item
        """
        self.name = name
        self.description = description

    def use(self, player: 'Player', world: 'World') -> bool:
        """
        Use the item.

        Args:
            player: The player using the item
            world: The game world

        Returns:
            True if the item was used successfully, False otherwise
        """
        print(f"You use the {self.name}, but nothing happens.")
        return True


class ItemRegistry:
    """
    Registry of all items in the game.
    """

    def __init__(self):
        """Initialize the item registry."""
        self.items: Dict[str, Item] = {}

    def register_item(self, item: Item) -> None:
        """
        Register an item in the registry.

        Args:
            item: The item to register
        """
        self.items[item.name] = item

    def get_item(self, name: str) -> Optional[Item]:
        """
        Get an item by name.

        Args:
            name: The name of the item

        Returns:
            The item if found, None otherwise
        """
        return self.items.get(name)

    def get_description(self, name: str) -> str:
        """
        Get the description of an item.

        Args:
            name: The name of the item

        Returns:
            The item description, or a default message if the item is not found
        """
        item = self.get_item(name)
        if item:
            return item.description
        return "A mysterious item."

