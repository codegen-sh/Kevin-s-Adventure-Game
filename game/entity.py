class Entity:
    """
    Base class for all game entities.
    
    This class provides common functionality for all game entities,
    such as players, items, and locations.
    """
    
    def __init__(self, name, description=""):
        """
        Initialize a new Entity.
        
        Args:
            name (str): The name of the entity
            description (str, optional): A description of the entity
        """
        self.name = name
        self.description = description
    
    def __str__(self):
        """Return a string representation of the entity."""
        return self.name
    
    def get_description(self):
        """Return the description of the entity."""
        return self.description
    
    def set_description(self, description):
        """Set the description of the entity."""
        self.description = description

