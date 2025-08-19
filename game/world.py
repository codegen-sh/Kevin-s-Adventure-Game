"""
World module for Kevin's Adventure Game.
This module handles the game world and locations.
"""
from locations.cave import explore_cave
from locations.forest import enter_forest
from locations.mountain import climb_mountain
from locations.village import visit_village


class Location:
    """
    Represents a location in the game world.
    
    Attributes:
        name (str): The name of the location
        description (str): A description of the location
        connections (list): A list of connected locations
        items (list): A list of items at the location
    """
    
    def __init__(self, name, description, connections=None, items=None):
        """
        Initialize a new Location instance.
        
        Args:
            name (str): The name of the location
            description (str): A description of the location
            connections (list, optional): A list of connected locations. Defaults to empty list.
            items (list, optional): A list of items at the location. Defaults to empty list.
        """
        self.name = name
        self.description = description
        self.connections = connections or []
        self.items = items or []
    
    def add_item(self, item):
        """
        Add an item to the location.
        
        Args:
            item (str): The item to add
        """
        self.items.append(item)
    
    def remove_item(self, item):
        """
        Remove an item from the location.
        
        Args:
            item (str): The item to remove
        
        Returns:
            bool: True if the item was removed, False otherwise
        """
        if item in self.items:
            self.items.remove(item)
            return True
        return False
    
    def has_item(self, item):
        """
        Check if the location has a specific item.
        
        Args:
            item (str): The item to check for
        
        Returns:
            bool: True if the location has the item, False otherwise
        """
        return item in self.items
    
    def add_connection(self, location):
        """
        Add a connection to another location.
        
        Args:
            location (str): The name of the location to connect to
        """
        if location not in self.connections:
            self.connections.append(location)
    
    def remove_connection(self, location):
        """
        Remove a connection to another location.
        
        Args:
            location (str): The name of the location to disconnect from
        
        Returns:
            bool: True if the connection was removed, False otherwise
        """
        if location in self.connections:
            self.connections.remove(location)
            return True
        return False
    
    def is_connected_to(self, location):
        """
        Check if this location is connected to another location.
        
        Args:
            location (str): The name of the location to check
        
        Returns:
            bool: True if the locations are connected, False otherwise
        """
        return location in self.connections


class World:
    """
    Represents the game world.
    
    Attributes:
        current_location (str): The name of the current location
        locations (dict): A dictionary of locations in the world
    """
    
    def __init__(self, current_location="Village", locations=None):
        """
        Initialize a new World instance.
        
        Args:
            current_location (str, optional): The name of the starting location. Defaults to "Village".
            locations (dict, optional): A dictionary of locations in the world. Defaults to None.
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
    
    def get_location(self, name):
        """
        Get a location by name.
        
        Args:
            name (str): The name of the location
        
        Returns:
            Location: The location with the given name, or None if not found
        """
        return self.locations.get(name)
    
    def get_current_location_name(self):
        """
        Get the name of the current location.
        
        Returns:
            str: The name of the current location
        """
        return self.current_location
    
    def get_current_location_object(self):
        """
        Get the current location object.
        
        Returns:
            Location: The current location object
        """
        return self.locations[self.current_location]
    
    def change_location(self, new_location):
        """
        Change the current location.
        
        Args:
            new_location (str): The name of the new location
        
        Returns:
            bool: True if the location was changed, False otherwise
        """
        current_loc = self.get_location(self.current_location)
        if current_loc and current_loc.is_connected_to(new_location):
            self.current_location = new_location
            return True
        return False
    
    def get_available_locations(self):
        """
        Get a list of locations connected to the current location.
        
        Returns:
            list: A list of location names
        """
        current_loc = self.get_location(self.current_location)
        return current_loc.connections if current_loc else []
    
    def interact_with_location(self, player):
        """
        Interact with the current location.
        
        Args:
            player: The player object
        """
        if self.current_location == "Forest":
            enter_forest(self.to_dict(), player)
        elif self.current_location == "Cave":
            explore_cave(self.to_dict(), player)
        elif self.current_location == "Village":
            visit_village(self.to_dict(), player)
        elif self.current_location == "Mountain":
            climb_mountain(self.to_dict(), player)
        else:
            print("There's nothing special to interact with here.")
    
    def to_dict(self):
        """
        Convert the world to a dictionary for backward compatibility.
        
        Returns:
            dict: A dictionary representation of the world
        """
        locations_dict = {}
        for name, location in self.locations.items():
            locations_dict[name] = {
                "description": location.description,
                "connections": location.connections,
                "items": location.items
            }
        
        return {
            "current_location": self.current_location,
            "locations": locations_dict
        }
    
    @classmethod
    def from_dict(cls, world_dict):
        """
        Create a World instance from a dictionary.
        
        Args:
            world_dict (dict): A dictionary representation of a world
        
        Returns:
            World: A new World instance
        """
        world = cls(current_location=world_dict["current_location"])
        
        for name, loc_data in world_dict["locations"].items():
            location = Location(
                name=name,
                description=loc_data["description"],
                connections=loc_data["connections"],
                items=loc_data["items"]
            )
            world.add_location(location)
        
        return world


def initialize_world():
    """
    Initialize a new game world.
    
    Returns:
        World: A new World instance with default locations
    """
    world = World(current_location="Village")
    
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
    
    return world


# Legacy functions for backward compatibility
def get_current_location(world):
    """
    Get the current location name.
    
    Args:
        world: The world object
    
    Returns:
        str: The name of the current location
    """
    if isinstance(world, World):
        return world.get_current_location_name()
    else:
        # For backward compatibility with dictionary-based world
        return world["current_location"]


def get_location_description(world, location):
    """
    Get the description of a location.
    
    Args:
        world: The world object
        location (str): The name of the location
    
    Returns:
        str: The description of the location
    """
    if isinstance(world, World):
        loc = world.get_location(location)
        return loc.description if loc else ""
    else:
        # For backward compatibility with dictionary-based world
        return world["locations"][location]["description"]


def get_available_locations(world):
    """
    Get a list of locations connected to the current location.
    
    Args:
        world: The world object
    
    Returns:
        list: A list of location names
    """
    if isinstance(world, World):
        return world.get_available_locations()
    else:
        # For backward compatibility with dictionary-based world
        current_location = get_current_location(world)
        return world["locations"][current_location]["connections"]


def change_location(world, new_location):
    """
    Change the current location.
    
    Args:
        world: The world object
        new_location (str): The name of the new location
    
    Returns:
        bool: True if the location was changed, False otherwise
    """
    if isinstance(world, World):
        return world.change_location(new_location)
    else:
        # For backward compatibility with dictionary-based world
        if new_location in get_available_locations(world):
            world["current_location"] = new_location
            return True
        return False


def interact_with_location(world, player):
    """
    Interact with the current location.
    
    Args:
        world: The world object
        player: The player object
    """
    if isinstance(world, World):
        world.interact_with_location(player)
    else:
        # For backward compatibility with dictionary-based world
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
    """
    Check if a location is accessible from the current location.
    
    Args:
        world: The world object
        location (str): The name of the location to check
    
    Returns:
        bool: True if the location is accessible, False otherwise
    """
    if isinstance(world, World):
        return location in world.get_available_locations()
    else:
        # For backward compatibility with dictionary-based world
        return location in get_available_locations(world)


def get_all_locations(world):
    """
    Get a list of all locations in the world.
    
    Args:
        world: The world object
    
    Returns:
        list: A list of location names
    """
    if isinstance(world, World):
        return list(world.locations.keys())
    else:
        # For backward compatibility with dictionary-based world
        return list(world["locations"].keys())

