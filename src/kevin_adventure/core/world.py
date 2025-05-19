"""
World module for Kevin's Adventure Game.
"""
from typing import Dict, List, Optional

from kevin_adventure.core.entity import Entity
from kevin_adventure.core.player import Player
from kevin_adventure.locations.location import Location


class World(Entity):
    """
    World class representing the game world.
    """

    def __init__(self, name: str = "Kevin's World"):
        """
        Initialize a new world.

        Args:
            name: The world's name
        """
        super().__init__(name)
        self.current_location: str = "Village"
        self.locations: Dict[str, Location] = {}
        self.weather: str = "clear"

    def initialize(self) -> None:
        """
        Initialize the world with default locations.
        """
        from kevin_adventure.locations.village import Village
        from kevin_adventure.locations.forest import Forest
        from kevin_adventure.locations.mountain import Mountain
        from kevin_adventure.locations.cave import Cave

        self.locations = {
            "Village": Village(),
            "Forest": Forest(),
            "Mountain": Mountain(),
            "Cave": Cave()
        }

    def get_current_location(self) -> str:
        """
        Get the current location.

        Returns:
            The current location name
        """
        return self.current_location

    def get_location_description(self, location: str) -> str:
        """
        Get the description of a location.

        Args:
            location: The location to get the description for

        Returns:
            The location's description
        """
        return self.locations[location].description

    def get_available_locations(self) -> List[str]:
        """
        Get the available locations from the current location.

        Returns:
            A list of available locations
        """
        return self.locations[self.current_location].connections

    def change_location(self, new_location: str) -> bool:
        """
        Change the current location.

        Args:
            new_location: The location to change to

        Returns:
            True if the location was changed, False otherwise
        """
        if new_location in self.get_available_locations():
            self.current_location = new_location
            return True
        return False

    def interact_with_location(self, player: Player) -> None:
        """
        Interact with the current location.

        Args:
            player: The player interacting with the location
        """
        self.locations[self.current_location].interact(player, self)

    def is_location_accessible(self, location: str) -> bool:
        """
        Check if a location is accessible from the current location.

        Args:
            location: The location to check

        Returns:
            True if the location is accessible, False otherwise
        """
        return location in self.get_available_locations()

    def get_all_locations(self) -> List[str]:
        """
        Get all locations in the world.

        Returns:
            A list of all locations
        """
        return list(self.locations.keys())

    def to_dict(self) -> Dict:
        """
        Convert the world to a dictionary for saving.

        Returns:
            A dictionary representation of the world
        """
        return {
            "name": self.name,
            "current_location": self.current_location,
            "weather": self.weather,
            "locations": {name: location.to_dict() for name, location in self.locations.items()}
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'World':
        """
        Create a world from a dictionary.

        Args:
            data: The dictionary to create the world from

        Returns:
            A new World instance
        """
        from kevin_adventure.locations.location import Location

        world = cls(data["name"])
        world.current_location = data["current_location"]
        world.weather = data.get("weather", "clear")
        
        # Initialize locations
        world.initialize()
        
        # Update locations from saved data
        for name, location_data in data["locations"].items():
            if name in world.locations:
                world.locations[name].update_from_dict(location_data)
        
        return world

