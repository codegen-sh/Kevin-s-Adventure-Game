"""
Configuration and constants for Kevin's Adventure Game.
Centralizes all game settings, item prices, and other constants.
"""

from typing import Dict, List, Tuple, Any

# Game Settings
GAME_SETTINGS = {
    "max_health": 100,
    "starting_health": 100,
    "starting_gold": 100,
    "starting_location": "Village",
    "text_width": 80,
    "save_directory": "saves"
}

# Player Settings
PLAYER_DEFAULTS = {
    "agility": 10,
    "perception": 10,
    "strength": 10
}

# Shop Prices
SHOP_PRICES = {
    "bread": 5,
    "torch": 10,
    "rope": 15,
    "sword": 50,
    "mysterious_potion": 20
}

# Inn Prices
INN_PRICES = {
    "rest": 10
}

# Item Values (for selling)
ITEM_VALUES = {
    "gemstone": 50,
    "gold_coin": 1,
    "silver_necklace": 25,
    "ancient_artifact": 100,
    "magic_ring": 75,
    "ancient_coin": 30
}

# Healing Values
HEALING_VALUES = {
    "bread": 20,
    "berries": 10,
    "mushrooms": 20,
    "mountain_herbs": 30,
    "hermit's_blessing": 50,
    "inn_rest": 50,
    "magical_spring": 30,
    "friendly_traveler": 10,
    "villager_advice": 10
}

# Damage Values
DAMAGE_VALUES = {
    "berries_poison": 5,
    "mushrooms_poison": 10,
    "wild_animal": 15,
    "cave_bats": 5,
    "climbing_accident": 10,
    "cave_in": 8,
    "trap_pitfall": (5, 15),  # Range
    "ancient_artifact_curse": 10
}

# Weather Effects
WEATHER_EFFECTS = {
    "rainy": {"agility": -2},
    "stormy": {"agility": -3, "perception": -3},
    "foggy": {"perception": -4},
    "windy": {"agility": -1}
}

# Random Event Probabilities
EVENT_PROBABILITIES = {
    "forest_explore": [
        ("find_berries", 40),
        ("encounter_animal", 25),
        ("discover_clearing", 10),
        (None, 25)
    ],
    "forest_forage": [
        ("find_mushrooms", 30),
        (None, 70)
    ],
    "mountain_weather": [
        ("clear_skies", 50),
        ("incoming_storm", 50)
    ],
    "mountain_herbs": [
        ("find_herbs", 30),
        (None, 70)
    ],
    "mountain_treasure": [
        ("find_treasure", 20),
        (None, 80)
    ],
    "village_talk": [
        ("hear_rumor", 40),
        ("receive_advice", 30),
        (None, 30)
    ],
    "village_quest": [
        ("receive_quest", 30),
        (None, 70)
    ],
    "cave_treasure": [
        ("find_treasure", 30),
        ("find_danger", 20),
        ("find_nothing", 50)
    ],
    "cave_walls": [
        ("find_paintings", 25),
        ("find_minerals", 35),
        ("find_passage", 15),
        ("nothing_special", 25)
    ],
    "cave_sounds": [
        ("hear_water", 40),
        ("hear_creatures", 30),
        ("hear_wind", 20),
        ("hear_silence", 10)
    ],
    "cave_mining": [
        ("find_gems", 25),
        ("find_ore", 35),
        ("cave_in_risk", 15),
        ("nothing_valuable", 25)
    ],
    "random_encounter": [
        ("friendly_traveler", 20),
        ("merchant", 15),
        ("lost_child", 15),
        ("wild_animal", 25),
        ("bandit", 25)
    ],
    "general_exploration": [
        ("nothing", 20),
        ("find_item", 20),
        ("encounter", 20),
        ("weather_change", 10),
        ("trap", 10),
        ("special_discovery", 20)
    ]
}

