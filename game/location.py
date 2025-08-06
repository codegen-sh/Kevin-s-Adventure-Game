"""
Location classes for Kevin's Adventure Game.
Defines the Location class and specific location implementations.
"""

from typing import List, Dict, Any, Optional, Callable
from abc import ABC, abstractmethod
import random


class Location(ABC):
    """
    Abstract base class for game locations.
    
    Attributes:
        name: Location name
        description: Location description
        items: List of items available at this location
        connections: List of connected location names
        visited: Whether the player has visited this location before
    """
    
    def __init__(self, name: str, description: str, connections: List[str] = None, items: List[str] = None):
        """
        Initialize a location.
        
        Args:
            name: Location name
            description: Location description  
            connections: List of connected location names
            items: List of items available at this location
        """
        self.name = name
        self.description = description
        self.connections = connections or []
        self.items = items or []
        self.visited = False
        self.special_state: Dict[str, Any] = {}
    
    def get_description(self) -> str:
        """
        Get the location description.
        
        Returns:
            Location description string
        """
        return self.description
    
    def get_full_description(self) -> str:
        """
        Get full location description including items and connections.
        
        Returns:
            Full description with items and available exits
        """
        desc = self.description
        
        if self.items:
            desc += f"\n\nYou can see: {', '.join(self.items)}"
        
        if self.connections:
            desc += f"\n\nYou can go to: {', '.join(self.connections)}"
        
        return desc
    
    def add_item(self, item: str) -> None:
        """Add an item to this location."""
        if item not in self.items:
            self.items.append(item)
    
    def remove_item(self, item: str) -> bool:
        """
        Remove an item from this location.
        
        Returns:
            True if item was removed, False if not found
        """
        if item in self.items:
            self.items.remove(item)
            return True
        return False
    
    def has_item(self, item: str) -> bool:
        """Check if location has a specific item."""
        return item in self.items
    
    def is_connected_to(self, location_name: str) -> bool:
        """Check if this location connects to another location."""
        return location_name in self.connections
    
    def add_connection(self, location_name: str) -> None:
        """Add a connection to another location."""
        if location_name not in self.connections:
            self.connections.append(location_name)
    
    def remove_connection(self, location_name: str) -> None:
        """Remove a connection to another location."""
        if location_name in self.connections:
            self.connections.remove(location_name)
    
    def visit(self) -> None:
        """Mark this location as visited."""
        self.visited = True
    
    @abstractmethod
    def interact(self, player, world) -> None:
        """
        Handle location-specific interactions.
        
        Args:
            player: Player instance
            world: World instance
        """
        pass
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert location to dictionary for saving."""
        return {
            "name": self.name,
            "description": self.description,
            "connections": self.connections.copy(),
            "items": self.items.copy(),
            "visited": self.visited,
            "special_state": self.special_state.copy()
        }


class Village(Location):
    """Village location implementation."""
    
    def __init__(self):
        super().__init__(
            name="Village",
            description="A small, peaceful village with thatched-roof houses and friendly inhabitants.",
            connections=["Forest", "Mountain"],
            items=["map", "bread"]
        )
    
    def interact(self, player, world) -> None:
        """Handle village-specific interactions."""
        from locations.village import visit_village
        visit_village(world, player)


class Forest(Location):
    """Forest location implementation."""
    
    def __init__(self):
        super().__init__(
            name="Forest", 
            description="A dense, mysterious forest with towering trees and the sound of rustling leaves.",
            connections=["Village", "Cave"],
            items=["stick", "berries"]
        )
    
    def interact(self, player, world) -> None:
        """Handle forest-specific interactions."""
        from locations.forest import enter_forest
        enter_forest(world, player)


class Cave(Location):
    """Cave location implementation."""
    
    def __init__(self):
        super().__init__(
            name="Cave",
            description="A dark, damp cave with echoing sounds and glittering minerals on the walls.",
            connections=["Forest"],
            items=["torch", "gemstone"]
        )
    
    def interact(self, player, world) -> None:
        """Handle cave-specific interactions."""
        from locations.cave import explore_cave
        explore_cave(world, player)


class Mountain(Location):
    """Mountain location implementation."""
    
    def __init__(self):
        super().__init__(
            name="Mountain",
            description="A tall, snow-capped mountain with treacherous paths and breathtaking views.",
            connections=["Village"],
            items=["rope", "pickaxe"]
        )
    
    def interact(self, player, world) -> None:
        """Handle mountain-specific interactions."""
        from locations.mountain import climb_mountain
        climb_mountain(world, player)


# Location factory for creating location instances
LOCATION_CLASSES = {
    "Village": Village,
    "Forest": Forest,
    "Cave": Cave,
    "Mountain": Mountain
}


def create_location(location_name: str) -> Optional[Location]:
    """
    Create a location instance by name.
    
    Args:
        location_name: Name of the location to create
        
    Returns:
        Location instance or None if not found
    """
    location_class = LOCATION_CLASSES.get(location_name)
    if location_class:
        return location_class()
    return None


def get_all_location_names() -> List[str]:
    """Get list of all available location names."""
    return list(LOCATION_CLASSES.keys())

