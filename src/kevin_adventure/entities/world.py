"""
World class for the Kevin's Adventure Game.
"""
from typing import Dict, List, Optional, Any

from kevin_adventure.entities.location import Location
from kevin_adventure.entities.item_registry import create_item


class World:
    """Represents the game world with locations and their connections."""

    def __init__(self):
        """Initialize a new world."""
        self.locations: Dict[str, Location] = {}
        self.current_location: str = "Village"
        self.weather: str = "clear"
        self.state: Dict[str, Any] = {}  # For tracking world state changes

    def initialize(self) -> None:
        """Initialize the world with default locations."""
        # Create locations
        self._create_village()
        self._create_forest()
        self._create_cave()
        self._create_mountain()

    def _create_village(self) -> None:
        """Create the Village location."""
        village = Location(
            name="Village",
            description="A small, peaceful village with thatched-roof houses and friendly inhabitants.",
            connections=["Forest", "Mountain"]
        )
        village.add_item(create_item("map"))
        village.add_item(create_item("bread"))
        self.locations["Village"] = village

    def _create_forest(self) -> None:
        """Create the Forest location."""
        forest = Location(
            name="Forest",
            description="A dense, mysterious forest with towering trees and the sound of rustling leaves.",
            connections=["Village", "Cave"]
        )
        forest.add_item(create_item("stick"))
        forest.add_item(create_item("berries"))
        self.locations["Forest"] = forest

    def _create_cave(self) -> None:
        """Create the Cave location."""
        cave = Location(
            name="Cave",
            description="A dark, damp cave with echoing sounds and glittering minerals on the walls.",
            connections=["Forest"]
        )
        cave.add_item(create_item("torch"))
        cave.add_item(create_item("gemstone"))
        self.locations["Cave"] = cave

    def _create_mountain(self) -> None:
        """Create the Mountain location."""
        mountain = Location(
            name="Mountain",
            description="A tall, snow-capped mountain with treacherous paths and breathtaking views.",
            connections=["Village"]
        )
        mountain.add_item(create_item("rope"))
        mountain.add_item(create_item("pickaxe"))
        self.locations["Mountain"] = mountain

    def get_current_location(self) -> Location:
        """Get the current location object."""
        return self.locations[self.current_location]

    def get_location(self, location_name: str) -> Optional[Location]:
        """Get a location by name."""
        return self.locations.get(location_name)

    def get_location_description(self, location_name: str) -> str:
        """Get the description of a location."""
        location = self.get_location(location_name)
        if location:
            return location.get_description()
        return f"Unknown location: {location_name}"

    def get_available_locations(self) -> List[str]:
        """Get the names of locations connected to the current location."""
        current_location = self.get_current_location()
        return current_location.get_connections()

    def is_location_accessible(self, location_name: str) -> bool:
        """Check if a location is accessible from the current location."""
        return location_name in self.get_available_locations()

    def change_location(self, new_location: str) -> bool:
        """
        Change the current location.
        
        Args:
            new_location: The name of the new location
            
        Returns:
            bool: True if the location was changed, False otherwise
        """
        if self.is_location_accessible(new_location):
            self.current_location = new_location
            return True
        return False

    def get_all_locations(self) -> List[str]:
        """Get the names of all locations in the world."""
        return list(self.locations.keys())

    def update_state(self, key: str, value: Any) -> None:
        """Update a world state value."""
        self.state[key] = value

    def get_state(self, key: str, default: Any = None) -> Any:
        """Get a world state value."""
        return self.state.get(key, default)

    def change_weather(self, new_weather: str) -> None:
        """Change the current weather."""
        self.weather = new_weather

    def get_weather(self) -> str:
        """Get the current weather."""
        return self.weather

    def to_dict(self) -> Dict[str, Any]:
        """Convert the world to a dictionary for saving."""
        return {
            "current_location": self.current_location,
            "weather": self.weather,
            "state": self.state.copy(),
            "locations": {name: location.to_dict() for name, location in self.locations.items()}
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'World':
        """Create a world from a dictionary (for loading)."""
        from kevin_adventure.entities.location import Location
        
        world = cls()
        world.current_location = data["current_location"]
        world.weather = data.get("weather", "clear")
        world.state = data.get("state", {}).copy()
        
        # Create locations from saved data
        for name, location_data in data["locations"].items():
            world.locations[name] = Location.from_dict(location_data)
        
        return world

