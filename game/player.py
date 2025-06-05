from typing import Dict, Any, List
from game.constants import DEFAULT_HEALTH, DEFAULT_GOLD, MAX_HEALTH, MIN_HEALTH, Messages
from game.exceptions import InsufficientHealthError


def create_player(name: str) -> Dict[str, Any]:
    """Create a new player with default stats."""
    return {
        "name": name,
        "health": DEFAULT_HEALTH,
        "gold": DEFAULT_GOLD,
        "inventory": [],
        "location": "Village"
    }


def get_player_status(player: Dict[str, Any]) -> str:
    """Get a formatted string of the player's current status."""
    health = player.get("health", 0)
    gold = player.get("gold", 0)
    inventory_count = len(player.get("inventory", []))
    
    return f"Health: {health}/{MAX_HEALTH} | Gold: {gold} | Items: {inventory_count}"


def add_item_to_inventory(player: Dict[str, Any], item: str) -> bool:
    """Add an item to the player's inventory."""
    if "inventory" not in player:
        player["inventory"] = []
    
    player["inventory"].append(item)
    return True


def remove_item_from_inventory(player: Dict[str, Any], item: str) -> bool:
    """Remove an item from the player's inventory."""
    inventory = player.get("inventory", [])
    if item in inventory:
        inventory.remove(item)
        return True
    return False


def move_player(player: Dict[str, Any], new_location: str) -> None:
    """Move the player to a new location."""
    player["location"] = new_location


def heal_player(player: Dict[str, Any], amount: int) -> int:
    """
    Heal the player by the specified amount.
    
    Returns:
        int: The actual amount healed
    """
    current_health = player.get("health", 0)
    new_health = min(current_health + amount, MAX_HEALTH)
    actual_healed = new_health - current_health
    player["health"] = new_health
    return actual_healed


def damage_player(player: Dict[str, Any], amount: int) -> None:
    """Damage the player by the specified amount."""
    current_health = player.get("health", MAX_HEALTH)
    new_health = max(current_health - amount, MIN_HEALTH)
    player["health"] = new_health
    
    if new_health <= MIN_HEALTH:
        print(Messages.PLAYER_DEFEATED)
