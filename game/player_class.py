"""
Player class for Kevin's Adventure Game.
Provides proper encapsulation of player data and methods with type hints.
"""
from typing import List, Dict, Any, Optional
from utils.text_formatting import format_inventory, print_game_over


class Player:
    """
    Represents a player in the game with health, inventory, location, and gold.
    
    Attributes:
        name (str): The player's name
        health (int): Current health points (0-100)
        max_health (int): Maximum health points
        inventory (List[str]): List of items in player's inventory
        location (str): Current location of the player
        gold (int): Amount of gold the player has
        agility (int): Player's agility stat (affects movement)
        perception (int): Player's perception stat (affects awareness)
    """
    
    def __init__(self, name: str, health: int = 100, max_health: int = 100, 
                 location: str = "Village", gold: int = 100) -> None:
        """
        Initialize a new player.
        
        Args:
            name: The player's name
            health: Starting health (default: 100)
            max_health: Maximum health (default: 100)
            location: Starting location (default: "Village")
            gold: Starting gold amount (default: 100)
        """
        self._validate_init_params(name, health, max_health, location, gold)
        
        self.name = name
        self.health = health
        self.max_health = max_health
        self.inventory: List[str] = []
        self.location = location
        self.gold = gold
        self.agility = 10  # Base agility stat
        self.perception = 10  # Base perception stat
    
    def _validate_init_params(self, name: str, health: int, max_health: int, 
                             location: str, gold: int) -> None:
        """Validate initialization parameters."""
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Player name must be a non-empty string")
        if not isinstance(health, int) or health < 0:
            raise ValueError("Health must be a non-negative integer")
        if not isinstance(max_health, int) or max_health <= 0:
            raise ValueError("Max health must be a positive integer")
        if health > max_health:
            raise ValueError("Health cannot exceed max health")
        if not isinstance(location, str) or not location.strip():
            raise ValueError("Location must be a non-empty string")
        if not isinstance(gold, int) or gold < 0:
            raise ValueError("Gold must be a non-negative integer")
    
    @property
    def is_alive(self) -> bool:
        """Check if the player is alive."""
        return self.health > 0
    
    @property
    def is_at_max_health(self) -> bool:
        """Check if the player is at maximum health."""
        return self.health >= self.max_health
    
    def get_status(self) -> str:
        """
        Get a formatted string of the player's current status.
        
        Returns:
            Formatted status string with health, inventory, and gold
        """
        return f"Health: {self.health}/{self.max_health} | Inventory: {format_inventory(self.inventory)} | Gold: {self.gold}"
    
    def add_item(self, item: str) -> bool:
        """
        Add an item to the player's inventory.
        
        Args:
            item: The item to add
            
        Returns:
            True if item was added successfully
            
        Raises:
            ValueError: If item is not a valid string
        """
        if not isinstance(item, str) or not item.strip():
            raise ValueError("Item must be a non-empty string")
        
        self.inventory.append(item.strip())
        print(f"You picked up: {item}")
        return True
    
    def remove_item(self, item: str) -> bool:
        """
        Remove an item from the player's inventory.
        
        Args:
            item: The item to remove
            
        Returns:
            True if item was removed, False if item not found
            
        Raises:
            ValueError: If item is not a valid string
        """
        if not isinstance(item, str) or not item.strip():
            raise ValueError("Item must be a non-empty string")
        
        item = item.strip()
        if item in self.inventory:
            self.inventory.remove(item)
            print(f"You dropped: {item}")
            return True
        else:
            print(f"You don't have {item} in your inventory.")
            return False
    
    def has_item(self, item: str) -> bool:
        """
        Check if the player has a specific item.
        
        Args:
            item: The item to check for
            
        Returns:
            True if player has the item, False otherwise
        """
        if not isinstance(item, str):
            return False
        return item.strip() in self.inventory
    
    def move_to(self, new_location: str) -> None:
        """
        Move the player to a new location.
        
        Args:
            new_location: The location to move to
            
        Raises:
            ValueError: If new_location is not a valid string
        """
        if not isinstance(new_location, str) or not new_location.strip():
            raise ValueError("Location must be a non-empty string")
        
        self.location = new_location.strip()
        print(f"You moved to: {new_location}")
    
    def heal(self, amount: int) -> int:
        """
        Heal the player by a specified amount.
        
        Args:
            amount: Amount of health to restore
            
        Returns:
            Actual amount healed
            
        Raises:
            ValueError: If amount is not a positive integer
        """
        if not isinstance(amount, int) or amount <= 0:
            raise ValueError("Heal amount must be a positive integer")
        
        old_health = self.health
        self.health = min(self.max_health, self.health + amount)
        actual_healed = self.health - old_health
        
        print(f"You healed for {actual_healed} health. Current health: {self.health}/{self.max_health}")
        return actual_healed
    
    def take_damage(self, amount: int) -> int:
        """
        Apply damage to the player.
        
        Args:
            amount: Amount of damage to apply
            
        Returns:
            Actual damage taken
            
        Raises:
            ValueError: If amount is not a positive integer
        """
        if not isinstance(amount, int) or amount <= 0:
            raise ValueError("Damage amount must be a positive integer")
        
        old_health = self.health
        self.health = max(0, self.health - amount)
        actual_damage = old_health - self.health
        
        print(f"You took {actual_damage} damage. Current health: {self.health}/{self.max_health}")
        
        if self.health == 0:
            print("You have been defeated.")
            print_game_over()
        
        return actual_damage
    
    def add_gold(self, amount: int) -> None:
        """
        Add gold to the player's purse.
        
        Args:
            amount: Amount of gold to add
            
        Raises:
            ValueError: If amount is not a non-negative integer
        """
        if not isinstance(amount, int) or amount < 0:
            raise ValueError("Gold amount must be a non-negative integer")
        
        self.gold += amount
        if amount > 0:
            print(f"You gained {amount} gold. Total gold: {self.gold}")
    
    def spend_gold(self, amount: int) -> bool:
        """
        Spend gold if the player has enough.
        
        Args:
            amount: Amount of gold to spend
            
        Returns:
            True if transaction successful, False if insufficient funds
            
        Raises:
            ValueError: If amount is not a positive integer
        """
        if not isinstance(amount, int) or amount <= 0:
            raise ValueError("Spend amount must be a positive integer")
        
        if self.gold >= amount:
            self.gold -= amount
            print(f"You spent {amount} gold. Remaining gold: {self.gold}")
            return True
        else:
            print(f"You don't have enough gold. You need {amount} but only have {self.gold}.")
            return False
    
    def modify_stat(self, stat_name: str, amount: int, min_value: int = 1) -> None:
        """
        Modify a player stat (agility, perception, etc.).
        
        Args:
            stat_name: Name of the stat to modify
            amount: Amount to modify (can be negative)
            min_value: Minimum value for the stat (default: 1)
            
        Raises:
            ValueError: If stat_name is invalid or amount is not an integer
        """
        if not isinstance(stat_name, str) or stat_name not in ['agility', 'perception']:
            raise ValueError("stat_name must be 'agility' or 'perception'")
        if not isinstance(amount, int):
            raise ValueError("Amount must be an integer")
        if not isinstance(min_value, int) or min_value < 0:
            raise ValueError("min_value must be a non-negative integer")
        
        current_value = getattr(self, stat_name)
        new_value = max(min_value, current_value + amount)
        setattr(self, stat_name, new_value)
        
        if amount != 0:
            change_desc = "increased" if amount > 0 else "decreased"
            print(f"Your {stat_name} has {change_desc} to {new_value}.")
    
    def to_dict(self) -> Dict[str, Any]:
        """
        Convert player to dictionary for saving.
        
        Returns:
            Dictionary representation of the player
        """
        return {
            "name": self.name,
            "health": self.health,
            "max_health": self.max_health,
            "inventory": self.inventory.copy(),
            "location": self.location,
            "gold": self.gold,
            "agility": self.agility,
            "perception": self.perception
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Player':
        """
        Create a player from dictionary data.
        
        Args:
            data: Dictionary containing player data
            
        Returns:
            New Player instance
            
        Raises:
            ValueError: If data is invalid or missing required fields
        """
        if not isinstance(data, dict):
            raise ValueError("Data must be a dictionary")
        
        required_fields = ["name", "health", "max_health", "location", "gold"]
        for field in required_fields:
            if field not in data:
                raise ValueError(f"Missing required field: {field}")
        
        player = cls(
            name=data["name"],
            health=data["health"],
            max_health=data["max_health"],
            location=data["location"],
            gold=data["gold"]
        )
        
        # Set optional fields
        if "inventory" in data and isinstance(data["inventory"], list):
            player.inventory = data["inventory"].copy()
        if "agility" in data and isinstance(data["agility"], int):
            player.agility = data["agility"]
        if "perception" in data and isinstance(data["perception"], int):
            player.perception = data["perception"]
        
        return player


# Backward compatibility functions
def create_player(name: str) -> Dict[str, Any]:
    """
    Create a player using the old function-based approach.
    This function maintains backward compatibility.
    
    Args:
        name: Player's name
        
    Returns:
        Dictionary representation of player (for compatibility)
    """
    player = Player(name)
    return player.to_dict()


def get_player_status(player_data: Dict[str, Any]) -> str:
    """
    Get player status from dictionary data.
    This function maintains backward compatibility.
    
    Args:
        player_data: Dictionary containing player data
        
    Returns:
        Formatted status string
    """
    if isinstance(player_data, dict):
        # Convert dict to Player object temporarily for status
        temp_player = Player.from_dict(player_data)
        return temp_player.get_status()
    else:
        raise ValueError("player_data must be a dictionary")


def add_item_to_inventory(player_data: Dict[str, Any], item: str) -> None:
    """
    Add item to inventory (backward compatibility).
    
    Args:
        player_data: Dictionary containing player data
        item: Item to add
    """
    if "inventory" not in player_data:
        player_data["inventory"] = []
    player_data["inventory"].append(item)
    print(f"You picked up: {item}")


def remove_item_from_inventory(player_data: Dict[str, Any], item: str) -> bool:
    """
    Remove item from inventory (backward compatibility).
    
    Args:
        player_data: Dictionary containing player data
        item: Item to remove
        
    Returns:
        True if item was removed, False otherwise
    """
    if "inventory" not in player_data:
        player_data["inventory"] = []
    
    if item in player_data["inventory"]:
        player_data["inventory"].remove(item)
        print(f"You dropped: {item}")
        return True
    else:
        print(f"You don't have {item} in your inventory.")
        return False


def move_player(player_data: Dict[str, Any], new_location: str) -> None:
    """
    Move player to new location (backward compatibility).
    
    Args:
        player_data: Dictionary containing player data
        new_location: Location to move to
    """
    player_data["location"] = new_location
    print(f"You moved to: {new_location}")


def heal_player(player_data: Dict[str, Any], amount: int) -> None:
    """
    Heal player (backward compatibility).
    
    Args:
        player_data: Dictionary containing player data
        amount: Amount to heal
    """
    max_health = player_data.get("max_health", 100)
    player_data["health"] = min(max_health, player_data["health"] + amount)
    print(f"You healed for {amount} health. Current health: {player_data['health']}")


def damage_player(player_data: Dict[str, Any], amount: int) -> None:
    """
    Damage player (backward compatibility).
    
    Args:
        player_data: Dictionary containing player data
        amount: Amount of damage
    """
    player_data["health"] = max(0, player_data["health"] - amount)
    print(f"You took {amount} damage. Current health: {player_data['health']}")
    if player_data["health"] == 0:
        print("You have been defeated.")
        print_game_over()

