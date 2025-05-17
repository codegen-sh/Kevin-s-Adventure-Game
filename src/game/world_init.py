"""
World initialization module for Kevin's Adventure Game.
Contains functions for initializing the game world.
"""
from src.game.weather import Weather
from src.game.world import World
from src.locations.cave import Cave
from src.locations.forest import Forest
from src.locations.mountain import Mountain
from src.locations.village import Village


def initialize_world() -> World:
    """
    Initialize the game world with all locations.

    Returns:
        The initialized world
    """
    world = World()
    
    # Create locations
    village = Village()
    forest = Forest()
    mountain = Mountain()
    cave = Cave()
    
    # Add locations to the world
    world.add_location(village)
    world.add_location(forest)
    world.add_location(mountain)
    world.add_location(cave)
    
    # Set the starting location
    world.current_location = "Village"
    
    # Initialize weather
    world.weather = Weather()
    
    return world

