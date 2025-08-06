"""
World module for Kevin's Adventure Game.
Contains the World class and world management functionality.
"""

from typing import Dict, List, Optional, Any
from game.location import Location, create_location, get_all_location_names


class World:
    """
    Represents the game world containing all locations.
    
    Attributes:
        current_location: Name of the current location
        locations: Dictionary of location name to Location instance
        global_state: Dictionary for storing global world state
    """
    
    def __init__(self):
        """Initialize the game world."""
        self.current_location = "Village"
        self.locations: Dict[str, Location] = {}
        self.global_state: Dict[str, Any] = {}
        self._initialize_locations()
    
    def _initialize_locations(self) -> None:
        """Initialize all game locations."""
        for location_name in get_all_location_names():
            location = create_location(location_name)
            if location:
                self.locations[location_name] = location
    
    def get_current_location(self) -> str:
        """Get the name of the current location."""
        return self.current_location
    
    def get_location(self, location_name: str) -> Optional[Location]:
        """
        Get a location instance by name.
        
        Args:
            location_name: Name of the location
            
        Returns:
            Location instance or None if not found
        """
        return self.locations.get(location_name)
    
    def get_current_location_instance(self) -> Optional[Location]:
        """Get the current location instance."""
        return self.get_location(self.current_location)
    
    def get_location_description(self, location_name: str = None) -> str:
        """
        Get description of a location.
        
        Args:
            location_name: Name of location, or None for current location
            
        Returns:
            Location description
        """
        if location_name is None:
            location_name = self.current_location
        
        location = self.get_location(location_name)
        if location:
            return location.get_description()
        return f"Unknown location: {location_name}"
    
    def get_available_locations(self) -> List[str]:
        """Get list of locations accessible from current location."""
        current_loc = self.get_current_location_instance()
        if current_loc:
            return current_loc.connections.copy()
        return []
    
    def change_location(self, new_location: str) -> bool:
        """
        Change the current location.
        
        Args:
            new_location: Name of the new location
            
        Returns:
            True if location change was successful, False otherwise
        """
        if self.is_location_accessible(new_location):
            self.current_location = new_location
            # Mark the new location as visited
            location = self.get_location(new_location)
            if location:
                location.visit()
            return True
        return False
    
    def is_location_accessible(self, location_name: str) -> bool:
        """
        Check if a location is accessible from the current location.
        
        Args:
            location_name: Name of the location to check
            
        Returns:
            True if location is accessible, False otherwise
        """
        return location_name in self.get_available_locations()
    
    def interact_with_current_location(self, player) -> None:
        """
        Interact with the current location.
        
        Args:
            player: Player instance
        """
        current_loc = self.get_current_location_instance()
        if current_loc:
            current_loc.interact(player, self)
        else:
            print("There's nothing special to interact with here.")
    
    def get_all_locations(self) -> List[str]:
        """Get list of all location names."""
        return list(self.locations.keys())
    
    def add_item_to_location(self, location_name: str, item: str) -> bool:
        """
        Add an item to a specific location.
        
        Args:
            location_name: Name of the location
            item: Item to add
            
        Returns:
            True if item was added, False if location not found
        """
        location = self.get_location(location_name)
        if location:
            location.add_item(item)
            return True
        return False
    
    def remove_item_from_location(self, location_name: str, item: str) -> bool:
        """
        Remove an item from a specific location.
        
        Args:
            location_name: Name of the location
            item: Item to remove
            
        Returns:
            True if item was removed, False if not found
        """
        location = self.get_location(location_name)
        if location:
            return location.remove_item(item)
        return False
    
    def get_location_items(self, location_name: str = None) -> List[str]:
        """
        Get items available at a location.
        
        Args:
            location_name: Name of location, or None for current location
            
        Returns:
            List of items at the location
        """
        if location_name is None:
            location_name = self.current_location
        
        location = self.get_location(location_name)
        if location:
            return location.items.copy()
        return []
    
    def set_global_state(self, key: str, value: Any) -> None:
        """Set a global world state value."""
        self.global_state[key] = value
    
    def get_global_state(self, key: str, default: Any = None) -> Any:
        """Get a global world state value."""
        return self.global_state.get(key, default)
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert world to dictionary for saving."""
        return {
            "current_location": self.current_location,
            "locations": {name: loc.to_dict() for name, loc in self.locations.items()},
            "global_state": self.global_state.copy()
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'World':
        """
        Create world from dictionary data.
        
        Args:
            data: Dictionary containing world data
            
        Returns:
            World instance created from the data
        """
        world = cls()
        world.current_location = data.get("current_location", "Village")
        world.global_state = data.get("global_state", {}).copy()
        
        # Restore location states
        locations_data = data.get("locations", {})
        for location_name, location_data in locations_data.items():
            location = world.get_location(location_name)
            if location:
                location.items = location_data.get("items", []).copy()
                location.visited = location_data.get("visited", False)
                location.special_state = location_data.get("special_state", {}).copy()
        
        return world


def initialize_world() -> World:
    """
    Initialize the game world (backward compatibility function).
    
    Returns:
        New World instance
    """
    return World()


# Backward compatibility functions for existing code
def get_current_location(world):
    """Get current location (backward compatibility function)."""
    if isinstance(world, World):
        return world.get_current_location()
    else:
        return world["current_location"]

def get_location_description(world, location):
    """Get location description (backward compatibility function)."""
    if isinstance(world, World):
        return world.get_location_description(location)
    else:
        return world["locations"][location]["description"]


def get_available_locations(world):
    """Get available locations (backward compatibility function)."""
    if isinstance(world, World):
        return world.get_available_locations()
    else:
        current_location = get_current_location(world)
        return world["locations"][current_location]["connections"]


def change_location(world, new_location):
    """Change location (backward compatibility function)."""
    if isinstance(world, World):
        return world.change_location(new_location)
    else:
        if new_location in get_available_locations(world):
            world["current_location"] = new_location
            return True
        return False


def interact_with_location(world, player):
    """Interact with location (backward compatibility function)."""
    if isinstance(world, World):
        world.interact_with_current_location(player)
    else:
        current_location = get_current_location(world)
        
        # Import here to avoid circular imports
        from locations.forest import enter_forest
        from locations.cave import explore_cave
        from locations.village import visit_village
        from locations.mountain import climb_mountain

        if current_location == "Forest":
            enter_forest(world, player)
        elif current_location == "Cave":
            explore_cave(world, player)
        elif current_location == "Village":
            visit_village(world, player)
        elif current_location == "Mountain":
            climb_mountain(world, player)
        else:
            print("There's nothing special to interact with here.")


def is_location_accessible(world, location):
    """Check if location is accessible (backward compatibility function)."""
    if isinstance(world, World):
        return world.is_location_accessible(location)
    else:
        return location in get_available_locations(world)


def get_all_locations(world):
    """Get all locations (backward compatibility function)."""
    if isinstance(world, World):
        return world.get_all_locations()
    else:
        return list(world["locations"].keys())
