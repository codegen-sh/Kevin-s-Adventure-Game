"""
Game Configuration - Settings and constants for Kevin's Adventure Game
"""

# Game Settings
GAME_TITLE = "Kevin's Adventure Game"
GAME_VERSION = "2.0.0"
DEFAULT_PLAYER_NAME = "Kevin"
DEFAULT_SAVE_DIRECTORY = "saves"

# Player Settings
DEFAULT_PLAYER_HEALTH = 100
DEFAULT_PLAYER_GOLD = 100
DEFAULT_STARTING_LOCATION = "Village"
EXPERIENCE_PER_LEVEL = 100
HEALTH_INCREASE_PER_LEVEL = 10

# World Settings
DEFAULT_TIME_OF_DAY = "morning"
DEFAULT_WEATHER = "clear"
TIME_PROGRESSION = {
    "morning": "afternoon",
    "afternoon": "evening", 
    "evening": "night",
    "night": "morning"
}

# Item Configuration
CONSUMABLE_ITEMS = [
    "bread", "healing potion", "berries", "ancient coin"
]

ITEM_EFFECTS = {
    "bread": {"type": "heal", "amount": 20},
    "healing potion": {"type": "heal", "amount": 50},
    "berries": {"type": "heal", "amount": 10},
    "ancient coin": {"type": "gold", "amount": 10},
    "torch": {"type": "utility", "description": "You light the torch, illuminating the area."},
    "map": {"type": "utility", "description": "You study the map and get a better sense of the area."},
    "rope": {"type": "utility", "description": "You examine the rope. It looks sturdy and useful for climbing."},
    "sword": {"type": "utility", "description": "You brandish your sword. You feel more confident in combat."},
    "pickaxe": {"type": "utility", "description": "You hold the pickaxe. Perfect for mining or breaking rocks."},
    "gemstone": {"type": "utility", "description": "The gemstone glitters beautifully in the light."},
    "glowing crystal": {"type": "utility", "description": "The crystal pulses with a mysterious energy."},
    "ancient artifact": {"type": "utility", "description": "You examine the ancient artifact. It seems to hold great power."},
    "cave pearl": {"type": "utility", "description": "The cave pearl shimmers with an otherworldly beauty."},
    "crystal shard": {"type": "utility", "description": "The crystal shard feels warm to the touch."}
}

# Command Aliases
MOVEMENT_COMMANDS = {
    "go": ["go", "move", "travel", "walk"],
    "north": ["north", "n"],
    "south": ["south", "s"], 
    "east": ["east", "e"],
    "west": ["west", "w"]
}

INTERACTION_COMMANDS = {
    "explore": ["explore", "interact", "look around", "examine"],
    "look": ["look", "l", "describe"],
    "inventory": ["inventory", "inv", "i"],
    "status": ["status", "stats", "health"],
    "help": ["help", "h", "?"],
    "locations": ["locations", "map"]
}

GAME_COMMANDS = {
    "quit": ["quit", "exit", "q"],
    "save": ["save"],
    "load": ["load"]
}

# Location Definitions
LOCATION_DEFINITIONS = {
    "Village": {
        "description": "A small, peaceful village with thatched-roof houses and friendly inhabitants.",
        "connections": ["Forest", "Mountain"],
        "items": ["map", "bread"]
    },
    "Forest": {
        "description": "A dense, mysterious forest with towering trees and the sound of rustling leaves.",
        "connections": ["Village", "Cave"],
        "items": ["stick", "berries"]
    },
    "Cave": {
        "description": "A dark, damp cave with echoing sounds and glittering minerals on the walls.",
        "connections": ["Forest"],
        "items": ["torch", "gemstone"]
    },
    "Mountain": {
        "description": "A tall, snow-capped mountain with treacherous paths and breathtaking views.",
        "connections": ["Village"],
        "items": ["rope", "pickaxe"]
    }
}

# Shop Configuration
SHOP_ITEMS = {
    "bread": {"price": 5, "description": "Fresh bread that restores health"},
    "torch": {"price": 10, "description": "A torch to light dark places"},
    "rope": {"price": 15, "description": "Strong rope for climbing"},
    "sword": {"price": 50, "description": "A sharp sword for protection"},
    "healing potion": {"price": 25, "description": "A magical potion that restores health"}
}

# Random Event Configuration
RANDOM_EVENT_CHANCE = 0.3  # 30% chance of random events
TREASURE_FIND_CHANCE = 0.6  # 60% chance of finding treasure when searching

# Display Configuration
HEALTH_BAR_LENGTH = 10
HEALTH_BAR_FILLED = '█'
HEALTH_BAR_EMPTY = '░'
SEPARATOR_LINE = '=' * 50

# Debug Settings
DEBUG_MODE = False
VERBOSE_LOGGING = False

