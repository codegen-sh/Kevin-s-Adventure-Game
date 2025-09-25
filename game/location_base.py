"""
Base location class and interface for all game locations.
"""
from abc import ABC, abstractmethod
from typing import Dict, Any, List, Optional
from game.player import Player


class Location(ABC):
    """
    Abstract base class for all game locations.
    """
    
    def __init__(self, name: str, description: str, connections: List[str], items: List[str] = None):
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
        self.connections = connections
        self.items = items or []
        self.visited = False
        self.special_state = {}
    
    @abstractmethod
    def explore(self, world: Dict[str, Any], player: Player) -> None:
        """
        Handle location-specific exploration and interactions.
        
        Args:
            world: World state dictionary
            player: Player instance
        """
        pass
    
    def get_description(self) -> str:
        """Get the location description."""
        return self.description
    
    def get_connections(self) -> List[str]:
        """Get list of connected locations."""
        return self.connections.copy()
    
    def get_items(self) -> List[str]:
        """Get list of available items."""
        return self.items.copy()
    
    def add_item(self, item: str) -> None:
        """Add an item to this location."""
        if item not in self.items:
            self.items.append(item)
    
    def remove_item(self, item: str) -> bool:
        """
        Remove an item from this location.
        
        Args:
            item: Item to remove
            
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
    
    def mark_visited(self) -> None:
        """Mark this location as visited."""
        self.visited = True
    
    def is_visited(self) -> bool:
        """Check if this location has been visited."""
        return self.visited
    
    def set_special_state(self, key: str, value: Any) -> None:
        """Set a special state value for this location."""
        self.special_state[key] = value
    
    def get_special_state(self, key: str, default: Any = None) -> Any:
        """Get a special state value for this location."""
        return self.special_state.get(key, default)
    
    def has_special_state(self, key: str) -> bool:
        """Check if location has a specific special state."""
        return key in self.special_state
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert location to dictionary format."""
        return {
            "description": self.description,
            "connections": self.connections.copy(),
            "items": self.items.copy(),
            "visited": self.visited,
            "special_state": self.special_state.copy()
        }
    
    def update_from_dict(self, data: Dict[str, Any]) -> None:
        """Update location from dictionary data."""
        self.description = data.get("description", self.description)
        self.connections = data.get("connections", self.connections)
        self.items = data.get("items", self.items)
        self.visited = data.get("visited", self.visited)
        self.special_state = data.get("special_state", self.special_state)


class InteractiveLocation(Location):
    """
    Base class for locations with interactive menus.
    """
    
    def __init__(self, name: str, description: str, connections: List[str], items: List[str] = None):
        super().__init__(name, description, connections, items)
        self.menu_options = []
    
    def add_menu_option(self, option: str, description: str, action: callable) -> None:
        """
        Add a menu option to this location.
        
        Args:
            option: Option key/number
            description: Option description
            action: Function to call when option is selected
        """
        self.menu_options.append({
            "option": option,
            "description": description,
            "action": action
        })
    
    def show_menu(self) -> None:
        """Display the location's interactive menu."""
        print(f"\n=== {self.name} ===")
        print(self.description)
        print("\nWhat would you like to do?")
        
        for i, menu_item in enumerate(self.menu_options, 1):
            print(f"{i}. {menu_item['description']}")
        
        print(f"{len(self.menu_options) + 1}. Leave {self.name}")
    
    def handle_menu_choice(self, choice: str, world: Dict[str, Any], player: Player) -> bool:
        """
        Handle menu choice selection.
        
        Args:
            choice: User's choice
            world: World state dictionary
            player: Player instance
            
        Returns:
            True if choice was handled, False if invalid
        """
        try:
            choice_num = int(choice)
            if 1 <= choice_num <= len(self.menu_options):
                menu_item = self.menu_options[choice_num - 1]
                menu_item["action"](world, player)
                return True
            elif choice_num == len(self.menu_options) + 1:
                print(f"You leave {self.name}.")
                return True
            else:
                print(f"Invalid choice. Please enter a number between 1 and {len(self.menu_options) + 1}.")
                return False
        except ValueError:
            print("Invalid input. Please enter a number.")
            return False
    
    def explore(self, world: Dict[str, Any], player: Player) -> None:
        """
        Default exploration behavior for interactive locations.
        
        Args:
            world: World state dictionary
            player: Player instance
        """
        self.mark_visited()
        
        while True:
            self.show_menu()
            try:
                choice = input("Enter your choice: ").strip()
                if self.handle_menu_choice(choice, world, player):
                    break
            except (KeyboardInterrupt, EOFError):
                print(f"\nReturning to {self.name} entrance.")
                break


class SimpleLocation(Location):
    """
    Simple location with basic description and no special interactions.
    """
    
    def explore(self, world: Dict[str, Any], player: Player) -> None:
        """
        Simple exploration - just show description and mark as visited.
        
        Args:
            world: World state dictionary
            player: Player instance
        """
        self.mark_visited()
        print(f"\n{self.description}")
        
        if self.items:
            print(f"You can see: {', '.join(self.items)}")
        
        if self.connections:
            print(f"You can travel to: {', '.join(self.connections)}")


def create_location_from_dict(name: str, data: Dict[str, Any]) -> Location:
    """
    Create a location instance from dictionary data.
    
    Args:
        name: Location name
        data: Location data dictionary
        
    Returns:
        Location instance
    """
    # For now, create simple locations. This can be extended to create
    # specific location types based on the name or data content.
    location = SimpleLocation(
        name=name,
        description=data.get("description", "A mysterious place."),
        connections=data.get("connections", []),
        items=data.get("items", [])
    )
    
    # Update with any saved state
    location.update_from_dict(data)
    
    return location
