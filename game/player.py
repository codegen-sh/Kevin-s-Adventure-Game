from typing import List, Dict, Any, Optional
from utils.text_formatting import format_inventory, print_game_over


class Player:
    """
    Player class representing the game character.
    """
    
    def __init__(self, name: str, health: int = 100, gold: int = 100, location: str = "Village"):
        """
        Initialize a new player.
        
        Args:
            name: Player's name
            health: Starting health (default: 100)
            gold: Starting gold (default: 100)
            location: Starting location (default: "Village")
        """
        self.name = name
        self.health = health
        self.max_health = 100
        self.inventory: List[str] = []
        self.location = location
        self.gold = gold
        self.knowledge: Dict[str, List[str]] = {}
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert player to dictionary for save/load compatibility."""
        return {
            "name": self.name,
            "health": self.health,
            "inventory": self.inventory.copy(),
            "location": self.location,
            "gold": self.gold,
            "knowledge": self.knowledge.copy()
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Player':
        """Create player from dictionary for save/load compatibility."""
        player = cls(
            name=data.get("name", "Kevin"),
            health=data.get("health", 100),
            gold=data.get("gold", 100),
            location=data.get("location", "Village")
        )
        player.inventory = data.get("inventory", [])
        player.knowledge = data.get("knowledge", {})
        return player
    
    def add_item(self, item: str) -> None:
        """Add an item to the player's inventory."""
        self.inventory.append(item)
        print(f"You picked up: {item}")
    
    def remove_item(self, item: str) -> bool:
        """Remove an item from the player's inventory."""
        if item in self.inventory:
            self.inventory.remove(item)
            print(f"You dropped: {item}")
            return True
        else:
            print(f"You don't have {item} in your inventory.")
            return False
    
    def has_item(self, item: str) -> bool:
        """Check if player has a specific item."""
        return item in self.inventory
    
    def move_to(self, new_location: str) -> None:
        """Move player to a new location."""
        self.location = new_location
        print(f"You moved to: {new_location}")
    
    def heal(self, amount: int) -> None:
        """Heal the player by a specific amount."""
        old_health = self.health
        self.health = min(self.max_health, self.health + amount)
        actual_heal = self.health - old_health
        print(f"You healed for {actual_heal} health. Current health: {self.health}")
    
    def take_damage(self, amount: int) -> None:
        """Deal damage to the player."""
        self.health = max(0, self.health - amount)
        print(f"You took {amount} damage. Current health: {self.health}")
        if self.health == 0:
            print("You have been defeated.")
            print_game_over()
    
    def is_alive(self) -> bool:
        """Check if player is still alive."""
        return self.health > 0
    
    def get_status(self) -> str:
        """Get formatted status string."""
        return f"Health: {self.health}/{self.max_health} | Inventory: {format_inventory(self.inventory)} | Gold: {self.gold}"
    
    def add_knowledge(self, category: str, knowledge: str) -> None:
        """Add knowledge to the player's knowledge base."""
        if category not in self.knowledge:
            self.knowledge[category] = []
        if knowledge not in self.knowledge[category]:
            self.knowledge[category].append(knowledge)
    
    def has_knowledge(self, category: str, knowledge: str) -> bool:
        """Check if player has specific knowledge."""
        return category in self.knowledge and knowledge in self.knowledge[category]


def create_player(name: str) -> Player:
    """
    Create a new player instance.
    
    Args:
        name: Player's name
        
    Returns:
        New Player instance
    """
    return Player(name)

def get_player_status(player):
    """Get player status - works with both Player class and dict."""
    if isinstance(player, Player):
        return player.get_status()
    return f"Health: {player['health']} | Inventory: {format_inventory(player['inventory'])} | Gold: {player['gold']}"

def add_item_to_inventory(player, item):
    """Add item to inventory - works with both Player class and dict."""
    if isinstance(player, Player):
        player.add_item(item)
    else:
        player['inventory'].append(item)
        print(f"You picked up: {item}")

def remove_item_from_inventory(player, item):
    """Remove item from inventory - works with both Player class and dict."""
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
    """Move player - works with both Player class and dict."""
    if isinstance(player, Player):
        player.move_to(new_location)
    else:
        player['location'] = new_location
        print(f"You moved to: {new_location}")

def heal_player(player, amount):
    """Heal player - works with both Player class and dict."""
    if isinstance(player, Player):
        player.heal(amount)
    else:
        player['health'] = min(100, player['health'] + amount)
        print(f"You healed for {amount} health. Current health: {player['health']}")

def damage_player(player, amount):
    """Damage player - works with both Player class and dict."""
    if isinstance(player, Player):
        player.take_damage(amount)
    else:
        player['health'] = max(0, player['health'] - amount)
        print(f"You took {amount} damage. Current health: {player['health']}")
        if player['health'] == 0:
            print("You have been defeated.")
            print_game_over()
