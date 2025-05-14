from game.entity import Entity
from locations.cave import explore_cave
from locations.forest import enter_forest
from locations.mountain import climb_mountain
from locations.village import visit_village


class Location(Entity):
    """
    Represents a location in the game world.
    
    This class handles location attributes, connections to other locations,
    and items available at the location.
    """
    
    def __init__(self, name, description="", connections=None, items=None):
        """
        Initialize a new Location.
        
        Args:
            name (str): The name of the location
            description (str, optional): A description of the location
            connections (list, optional): A list of connected locations
            items (list, optional): A list of items available at the location
        """
        super().__init__(name, description)
        self.connections = connections or []
        self.items = items or []
    
    def add_connection(self, location):
        """Add a connection to another location."""
        if location not in self.connections:
            self.connections.append(location)
    
    def remove_connection(self, location):
        """Remove a connection to another location."""
        if location in self.connections:
            self.connections.remove(location)
    
    def add_item(self, item):
        """Add an item to the location."""
        if item not in self.items:
            self.items.append(item)
    
    def remove_item(self, item):
        """Remove an item from the location."""
        if item in self.items:
            self.items.remove(item)
            return True
        return False


class World:
    """
    Represents the game world.
    
    This class manages locations, the player's current location,
    and interactions with the world.
    """
    
    def __init__(self):
        """Initialize a new World."""
        self.locations = {}
        self.current_location = None
        self.weather = "clear"
    
    def add_location(self, location):
        """Add a location to the world."""
        self.locations[location.name] = location
    
    def get_location(self, name):
        """Get a location by name."""
        return self.locations.get(name)
    
    def set_current_location(self, location_name):
        """Set the current location."""
        if location_name in self.locations:
            self.current_location = location_name
            return True
        return False
    
    def get_current_location(self):
        """Get the current location name."""
        return self.current_location
    
    def get_current_location_object(self):
        """Get the current location object."""
        return self.locations.get(self.current_location)
    
    def get_available_locations(self):
        """Get a list of available locations from the current location."""
        current_loc = self.get_current_location_object()
        return current_loc.connections if current_loc else []
    
    def is_location_accessible(self, location_name):
        """Check if a location is accessible from the current location."""
        return location_name in self.get_available_locations()
    
    def get_all_locations(self):
        """Get a list of all location names in the world."""
        return list(self.locations.keys())


def initialize_world():
    """
    Initialize the game world with default locations.
    
    For backward compatibility, returns a dictionary representation of the world.
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


def create_world():
    """
    Create a new World object with default locations.
    
    Returns:
        World: A new World object with default locations
    """
    world = World()
    
    # Create locations
    village = Location(
        "Village",
        "A small, peaceful village with thatched-roof houses and friendly inhabitants.",
        ["Forest", "Mountain"],
        ["map", "bread"]
    )
    
    forest = Location(
        "Forest",
        "A dense, mysterious forest with towering trees and the sound of rustling leaves.",
        ["Village", "Cave"],
        ["stick", "berries"]
    )
    
    cave = Location(
        "Cave",
        "A dark, damp cave with echoing sounds and glittering minerals on the walls.",
        ["Forest"],
        ["torch", "gemstone"]
    )
    
    mountain = Location(
        "Mountain",
        "A tall, snow-capped mountain with treacherous paths and breathtaking views.",
        ["Village"],
        ["rope", "pickaxe"]
    )
    
    # Add locations to the world
    world.add_location(village)
    world.add_location(forest)
    world.add_location(cave)
    world.add_location(mountain)
    
    # Set the starting location
    world.set_current_location("Village")
    
    return world


# Legacy functions for backward compatibility
def get_current_location(world):
    """Get the current location name."""
    if isinstance(world, World):
        return world.get_current_location()
    return world["current_location"]

def get_location_description(world, location):
    """Get the description of a location."""
    if isinstance(world, World):
        loc = world.get_location(location)
        return loc.description if loc else ""
    return world["locations"][location]["description"]

def get_available_locations(world):
    """Get a list of available locations from the current location."""
    if isinstance(world, World):
        return world.get_available_locations()
    current_location = get_current_location(world)
    return world["locations"][current_location]["connections"]

def change_location(world, new_location):
    """Change the current location."""
    if isinstance(world, World):
        return world.set_current_location(new_location)
    if new_location in get_available_locations(world):
        world["current_location"] = new_location
        return True
    return False

def interact_with_location(world, player):
    """Interact with the current location."""
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
    return location in get_available_locations(world)

def get_all_locations(world):
    """Get a list of all location names in the world."""
    if isinstance(world, World):
        return world.get_all_locations()
    return list(world["locations"].keys())
