"""
Player Class - Object-oriented player representation for Kevin's Adventure Game
"""
from utils.text_formatting import format_inventory, print_game_over


class Player:
    """Represents a player in the game with stats, inventory, and abilities."""
    
    def __init__(self, name="Kevin", health=100, gold=100, location="Village"):
        self.name = name
        self.max_health = 100
        self.health = health
        self.gold = gold
        self.location = location
        self.inventory = []
        self.experience = 0
        self.level = 1
    
    def __str__(self):
        return f"{self.name} (Level {self.level})"
    
    def __repr__(self):
        return f"Player(name='{self.name}', health={self.health}, gold={self.gold})"
    
    @property
    def is_alive(self):
        """Check if the player is still alive."""
        return self.health > 0
    
    @property
    def health_percentage(self):
        """Get health as a percentage."""
        return (self.health / self.max_health) * 100
    
    def get_status(self):
        """Get a formatted status string."""
        inventory_str = format_inventory(self.inventory)
        health_bar = self._get_health_bar()
        return (f"Health: {health_bar} ({self.health}/{self.max_health}) | "
                f"Gold: {self.gold} | Level: {self.level} | "
                f"Inventory: {inventory_str}")
    
    def _get_health_bar(self):
        """Create a visual health bar."""
        bar_length = 10
        filled_length = int(bar_length * self.health / self.max_health)
        bar = '█' * filled_length + '░' * (bar_length - filled_length)
        return f"[{bar}]"
    
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
    
    def has_item(self, item):
        """Check if the player has a specific item."""
        return item in self.inventory
    
    def use_item(self, item):
        """Use an item from the player's inventory."""
        if not self.has_item(item):
            print(f"You don't have '{item}' in your inventory.")
            return False
        
        # Define item effects
        item_effects = {
            "bread": lambda: self.heal(20),
            "healing potion": lambda: self.heal(50),
            "berries": lambda: self.heal(10),
            "torch": lambda: print("You light the torch, illuminating the area."),
            "map": lambda: print("You study the map and get a better sense of the area."),
            "rope": lambda: print("You examine the rope. It looks sturdy and useful for climbing."),
            "sword": lambda: print("You brandish your sword. You feel more confident in combat."),
            "pickaxe": lambda: print("You hold the pickaxe. Perfect for mining or breaking rocks."),
            "gemstone": lambda: print("The gemstone glitters beautifully in the light."),
            "glowing crystal": lambda: print("The crystal pulses with a mysterious energy."),
            "ancient artifact": lambda: print("You examine the ancient artifact. It seems to hold great power."),
            "cave pearl": lambda: print("The cave pearl shimmers with an otherworldly beauty."),
            "crystal shard": lambda: print("The crystal shard feels warm to the touch."),
            "ancient coin": lambda: self.add_gold(10, "You examine the ancient coin and add it to your gold pouch.")
        }
        
        if item in item_effects:
            item_effects[item]()
            
            # Remove consumable items after use
            consumable_items = ["bread", "healing potion", "berries", "ancient coin"]
            if item in consumable_items:
                self.remove_item(item)
            
            return True
        else:
            print(f"You can't use '{item}' right now.")
            return False
    
    def heal(self, amount):
        """Heal the player by the specified amount."""
        old_health = self.health
        self.health = min(self.max_health, self.health + amount)
        actual_healing = self.health - old_health
        print(f"You healed for {actual_healing} health. Current health: {self.health}/{self.max_health}")
    
    def take_damage(self, amount):
        """Deal damage to the player."""
        self.health = max(0, self.health - amount)
        print(f"You took {amount} damage. Current health: {self.health}/{self.max_health}")
        
        if self.health == 0:
            print("You have been defeated.")
            print_game_over()
    
    def add_gold(self, amount, message=None):
        """Add gold to the player's purse."""
        self.gold += amount
        if message:
            print(f"{message} (+{amount} gold)")
        else:
            print(f"You gained {amount} gold. Total: {self.gold}")
    
    def spend_gold(self, amount):
        """Spend gold if the player has enough."""
        if self.gold >= amount:
            self.gold -= amount
            return True
        else:
            print(f"You don't have enough gold. You need {amount} but only have {self.gold}.")
            return False
    
    def move_to(self, location):
        """Move the player to a new location."""
        self.location = location
        print(f"You moved to: {location}")
    
    def add_experience(self, amount):
        """Add experience points and handle level ups."""
        self.experience += amount
        print(f"You gained {amount} experience points!")
        
        # Simple leveling system: 100 XP per level
        new_level = (self.experience // 100) + 1
        if new_level > self.level:
            self.level_up(new_level)
    
    def level_up(self, new_level):
        """Handle player leveling up."""
        old_level = self.level
        self.level = new_level
        
        # Increase max health and heal player
        health_increase = (new_level - old_level) * 10
        self.max_health += health_increase
        self.health = self.max_health  # Full heal on level up
        
        print(f"🎉 Level up! You are now level {self.level}!")
        print(f"Your maximum health increased by {health_increase}!")
        print(f"You have been fully healed!")
    
    def show_inventory(self):
        """Display the player's inventory."""
        if self.inventory:
            print("Your inventory contains:")
            for i, item in enumerate(self.inventory, 1):
                print(f"{i}. {item}")
        else:
            print("Your inventory is empty.")
    
    def to_dict(self):
        """Convert player to dictionary for saving."""
        return {
            "name": self.name,
            "health": self.health,
            "max_health": self.max_health,
            "gold": self.gold,
            "location": self.location,
            "inventory": self.inventory.copy(),
            "experience": self.experience,
            "level": self.level
        }
    
    @classmethod
    def from_dict(cls, data):
        """Create player from dictionary (for loading)."""
        player = cls(
            name=data.get("name", "Kevin"),
            health=data.get("health", 100),
            gold=data.get("gold", 100),
            location=data.get("location", "Village")
        )
        player.max_health = data.get("max_health", 100)
        player.inventory = data.get("inventory", [])
        player.experience = data.get("experience", 0)
        player.level = data.get("level", 1)
        return player

