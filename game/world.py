from locations.cave import explore_cave
from locations.forest import enter_forest
from locations.mountain import climb_mountain
from locations.village import visit_village
from game.location import Location


class World:
    """
    Represents the game world containing all locations
    """
    
    def __init__(self, current_location="Village"):
        """
        Initialize the game world
        
        Args:
            current_location (str): Starting location name
        """
        self.current_location = current_location
        self.locations = {}
        self._initialize_default_locations()
    
    def _initialize_default_locations(self):
        """Initialize the default game locations"""
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
        self.locations = {
            "Village": village,
            "Forest": forest,
            "Cave": cave,
            "Mountain": mountain
        }
    
    def get_current_location(self):
        """Get the current location name"""
        return self.current_location
    
    def get_current_location_obj(self):
        """Get the current location object"""
        return self.locations.get(self.current_location)
    
    def get_location(self, location_name):
        """
        Get a location object by name
        
        Args:
            location_name (str): Name of the location
            
        Returns:
            Location: Location object or None if not found
        """
        return self.locations.get(location_name)
    
    def get_location_description(self, location_name):
        """
        Get description of a location
        
        Args:
            location_name (str): Name of the location
            
        Returns:
            str: Location description
        """
        location = self.get_location(location_name)
        return location.description if location else "Unknown location."
    
    def get_available_locations(self):
        """
        Get locations accessible from current location
        
        Returns:
            list: List of accessible location names
        """
        current_loc = self.get_current_location_obj()
        return current_loc.get_connections() if current_loc else []
    
    def change_location(self, new_location):
        """
        Change current location if accessible
        
        Args:
            new_location (str): Name of new location
            
        Returns:
            bool: True if location changed successfully
        """
        if self.is_location_accessible(new_location):
            self.current_location = new_location
            return True
        return False
    
    def is_location_accessible(self, location_name):
        """
        Check if a location is accessible from current location
        
        Args:
            location_name (str): Name of location to check
            
        Returns:
            bool: True if accessible
        """
        current_loc = self.get_current_location_obj()
        return current_loc.is_connected_to(location_name) if current_loc else False
    
    def get_all_locations(self):
        """
        Get all location names
        
        Returns:
            list: List of all location names
        """
        return list(self.locations.keys())
    
    def add_location(self, location):
        """
        Add a new location to the world
        
        Args:
            location (Location): Location object to add
        """
        self.locations[location.name] = location
    
    def remove_location(self, location_name):
        """
        Remove a location from the world
        
        Args:
            location_name (str): Name of location to remove
        """
        if location_name in self.locations:
            del self.locations[location_name]
    
    def interact_with_location(self, player):
        """
        Interact with the current location
        
        Args:
            player: Player object
        """
        current_location = self.get_current_location()
        
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
    
    def to_dict(self):
        """
        Convert world to dictionary for saving
        
        Returns:
            dict: World data as dictionary
        """
        return {
            "current_location": self.current_location,
            "locations": {name: loc.to_dict() for name, loc in self.locations.items()}
        }
    
    @classmethod
    def from_dict(cls, data):
        """
        Create world from dictionary data
        
        Args:
            data (dict): World data dictionary
            
        Returns:
            World: New world instance
        """
        world = cls(current_location=data.get("current_location", "Village"))
        
        # Load locations
        locations_data = data.get("locations", {})
        world.locations = {}
        for name, loc_data in locations_data.items():
            world.locations[name] = Location.from_dict(loc_data)
        
        return world


def initialize_world():
    """Create a new world (backward compatibility)"""
    return World()


# Backward compatibility functions for existing code
def get_current_location(world):
    """Get current location (backward compatibility)"""
    if isinstance(world, World):
        return world.get_current_location()
    else:
        # Handle old dictionary format
        return world["current_location"]

def get_location_description(world, location):
    """Get location description (backward compatibility)"""
    if isinstance(world, World):
        return world.get_location_description(location)
    else:
        # Handle old dictionary format
        return world["locations"][location]["description"]

def get_available_locations(world):
    """Get available locations (backward compatibility)"""
    if isinstance(world, World):
        return world.get_available_locations()
    else:
        # Handle old dictionary format
        current_location = get_current_location(world)
        return world["locations"][current_location]["connections"]

def change_location(world, new_location):
    """Change location (backward compatibility)"""
    if isinstance(world, World):
        return world.change_location(new_location)
    else:
        # Handle old dictionary format
        if new_location in get_available_locations(world):
            world["current_location"] = new_location
            return True
        return False

def interact_with_location(world, player):
    """Interact with location (backward compatibility)"""
    if isinstance(world, World):
        world.interact_with_location(player)
    else:
        # Handle old dictionary format
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
    """Check if location is accessible (backward compatibility)"""
    if isinstance(world, World):
        return world.is_location_accessible(location)
    else:
        # Handle old dictionary format
        return location in get_available_locations(world)

def get_all_locations(world):
    """Get all locations (backward compatibility)"""
    if isinstance(world, World):
        return world.get_all_locations()
    else:
        # Handle old dictionary format
        return list(world["locations"].keys())
