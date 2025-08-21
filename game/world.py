"""
World module for Kevin's Adventure Game.
Contains the World and Location classes and related functions.
"""
from locations.cave import explore_cave
from locations.forest import enter_forest
from locations.mountain import climb_mountain
from locations.village import visit_village


class Location:
    """
    Location class representing a game location.
    
    Attributes:
        name (str): The name of the location
        description (str): A description of the location
        connections (list): List of connected location names
        items (list): List of items available at the location
    """
    
    def __init__(self, name, description, connections=None, items=None):
        """
        Initialize a new Location instance.
        
        Args:
            name (str): The name of the location
            description (str): A description of the location
            connections (list, optional): List of connected location names. Defaults to empty list.
            items (list, optional): List of items available at the location. Defaults to empty list.
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
    
    def to_dict(self):
        """
        Convert the Location instance to a dictionary.
        
        Returns:
            dict: A dictionary representation of the location
        """
        return {
            "description": self.description,
            "connections": self.connections.copy(),
            "items": self.items.copy()
        }
    
    @classmethod
    def from_dict(cls, name, location_dict):
        """
        Create a Location instance from a dictionary.
        
        Args:
            name (str): The name of the location
            location_dict (dict): A dictionary representation of a location
            
        Returns:
            Location: A new Location instance
        """
        return cls(
            name=name,
            description=location_dict["description"],
            connections=location_dict["connections"].copy(),
            items=location_dict["items"].copy()
        )


class World:
    """
    World class representing the game world.
    
    Attributes:
        current_location (str): The name of the current location
        locations (dict): Dictionary of Location instances
    """
    
    def __init__(self, current_location="Village", locations=None):
        """
        Initialize a new World instance.
        
        Args:
            current_location (str, optional): The name of the current location. Defaults to "Village".
            locations (dict, optional): Dictionary of Location instances. Defaults to None.
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
            location_name (str): The name of the location
            
        Returns:
            Location: The location instance, or None if not found
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
        Get the current location instance.
        
        Returns:
            Location: The current location instance
        """
        return self.locations.get(self.current_location)
    
    def get_location_description(self, location_name):
        """
        Get the description of a location.
        
        Args:
            location_name (str): The name of the location
            
        Returns:
            str: The description of the location
        """
        location = self.get_location(location_name)
        return location.description if location else ""
    
    def get_available_locations(self):
        """
        Get the names of locations connected to the current location.
        
        Returns:
            list: List of connected location names
        """
        current_location = self.get_current_location()
        return current_location.connections if current_location else []
    
    def change_location(self, new_location):
        """
        Change the current location.
        
        Args:
            new_location (str): The name of the new location
            
        Returns:
            bool: True if the location was changed, False otherwise
        """
        if new_location in self.get_available_locations():
            self.current_location = new_location
            return True
        return False
    
    def interact_with_location(self, player):
        """
        Interact with the current location.
        
        Args:
            player: The player instance
        """
        current_location = self.get_current_location_name()
        
        if current_location == "Forest":
            enter_forest(self.to_dict(), player)
        elif current_location == "Cave":
            explore_cave(self.to_dict(), player)
        elif current_location == "Village":
            visit_village(self.to_dict(), player)
        elif current_location == "Mountain":
            climb_mountain(self.to_dict(), player)
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
    
    def get_all_location_names(self):
        """
        Get the names of all locations in the world.
        
        Returns:
            list: List of all location names
        """
        return list(self.locations.keys())
    
    def to_dict(self):
        """
        Convert the World instance to a dictionary.
        
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
    def from_dict(cls, world_dict):
        """
        Create a World instance from a dictionary.
        
        Args:
            world_dict (dict): A dictionary representation of a world
            
        Returns:
            World: A new World instance
        """
        world = cls(current_location=world_dict["current_location"])
        
        for name, location_dict in world_dict["locations"].items():
            location = Location.from_dict(name, location_dict)
            world.add_location(location)
        
        return world


# Initialize a default world
def initialize_world():
    """
    Initialize a default world with predefined locations.
    
    Returns:
        dict: A dictionary representation of the initialized world
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
    
    # Add locations to world
    world.add_location(village)
    world.add_location(forest)
    world.add_location(cave)
    world.add_location(mountain)
    
    return world.to_dict()


# Legacy functions for backward compatibility
def get_current_location(world):
    """
    Get the name of the current location.
    
    Args:
        world (dict): The game world state
        
    Returns:
        str: The name of the current location
    """
    if isinstance(world, World):
        return world.get_current_location_name()
    else:
        # Handle dictionary case for backward compatibility
        return world["current_location"]

def get_location_description(world, location):
    """
    Get the description of a location.
    
    Args:
        world (dict): The game world state
        location (str): The name of the location
        
    Returns:
        str: The description of the location
    """
    if isinstance(world, World):
        return world.get_location_description(location)
    else:
        # Handle dictionary case for backward compatibility
        return world["locations"][location]["description"]

def get_available_locations(world):
    """
    Get the names of locations connected to the current location.
    
    Args:
        world (dict): The game world state
        
    Returns:
        list: List of connected location names
    """
    if isinstance(world, World):
        return world.get_available_locations()
    else:
        # Handle dictionary case for backward compatibility
        current_location = get_current_location(world)
        return world["locations"][current_location]["connections"]

def change_location(world, new_location):
    """
    Change the current location.
    
    Args:
        world (dict): The game world state
        new_location (str): The name of the new location
        
    Returns:
        bool: True if the location was changed, False otherwise
    """
    if isinstance(world, World):
        return world.change_location(new_location)
    else:
        # Handle dictionary case for backward compatibility
        if new_location in get_available_locations(world):
            world["current_location"] = new_location
            return True
        return False

def interact_with_location(world, player):
    """
    Interact with the current location.
    
    Args:
        world (dict): The game world state
        player: The player instance
    """
    if isinstance(world, World):
        world.interact_with_location(player)
    else:
        # Handle dictionary case for backward compatibility
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
        world (dict): The game world state
        location (str): The name of the location to check
        
    Returns:
        bool: True if the location is accessible, False otherwise
    """
    if isinstance(world, World):
        return world.is_location_accessible(location)
    else:
        # Handle dictionary case for backward compatibility
        return location in get_available_locations(world)

def get_all_locations(world):
    """
    Get the names of all locations in the world.
    
    Args:
        world (dict): The game world state
        
    Returns:
        list: List of all location names
    """
    if isinstance(world, World):
        return world.get_all_location_names()
    else:
        # Handle dictionary case for backward compatibility
        return list(world["locations"].keys())

