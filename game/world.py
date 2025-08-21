"""
World module for Kevin's Adventure Game.

This module contains the World class and related functions for managing the game world.
"""
from typing import Dict, List, Optional, Set, Union

from locations.cave import explore_cave
from locations.forest import enter_forest
from locations.mountain import climb_mountain
from locations.village import visit_village


class World:
    """
    Class representing the game world.
    
    Attributes:
        current_location (str): The player's current location
        locations (Dict[str, Dict]): Dictionary of locations in the world
        weather (str): The current weather
        state (Dict): The world state
    """
    
    def __init__(self):
        """Initialize a new World."""
        self.current_location = "Village"
        self.locations = {
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
        self.weather = "clear"
        self.state = {
            "discovered_locations": set(),
            "active_quests": [],
            "completed_quests": [],
            "time_of_day": "day",
            "days_passed": 0,
            "special_discoveries": set()
        }
    
    def get_current_location(self) -> str:
        """
        Get the current location.
        
        Returns:
            str: The current location
        """
        return self.current_location
    
    def get_location_description(self, location: str) -> str:
        """
        Get the description of a location.
        
        Args:
            location (str): The location
            
        Returns:
            str: The location description
        """
        return self.locations[location]["description"]
    
    def get_available_locations(self) -> List[str]:
        """
        Get the available locations from the current location.
        
        Returns:
            List[str]: The available locations
        """
        return self.locations[self.current_location]["connections"]
    
    def change_location(self, new_location: str) -> bool:
        """
        Change the current location.
        
        Args:
            new_location (str): The new location
            
        Returns:
            bool: True if the location was changed, False otherwise
        """
        if new_location in self.get_available_locations():
            self.current_location = new_location
            return True
        return False
    
    def interact_with_location(self, player) -> None:
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
    
    def is_location_accessible(self, location: str) -> bool:
        """
        Check if a location is accessible from the current location.
        
        Args:
            location (str): The location to check
            
        Returns:
            bool: True if the location is accessible, False otherwise
        """
        return location in self.get_available_locations()
    
    def get_all_locations(self) -> List[str]:
        """
        Get all locations in the world.
        
        Returns:
            List[str]: All locations
        """
        return list(self.locations.keys())
    
    def add_location(self, name: str, description: str, connections: List[str], items: List[str]) -> None:
        """
        Add a new location to the world.
        
        Args:
            name (str): The location name
            description (str): The location description
            connections (List[str]): The locations connected to this one
            items (List[str]): The items in this location
        """
        self.locations[name] = {
            "description": description,
            "connections": connections,
            "items": items
        }
        
        # Add this location to the connections of the connected locations
        for connection in connections:
            if connection in self.locations and name not in self.locations[connection]["connections"]:
                self.locations[connection]["connections"].append(name)
    
    def get_location_items(self, location: str) -> List[str]:
        """
        Get the items in a location.
        
        Args:
            location (str): The location
            
        Returns:
            List[str]: The items in the location
        """
        return self.locations[location]["items"]
    
    def add_item_to_location(self, location: str, item: str) -> None:
        """
        Add an item to a location.
        
        Args:
            location (str): The location
            item (str): The item to add
        """
        if item not in self.locations[location]["items"]:
            self.locations[location]["items"].append(item)
    
    def remove_item_from_location(self, location: str, item: str) -> bool:
        """
        Remove an item from a location.
        
        Args:
            location (str): The location
            item (str): The item to remove
            
        Returns:
            bool: True if the item was removed, False otherwise
        """
        if item in self.locations[location]["items"]:
            self.locations[location]["items"].remove(item)
            return True
        return False
    
    def to_dict(self) -> Dict[str, Union[str, Dict, List[str]]]:
        """
        Convert the world to a dictionary for saving.
        
        Returns:
            dict: A dictionary representation of the world
        """
        # Convert sets to lists for JSON serialization
        state_dict = self.state.copy()
        state_dict["discovered_locations"] = list(self.state["discovered_locations"])
        state_dict["special_discoveries"] = list(self.state["special_discoveries"])
        
        return {
            "current_location": self.current_location,
            "locations": self.locations,
            "weather": self.weather,
            "state": state_dict
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Union[str, Dict, List[str]]]) -> 'World':
        """
        Create a world from a dictionary.
        
        Args:
            data (dict): A dictionary representation of a world
            
        Returns:
            World: A new World instance
        """
        world = cls()
        world.current_location = data["current_location"]
        world.locations = data["locations"]
        world.weather = data.get("weather", "clear")
        
        # Convert lists back to sets
        state_dict = data.get("state", {})
        if state_dict:
            world.state = state_dict.copy()
            world.state["discovered_locations"] = set(state_dict.get("discovered_locations", []))
            world.state["special_discoveries"] = set(state_dict.get("special_discoveries", []))
        
        return world


# Legacy functions for backward compatibility
def initialize_world() -> Dict[str, Union[str, Dict]]:
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

def get_current_location(world: Dict[str, Union[str, Dict]]) -> str:
    """
    Get the current location.
    
    Args:
        world (dict): The game world state
        
    Returns:
        str: The current location
    """
    return world["current_location"]

def get_location_description(world: Dict[str, Union[str, Dict]], location: str) -> str:
    """
    Get the description of a location.
    
    Args:
        world (dict): The game world state
        location (str): The location
        
    Returns:
        str: The location description
    """
    return world["locations"][location]["description"]

def get_available_locations(world: Dict[str, Union[str, Dict]]) -> List[str]:
    """
    Get the available locations from the current location.
    
    Args:
        world (dict): The game world state
        
    Returns:
        List[str]: The available locations
    """
    current_location = get_current_location(world)
    return world["locations"][current_location]["connections"]

def change_location(world: Dict[str, Union[str, Dict]], new_location: str) -> bool:
    """
    Change the current location.
    
    Args:
        world (dict): The game world state
        new_location (str): The new location
        
    Returns:
        bool: True if the location was changed, False otherwise
    """
    if new_location in get_available_locations(world):
        world["current_location"] = new_location
        return True
    return False

def interact_with_location(world: Dict[str, Union[str, Dict]], player) -> None:
    """
    Interact with the current location.
    
    Args:
        world (dict): The game world state
        player: The player
    """
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

def is_location_accessible(world: Dict[str, Union[str, Dict]], location: str) -> bool:
    """
    Check if a location is accessible from the current location.
    
    Args:
        world (dict): The game world state
        location (str): The location to check
        
    Returns:
        bool: True if the location is accessible, False otherwise
    """
    return location in get_available_locations(world)

def get_all_locations(world: Dict[str, Union[str, Dict]]) -> List[str]:
    """
    Get all locations in the world.
    
    Args:
        world (dict): The game world state
        
    Returns:
        List[str]: All locations
    """
    return list(world["locations"].keys())

