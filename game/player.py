from utils.text_formatting import format_inventory, print_game_over


class Player:
    """
    A class to represent the player in the game.
    
    Attributes:
        name (str): The player's name
        health (int): The player's health points
        inventory (list): The player's inventory
        location (str): The player's current location
        gold (int): The player's gold
        max_health (int): The player's maximum health
        agility (int): The player's agility stat
        perception (int): The player's perception stat
    """
    
    def __init__(self, name, health=100, inventory=None, location="Village", gold=100, max_health=100, agility=10, perception=10):
        """
        Initialize a new Player.
        
        Args:
            name (str): The player's name
            health (int, optional): The player's initial health. Defaults to 100.
            inventory (list, optional): The player's initial inventory. Defaults to empty list.
            location (str, optional): The player's initial location. Defaults to "Village".
            gold (int, optional): The player's initial gold. Defaults to 100.
            max_health (int, optional): The player's maximum health. Defaults to 100.
            agility (int, optional): The player's agility stat. Defaults to 10.
            perception (int, optional): The player's perception stat. Defaults to 10.
        """
        self.name = name
        self.health = health
        self.inventory = inventory if inventory is not None else []
        self.location = location
        self.gold = gold
        self.max_health = max_health
        self.agility = agility
        self.perception = perception
    
    def get_status(self):
        """
        Get the player's current status.
        
        Returns:
            str: A string representation of the player's status
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
    
    def move(self, new_location):
        """
        Move the player to a new location.
        
        Args:
            new_location (str): The location to move to
        """
        self.location = new_location
        print(f"You moved to: {new_location}")
    
    def heal(self, amount):
        """
        Heal the player.
        
        Args:
            amount (int): The amount to heal
        """
        self.health = min(self.max_health, self.health + amount)
        print(f"You healed for {amount} health. Current health: {self.health}")
    
    def damage(self, amount):
        """
        Damage the player.
        
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
        Check if the player has an item.
        
        Args:
            item (str): The item to check for
        
        Returns:
            bool: True if the player has the item, False otherwise
        """
        return item in self.inventory
    
    def to_dict(self):
        """
        Convert the player to a dictionary for saving.
        
        Returns:
            dict: A dictionary representation of the player
        """
        return {
            "name": self.name,
            "health": self.health,
            "inventory": self.inventory,
            "location": self.location,
            "gold": self.gold,
            "max_health": self.max_health,
            "agility": self.agility,
            "perception": self.perception
        }
    
    @classmethod
    def from_dict(cls, data):
        """
        Create a Player from a dictionary.
        
        Args:
            data (dict): A dictionary representation of a player
        
        Returns:
            Player: A new Player instance
        """
        return cls(
            name=data.get("name", "Kevin"),
            health=data.get("health", 100),
            inventory=data.get("inventory", []),
            location=data.get("location", "Village"),
            gold=data.get("gold", 100),
            max_health=data.get("max_health", 100),
            agility=data.get("agility", 10),
            perception=data.get("perception", 10)
        )


# Legacy functions for backward compatibility
def create_player(name):
    """
    Create a new player.
    
    Args:
        name (str): The player's name
    
    Returns:
        dict: A dictionary representing the player
    """
    return {
        "name": name,
        "health": 100,
        "inventory": [],
        "location": "Village",
        "gold": 100
    }

def get_player_status(player):
    """
    Get the player's current status.
    
    Args:
        player (dict or Player): The player
    
    Returns:
        str: A string representation of the player's status
    """
    if isinstance(player, Player):
        return player.get_status()
    return f"Health: {player['health']} | Inventory: {format_inventory(player['inventory'])} | Gold: {player['gold']}"

def add_item_to_inventory(player, item):
    """
    Add an item to the player's inventory.
    
    Args:
        player (dict or Player): The player
        item (str): The item to add
    """
    if isinstance(player, Player):
        player.add_item(item)
    else:
        player['inventory'].append(item)
        print(f"You picked up: {item}")

def remove_item_from_inventory(player, item):
    """
    Remove an item from the player's inventory.
    
    Args:
        player (dict or Player): The player
        item (str): The item to remove
    
    Returns:
        bool: True if the item was removed, False otherwise
    """
    if isinstance(player, Player):
        return player.remove_item(item)
    else:
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
        player (dict or Player): The player
        new_location (str): The location to move to
    """
    if isinstance(player, Player):
        player.move(new_location)
    else:
        player['location'] = new_location
        print(f"You moved to: {new_location}")

def heal_player(player, amount):
    """
    Heal the player.
    
    Args:
        player (dict or Player): The player
        amount (int): The amount to heal
    """
    if isinstance(player, Player):
        player.heal(amount)
    else:
        player['health'] = min(100, player['health'] + amount)
        print(f"You healed for {amount} health. Current health: {player['health']}")

def damage_player(player, amount):
    """
    Damage the player.
    
    Args:
        player (dict or Player): The player
        amount (int): The amount of damage to take
    """
    if isinstance(player, Player):
        player.damage(amount)
    else:
        player['health'] = max(0, player['health'] - amount)
        print(f"You took {amount} damage. Current health: {player['health']}")
        if player['health'] == 0:
            print("You have been defeated.")
            print_game_over()

