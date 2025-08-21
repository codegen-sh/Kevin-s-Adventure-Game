"""
Player module for Kevin's Adventure Game.
This module handles all player-related functionality.
"""

from utils.text_formatting import format_inventory, print_game_over


class Player:
    """
    Player class representing the game's protagonist.
    Manages player state including health, inventory, location, and gold.
    """
    
    def __init__(self, name, health=100, inventory=None, location="Village", gold=100):
        """
        Initialize a new Player instance.
        
        Args:
            name (str): The player's name
            health (int): The player's starting health (default: 100)
            inventory (list): The player's starting inventory (default: empty list)
            location (str): The player's starting location (default: "Village")
            gold (int): The player's starting gold (default: 100)
        """
        self.name = name
        self.health = health
        self.inventory = inventory or []
        self.location = location
        self.gold = gold
    
    def get_status(self):
        """
        Get a string representation of the player's current status.
        
        Returns:
            str: A formatted string with player health, inventory, and gold
        """
        return f"Health: {self.health} | Inventory: {format_inventory(self.inventory)} | Gold: {self.gold}"
    
    def add_item(self, item):
        """
        Add an item to the player's inventory.
        
        Args:
            item (str): The item to add
        """
        self.inventory.append(item)
        print(f"You picked up: {item}")
    
    def remove_item(self, item):
        """
        Remove an item from the player's inventory.
        
        Args:
            item (str): The item to remove
            
        Returns:
            bool: True if the item was removed, False if it wasn't in the inventory
        """
        if item in self.inventory:
            self.inventory.remove(item)
            print(f"You dropped: {item}")
            return True
        else:
            print(f"You don't have {item} in your inventory.")
            return False
    
    def move(self, new_location):
        """
        Move the player to a new location.
        
        Args:
            new_location (str): The name of the new location
        """
        self.location = new_location
        print(f"You moved to: {new_location}")
    
    def heal(self, amount):
        """
        Heal the player by a specified amount.
        
        Args:
            amount (int): The amount of health to restore
        """
        self.health = min(100, self.health + amount)
        print(f"You healed for {amount} health. Current health: {self.health}")
    
    def take_damage(self, amount):
        """
        Damage the player by a specified amount.
        
        Args:
            amount (int): The amount of damage to take
        """
        self.health = max(0, self.health - amount)
        print(f"You took {amount} damage. Current health: {self.health}")
        if self.health == 0:
            print("You have been defeated.")
            print_game_over()
    
    def has_item(self, item):
        """
        Check if the player has a specific item.
        
        Args:
            item (str): The item to check for
            
        Returns:
            bool: True if the player has the item, False otherwise
        """
        return item in self.inventory
    
    def to_dict(self):
        """
        Convert the player object to a dictionary for saving.
        
        Returns:
            dict: A dictionary representation of the player
        """
        return {
            "name": self.name,
            "health": self.health,
            "inventory": self.inventory.copy(),
            "location": self.location,
            "gold": self.gold
        }
    
    @classmethod
    def from_dict(cls, data):
        """
        Create a Player instance from a dictionary.
        
        Args:
            data (dict): A dictionary with player data
            
        Returns:
            Player: A new Player instance with the loaded data
        """
        return cls(
            name=data["name"],
            health=data["health"],
            inventory=data["inventory"],
            location=data["location"],
            gold=data["gold"]
        )


# Legacy functions for backward compatibility
def create_player(name):
    """Create a new player with default values."""
    return Player(name).to_dict()

def get_player_status(player):
    """Get the player's status string."""
    if isinstance(player, Player):
        return player.get_status()
    else:
        # Handle dictionary-based player for backward compatibility
        return f"Health: {player['health']} | Inventory: {format_inventory(player['inventory'])} | Gold: {player['gold']}"

def add_item_to_inventory(player, item):
    """Add an item to the player's inventory."""
    if isinstance(player, Player):
        player.add_item(item)
    else:
        # Handle dictionary-based player for backward compatibility
        player['inventory'].append(item)
        print(f"You picked up: {item}")

def remove_item_from_inventory(player, item):
    """Remove an item from the player's inventory."""
    if isinstance(player, Player):
        return player.remove_item(item)
    else:
        # Handle dictionary-based player for backward compatibility
        if item in player['inventory']:
            player['inventory'].remove(item)
            print(f"You dropped: {item}")
            return True
        else:
            print(f"You don't have {item} in your inventory.")
            return False

def move_player(player, new_location):
    """Move the player to a new location."""
    if isinstance(player, Player):
        player.move(new_location)
    else:
        # Handle dictionary-based player for backward compatibility
        player['location'] = new_location
        print(f"You moved to: {new_location}")

def heal_player(player, amount):
    """Heal the player by a specified amount."""
    if isinstance(player, Player):
        player.heal(amount)
    else:
        # Handle dictionary-based player for backward compatibility
        player['health'] = min(100, player['health'] + amount)
        print(f"You healed for {amount} health. Current health: {player['health']}")

def damage_player(player, amount):
    """Damage the player by a specified amount."""
    if isinstance(player, Player):
        player.take_damage(amount)
    else:
        # Handle dictionary-based player for backward compatibility
        player['health'] = max(0, player['health'] - amount)
        print(f"You took {amount} damage. Current health: {player['health']}")
        if player['health'] == 0:
            print("You have been defeated.")
            print_game_over()

