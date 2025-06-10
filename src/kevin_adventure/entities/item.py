"""
Item class for the Kevin's Adventure Game.
"""
from typing import Dict, Any, Optional, Callable


class Item:
    """Represents an item in the game that can be picked up, dropped, and used."""

    def __init__(self, name: str, description: str = "", use_handler: Optional[Callable] = None):
        """
        Initialize a new item.
        
        Args:
            name: The name of the item
            description: A description of the item
            use_handler: A function that handles using the item
        """
        self.name = name
        self.description = description
        self.use_handler = use_handler

    def get_description(self) -> str:
        """Get the description of the item."""
        return self.description or f"A {self.name}. Nothing special about it."

    def use(self, player, world) -> bool:
        """
        Use the item.
        
        Args:
            player: The player using the item
            world: The game world
            
        Returns:
            bool: True if the item was used successfully, False otherwise
        """
        if self.use_handler:
            return self.use_handler(self, player, world)
        else:
            # Default behavior if no use handler is specified
            from kevin_adventure.ui.text_ui import TextUI
            ui = TextUI()
            ui.display_message(f"You're not sure how to use the {self.name}.")
            return False

    def to_dict(self) -> Dict[str, Any]:
        """Convert the item to a dictionary for saving."""
        return {
            "name": self.name,
            "description": self.description,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Item':
        """Create an item from a dictionary (for loading)."""
        from kevin_adventure.entities.item_registry import get_item_use_handler
        
        name = data["name"]
        description = data.get("description", "")
        
        # Get the use handler for this item type
        use_handler = get_item_use_handler(name)
        
        return cls(name=name, description=description, use_handler=use_handler)

