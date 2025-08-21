"""
Base module for location classes in the game.
"""

from abc import ABC, abstractmethod

from ui.input_handler import get_numeric_choice


class BaseLocation(ABC):
    """
    Abstract base class for all locations in the game.
    
    Attributes:
        name (str): The name of the location
        description (str): A description of the location
        connections (list): A list of connected locations
        items (list): A list of items at the location
    """
    
    def __init__(self, name, description, connections=None, items=None):
        """
        Initialize a new BaseLocation.
        
        Args:
            name (str): The name of the location
            description (str): A description of the location
            connections (list, optional): A list of connected locations. Defaults to None.
            items (list, optional): A list of items at the location. Defaults to None.
        """
        self.name = name
        self.description = description
        self.connections = connections if connections is not None else []
        self.items = items if items is not None else []
    
    def get_description(self):
        """
        Get the description of the location.
        
        Returns:
            str: The description
        """
        return self.description
    
    def get_connections(self):
        """
        Get the connections from this location.
        
        Returns:
            list: The connections
        """
        return self.connections
    
    def get_items(self):
        """
        Get the items at this location.
        
        Returns:
            list: The items
        """
        return self.items
    
    def add_item(self, item):
        """
        Add an item to this location.
        
        Args:
            item (str): The item to add
        """
        if item not in self.items:
            self.items.append(item)
    
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
    
    def add_connection(self, location):
        """
        Add a connection to this location.
        
        Args:
            location (str): The location to connect to
        """
        if location not in self.connections:
            self.connections.append(location)
    
    def remove_connection(self, location):
        """
        Remove a connection from this location.
        
        Args:
            location (str): The location to disconnect
        
        Returns:
            bool: True if the connection was removed, False otherwise
        """
        if location in self.connections:
            self.connections.remove(location)
            return True
        return False
    
    def enter(self, world, player):
        """
        Enter this location.
        
        Args:
            world: The world state
            player: The player
        """
        print(f"You enter {self.name}. {self.description}")
        
        while True:
            options = self.get_options()
            print("\nWhat would you like to do?")
            for i, option in enumerate(options, 1):
                print(f"{i}. {option}")
            
            choice = get_numeric_choice(1, len(options), "Enter your choice: ")
            
            if choice == len(options):  # Last option is always to leave
                print(f"You decide to leave {self.name}.")
                break
            else:
                self.handle_choice(choice - 1, world, player)
    
    @abstractmethod
    def get_options(self):
        """
        Get the options available at this location.
        
        Returns:
            list: A list of option strings
        """
        pass
    
    @abstractmethod
    def handle_choice(self, choice, world, player):
        """
        Handle a choice made by the player.
        
        Args:
            choice (int): The index of the chosen option
            world: The world state
            player: The player
        """
        pass
    
    def to_dict(self):
        """
        Convert the location to a dictionary for saving.
        
        Returns:
            dict: A dictionary representation of the location
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
            BaseLocation: A new location instance
        """
        return cls(
            name=data.get("name", "Unknown"),
            description=data.get("description", ""),
            connections=data.get("connections", []),
            items=data.get("items", [])
        )

