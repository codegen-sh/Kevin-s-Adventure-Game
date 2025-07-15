from utils.text_formatting import format_inventory, print_game_over


class Player:
    """
    Player class representing the game character
    """
    
    def __init__(self, name, health=100, gold=100, location="Village"):
        """
        Initialize a new player
        
        Args:
            name (str): Player's name
            health (int): Starting health (default: 100)
            gold (int): Starting gold (default: 100)
            location (str): Starting location (default: "Village")
        """
        self.name = name
        self.health = max(0, min(100, health))  # Ensure health is between 0-100
        self.inventory = []
        self.location = location
        self.gold = max(0, gold)  # Ensure gold is not negative
        self.max_health = 100
    
    def get_status(self):
        """Get formatted player status string"""
        return f"Health: {self.health}/{self.max_health} | Inventory: {format_inventory(self.inventory)} | Gold: {self.gold}"
    
    def add_item(self, item):
        """
        Add an item to the player's inventory
        
        Args:
            item (str): Item to add
        """
        self.inventory.append(item)
        print(f"You picked up: {item}")
    
    def remove_item(self, item):
        """
        Remove an item from the player's inventory
        
        Args:
            item (str): Item to remove
            
        Returns:
            bool: True if item was removed, False if not found
        """
        if item in self.inventory:
            self.inventory.remove(item)
            print(f"You dropped: {item}")
            return True
        else:
            print(f"You don't have {item} in your inventory.")
            return False
    
    def has_item(self, item):
        """
        Check if player has a specific item
        
        Args:
            item (str): Item to check for
            
        Returns:
            bool: True if player has the item
        """
        return item in self.inventory
    
    def move_to(self, new_location):
        """
        Move player to a new location
        
        Args:
            new_location (str): Location to move to
        """
        self.location = new_location
        print(f"You moved to: {new_location}")
    
    def heal(self, amount):
        """
        Heal the player by a certain amount
        
        Args:
            amount (int): Amount to heal
        """
        old_health = self.health
        self.health = min(self.max_health, self.health + amount)
        actual_healing = self.health - old_health
        print(f"You healed for {actual_healing} health. Current health: {self.health}/{self.max_health}")
    
    def take_damage(self, amount):
        """
        Deal damage to the player
        
        Args:
            amount (int): Amount of damage to deal
        """
        self.health = max(0, self.health - amount)
        print(f"You took {amount} damage. Current health: {self.health}/{self.max_health}")
        
        if self.health == 0:
            print("You have been defeated.")
            print_game_over()
    
    def is_alive(self):
        """
        Check if player is still alive
        
        Returns:
            bool: True if player has health > 0
        """
        return self.health > 0
    
    def spend_gold(self, amount):
        """
        Spend gold if player has enough
        
        Args:
            amount (int): Amount of gold to spend
            
        Returns:
            bool: True if transaction successful, False if not enough gold
        """
        if self.gold >= amount:
            self.gold -= amount
            return True
        return False
    
    def add_gold(self, amount):
        """
        Add gold to player's purse
        
        Args:
            amount (int): Amount of gold to add
        """
        self.gold += amount
    
    def to_dict(self):
        """
        Convert player to dictionary for saving
        
        Returns:
            dict: Player data as dictionary
        """
        return {
            "name": self.name,
            "health": self.health,
            "inventory": self.inventory.copy(),
            "location": self.location,
            "gold": self.gold,
            "max_health": self.max_health
        }
    
    @classmethod
    def from_dict(cls, data):
        """
        Create player from dictionary data
        
        Args:
            data (dict): Player data dictionary
            
        Returns:
            Player: New player instance
        """
        player = cls(
            name=data.get("name", "Kevin"),
            health=data.get("health", 100),
            gold=data.get("gold", 100),
            location=data.get("location", "Village")
        )
        player.inventory = data.get("inventory", []).copy()
        player.max_health = data.get("max_health", 100)
        return player


# Backward compatibility functions for existing code
def create_player(name):
    """Create a new player (backward compatibility)"""
    return Player(name)

def get_player_status(player):
    """Get player status (backward compatibility)"""
    if isinstance(player, Player):
        return player.get_status()
    else:
        # Handle old dictionary format
        return f"Health: {player['health']} | Inventory: {format_inventory(player['inventory'])} | Gold: {player['gold']}"

def add_item_to_inventory(player, item):
    """Add item to inventory (backward compatibility)"""
    if isinstance(player, Player):
        player.add_item(item)
    else:
        # Handle old dictionary format
        player['inventory'].append(item)
        print(f"You picked up: {item}")

def remove_item_from_inventory(player, item):
    """Remove item from inventory (backward compatibility)"""
    if isinstance(player, Player):
        return player.remove_item(item)
    else:
        # Handle old dictionary format
        if item in player['inventory']:
            player['inventory'].remove(item)
            print(f"You dropped: {item}")
            return True
        else:
            print(f"You don't have {item} in your inventory.")
            return False

def move_player(player, new_location):
    """Move player (backward compatibility)"""
    if isinstance(player, Player):
        player.move_to(new_location)
    else:
        # Handle old dictionary format
        player['location'] = new_location
        print(f"You moved to: {new_location}")

def heal_player(player, amount):
    """Heal player (backward compatibility)"""
    if isinstance(player, Player):
        player.heal(amount)
    else:
        # Handle old dictionary format
        player['health'] = min(100, player['health'] + amount)
        print(f"You healed for {amount} health. Current health: {player['health']}")

def damage_player(player, amount):
    """Damage player (backward compatibility)"""
    if isinstance(player, Player):
        player.take_damage(amount)
    else:
        # Handle old dictionary format
        player['health'] = max(0, player['health'] - amount)
        print(f"You took {amount} damage. Current health: {player['health']}")
        if player['health'] == 0:
            print("You have been defeated.")
            print_game_over()
