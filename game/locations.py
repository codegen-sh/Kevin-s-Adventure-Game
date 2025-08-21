"""
Base location module for Kevin's Adventure Game.
This module defines the base Location class that all locations inherit from.
"""
from abc import ABC, abstractmethod


class Location(ABC):
    """
    Base class for all game locations.
    
    Attributes:
        name (str): The name of the location
        description (str): A description of the location
        connections (list): A list of connected location names
        items (list): A list of items available in the location
    """
    
    def __init__(self, name, description, connections=None, items=None):
        """
        Initialize a new Location.
        
        Args:
            name (str): The name of the location
            description (str): A description of the location
            connections (list, optional): A list of connected location names
            items (list, optional): A list of items available in the location
        """
        self.name = name
        self.description = description
        self.connections = connections or []
        self.items = items or []
    
    @abstractmethod
    def interact(self, world, player):
        """
        Handle player interaction with this location.
        
        Args:
            world: The game world state
            player: The player's current state
        
        Returns:
            None
        """
        pass
    
    def add_item(self, item):
        """
        Add an item to this location.
        
        Args:
            item (str): The item to add
        
        Returns:
            None
        """
        if item not in self.items:
            self.items.append(item)
            print(f"A {item} has been added to {self.name}.")
        else:
            print(f"There's already a {item} in {self.name}.")
    
    def remove_item(self, item):
        """
        Remove an item from this location.
        
        Args:
            item (str): The item to remove
        
        Returns:
            bool: True if the item was removed, False otherwise
        """
        if item in self.items:
            self.items.remove(item)
            return True
        return False
    
    def get_description(self):
        """
        Get the description of this location.
        
        Returns:
            str: The location description
        """
        return self.description
    
    def get_connections(self):
        """
        Get the connections from this location.
        
        Returns:
            list: A list of connected location names
        """
        return self.connections
    
    def get_items(self):
        """
        Get the items available in this location.
        
        Returns:
            list: A list of items
        """
        return self.items
    
    def to_dict(self):
        """
        Convert this location to a dictionary for serialization.
        
        Returns:
            dict: A dictionary representation of this location
        """
        return {
            "name": self.name,
            "description": self.description,
            "connections": self.connections,
            "items": self.items
        }
    
    @classmethod
    def from_dict(cls, data):
        """
        Create a location from a dictionary.
        
        Args:
            data (dict): A dictionary representation of a location
        
        Returns:
            Location: A new Location instance
        """
        return cls(
            name=data["name"],
            description=data["description"],
            connections=data["connections"],
            items=data["items"]
        )

