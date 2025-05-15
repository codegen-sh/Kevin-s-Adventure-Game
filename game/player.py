"""
Player module for the game.
"""
from game.base import GameObject
from utils.text_formatting import format_inventory, print_game_over


class Player(GameObject):
    """Class representing the player in the game."""
    
    def __init__(self, name, health=100, inventory=None, location="Village", gold=100):
        super().__init__(name)
        self.health = health
        self.inventory = inventory or []
        self.location = location
        self.gold = gold
    
    def get_status(self):
        """Get the player's current status."""
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
    
    def take_damage(self, amount):
        """Damage the player by a specified amount."""
        self.health = max(0, self.health - amount)
        print(f"You took {amount} damage. Current health: {self.health}")
        if self.health == 0:
            print("You have been defeated.")
            print_game_over()
    
    def has_item(self, item_name):
        """Check if the player has a specific item."""
        return item_name in self.inventory
    
    def add_gold(self, amount):
        """Add gold to the player's inventory."""
        self.gold += amount
        print(f"You gained {amount} gold. Current gold: {self.gold}")
    
    def remove_gold(self, amount):
        """Remove gold from the player's inventory."""
        if self.gold >= amount:
            self.gold -= amount
            print(f"You spent {amount} gold. Current gold: {self.gold}")
            return True
        else:
            print(f"You don't have enough gold. Current gold: {self.gold}")
            return False


# Compatibility functions for legacy code
def create_player(name):
    """Create a new player with the given name."""
    return Player(name)


def get_player_status(player):
    """Get the player's current status."""
    if isinstance(player, Player):
        return player.get_status()
    else:
        # Legacy support for dictionary-based player
        return f"Health: {player['health']} | Inventory: {format_inventory(player['inventory'])} | Gold: {player['gold']}"


def add_item_to_inventory(player, item):
    """Add an item to the player's inventory."""
    if isinstance(player, Player):
        player.add_item(item)
    else:
        # Legacy support for dictionary-based player
        player['inventory'].append(item)
        print(f"You picked up: {item}")


def remove_item_from_inventory(player, item):
    """Remove an item from the player's inventory."""
    if isinstance(player, Player):
        return player.remove_item(item)
    else:
        # Legacy support for dictionary-based player
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
        # Legacy support for dictionary-based player
        player['location'] = new_location
        print(f"You moved to: {new_location}")


def heal_player(player, amount):
    """Heal the player by a specified amount."""
    if isinstance(player, Player):
        player.heal(amount)
    else:
        # Legacy support for dictionary-based player
        player['health'] = min(100, player['health'] + amount)
        print(f"You healed for {amount} health. Current health: {player['health']}")


def damage_player(player, amount):
    """Damage the player by a specified amount."""
    if isinstance(player, Player):
        player.take_damage(amount)
    else:
        # Legacy support for dictionary-based player
        player['health'] = max(0, player['health'] - amount)
        print(f"You took {amount} damage. Current health: {player['health']}")
        if player['health'] == 0:
            print("You have been defeated.")
            print_game_over()

