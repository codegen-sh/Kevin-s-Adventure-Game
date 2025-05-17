"""
World module for Kevin's Adventure Game.
Contains the World class that manages the game world state.
"""
from typing import Dict, List, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from src.game.location import Location
    from src.game.player import Player
    from src.game.weather import Weather


class World:
    """
    Represents the game world.
    Manages locations, weather, and game state.
    """

    def __init__(self):
        """Initialize a new game world."""
        self.locations: Dict[str, 'Location'] = {}
        self.current_location: str = "Village"
        self.weather: 'Weather' = None
        self.state: Dict[str, bool] = {
            "hidden_cave_discovered": False,
            "hidden_path_discovered": False,
            "map_revealed": False,
            "river_discovered": False,
            "clearing_discovered": False,
            "cave_discovered": False,
            "underground_lake_discovered": False,
            "hidden_passage_discovered": False,
            "ancient_writing_discovered": False,
            "cave_creature_heard": False,
        }

    def add_location(self, location: 'Location') -> None:
        """
        Add a location to the world.

        Args:
            location: The location to add
        """
        self.locations[location.name] = location

    def get_current_location(self) -> 'Location':
        """
        Get the current location object.

        Returns:
            The current location object
        """
        return self.locations[self.current_location]

    def change_location(self, new_location: str) -> bool:
        """
        Change the current location.

        Args:
            new_location: The name of the new location

        Returns:
            True if the location was changed, False otherwise
        """
        if new_location in self.get_available_locations():
            self.current_location = new_location
            return True
        return False

    def get_available_locations(self) -> List[str]:
        """
        Get a list of locations connected to the current location.

        Returns:
            A list of location names
        """
        return self.locations[self.current_location].connections

    def get_location_description(self, location_name: str) -> str:
        """
        Get the description of a location.

        Args:
            location_name: The name of the location

        Returns:
            The location description
        """
        return self.locations[location_name].description

    def update_state(self, key: str, value: bool = True) -> None:
        """
        Update the world state.

        Args:
            key: The state key to update
            value: The new value for the state
        """
        self.state[key] = value
        print(f"World state updated: {key} = {value}")

    def is_location_accessible(self, location_name: str) -> bool:
        """
        Check if a location is accessible from the current location.

        Args:
            location_name: The name of the location to check

        Returns:
            True if the location is accessible, False otherwise
        """
        return location_name in self.get_available_locations()

    def get_all_locations(self) -> List[str]:
        """
        Get a list of all locations in the world.

        Returns:
            A list of all location names
        """
        return list(self.locations.keys())

    def initialize_default_world(self) -> None:
        """Initialize the default world with standard locations."""
        from src.game.world_init import initialize_world
        
        # Get a fully initialized world
        new_world = initialize_world()
        
        # Copy all attributes from the new world to this one
        self.locations = new_world.locations
        self.current_location = new_world.current_location
        self.weather = new_world.weather
        self.state = new_world.state