# Item Descriptions
ITEM_DESCRIPTIONS = {
    "map": "An old, worn map of the surrounding area. It might help you navigate.",
    "bread": "A fresh loaf of bread. It looks delicious and nutritious.",
    "stick": "A sturdy wooden stick. It could be used as a simple weapon or tool.",
    "berries": "A handful of colorful berries. They might be edible... or not.",
    "torch": "A flaming torch that provides light in dark areas.",
    "gemstone": "A sparkling gemstone. It looks valuable.",
    "rope": "A coil of strong rope. Useful for climbing or tying things.",
    "pickaxe": "A sturdy pickaxe. Perfect for mining or breaking through rocks.",
    "mushrooms": "Some wild mushrooms. They could be edible or poisonous.",
    "mountain_herbs": "Rare medicinal herbs found on the mountain. They might have healing properties.",
    "ancient_coin": "An old coin with strange markings. It might be valuable to collectors.",
    "hermit's_blessing": "A mystical blessing from the mountain hermit. It fills you with energy.",
    "gold_coin": "A shiny gold coin. Standard currency in this realm.",
    "silver_necklace": "A delicate silver necklace. It could fetch a good price.",
    "ancient_artifact": "A mysterious object from a long-lost civilization. Its purpose is unknown.",
    "magic_ring": "A ring imbued with magical properties. Its effects are yet to be discovered.",
    "mysterious_potion": "A vial containing a strange, swirling liquid. Its effects are unknown.",
    "sword": "A well-crafted sword with a sharp blade. Useful for combat and self-defense.",
    "mysterious_package": "A sealed package that needs to be delivered to the mountain hermit.",
    "unicorn_hair": "A strand of hair from a magical unicorn. It shimmers with otherworldly light.",
    "dragon_scale": "A scale from a friendly dragon. It's warm to the touch and very durable."
}

# Location Descriptions
LOCATION_DESCRIPTIONS = {
    "Village": "A small, peaceful village with thatched-roof houses and friendly inhabitants.",
    "Forest": "A dense, mysterious forest with towering trees and the sound of rustling leaves.",
    "Cave": "A dark, damp cave with echoing sounds and glittering minerals on the walls.",
    "Mountain": "A tall, snow-capped mountain with treacherous paths and breathtaking views."
}

# Weather Descriptions
WEATHER_DESCRIPTIONS = {
    "clear": "The sky is clear and the sun is shining brightly.",
    "cloudy": "Gray clouds cover the sky, blocking out the sun.",
    "rainy": "A steady rain is falling, creating puddles on the ground.",
    "stormy": "Dark clouds loom overhead as thunder rumbles in the distance.",
    "foggy": "A thick fog has settled in, limiting visibility to just a few feet.",
    "windy": "Strong gusts of wind blow through the area, rustling leaves and branches."
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
    "help": """
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
- explore: Explore for random events
- help: Show this help message
- quit: Save and exit the game
""",
    "game_over": """
Game Over

Your adventure has come to an end. Thank you for playing!
""",
    "save_success": "Game saved successfully!",
    "load_success": "Game loaded successfully!",
    "invalid_command": "Unknown command. Type 'help' for available commands.",
    "not_enough_gold": "You don't have enough gold for that.",
    "item_not_found": "You don't see that item here.",
    "location_not_accessible": "You can't go there from here.",
    "inventory_empty": "Your inventory is empty."
}

# Treasure Types and Probabilities
TREASURE_TYPES = [
    ("gold_coin", 5),
    ("silver_necklace", 10),
    ("ancient_artifact", 20),
    ("magic_ring", 30)
]

# Mythical Creatures
MYTHICAL_CREATURES = {
    "phoenix": {
        "description": "A majestic phoenix appears in a burst of flames!",
        "effect": "heal",
        "value": 50
    },
    "unicorn": {
        "description": "A graceful unicorn materializes before you!",
        "effect": "item",
        "value": "unicorn_hair"
    },
    "dragon": {
        "description": "A powerful dragon descends from the sky! The dragon is friendly and will help you.",
        "effect": "item",
        "value": "dragon_scale"
    }
}

# Quest Rewards
QUEST_REWARDS = {
    "hermit_package": {
        "item": "hermit's_blessing",
        "healing": 100,
        "description": "The hermit thanks you and gives you their blessing."
    }
}

def get_random_event_probabilities(event_type: str) -> List[Tuple[str, int]]:
    """Get random event probabilities for a specific event type."""
    return EVENT_PROBABILITIES.get(event_type, [])

def get_item_description(item: str) -> str:
    """Get description for an item."""
    return ITEM_DESCRIPTIONS.get(item, "A mysterious item.")

def get_item_value(item: str) -> int:
    """Get the gold value of an item."""
    return ITEM_VALUES.get(item, 0)

def get_shop_price(item: str) -> int:
    """Get the shop price for an item."""
    return SHOP_PRICES.get(item, 0)

def get_healing_value(source: str) -> int:
    """Get the healing value for a healing source."""
    return HEALING_VALUES.get(source, 0)

def get_damage_value(source: str) -> int:
    """Get the damage value for a damage source."""
    damage = DAMAGE_VALUES.get(source, 0)
    if isinstance(damage, tuple):
        import random
        return random.randint(damage[0], damage[1])
    return damage

