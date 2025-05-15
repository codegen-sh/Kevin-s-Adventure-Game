"""
Base classes for the game objects.
"""
from abc import ABC, abstractmethod


class GameObject(ABC):
    """Base class for all game objects."""
    
    def __init__(self, name, description=""):
        self.name = name
        self.description = description
    
    def __str__(self):
        return self.name


class Location(GameObject):
    """Base class for all locations in the game."""
    
    def __init__(self, name, description="", connections=None, items=None):
        super().__init__(name, description)
        self.connections = connections or []
        self.items = items or []
    
    def add_connection(self, location):
        """Add a connection to another location."""
        if location not in self.connections:
            self.connections.append(location)
    
    def remove_connection(self, location):
        """Remove a connection to another location."""
        if location in self.connections:
            self.connections.remove(location)
    
    def add_item(self, item):
        """Add an item to this location."""
        if item not in self.items:
            self.items.append(item)
    
    def remove_item(self, item):
        """Remove an item from this location."""
        if item in self.items:
            self.items.remove(item)
            return True
        return False
    
    @abstractmethod
    def interact(self, player, world):
        """Interact with this location."""
        pass


class Item(GameObject):
    """Base class for all items in the game."""
    
    def __init__(self, name, description="", value=0, usable=False):
        super().__init__(name, description)
        self.value = value
        self.usable = usable
    
    def use(self, player, world):
        """Use this item."""
        if not self.usable:
            return f"{self.name} cannot be used."
        return f"You used {self.name}."


class Action:
    """Base class for all actions in the game."""
    
    def __init__(self, name, description=""):
        self.name = name
        self.description = description
    
    def execute(self, player, world, *args):
        """Execute this action."""
        pass

