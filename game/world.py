"""
World module for Kevin's Adventure Game.
This module handles the game world, locations, and navigation.
"""

from locations.cave import explore_cave
from locations.forest import enter_forest
from locations.mountain import climb_mountain
from locations.village import visit_village


class Location:
    """
    Represents a location in the game world.
    """
    
    def __init__(self, name, description, connections=None, items=None):
        """
        Initialize a new Location.
        
        Args:
            name (str): The name of the location
            description (str): A description of the location
            connections (list): A list of connected location names
            items (list): A list of items available at this location
        """
        self.name = name
        self.description = description
        self.connections = connections or []
        self.items = items or []
    
    def add_connection(self, location_name):
        """
        Add a connection to another location.
        
        Args:
            location_name (str): The name of the location to connect to
        """
        if location_name not in self.connections:
            self.connections.append(location_name)
    
    def remove_connection(self, location_name):
        """
        Remove a connection to another location.
        
        Args:
            location_name (str): The name of the location to disconnect from
        """
        if location_name in self.connections:
            self.connections.remove(location_name)
    
    def add_item(self, item):
        """
        Add an item to this location.
        
        Args:
            item (str): The item to add
        """
        self.items.append(item)
    
    def remove_item(self, item):
        """
        Remove an item from this location.
        
        Args:
            item (str): The item to remove
            
        Returns:
            bool: True if the item was removed, False if it wasn't at this location
        """
        if item in self.items:
            self.items.remove(item)
            return True
        return False
    
    def to_dict(self):
        """
        Convert the location to a dictionary for saving.
        
        Returns:
            dict: A dictionary representation of the location
        """
        return {
            "description": self.description,
            "connections": self.connections.copy(),
            "items": self.items.copy()
        }
    
    @classmethod
    def from_dict(cls, name, data):
        """
        Create a Location instance from a dictionary.
        
        Args:
            name (str): The name of the location
            data (dict): A dictionary with location data
            
        Returns:
            Location: A new Location instance with the loaded data
        """
        return cls(
            name=name,
            description=data["description"],
            connections=data["connections"],
            items=data["items"]
        )


class World:
    """
    Represents the game world, containing locations and the current state.
    """
    
    def __init__(self, current_location="Village", locations=None):
        """
        Initialize a new World.
        
        Args:
            current_location (str): The name of the starting location
            locations (dict): A dictionary of Location objects
        """
        self.current_location = current_location
        self.locations = locations or {}
    
    def add_location(self, location):
        """
        Add a location to the world.
        
        Args:
            location (Location): The location to add
        """
        self.locations[location.name] = location
    
    def get_location(self, location_name):
        """
        Get a location by name.
        
        Args:
            location_name (str): The name of the location to get
            
        Returns:
            Location: The requested location, or None if it doesn't exist
        """
        return self.locations.get(location_name)
    
    def get_current_location_name(self):
        """
        Get the name of the current location.
        
        Returns:
            str: The name of the current location
        """
        return self.current_location
    
    def get_current_location(self):
        """
        Get the current location object.
        
        Returns:
            Location: The current location object
        """
        return self.locations[self.current_location]
    
    def get_location_description(self, location_name):
        """
        Get the description of a location.
        
        Args:
            location_name (str): The name of the location
            
        Returns:
            str: The description of the location
        """
        location = self.get_location(location_name)
        return location.description if location else "Unknown location"
    
    def get_available_locations(self):
        """
        Get a list of locations connected to the current location.
        
        Returns:
            list: A list of location names
        """
        current_location = self.get_current_location()
        return current_location.connections
    
    def change_location(self, new_location):
        """
        Change the current location.
        
        Args:
            new_location (str): The name of the new location
            
        Returns:
            bool: True if the location was changed, False if the new location is not accessible
        """
        if new_location in self.get_available_locations():
            self.current_location = new_location
            return True
        return False
    
    def interact_with_location(self, player):
        """
        Interact with the current location.
        
        Args:
            player: The player object
        """
        current_location = self.current_location
        
        if current_location == "Forest":
            enter_forest(self, player)
        elif current_location == "Cave":
            explore_cave(self, player)
        elif current_location == "Village":
            visit_village(self, player)
        elif current_location == "Mountain":
            climb_mountain(self, player)
        else:
            print("There's nothing special to interact with here.")
    
    def is_location_accessible(self, location_name):
        """
        Check if a location is accessible from the current location.
        
        Args:
            location_name (str): The name of the location to check
            
        Returns:
            bool: True if the location is accessible, False otherwise
        """
        return location_name in self.get_available_locations()
    
    def get_all_locations(self):
        """
        Get a list of all location names in the world.
        
        Returns:
            list: A list of all location names
        """
        return list(self.locations.keys())
    
    def to_dict(self):
        """
        Convert the world to a dictionary for saving.
        
        Returns:
            dict: A dictionary representation of the world
        """
        locations_dict = {}
        for name, location in self.locations.items():
            locations_dict[name] = location.to_dict()
        
        return {
            "current_location": self.current_location,
            "locations": locations_dict
        }
    
    @classmethod
    def from_dict(cls, data):
        """
        Create a World instance from a dictionary.
        
        Args:
            data (dict): A dictionary with world data
            
        Returns:
            World: A new World instance with the loaded data
        """
        world = cls(current_location=data["current_location"])
        
        for name, location_data in data["locations"].items():
            location = Location.from_dict(name, location_data)
            world.add_location(location)
        
        return world


