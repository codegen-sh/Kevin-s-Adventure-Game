"""
Configuration module for Kevin's Adventure Game.
This module contains game settings and configuration parameters.
"""

# Player configuration
PLAYER_CONFIG = {
    "DEFAULT_NAME": "Kevin",
    "DEFAULT_HEALTH": 100,
    "DEFAULT_GOLD": 100,
    "DEFAULT_LOCATION": "Village",
    "MAX_HEALTH": 100,
    "MAX_INVENTORY_SIZE": 20  # Optional inventory size limit
}

# World configuration
WORLD_CONFIG = {
    "DEFAULT_LOCATION": "Village",
    "AVAILABLE_LOCATIONS": [
        "Village",
        "Forest",
        "Cave",
        "Mountain"
    ]
}

# Game mechanics configuration
GAME_MECHANICS = {
    "RANDOM_EVENT_CHANCE": 0.3,  # Chance of a random event occurring after an action
    "HEALING_ITEM_VALUE": {
        "potion": 20,
        "healing_potion": 30,
        "bread": 10,
        "berries": 5,
        "mushrooms": 8
    },
    "DAMAGE_VALUES": {
        "fall": 10,
        "animal_attack": 15,
        "trap": {
            "min": 5,
            "max": 15
        }
    }
}

# Item configuration
ITEMS = {
    "map": {
        "description": "A weathered map of the surrounding area. It shows the village, forest, cave, and mountain.",
        "usable": True,
        "value": 5
    },
    "bread": {
        "description": "A fresh loaf of bread. It smells delicious and would restore some health if eaten.",
        "usable": True,
        "value": 3,
        "healing": 10
    },
    "stick": {
        "description": "A sturdy wooden stick. It could be used as a simple weapon or tool.",
        "usable": True,
        "value": 2
    },
    "berries": {
        "description": "Plump, juicy berries. They look safe to eat and would restore some health.",
        "usable": True,
        "value": 2,
        "healing": 5
    },
    "torch": {
        "description": "A wooden torch that can be lit to illuminate dark areas.",
        "usable": True,
        "value": 5
    },
    "gemstone": {
        "description": "A sparkling gemstone that seems valuable.",
        "usable": False,
        "value": 20
    },
    "rope": {
        "description": "A coil of strong rope. Useful for climbing or binding things.",
        "usable": True,
        "value": 8
    },
    "pickaxe": {
        "description": "A sturdy pickaxe for mining or breaking rocks.",
        "usable": True,
        "value": 12
    },
    "mushrooms": {
        "description": "Edible mushrooms that would restore some health if eaten.",
        "usable": True,
        "value": 3,
        "healing": 8
    },
    "potion": {
        "description": "A mysterious potion that might have healing properties.",
        "usable": True,
        "value": 15,
        "healing": 20
    },
    "healing_potion": {
        "description": "A potion that will restore a significant amount of health when consumed.",
        "usable": True,
        "value": 25,
        "healing": 30
    },
    "gold_coin": {
        "description": "A shiny gold coin. It's worth 5 gold.",
        "usable": False,
        "value": 5
    },
    "silver_necklace": {
        "description": "A beautiful silver necklace. It's worth 10 gold.",
        "usable": False,
        "value": 10
    },
    "ancient_artifact": {
        "description": "A mysterious artifact from an ancient civilization. It's worth 20 gold.",
        "usable": False,
        "value": 20
    },
    "magic_ring": {
        "description": "A ring with magical properties. It's worth 30 gold.",
        "usable": True,
        "value": 30
    }
}

# Save/load configuration
SAVE_CONFIG = {
    "SAVE_DIRECTORY": "saves",
    "AUTOSAVE_ENABLED": True,
    "AUTOSAVE_FREQUENCY": 10  # Number of actions between autosaves
}

# Weather configuration
WEATHER_CONFIG = {
    "WEATHER_TYPES": [
        "sunny",
        "rainy",
        "windy",
        "foggy",
        "stormy"
    ],
    "WEATHER_EFFECTS": {
        "sunny": {
            "description": "The sun is shining brightly.",
            "health_effect": 1  # Small health regeneration in sunny weather
        },
        "rainy": {
            "description": "It's raining steadily.",
            "health_effect": 0
        },
        "windy": {
            "description": "A strong wind is blowing.",
            "health_effect": 0
        },
        "foggy": {
            "description": "A thick fog limits visibility.",
            "health_effect": 0
        },
        "stormy": {
            "description": "A fierce storm rages overhead.",
            "health_effect": -1  # Small health drain in stormy weather
        }
    },
    "WEATHER_CHANGE_CHANCE": 0.2  # Chance of weather changing after each action
}

# Command configuration
COMMANDS = {
    "move": {
        "aliases": ["go", "travel", "walk"],
        "description": "Move to a new location"
    },
    "look": {
        "aliases": ["examine", "observe"],
        "description": "Examine your surroundings"
    },
    "inventory": {
        "aliases": ["inv", "items", "i"],
        "description": "Check your inventory"
    },
    "pickup": {
        "aliases": ["take", "get", "grab"],
        "description": "Pick up an item"
    },
    "drop": {
        "aliases": ["discard", "throw"],
        "description": "Drop an item from your inventory"
    },
    "use": {
        "aliases": ["utilize", "activate"],
        "description": "Use an item"
    },
    "examine": {
        "aliases": ["inspect", "check"],
        "description": "Get a description of an item"
    },
    "status": {
        "aliases": ["stats", "health"],
        "description": "Check your current status"
    },
    "interact": {
        "aliases": ["talk", "speak"],
        "description": "Interact with your current location"
    },
    "help": {
        "aliases": ["?", "commands"],
        "description": "Show help message"
    },
    "quit": {
        "aliases": ["exit", "q"],
        "description": "Save and exit the game"
    }
}

