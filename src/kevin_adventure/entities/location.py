"""
Location class for the Kevin's Adventure Game.
"""
from typing import Dict, List, Optional, Any, Callable

from kevin_adventure.entities.item import Item


class Location:
    """Represents a location in the game world."""

    def __init__(self, name: str, description: str, connections: List[str] = None):
        """
        Initialize a new location.
        
        Args:
            name: The name of the location
            description: A description of the location
            connections: A list of location names that this location is connected to
        """
        self.name = name
        self.description = description
        self.connections = connections or []
        self.items: List[Item] = []
        self.interaction_handler: Optional[Callable] = None

    def get_description(self) -> str:
        """Get the description of the location."""
        return self.description

    def get_connections(self) -> List[str]:
        """Get the names of locations connected to this location."""
        return self.connections.copy()

    def add_connection(self, location_name: str) -> None:
        """Add a connection to another location."""
        if location_name not in self.connections:
            self.connections.append(location_name)

    def remove_connection(self, location_name: str) -> bool:
        """
        Remove a connection to another location.
        
        Args:
            location_name: The name of the location to disconnect from
            
        Returns:
            bool: True if the connection was removed, False if it didn't exist
        """
        if location_name in self.connections:
            self.connections.remove(location_name)
            return True
        return False

    def get_items(self) -> List[Item]:
        """Get all items in this location."""
        return self.items.copy()

    def add_item(self, item: Item) -> None:
        """Add an item to this location."""
        self.items.append(item)

    def remove_item(self, item_name: str) -> Optional[Item]:
        """
        Remove an item from this location.
        
        Args:
            item_name: The name of the item to remove
            
        Returns:
            The removed item, or None if the item was not found
        """
        for i, item in enumerate(self.items):
            if item.name.lower() == item_name.lower():
                return self.items.pop(i)
        return None

    def get_item(self, item_name: str) -> Optional[Item]:
        """
        Get an item from this location without removing it.
        
        Args:
            item_name: The name of the item to get
            
        Returns:
            The item, or None if the item was not found
        """
        for item in self.items:
            if item.name.lower() == item_name.lower():
                return item
        return None

    def has_item(self, item_name: str) -> bool:
        """Check if this location has an item."""
        return any(item.name.lower() == item_name.lower() for item in self.items)

    def set_interaction_handler(self, handler: Callable) -> None:
        """Set the interaction handler for this location."""
        self.interaction_handler = handler

    def interact(self, player, world) -> bool:
        """
        Interact with this location.
        
        Args:
            player: The player interacting with the location
            world: The game world
            
        Returns:
            bool: True if the interaction was successful, False otherwise
        """
        if self.interaction_handler:
            return self.interaction_handler(self, player, world)
        else:
            from kevin_adventure.ui.text_ui import TextUI
            ui = TextUI()
            ui.display_message(f"There's nothing special to interact with in the {self.name}.")
            return False

    def to_dict(self) -> Dict[str, Any]:
        """Convert the location to a dictionary for saving."""
        return {
            "name": self.name,
            "description": self.description,
            "connections": self.connections.copy(),
            "items": [item.to_dict() for item in self.items],
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Location':
        """Create a location from a dictionary (for loading)."""
        from kevin_adventure.entities.item import Item
        from kevin_adventure.entities.item_registry import get_item_use_handler
        
        location = cls(
            name=data["name"],
            description=data["description"],
            connections=data.get("connections", []).copy()
        )
        
        # Create items from saved data
        for item_data in data.get("items", []):
            item_name = item_data["name"]
            item_description = item_data.get("description", "")
            use_handler = get_item_use_handler(item_name)
            
            item = Item(name=item_name, description=item_description, use_handler=use_handler)
            location.add_item(item)
        
        # Set interaction handler based on location name
        from kevin_adventure.locations.location_registry import get_location_interaction_handler
        location.set_interaction_handler(get_location_interaction_handler(data["name"]))
        
        return location