def initialize_world():
    """
    Initialize a new game world with default locations.
    
    Returns:
        dict: A dictionary representation of the world (for backward compatibility)
    """
    world = World()
    
    # Create locations
    village = Location(
        name="Village",
        description="A small, peaceful village with thatched-roof houses and friendly inhabitants.",
        connections=["Forest", "Mountain"],
        items=["map", "bread"]
    )
    
    forest = Location(
        name="Forest",
        description="A dense, mysterious forest with towering trees and the sound of rustling leaves.",
        connections=["Village", "Cave"],
        items=["stick", "berries"]
    )
    
    cave = Location(
        name="Cave",
        description="A dark, damp cave with echoing sounds and glittering minerals on the walls.",
        connections=["Forest"],
        items=["torch", "gemstone"]
    )
    
    mountain = Location(
        name="Mountain",
        description="A tall, snow-capped mountain with treacherous paths and breathtaking views.",
        connections=["Village"],
        items=["rope", "pickaxe"]
    )
    
    # Add locations to the world
    world.add_location(village)
    world.add_location(forest)
    world.add_location(cave)
    world.add_location(mountain)
    
    # Return dictionary for backward compatibility
    return world.to_dict()


# Legacy functions for backward compatibility
def get_current_location(world):
    """Get the name of the current location."""
    if isinstance(world, World):
        return world.get_current_location_name()
    else:
        # Handle dictionary-based world for backward compatibility
        return world["current_location"]

def get_location_description(world, location):
    """Get the description of a location."""
    if isinstance(world, World):
        return world.get_location_description(location)
    else:
        # Handle dictionary-based world for backward compatibility
        return world["locations"][location]["description"]

def get_available_locations(world):
    """Get a list of locations connected to the current location."""
    if isinstance(world, World):
        return world.get_available_locations()
    else:
        # Handle dictionary-based world for backward compatibility
        current_location = get_current_location(world)
        return world["locations"][current_location]["connections"]

def change_location(world, new_location):
    """Change the current location."""
    if isinstance(world, World):
        return world.change_location(new_location)
    else:
        # Handle dictionary-based world for backward compatibility
        if new_location in get_available_locations(world):
            world["current_location"] = new_location
            return True
        return False

def interact_with_location(world, player):
    """Interact with the current location."""
    if isinstance(world, World):
        world.interact_with_location(player)
    else:
        # Handle dictionary-based world for backward compatibility
        current_location = get_current_location(world)
        
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
    """Check if a location is accessible from the current location."""
    if isinstance(world, World):
        return world.is_location_accessible(location)
    else:
        # Handle dictionary-based world for backward compatibility
        return location in get_available_locations(world)

def get_all_locations(world):
    """Get a list of all location names in the world."""
    if isinstance(world, World):
        return world.get_all_locations()
    else:
        # Handle dictionary-based world for backward compatibility
        return list(world["locations"].keys())

