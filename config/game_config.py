"""
Game configuration module for Kevin's Adventure Game.
Contains all game settings, constants, and configurable values.
"""

# Game Settings
GAME_SETTINGS = {
    "starting_health": 100,
    "starting_gold": 100,
    "max_health": 200,
    "save_directory": "saves",
    "auto_save": True,
    "random_event_chance": 0.7,  # 70% chance of random events
}

# Player Settings
PLAYER_DEFAULTS = {
    "name": "Kevin",
    "health": GAME_SETTINGS["starting_health"],
    "gold": GAME_SETTINGS["starting_gold"],
    "inventory": [],
    "location": "Village",
}

# Item Healing/Damage Values
ITEM_EFFECTS = {
    "bread": {"heal": 20, "consumable": True},
    "berries": {"heal": 10, "damage": 5, "consumable": True, "poison_chance": 0.3},
    "mushrooms": {"heal": 20, "damage": 10, "consumable": True, "poison_chance": 0.5},
    "mountain_herbs": {"heal": 30, "consumable": True},
    "hermit's_blessing": {"heal": 50, "consumable": True},
    "rope": {"heal": 5, "location_specific": "Mountain"},
    "mysterious_potion": {"heal": 25, "consumable": True},
}

# Item Prices (for shops)
ITEM_PRICES = {
    "bread": 5,
    "torch": 10,
    "rope": 15,
    "sword": 50,
    "pickaxe": 25,
    "map": 20,
}

# Trading Values
TRADING_VALUES = {
    "gemstone": 50,
    "ancient_coin": 30,
    "silver_necklace": 25,
    "ancient_artifact": 100,
    "magic_ring": 75,
}

# Random Event Probabilities
RANDOM_EVENT_WEIGHTS = {
    "nothing": 20,
    "find_item": 20,
    "encounter": 20,
    "weather_change": 10,
    "trap": 10,
    "special_discovery": 20,
}

# Encounter Types and Probabilities
ENCOUNTER_TYPES = {
    "friendly_traveler": {"weight": 25, "heal": 10},
    "merchant": {"weight": 20, "cost": 20, "item": "mysterious_potion"},
    "lost_child": {"weight": 15, "reward": 15},
    "wild_animal": {"weight": 25, "damage": 15},
    "bandit": {"weight": 15, "steal_amount": 10},
}

# Treasure Types and Values
TREASURE_TYPES = {
    "gold_coin": {"weight": 5, "value": 5},
    "silver_necklace": {"weight": 10, "value": 10},
    "ancient_artifact": {"weight": 20, "value": 20},
    "magic_ring": {"weight": 30, "value": 30},
}

# Weather Types
WEATHER_TYPES = ["sunny", "rainy", "windy", "foggy", "stormy"]

# Trap Types and Damage
TRAP_TYPES = {
    "pitfall": {"min_damage": 5, "max_damage": 15},
    "snare": {"min_damage": 3, "max_damage": 10},
    "poison_dart": {"min_damage": 8, "max_damage": 20},
}

# Discovery Types
DISCOVERY_TYPES = [
    "hidden_cave",
    "ancient_ruins", 
    "magical_spring",
    "abandoned_camp"
]

# Text Display Settings
DISPLAY_SETTINGS = {
    "text_width": 80,
    "separator_char": "-",
    "separator_length": 80,
}

# Game Messages
MESSAGES = {
    "welcome": """
Welcome to Kevin's Adventure Game!

Explore a world of mystery and danger as you navigate through
forests, caves, villages, and mountains. Collect items, interact
with characters, and uncover the secrets of this magical realm.

Type 'help' at any time to see available commands.

Your journey begins now. Good luck, adventurer!
""",
    "game_over": """
Game Over

Your adventure has come to an end. Thank you for playing!
""",
    "save_success": "Game saved successfully as {filename}",
    "save_error": "Error saving game: {error}",
    "load_success": "Game loaded successfully from {filename}",
    "load_error": "Error loading game: {error}",
    "invalid_command": "Unknown command: '{command}'. Type 'help' for available commands.",
    "no_item": "You don't have {item} in your inventory.",
    "item_not_found": "There's no '{item}' here to pick up.",
    "item_picked_up": "You picked up the {item}.",
    "item_dropped": "You dropped the {item}.",
    "item_used": "You used the {item}.",
    "cant_use_item": "You can't use the {item} right now.",
    "location_blocked": "The path to {location} is blocked or inaccessible.",
    "moved_to_location": "You travel to {location}.",
    "inventory_empty": "Your inventory is empty.",
    "no_gold": "You don't have enough gold.",
}

# Help Text
HELP_TEXT = """
Available commands:
- move [location]: Move to a new location
- look: Examine your surroundings
- inventory: Check your inventory
- pickup [item]: Pick up an item
- drop [item]: Drop an item from your inventory
- use [item]: Use an item
- examine [item]: Get a description of an item
- status: Check your current status
- interact: Interact with your current location
- help: Show this help message
- quit: Save and exit the game
"""

