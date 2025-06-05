"""
Game constants and configuration values.
Centralizes all magic strings and configuration to improve maintainability.
"""
from typing import Dict, List, Tuple

# Game Configuration
GAME_TITLE = "Kevin's Adventure Game"
DEFAULT_PLAYER_NAME = "Kevin"
DEFAULT_HEALTH = 100
DEFAULT_GOLD = 0
SAVE_FILE_EXTENSION = ".save"

# Player Stats
MAX_HEALTH = 100
MIN_HEALTH = 0

# Random Event Probabilities
RANDOM_EVENT_CHANCE = 0.3  # 30% chance on movement
EXPLORATION_EVENT_CHANCE = 0.4  # 40% chance when exploring
WAITING_EVENT_CHANCE = 0.2  # 20% chance when waiting

# Location Names
class Locations:
    FOREST = "Forest"
    VILLAGE = "Village"
    MOUNTAIN = "Mountain"
    CAVE = "Cave"

# Item Names
class Items:
    # Basic Items
    MAP = "map"
    BREAD = "bread"
    STICK = "stick"
    BERRIES = "berries"
    TORCH = "torch"
    ROPE = "rope"
    PICKAXE = "pickaxe"
    MUSHROOMS = "mushrooms"
    
    # Valuable Items
    GEMSTONE = "gemstone"
    GOLD_COIN = "gold_coin"
    SILVER_NECKLACE = "silver_necklace"
    ANCIENT_COIN = "ancient_coin"
    ANCIENT_ARTIFACT = "ancient_artifact"
    MAGIC_RING = "magic_ring"
    
    # Special Items
    MOUNTAIN_HERBS = "mountain_herbs"
    HERMITS_BLESSING = "hermit's_blessing"
    MYSTERIOUS_POTION = "mysterious_potion"
    SWORD = "sword"

# Item Descriptions
ITEM_DESCRIPTIONS: Dict[str, str] = {
    Items.MAP: "An old, worn map of the surrounding area. It might help you navigate.",
    Items.BREAD: "A fresh loaf of bread. It looks delicious and nutritious.",
    Items.STICK: "A sturdy wooden stick. It could be used as a simple weapon or tool.",
    Items.BERRIES: "A handful of colorful berries. They might be edible... or not.",
    Items.TORCH: "A flaming torch that provides light in dark areas.",
    Items.GEMSTONE: "A sparkling gemstone. It looks valuable.",
    Items.ROPE: "A coil of strong rope. Useful for climbing or tying things.",
    Items.PICKAXE: "A sturdy pickaxe. Perfect for mining or breaking through rocks.",
    Items.MUSHROOMS: "Some wild mushrooms. They could be edible or poisonous.",
    Items.MOUNTAIN_HERBS: "Rare medicinal herbs found on the mountain. They might have healing properties.",
    Items.ANCIENT_COIN: "An old coin with strange markings. It might be valuable to collectors.",
    Items.HERMITS_BLESSING: "A mystical blessing from the mountain hermit. It fills you with energy.",
    Items.GOLD_COIN: "A shiny gold coin. Standard currency in this realm.",
    Items.SILVER_NECKLACE: "A delicate silver necklace. It could fetch a good price.",
    Items.ANCIENT_ARTIFACT: "A mysterious object from a long-lost civilization. Its purpose is unknown.",
    Items.MAGIC_RING: "A ring imbued with magical properties. Its effects are yet to be discovered.",
    Items.MYSTERIOUS_POTION: "A vial containing a strange, swirling liquid. Its effects are unknown.",
    Items.SWORD: "A well-crafted sword with a sharp blade. Useful for combat and self-defense."
}

# Weather Types
class Weather:
    SUNNY = "sunny"
    RAINY = "rainy"
    WINDY = "windy"
    FOGGY = "foggy"
    STORMY = "stormy"

WEATHER_TYPES = [Weather.SUNNY, Weather.RAINY, Weather.WINDY, Weather.FOGGY, Weather.STORMY]

# Random Events
class EventTypes:
    NOTHING = "nothing"
    FIND_ITEM = "find_item"
    ENCOUNTER = "encounter"
    WEATHER_CHANGE = "weather_change"
    TRAP = "trap"
    SPECIAL_DISCOVERY = "special_discovery"

