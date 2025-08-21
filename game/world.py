from locations.cave import explore_cave
from locations.forest import enter_forest
from locations.mountain import climb_mountain
from locations.village import visit_village


class World:
    """
    A class to represent the game world.
    
    Attributes:
        current_location (str): The player's current location
        locations (dict): A dictionary of locations in the world
        weather (str): The current weather
        time (int): The current time (in minutes)
        visibility (str): The current visibility level
        hidden_locations (list): A list of hidden locations
    """
    
    def __init__(self, current_location="Village", locations=None, weather="clear", time=0, visibility="normal", hidden_locations=None):
        """
        Initialize a new World.
        
        Args:
            current_location (str, optional): The initial current location. Defaults to "Village".
            locations (dict, optional): A dictionary of locations. Defaults to None.
            weather (str, optional): The initial weather. Defaults to "clear".
            time (int, optional): The initial time. Defaults to 0.
            visibility (str, optional): The initial visibility. Defaults to "normal".
            hidden_locations (list, optional): A list of hidden locations. Defaults to None.
        """
        self.current_location = current_location
        self.locations = locations if locations is not None else self._initialize_default_locations()
        self.weather = weather
        self.time = time
        self.visibility = visibility
        self.hidden_locations = hidden_locations if hidden_locations is not None else []
    
    def _initialize_default_locations(self):
        """
        Initialize the default locations in the world.
        
        Returns:
            dict: A dictionary of default locations
        """
        return {
            "Village": {
                "description": "A small, peaceful village with thatched-roof houses and friendly inhabitants.",
                "connections": ["Forest", "Mountain"],
                "items": ["map", "bread"]
            },
            "Forest": {
                "description": "A dense, mysterious forest with towering trees and the sound of rustling leaves.",
                "connections": ["Village", "Cave"],
                "items": ["stick", "berries"]
            },
            "Cave": {
                "description": "A dark, damp cave with echoing sounds and glittering minerals on the walls.",
                "connections": ["Forest"],
                "items": ["torch", "gemstone"]
            },
            "Mountain": {
                "description": "A tall, snow-capped mountain with treacherous paths and breathtaking views.",
                "connections": ["Village"],
                "items": ["rope", "pickaxe"]
            }
        }
    
    def get_current_location(self):
        """
        Get the current location.
        
        Returns:
            str: The current location
        """
        return self.current_location
    
    def get_location_description(self, location):
        """
        Get the description of a location.
        
        Args:
            location (str): The location to get the description of
        
        Returns:
            str: The description of the location
        """
        return self.locations[location]["description"]
    
    def get_available_locations(self):
        """
        Get the locations that can be reached from the current location.
        
        Returns:
            list: A list of available locations
        """
        return self.locations[self.current_location]["connections"]
    
    def change_location(self, new_location):
        """
        Change the current location.
        
        Args:
            new_location (str): The location to change to
        
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
            player: The player
        """
        current_location = self.get_current_location()
        
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
    
    def is_location_accessible(self, location):
        """
        Check if a location is accessible from the current location.
        
        Args:
            location (str): The location to check
        
        Returns:
            bool: True if the location is accessible, False otherwise
        """
        return location in self.get_available_locations()
    
    def get_all_locations(self):
        """
        Get all locations in the world.
        
        Returns:
            list: A list of all locations
        """
        return list(self.locations.keys())
    
    def add_location(self, name, description, connections, items):
        """
        Add a new location to the world.
        
        Args:
            name (str): The name of the location
            description (str): The description of the location
            connections (list): A list of connected locations
            items (list): A list of items at the location
        """
        self.locations[name] = {
            "description": description,
            "connections": connections,
            "items": items
        }
    
    def add_connection(self, location, connection):
        """
        Add a connection between two locations.
        
        Args:
            location (str): The location to add the connection to
            connection (str): The location to connect to
        
        Returns:
            bool: True if the connection was added, False otherwise
        """
        if location in self.locations and connection in self.locations:
            if connection not in self.locations[location]["connections"]:
                self.locations[location]["connections"].append(connection)
            if location not in self.locations[connection]["connections"]:
                self.locations[connection]["connections"].append(location)
            return True
        return False
    
    def to_dict(self):
        """
        Convert the world to a dictionary for saving.
        
        Returns:
            dict: A dictionary representation of the world
        """
        return {
            "current_location": self.current_location,
            "locations": self.locations,
            "weather": self.weather,
            "time": self.time,
            "visibility": self.visibility,
            "hidden_locations": self.hidden_locations
        }
    
    @classmethod
    def from_dict(cls, data):
        """
        Create a World from a dictionary.
        
        Args:
            data (dict): A dictionary representation of a world
        
        Returns:
            World: A new World instance
        """
        return cls(
            current_location=data.get("current_location", "Village"),
            locations=data.get("locations"),
            weather=data.get("weather", "clear"),
            time=data.get("time", 0),
            visibility=data.get("visibility", "normal"),
            hidden_locations=data.get("hidden_locations", [])
        )


