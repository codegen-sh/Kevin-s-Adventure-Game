"""
Base location abstract class for Kevin's Adventure Game.
Provides consistent interface for all game locations.
"""
from abc import ABC, abstractmethod
from typing import List, Dict, Any, Optional, Tuple
from dataclasses import dataclass


@dataclass
class LocationData:
    """
    Data class for location information.
    
    Attributes:
        name: The location's name
        description: Description of the location
        connections: List of connected location names
        items: List of items available at this location
        visited: Whether the player has visited this location before
        special_properties: Dictionary of special location properties
    """
    name: str
    description: str
    connections: List[str]
    items: List[str]
    visited: bool = False
    special_properties: Dict[str, Any] = None
    
    def __post_init__(self):
        if self.special_properties is None:
            self.special_properties = {}


class BaseLocation(ABC):
    """
    Abstract base class for all game locations.
    
    This class defines the interface that all locations must implement,
    ensuring consistency across the game world.
    """
    
    def __init__(self, location_data: LocationData) -> None:
        """
        Initialize the location with its data.
        
        Args:
            location_data: LocationData object containing location information
            
        Raises:
            ValueError: If location_data is invalid
        """
        if not isinstance(location_data, LocationData):
            raise ValueError("location_data must be a LocationData instance")
        
        self._data = location_data
        self._validate_location_data()
    
    def _validate_location_data(self) -> None:
        """Validate the location data."""
        if not self._data.name or not isinstance(self._data.name, str):
            raise ValueError("Location name must be a non-empty string")
        if not self._data.description or not isinstance(self._data.description, str):
            raise ValueError("Location description must be a non-empty string")
        if not isinstance(self._data.connections, list):
            raise ValueError("Connections must be a list")
        if not isinstance(self._data.items, list):
            raise ValueError("Items must be a list")
    
    @property
    def name(self) -> str:
        """Get the location's name."""
        return self._data.name
    
    @property
    def description(self) -> str:
        """Get the location's description."""
        return self._data.description
    
    @property
    def connections(self) -> List[str]:
        """Get the list of connected locations."""
        return self._data.connections.copy()
    
    @property
    def items(self) -> List[str]:
        """Get the list of items at this location."""
        return self._data.items.copy()
    
    @property
    def visited(self) -> bool:
        """Check if this location has been visited."""
        return self._data.visited
    
    @property
    def special_properties(self) -> Dict[str, Any]:
        """Get the special properties of this location."""
        return self._data.special_properties.copy()
    
    def mark_visited(self) -> None:
        """Mark this location as visited."""
        self._data.visited = True
    
    def add_item(self, item: str) -> bool:
        """
        Add an item to this location.
        
        Args:
            item: The item to add
            
        Returns:
            True if item was added, False if it already exists
            
        Raises:
            ValueError: If item is not a valid string
        """
        if not isinstance(item, str) or not item.strip():
            raise ValueError("Item must be a non-empty string")
        
        item = item.strip()
        if item not in self._data.items:
            self._data.items.append(item)
            print(f"A {item} has been added to {self.name}.")
            return True
        else:
            print(f"There's already a {item} in {self.name}.")
            return False
    
    def remove_item(self, item: str) -> bool:
        """
        Remove an item from this location.
        
        Args:
            item: The item to remove
            
        Returns:
            True if item was removed, False if not found
            
        Raises:
            ValueError: If item is not a valid string
        """
        if not isinstance(item, str) or not item.strip():
            raise ValueError("Item must be a non-empty string")
        
        item = item.strip()
        if item in self._data.items:
            self._data.items.remove(item)
            return True
        return False
    
    def has_item(self, item: str) -> bool:
        """
        Check if this location has a specific item.
        
        Args:
            item: The item to check for
            
        Returns:
            True if the item is present, False otherwise
        """
        if not isinstance(item, str):
            return False
        return item.strip() in self._data.items
    
    def is_connected_to(self, location_name: str) -> bool:
        """
        Check if this location is connected to another location.
        
        Args:
            location_name: Name of the location to check
            
        Returns:
            True if connected, False otherwise
        """
        if not isinstance(location_name, str):
            return False
        return location_name.strip() in self._data.connections
    
    def add_connection(self, location_name: str) -> bool:
        """
        Add a connection to another location.
        
        Args:
            location_name: Name of the location to connect to
            
        Returns:
            True if connection was added, False if it already exists
            
        Raises:
            ValueError: If location_name is not a valid string
        """
        if not isinstance(location_name, str) or not location_name.strip():
            raise ValueError("Location name must be a non-empty string")
        
        location_name = location_name.strip()
        if location_name not in self._data.connections:
            self._data.connections.append(location_name)
            return True
        return False
    
    def remove_connection(self, location_name: str) -> bool:
        """
        Remove a connection to another location.
        
        Args:
            location_name: Name of the location to disconnect from
            
        Returns:
            True if connection was removed, False if not found
        """
        if not isinstance(location_name, str):
            return False
        
        location_name = location_name.strip()
        if location_name in self._data.connections:
            self._data.connections.remove(location_name)
            return True
        return False
    
    def set_special_property(self, key: str, value: Any) -> None:
        """
        Set a special property for this location.
        
        Args:
            key: Property key
            value: Property value
            
        Raises:
            ValueError: If key is not a valid string
        """
        if not isinstance(key, str) or not key.strip():
            raise ValueError("Property key must be a non-empty string")
        
        self._data.special_properties[key.strip()] = value
    
    def get_special_property(self, key: str, default: Any = None) -> Any:
        """
        Get a special property value.
        
        Args:
            key: Property key
            default: Default value if key not found
            
        Returns:
            Property value or default
        """
        if not isinstance(key, str):
            return default
        return self._data.special_properties.get(key.strip(), default)
    
    def get_full_description(self) -> str:
        """
        Get the full description including any dynamic elements.
        
        Returns:
            Complete location description
        """
        base_desc = self.description
        
        # Add visited status for first-time visitors
        if not self.visited:
            base_desc = f"[First Visit] {base_desc}"
        
        # Add items description if any items are present
        if self.items:
            items_desc = ", ".join(self.items)
            base_desc += f"\n\nYou can see: {items_desc}"
        
        # Add connections description
        if self.connections:
            connections_desc = ", ".join(self.connections)
            base_desc += f"\n\nYou can travel to: {connections_desc}"
        
        return base_desc
    
    @abstractmethod
    def enter(self, player: 'Player', world: 'World') -> None:
        """
        Handle player entering this location.
        
        Args:
            player: The player entering the location
            world: The game world state
        """
        pass
    
    @abstractmethod
    def get_available_actions(self, player: 'Player', world: 'World') -> List[str]:
        """
        Get list of available actions at this location.
        
        Args:
            player: The current player
            world: The game world state
            
        Returns:
            List of available action names
        """
        pass
    
    @abstractmethod
    def perform_action(self, action: str, player: 'Player', world: 'World') -> bool:
        """
        Perform a specific action at this location.
        
        Args:
            action: The action to perform
            player: The current player
            world: The game world state
            
        Returns:
            True if action was successful, False otherwise
        """
        pass
    
    def get_random_event(self, player: 'Player', world: 'World') -> Optional[str]:
        """
        Get a random event that might occur at this location.
        
        Args:
            player: The current player
            world: The game world state
            
        Returns:
            Description of random event, or None if no event occurs
        """
        # Default implementation - no random events
        # Subclasses can override this to provide location-specific events
        return None
    
    def on_item_used(self, item: str, player: 'Player', world: 'World') -> bool:
        """
        Handle when an item is used at this location.
        
        Args:
            item: The item being used
            player: The current player
            world: The game world state
            
        Returns:
            True if the item had a special effect at this location, False otherwise
        """
        # Default implementation - no special item effects
        # Subclasses can override this to provide location-specific item interactions
        return False
    
    def to_dict(self) -> Dict[str, Any]:
        """
        Convert location to dictionary for saving.
        
        Returns:
            Dictionary representation of the location
        """
        return {
            "name": self._data.name,
            "description": self._data.description,
            "connections": self._data.connections.copy(),
            "items": self._data.items.copy(),
            "visited": self._data.visited,
            "special_properties": self._data.special_properties.copy()
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'BaseLocation':
        """
        Create a location from dictionary data.
        
        Args:
            data: Dictionary containing location data
            
        Returns:
            New location instance
            
        Raises:
            ValueError: If data is invalid or missing required fields
        """
        if not isinstance(data, dict):
            raise ValueError("Data must be a dictionary")
        
        required_fields = ["name", "description", "connections", "items"]
        for field in required_fields:
            if field not in data:
                raise ValueError(f"Missing required field: {field}")
        
        location_data = LocationData(
            name=data["name"],
            description=data["description"],
            connections=data["connections"].copy() if isinstance(data["connections"], list) else [],
            items=data["items"].copy() if isinstance(data["items"], list) else [],
            visited=data.get("visited", False),
            special_properties=data.get("special_properties", {}).copy() if isinstance(data.get("special_properties"), dict) else {}
        )
        
        return cls(location_data)


class GenericLocation(BaseLocation):
    """
    Generic location implementation for simple locations.
    
    This class provides a basic implementation of BaseLocation
    for locations that don't need special behavior.
    """
    
    def enter(self, player: 'Player', world: 'World') -> None:
        """Handle player entering this generic location."""
        if not self.visited:
            print(f"\n=== {self.name} ===")
            print(self.description)
            self.mark_visited()
        else:
            print(f"\nYou return to the {self.name}.")
        
        # Show available items
        if self.items:
            print(f"\nItems here: {', '.join(self.items)}")
    
    def get_available_actions(self, player: 'Player', world: 'World') -> List[str]:
        """Get available actions for generic location."""
        actions = ["look", "inventory", "status"]
        
        # Add item-related actions
        if self.items:
            actions.extend(["take", "examine"])
        
        # Add movement actions
        if self.connections:
            actions.append("go")
        
        return actions
    
    def perform_action(self, action: str, player: 'Player', world: 'World') -> bool:
        """Perform action at generic location."""
        action = action.lower().strip()
        
        if action == "look":
            print(self.get_full_description())
            return True
        elif action == "inventory":
            if player.inventory:
                print(f"Inventory: {', '.join(player.inventory)}")
            else:
                print("Your inventory is empty.")
            return True
        elif action == "status":
            print(player.get_status())
            return True
        elif action == "take":
            if self.items:
                print(f"Available items: {', '.join(self.items)}")
                item_choice = input("Which item would you like to take? ").strip()
                if self.has_item(item_choice):
                    self.remove_item(item_choice)
                    player.add_item(item_choice)
                    return True
                else:
                    print(f"There's no {item_choice} here.")
                    return False
            else:
                print("There are no items to take here.")
                return False
        elif action == "examine":
            if self.items:
                print(f"You can examine: {', '.join(self.items)}")
                # This would need item descriptions - could be enhanced
                return True
            else:
                print("There's nothing special to examine here.")
                return False
        elif action == "go":
            if self.connections:
                print(f"You can go to: {', '.join(self.connections)}")
                destination = input("Where would you like to go? ").strip()
                if self.is_connected_to(destination):
                    # The world should handle the actual movement
                    return True
                else:
                    print(f"You can't go to {destination} from here.")
                    return False
            else:
                print("There's nowhere to go from here.")
                return False
        else:
            print(f"You can't {action} here.")
            return False

