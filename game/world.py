"""
World management module for Kevin's Adventure Game.

This module handles the game world state, location management, and world initialization.
It manages the connections between different locations and provides utilities for
world navigation and state tracking.
"""

from locations.cave import explore_cave
from locations.forest import enter_forest
from locations.mountain import climb_mountain
from locations.village import visit_village


def initialize_world():
    """
    Initialize the game world with all locations and their properties.
    
    Returns:
        dict: A dictionary containing world data with the following structure:
            - current_location (str): The starting location
            - locations (dict): Dictionary of location data, where each location has:
                - description (str): Text description of the location
                - connections (list): List of connected location names
                - items (list): List of items available at this location
    
    Example:
        >>> world = initialize_world()
        >>> print(world["current_location"])
        Village
        >>> print(len(world["locations"]))
        4
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
    Get the name of the current location in the world.
    
    Args:
        world (dict): The world state object
        
    Returns:
        str: The name of the current location
        
    Example:
        >>> world = initialize_world()
        >>> location = get_current_location(world)
        >>> print(location)
        Village
    """
    return world["current_location"]

def get_location_description(world, location):
    """
    Get the description of a specific location.
    
    Args:
        world (dict): The world state object
        location (str): The name of the location
        
    Returns:
        str: The description of the location, or a default message if not found
        
    Example:
        >>> world = initialize_world()
        >>> desc = get_location_description(world, "Village")
        >>> print("peaceful" in desc)
        True
    """
    return world["locations"].get(location, {}).get("description", "A mysterious place.")

def get_location_items(world, location):
    """
    Get the list of items available at a specific location.
    
    Args:
        world (dict): The world state object
        location (str): The name of the location
        
    Returns:
        list: List of item names available at the location
        
    Example:
        >>> world = initialize_world()
        >>> items = get_location_items(world, "Village")
        >>> print("map" in items)
        True
    """
    return world["locations"].get(location, {}).get("items", [])

def change_location(world, new_location):
    """
    Change the current location in the world.
    
    Args:
        world (dict): The world state object to modify
        new_location (str): The name of the new location
        
    Side Effects:
        - Updates the world's current_location
        
    Example:
        >>> world = initialize_world()
        >>> change_location(world, "Forest")
        >>> print(get_current_location(world))
        Forest
    """
    world["current_location"] = new_location

def get_available_locations(world):
    """
    Get a list of locations that can be reached from the current location.
    
    Args:
        world (dict): The world state object
        
    Returns:
        list: List of location names that are connected to the current location
        
    Example:
        >>> world = initialize_world()
        >>> locations = get_available_locations(world)
        >>> print(locations)
        ['Forest', 'Mountain']
    """
    current_location = get_current_location(world)
    return world["locations"][current_location]["connections"]

def get_all_locations(world):
    """
    Get a list of all locations in the world.
    
    Args:
        world (dict): The world state object
        
    Returns:
        list: List of all location names in the world
        
    Example:
        >>> world = initialize_world()
        >>> all_locations = get_all_locations(world)
        >>> print(sorted(all_locations))
        ['Cave', 'Forest', 'Mountain', 'Village']
    """
    return list(world["locations"].keys())

def interact_with_location(world, player):
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
    return location in get_available_locations(world)
