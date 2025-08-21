"""
Player module for Kevin's Adventure Game.
Contains the Player class and related functions.
"""
from utils.text_formatting import format_inventory, print_game_over


class Player:
    """
    Player class representing the game player.
    
    Attributes:
        name (str): The player's name
        health (int): The player's health points (0-100)
        inventory (list): List of items the player is carrying
        location (str): The player's current location
        gold (int): The amount of gold the player has
    """
    
    def __init__(self, name, health=100, inventory=None, location="Village", gold=100):
        """
        Initialize a new Player instance.
        
        Args:
            name (str): The player's name
            health (int, optional): The player's initial health. Defaults to 100.
            inventory (list, optional): The player's initial inventory. Defaults to empty list.
            location (str, optional): The player's initial location. Defaults to "Village".
            gold (int, optional): The player's initial gold. Defaults to 100.
        """
        self.name = name
        self.health = health
        self.inventory = inventory or []
        self.location = location
        self.gold = gold
    
    def get_status(self):
        """
        Get a string representation of the player's status.
        
        Returns:
            str: A string describing the player's health, inventory, and gold
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
            bool: True if the item was removed, False otherwise
        """
        if item in self.inventory:
            self.inventory.remove(item)
            print(f"You dropped: {item}")
            return True
        else:
            print(f"You don't have {item} in your inventory.")
            return False
    
    def move_to(self, new_location):
        """
        Move the player to a new location.
        
        Args:
            new_location (str): The new location
        """
        self.location = new_location
        print(f"You moved to: {new_location}")
    
    def heal(self, amount):
        """
        Heal the player by a specified amount.
        
        Args:
            amount (int): The amount to heal
        """
        self.health = min(100, self.health + amount)
        print(f"You healed for {amount} health. Current health: {self.health}")
    
    def damage(self, amount):
        """
        Damage the player by a specified amount.
        
        Args:
            amount (int): The amount of damage
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
        Convert the Player instance to a dictionary.
        
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
    def from_dict(cls, player_dict):
        """
        Create a Player instance from a dictionary.
        
        Args:
            player_dict (dict): A dictionary representation of a player
            
        Returns:
            Player: A new Player instance
        """
        return cls(
            name=player_dict["name"],
            health=player_dict["health"],
            inventory=player_dict["inventory"].copy(),
            location=player_dict["location"],
            gold=player_dict["gold"]
        )


# Legacy functions for backward compatibility
def create_player(name):
    """
    Create a new player with default values.
    
    Args:
        name (str): The player's name
        
    Returns:
        dict: A dictionary representing the player
    """
    player = Player(name)
    return player.to_dict()

def get_player_status(player):
    """
    Get a string representation of the player's status.
    
    Args:
        player (dict): The player's current state
        
    Returns:
        str: A string describing the player's health, inventory, and gold
    """
    if isinstance(player, Player):
        return player.get_status()
    else:
        # Handle dictionary case for backward compatibility
        return f"Health: {player['health']} | Inventory: {format_inventory(player['inventory'])} | Gold: {player['gold']}"

def add_item_to_inventory(player, item):
    """
    Add an item to the player's inventory.
    
    Args:
        player (dict): The player's current state
        item (str): The item to add
    """
    if isinstance(player, Player):
        player.add_item(item)
    else:
        # Handle dictionary case for backward compatibility
        player['inventory'].append(item)
        print(f"You picked up: {item}")

def remove_item_from_inventory(player, item):
    """
    Remove an item from the player's inventory.
    
    Args:
        player (dict): The player's current state
        item (str): The item to remove
        
    Returns:
        bool: True if the item was removed, False otherwise
    """
    if isinstance(player, Player):
        return player.remove_item(item)
    else:
        # Handle dictionary case for backward compatibility
        if item in player['inventory']:
            player['inventory'].remove(item)
            print(f"You dropped: {item}")
            return True
        else:
            print(f"You don't have {item} in your inventory.")
            return False

def move_player(player, new_location):
    """
    Move the player to a new location.
    
    Args:
        player (dict): The player's current state
        new_location (str): The new location
    """
    if isinstance(player, Player):
        player.move_to(new_location)
    else:
        # Handle dictionary case for backward compatibility
        player['location'] = new_location
        print(f"You moved to: {new_location}")

def heal_player(player, amount):
    """
    Heal the player by a specified amount.
    
    Args:
        player (dict): The player's current state
        amount (int): The amount to heal
    """
    if isinstance(player, Player):
        player.heal(amount)
    else:
        # Handle dictionary case for backward compatibility
        player['health'] = min(100, player['health'] + amount)
        print(f"You healed for {amount} health. Current health: {player['health']}")

def damage_player(player, amount):
    """
    Damage the player by a specified amount.
    
    Args:
        player (dict): The player's current state
        amount (int): The amount of damage
    """
    if isinstance(player, Player):
        player.damage(amount)
    else:
        # Handle dictionary case for backward compatibility
        player['health'] = max(0, player['health'] - amount)
        print(f"You took {amount} damage. Current health: {player['health']}")
        if player['health'] == 0:
            print("You have been defeated.")
            print_game_over()

