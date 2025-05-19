"""
Entity module for Kevin's Adventure Game.
"""
from typing import Dict


class Entity:
    """
    Base class for all game entities.
    """

    def __init__(self, name: str):
        """
        Initialize a new entity.

        Args:
            name: The entity's name
        """
        self.name = name

    def __str__(self) -> str:
        """
        Get a string representation of the entity.

        Returns:
            The entity's name
        """
        return self.name

    def to_dict(self) -> Dict:
        """
        Convert the entity to a dictionary for saving.

        Returns:
            A dictionary representation of the entity
        """
        return {"name": self.name}

    @classmethod
    def from_dict(cls, data: Dict) -> 'Entity':
        """
        Create an entity from a dictionary.

        Args:
            data: The dictionary to create the entity from

        Returns:
            A new Entity instance
        """
        return cls(data["name"])