# Legacy functions for backward compatibility
def initialize_world():
    """
    Initialize the game world.
    
    Returns:
        dict: A dictionary representing the world
    """
    return {
        "current_location": "Village",
        "locations": {
            "Village": {
                "description": "A small, peaceful village with thatched-roof houses and friendly inhabitants.",
                "connections": ["Forest", "Mountain"],
                "items": ["map", "bread"]
            },
            "Forest": {
                "description": "A dense, mysterious forest with towering trees and the sound of rustling leaves.",
                "connections": ["Village", "Cave"],
                "items": ["stick", "berries"]
            },
            "Cave": {
                "description": "A dark, damp cave with echoing sounds and glittering minerals on the walls.",
                "connections": ["Forest"],
                "items": ["torch", "gemstone"]
            },
            "Mountain": {
                "description": "A tall, snow-capped mountain with treacherous paths and breathtaking views.",
                "connections": ["Village"],
                "items": ["rope", "pickaxe"]
            }
        }
    }

def get_current_location(world):
    """
    Get the current location.
    
    Args:
        world (dict or World): The world
    
    Returns:
        str: The current location
    """
    if isinstance(world, World):
        return world.get_current_location()
    return world["current_location"]

def get_location_description(world, location):
    """
    Get the description of a location.
    
    Args:
        world (dict or World): The world
        location (str): The location to get the description of
    
    Returns:
        str: The description of the location
    """
    if isinstance(world, World):
        return world.get_location_description(location)
    return world["locations"][location]["description"]

def get_available_locations(world):
    """
    Get the locations that can be reached from the current location.
    
    Args:
        world (dict or World): The world
    
    Returns:
        list: A list of available locations
    """
    if isinstance(world, World):
        return world.get_available_locations()
    current_location = get_current_location(world)
    return world["locations"][current_location]["connections"]

def change_location(world, new_location):
    """
    Change the current location.
    
    Args:
        world (dict or World): The world
        new_location (str): The location to change to
    
    Returns:
        bool: True if the location was changed, False otherwise
    """
    if isinstance(world, World):
        return world.change_location(new_location)
    if new_location in get_available_locations(world):
        world["current_location"] = new_location
        return True
    return False

def interact_with_location(world, player):
    """
    Interact with the current location.
    
    Args:
        world (dict or World): The world
        player: The player
    """
    if isinstance(world, World):
        world.interact_with_location(player)
    else:
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
        world (dict or World): The world
        location (str): The location to check
    
    Returns:
        bool: True if the location is accessible, False otherwise
    """
    if isinstance(world, World):
        return world.is_location_accessible(location)
    return location in get_available_locations(world)

def get_all_locations(world):
    """
    Get all locations in the world.
    
    Args:
        world (dict or World): The world
    
    Returns:
        list: A list of all locations
    """
    if isinstance(world, World):
        return world.get_all_locations()
    return list(world["locations"].keys())

