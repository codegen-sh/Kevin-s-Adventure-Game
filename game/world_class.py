"""
World Class - Object-oriented world representation for Kevin's Adventure Game
"""
from typing import Dict, List, Optional


class Location:
    """Represents a single location in the game world."""
    
    def __init__(self, name: str, description: str, connections: List[str] = None, items: List[str] = None):
        self.name = name
        self.description = description
        self.connections = connections or []
        self.items = items or []
        self.visited = False
        self.npcs = []
        self.special_features = []
    
    def __str__(self):
        return self.name
    
    def __repr__(self):
        return f"Location(name='{self.name}', connections={self.connections})"
    
    def add_item(self, item: str):
        """Add an item to this location."""
        self.items.append(item)
    
    def remove_item(self, item: str) -> bool:
        """Remove an item from this location."""
        if item in self.items:
            self.items.remove(item)
            return True
        return False
    
    def has_item(self, item: str) -> bool:
        """Check if this location has a specific item."""
        return item in self.items
    
    def add_connection(self, location_name: str):
        """Add a connection to another location."""
        if location_name not in self.connections:
            self.connections.append(location_name)
    
    def remove_connection(self, location_name: str):
        """Remove a connection to another location."""
        if location_name in self.connections:
            self.connections.remove(location_name)
    
    def is_connected_to(self, location_name: str) -> bool:
        """Check if this location is connected to another."""
        return location_name in self.connections
    
    def visit(self):
        """Mark this location as visited."""
        self.visited = True
    
    def get_full_description(self) -> str:
        """Get a full description including items and connections."""
        desc = self.description
        
        if self.items:
            desc += f"\n\nYou can see: {', '.join(self.items)}"
        
        if self.connections:
            desc += f"\n\nYou can travel to: {', '.join(self.connections)}"
        
        return desc


class World:
    """Represents the game world with all locations and their relationships."""
    
    def __init__(self):
        self.locations: Dict[str, Location] = {}
        self.current_location = "Village"
        self.time_of_day = "morning"
        self.weather = "clear"
        self.day_count = 1
    
    def add_location(self, location: Location):
        """Add a location to the world."""
        self.locations[location.name] = location
    
    def get_location(self, name: str) -> Optional[Location]:
        """Get a location by name."""
        return self.locations.get(name)
    
    def get_current_location(self) -> Optional[Location]:
        """Get the current location object."""
        return self.locations.get(self.current_location)
    
    def move_to_location(self, location_name: str) -> bool:
        """Move to a new location if possible."""
        current_loc = self.get_current_location()
        
        if not current_loc:
            return False
        
        if location_name not in current_loc.connections:
            return False
        
        if location_name not in self.locations:
            return False
        
        self.current_location = location_name
        self.locations[location_name].visit()
        return True
    
    def get_available_locations(self) -> List[str]:
        """Get list of locations accessible from current location."""
        current_loc = self.get_current_location()
        return current_loc.connections if current_loc else []
    
    def get_current_location_description(self) -> str:
        """Get description of current location."""
        current_loc = self.get_current_location()
        return current_loc.get_full_description() if current_loc else "You are nowhere."
    
    def add_item_to_location(self, location_name: str, item: str):
        """Add an item to a specific location."""
        location = self.get_location(location_name)
        if location:
            location.add_item(item)
    
    def remove_item_from_location(self, location_name: str, item: str) -> bool:
        """Remove an item from a specific location."""
        location = self.get_location(location_name)
        return location.remove_item(item) if location else False
    
    def advance_time(self):
        """Advance the time of day."""
        time_progression = {
            "morning": "afternoon",
            "afternoon": "evening", 
            "evening": "night",
            "night": "morning"
        }
        
        old_time = self.time_of_day
        self.time_of_day = time_progression.get(self.time_of_day, "morning")
        
        # If we've cycled back to morning, advance the day
        if old_time == "night" and self.time_of_day == "morning":
            self.day_count += 1
    
    def get_world_status(self) -> str:
        """Get current world status (time, weather, etc.)."""
        return f"Day {self.day_count}, {self.time_of_day.title()}, Weather: {self.weather.title()}"
    
    def to_dict(self) -> dict:
        """Convert world to dictionary for saving."""
        locations_dict = {}
        for name, location in self.locations.items():
            locations_dict[name] = {
                "description": location.description,
                "connections": location.connections.copy(),
                "items": location.items.copy(),
                "visited": location.visited
            }
        
        return {
            "current_location": self.current_location,
            "locations": locations_dict,
            "time_of_day": self.time_of_day,
            "weather": self.weather,
            "day_count": self.day_count
        }
    
    @classmethod
    def from_dict(cls, data: dict):
        """Create world from dictionary (for loading)."""
        world = cls()
        world.current_location = data.get("current_location", "Village")
        world.time_of_day = data.get("time_of_day", "morning")
        world.weather = data.get("weather", "clear")
        world.day_count = data.get("day_count", 1)
        
        # Recreate locations
        locations_data = data.get("locations", {})
        for name, loc_data in locations_data.items():
            location = Location(
                name=name,
                description=loc_data.get("description", ""),
                connections=loc_data.get("connections", []),
                items=loc_data.get("items", [])
            )
            location.visited = loc_data.get("visited", False)
            world.add_location(location)
        
        return world


def create_default_world() -> World:
    """Create the default game world with all locations."""
    world = World()
    
    # Create all locations
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
    
    # Add all locations to world
    world.add_location(village)
    world.add_location(forest)
    world.add_location(cave)
    world.add_location(mountain)
    
    # Mark village as visited (starting location)
    village.visit()
    
    return world

