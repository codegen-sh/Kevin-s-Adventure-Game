"""
Location class for representing game locations
"""


class Location:
    """
    Represents a location in the game world
    """
    
    def __init__(self, name, description, connections=None, items=None):
        """
        Initialize a location
        
        Args:
            name (str): Name of the location
            description (str): Description of the location
            connections (list): List of connected location names
            items (list): List of items available in this location
        """
        self.name = name
        self.description = description
        self.connections = connections or []
        self.items = items or []
    
    def add_connection(self, location_name):
        """
        Add a connection to another location
        
        Args:
            location_name (str): Name of the location to connect to
        """
        if location_name not in self.connections:
            self.connections.append(location_name)
    
    def remove_connection(self, location_name):
        """
        Remove a connection to another location
        
        Args:
            location_name (str): Name of the location to disconnect from
        """
        if location_name in self.connections:
            self.connections.remove(location_name)
    
    def is_connected_to(self, location_name):
        """
        Check if this location is connected to another location
        
        Args:
            location_name (str): Name of the location to check
            
        Returns:
            bool: True if connected, False otherwise
        """
        return location_name in self.connections
    
    def add_item(self, item):
        """
        Add an item to this location
        
        Args:
            item (str): Item to add
        """
        if item not in self.items:
            self.items.append(item)
    
    def remove_item(self, item):
        """
        Remove an item from this location
        
        Args:
            item (str): Item to remove
            
        Returns:
            bool: True if item was removed, False if not found
        """
        if item in self.items:
            self.items.remove(item)
            return True
        return False
    
    def has_item(self, item):
        """
        Check if this location has a specific item
        
        Args:
            item (str): Item to check for
            
        Returns:
            bool: True if item is present
        """
        return item in self.items
    
    def get_available_items(self):
        """
        Get list of available items
        
        Returns:
            list: Copy of items list
        """
        return self.items.copy()
    
    def get_connections(self):
        """
        Get list of connected locations
        
        Returns:
            list: Copy of connections list
        """
        return self.connections.copy()
    
    def to_dict(self):
        """
        Convert location to dictionary for saving
        
        Returns:
            dict: Location data as dictionary
        """
        return {
            "name": self.name,
            "description": self.description,
            "connections": self.connections.copy(),
            "items": self.items.copy()
        }
    
    @classmethod
    def from_dict(cls, data):
        """
        Create location from dictionary data
        
        Args:
            data (dict): Location data dictionary
            
        Returns:
            Location: New location instance
        """
        return cls(
            name=data.get("name", "Unknown"),
            description=data.get("description", "A mysterious place."),
            connections=data.get("connections", []).copy(),
            items=data.get("items", []).copy()
        )
    
    def __str__(self):
        """String representation of the location"""
        return f"Location: {self.name} - {self.description}"
    
    def __repr__(self):
        """Developer representation of the location"""
        return f"Location(name='{self.name}', connections={self.connections}, items={self.items})"
