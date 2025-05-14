from game.entity import Entity
from utils.text_formatting import format_inventory, print_game_over


class Player(Entity):
    """
    Represents the player character in the game.
    
    This class handles player attributes, inventory management,
    movement, and health-related functions.
    """
    
    def __init__(self, name):
        """
        Initialize a new Player.
        
        Args:
            name (str): The name of the player
        """
        super().__init__(name)
        self.health = 100
        self.inventory = []
        self.location = "Village"
        self.gold = 100
    
    def get_status(self):
        """Return a string representation of the player's status."""
        return f"Health: {self.health} | Inventory: {format_inventory(self.inventory)} | Gold: {self.gold}"
    
    def add_item(self, item):
        """Add an item to the player's inventory."""
        self.inventory.append(item)
        print(f"You picked up: {item}")
    
    def remove_item(self, item):
        """Remove an item from the player's inventory."""
        if item in self.inventory:
            self.inventory.remove(item)
            print(f"You dropped: {item}")
            return True
        else:
            print(f"You don't have {item} in your inventory.")
            return False
    
    def move(self, new_location):
        """Move the player to a new location."""
        self.location = new_location
        print(f"You moved to: {new_location}")
    
    def heal(self, amount):
        """Heal the player by a specified amount."""
        self.health = min(100, self.health + amount)
        print(f"You healed for {amount} health. Current health: {self.health}")
    
    def damage(self, amount):
        """Damage the player by a specified amount."""
        self.health = max(0, self.health - amount)
        print(f"You took {amount} damage. Current health: {self.health}")
        if self.health == 0:
            print("You have been defeated.")
            print_game_over()


# Legacy functions for backward compatibility
def create_player(name):
    """Create a new player with the given name."""
    return {
        "name": name,
        "health": 100,
        "inventory": [],
        "location": "Village",
        "gold": 100
    }

def get_player_status(player):
    """Get the player's status as a string."""
    if isinstance(player, Player):
        return player.get_status()
    return f"Health: {player['health']} | Inventory: {format_inventory(player['inventory'])} | Gold: {player['gold']}"

def add_item_to_inventory(player, item):
    """Add an item to the player's inventory."""
    if isinstance(player, Player):
        player.add_item(item)
    else:
        player['inventory'].append(item)
        print(f"You picked up: {item}")

def remove_item_from_inventory(player, item):
    """Remove an item from the player's inventory."""
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
    """Move the player to a new location."""
    if isinstance(player, Player):
        player.move(new_location)
    else:
        player['location'] = new_location
        print(f"You moved to: {new_location}")

def heal_player(player, amount):
    """Heal the player by a specified amount."""
    if isinstance(player, Player):
        player.heal(amount)
    else:
        player['health'] = min(100, player['health'] + amount)
        print(f"You healed for {amount} health. Current health: {player['health']}")

def damage_player(player, amount):
    """Damage the player by a specified amount."""
    if isinstance(player, Player):
        player.damage(amount)
    else:
        player['health'] = max(0, player['health'] - amount)
        print(f"You took {amount} damage. Current health: {player['health']}")
        if player['health'] == 0:
            print("You have been defeated.")
            print_game_over()