# Event Probabilities (event_type, weight)
RANDOM_EVENT_WEIGHTS: List[Tuple[str, int]] = [
    (EventTypes.NOTHING, 20),
    (EventTypes.FIND_ITEM, 20),
    (EventTypes.ENCOUNTER, 20),
    (EventTypes.WEATHER_CHANGE, 10),
    (EventTypes.TRAP, 10),
    (EventTypes.SPECIAL_DISCOVERY, 20)
]

# Encounter Types
class Encounters:
    FRIENDLY_TRAVELER = "friendly_traveler"
    MERCHANT = "merchant"
    LOST_CHILD = "lost_child"
    WILD_ANIMAL = "wild_animal"
    BANDIT = "bandit"

ENCOUNTER_TYPES = [
    Encounters.FRIENDLY_TRAVELER,
    Encounters.MERCHANT,
    Encounters.LOST_CHILD,
    Encounters.WILD_ANIMAL,
    Encounters.BANDIT
]

# Treasure Types with Values
TREASURE_TYPES: List[Tuple[str, int]] = [
    (Items.GOLD_COIN, 5),
    (Items.SILVER_NECKLACE, 10),
    (Items.ANCIENT_ARTIFACT, 20),
    (Items.MAGIC_RING, 30)
]

# Trap Types
class Traps:
    PITFALL = "pitfall"
    SNARE = "snare"
    POISON_DART = "poison_dart"

TRAP_TYPES = [Traps.PITFALL, Traps.SNARE, Traps.POISON_DART]

# Discovery Types
class Discoveries:
    HIDDEN_CAVE = "hidden_cave"
    ANCIENT_RUINS = "ancient_ruins"
    MAGICAL_SPRING = "magical_spring"
    ABANDONED_CAMP = "abandoned_camp"

DISCOVERY_TYPES = [
    Discoveries.HIDDEN_CAVE,
    Discoveries.ANCIENT_RUINS,
    Discoveries.MAGICAL_SPRING,
    Discoveries.ABANDONED_CAMP
]

# Item Effects
class ItemEffects:
    HEAL = "heal"
    DAMAGE = "damage"
    TELEPORT = "teleport"
    REVEAL_SECRET = "reveal_secret"
    WISDOM = "wisdom"
    CURSE = "curse"

# Command Aliases
MOVEMENT_COMMANDS = ["go", "move", "travel", "walk"]
INVENTORY_COMMANDS = ["inventory", "inv", "i"]
EXAMINATION_COMMANDS = ["look", "examine", "l"]
INTERACTION_COMMANDS = ["interact", "talk"]
STATUS_COMMANDS = ["status", "stats", "health"]
LOCATION_COMMANDS = ["location", "where", "where am i"]
EXPLORATION_COMMANDS = ["explore", "search"]
WAITING_COMMANDS = ["wait", "rest"]

# Help Text
HELP_TEXT = """
Available Commands:
- Movement: go, move, travel, walk [location]
- Inventory: inventory, inv, i
- Items: use [item], take [item], drop [item]
- Examination: look, examine [target]
- Interaction: interact, talk
- Status: status, stats, health
- Location: location, where
- Exploration: explore, search
- Other: wait, rest, help, quit

Examples:
- go village
- use bread
- take map
- examine sword
- look around
"""

# Color Codes for Text Formatting
class Colors:
    RED = "red"
    GREEN = "green"
    BLUE = "blue"
    YELLOW = "yellow"
    PURPLE = "purple"
    CYAN = "cyan"
    WHITE = "white"
    BOLD = "bold"

# Game Messages
class Messages:
    WELCOME = f"Welcome to {GAME_TITLE}!"
    GAME_SAVED = "Your progress has been saved."
    GAME_LOADED = "Game loaded successfully!"
    INVALID_COMMAND = "I don't understand that command. Type 'help' for available commands."
    INVENTORY_EMPTY = "Your inventory is empty."
    ITEM_NOT_FOUND = "You don't see that item here."
    ALREADY_AT_LOCATION = "You are already there!"
    LOCATION_NOT_ACCESSIBLE = "You cannot go there from here."
    HEALTH_RESTORED = "Your health has been restored!"
    PLAYER_DEFEATED = "You have been defeated!"

