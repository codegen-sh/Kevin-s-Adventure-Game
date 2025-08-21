"""
Models module for Kevin's Adventure Game.
This module defines the core data models used in the game.
"""
from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Player:
    """
    Player class representing the player's state in the game.
    
    Attributes:
        name (str): The player's name
        health (int): The player's current health
        inventory (List[str]): The player's inventory
        location (str): The player's current location
        gold (int): The player's gold
    """
    name: str
    health: int = 100
    inventory: List[str] = field(default_factory=list)
    location: str = "Village"
    gold: int = 100
    
    def add_item(self, item: str) -> None:
        """
        Add an item to the player's inventory.
        
        Args:
            item (str): The item to add
        """
        self.inventory.append(item)
        print(f"You picked up: {item}")
    
    def remove_item(self, item: str) -> bool:
        """
        Remove an item from the player's inventory.
        
        Args:
            item (str): The item to remove
        
        Returns:
            bool: True if the item was removed, False otherwise
        """
        if item in self.inventory:
            self.inventory.remove(item)
            print(f"You dropped: {item}")
            return True
        else:
            print(f"You don't have {item} in your inventory.")
            return False
    
    def move(self, new_location: str) -> None:
        """
        Move the player to a new location.
        
        Args:
            new_location (str): The new location
        """
        self.location = new_location
        print(f"You moved to: {new_location}")
    
    def heal(self, amount: int) -> None:
        """
        Heal the player.
        
        Args:
            amount (int): The amount to heal
        """
        self.health = min(100, self.health + amount)
        print(f"You healed for {amount} health. Current health: {self.health}")
    
    def damage(self, amount: int) -> None:
        """
        Damage the player.
        
        Args:
            amount (int): The amount of damage
        """
        self.health = max(0, self.health - amount)
        print(f"You took {amount} damage. Current health: {self.health}")
        if self.health == 0:
            print("You have been defeated.")
            from utils.text_formatting import print_game_over
            print_game_over()
    
    def get_status(self) -> str:
        """
        Get the player's status.
        
        Returns:
            str: The player's status
        """
        from utils.text_formatting import format_inventory
        return f"Health: {self.health} | Inventory: {format_inventory(self.inventory)} | Gold: {self.gold}"
    
    def to_dict(self) -> dict:
        """
        Convert the player to a dictionary for serialization.
        
        Returns:
            dict: A dictionary representation of the player
        """
        return {
            "name": self.name,
            "health": self.health,
            "inventory": self.inventory,
            "location": self.location,
            "gold": self.gold
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> 'Player':
        """
        Create a player from a dictionary.
        
        Args:
            data (dict): A dictionary representation of a player
        
        Returns:
            Player: A new Player instance
        """
        return cls(
            name=data["name"],
            health=data["health"],
            inventory=data["inventory"],
            location=data["location"],
            gold=data["gold"]
        )


@dataclass
class Item:
    """
    Item class representing an item in the game.
    
    Attributes:
        name (str): The item's name
        description (str): The item's description
        value (int): The item's value in gold
        usable (bool): Whether the item can be used
    """
    name: str
    description: str
    value: int = 0
    usable: bool = True
    
    def use(self, player: Player, world: 'World') -> bool:
        """
        Use the item.
        
        Args:
            player (Player): The player using the item
            world (World): The game world
        
        Returns:
            bool: True if the item was used successfully, False otherwise
        """
        print(f"You use the {self.name}.")
        return True
    
    def to_dict(self) -> dict:
        """
        Convert the item to a dictionary for serialization.
        
        Returns:
            dict: A dictionary representation of the item
        """
        return {
            "name": self.name,
            "description": self.description,
            "value": self.value,
            "usable": self.usable
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> 'Item':
        """
        Create an item from a dictionary.
        
        Args:
            data (dict): A dictionary representation of an item
        
        Returns:
            Item: A new Item instance
        """
        return cls(
            name=data["name"],
            description=data["description"],
            value=data.get("value", 0),
            usable=data.get("usable", True)
        )


@dataclass
class World:
    """
    World class representing the game world.
    
    Attributes:
        current_location (str): The current location
        locations (dict): A dictionary of locations
        weather (str): The current weather
    """
    current_location: str = "Village"
    locations: dict = field(default_factory=dict)
    weather: str = "clear"
    
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
            List[str]: A list of available locations
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
    
    def get_all_locations(self) -> List[str]:
        """
        Get all locations in the world.
        
        Returns:
            List[str]: A list of all locations
        """
        return list(self.locations.keys())
    
    def is_location_accessible(self, location: str) -> bool:
        """
        Check if a location is accessible from the current location.
        
        Args:
            location (str): The location to check
        
        Returns:
            bool: True if the location is accessible, False otherwise
        """
        return location in self.get_available_locations()
    
    def to_dict(self) -> dict:
        """
        Convert the world to a dictionary for serialization.
        
        Returns:
            dict: A dictionary representation of the world
        """
        return {
            "current_location": self.current_location,
            "locations": self.locations,
            "weather": self.weather
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> 'World':
        """
        Create a world from a dictionary.
        
        Args:
            data (dict): A dictionary representation of a world
        
        Returns:
            World: A new World instance
        """
        return cls(
            current_location=data["current_location"],
            locations=data["locations"],
            weather=data.get("weather", "clear")
        )

