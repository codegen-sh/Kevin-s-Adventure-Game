"""
Module for handling item-related functionality in the game.
"""

# Dictionary of item descriptions
ITEM_DESCRIPTIONS = {
    # Basic items
    "map": "A weathered map showing the major locations in the area.",
    "bread": "A fresh loaf of bread. It smells delicious and will restore some health.",
    "stick": "A sturdy wooden stick. Could be useful for many things.",
    "berries": "Plump, juicy berries. They look safe to eat and will restore some health.",
    "torch": "A wooden torch that can be lit to provide light in dark places.",
    "gemstone": "A beautiful, sparkling gemstone. It might be valuable.",
    "rope": "A coil of strong rope. Useful for climbing or tying things.",
    "pickaxe": "A sturdy pickaxe for mining or breaking rocks.",
    "mushrooms": "Edible mushrooms that can restore some health.",
    
    # Weapons
    "sword": "A sharp, well-balanced sword. Useful in combat.",
    "bow": "A wooden bow with a taut string. Requires arrows to use effectively.",
    "arrows": "A bundle of arrows with sharp metal tips.",
    "dagger": "A small but sharp dagger. Easy to conceal.",
    
    # Armor
    "leather_armor": "Basic armor made from tanned leather. Provides some protection.",
    "shield": "A wooden shield reinforced with metal. Helps block attacks.",
    "helmet": "A metal helmet that protects your head.",
    
    # Magical items
    "mysterious_potion": "A strange, glowing potion. Who knows what it does?",
    "healing_potion": "A red potion that restores health when consumed.",
    "magic_ring": "A ring with arcane symbols. It seems to radiate magical energy.",
    "ancient_artifact": "An ancient artifact with mysterious symbols carved into it.",
    
    # Mythical creature items
    "unicorn_hair": "A shimmering hair from a unicorn's mane. It glows with magical energy.",
    "dragon_scale": "A tough, iridescent scale from a dragon. Extremely durable and heat-resistant.",
    "phoenix_feather": "A feather that glows like fire. It's warm to the touch.",
    "griffin_feather": "A large, strong feather from a griffin. Useful for crafting.",
    "troll_tooth": "A large, yellowed tooth from a troll. It's surprisingly valuable to collectors.",
    
    # Crafting materials
    "wood": "A piece of wood suitable for crafting.",
    "stone": "A chunk of stone that could be used for building or crafting.",
    "iron_ore": "Raw iron ore that needs to be smelted.",
    "copper_ore": "Raw copper ore that needs to be smelted.",
    "silver_nugget": "A small nugget of pure silver.",
    "gold_nugget": "A small nugget of pure gold.",
    
    # Miscellaneous
    "water_flask": "A flask filled with clean water.",
    "bedroll": "A rolled-up sleeping mat. Makes resting more comfortable.",
    "fishing_rod": "A simple rod for catching fish.",
    "flute": "A wooden flute that can play beautiful melodies.",
    "glowing_crystal": "A crystal that emits a soft, blue light.",
    "healing_herb": "A rare herb known for its healing properties."
}

# Item categories for organization
ITEM_CATEGORIES = {
    "weapon": ["sword", "bow", "arrows", "dagger", "stick"],
    "armor": ["leather_armor", "shield", "helmet"],
    "food": ["bread", "berries", "mushrooms"],
    "tool": ["map", "torch", "rope", "pickaxe", "fishing_rod", "bedroll", "water_flask"],
    "valuable": ["gemstone", "gold_nugget", "silver_nugget", "ancient_artifact"],
    "magical": ["mysterious_potion", "healing_potion", "magic_ring", "glowing_crystal"],
    "crafting": ["wood", "stone", "iron_ore", "copper_ore"],
    "mythical": ["unicorn_hair", "dragon_scale", "phoenix_feather", "griffin_feather", "troll_tooth"]
}

# Item effects when used
ITEM_EFFECTS = {
    "bread": {"health": 15},
    "berries": {"health": 10},
    "mushrooms": {"health": 8},
    "healing_potion": {"health": 50},
    "mysterious_potion": {"random_effect": True},
    "water_flask": {"health": 5, "stamina": 10}
}

# Item values for buying/selling
ITEM_VALUES = {
    "map": 5,
    "bread": 2,
    "stick": 1,
    "berries": 2,
    "torch": 3,
    "gemstone": 50,
    "rope": 10,
    "pickaxe": 15,
    "mushrooms": 3,
    "sword": 30,
    "bow": 25,
    "arrows": 5,
    "dagger": 15,
    "leather_armor": 20,
    "shield": 15,
    "helmet": 20,
    "mysterious_potion": 30,
    "healing_potion": 25,
    "magic_ring": 100,
    "ancient_artifact": 200,
    "unicorn_hair": 150,
    "dragon_scale": 200,
    "phoenix_feather": 150,
    "griffin_feather": 75,
    "troll_tooth": 40,
    "wood": 2,
    "stone": 1,
    "iron_ore": 8,
    "copper_ore": 5,
    "silver_nugget": 20,
    "gold_nugget": 40,
    "water_flask": 5,
    "bedroll": 10,
    "fishing_rod": 8,
    "flute": 15,
    "glowing_crystal": 35,
    "healing_herb": 15
}


def get_item_description(item_name):
    """
    Get the description of an item.
    
    Args:
        item_name (str): The name of the item
    
    Returns:
        str: The item description or a default message if not found
    """
    return ITEM_DESCRIPTIONS.get(item_name, f"A {item_name}. Nothing special about it.")


def get_item_value(item_name):
    """
    Get the monetary value of an item.
    
    Args:
        item_name (str): The name of the item
    
    Returns:
        int: The item value in gold or 1 if not specified
    """
    return ITEM_VALUES.get(item_name, 1)


def get_item_category(item_name):
    """
    Get the category of an item.
    
    Args:
        item_name (str): The name of the item
    
    Returns:
        str: The item category or 'miscellaneous' if not categorized
    """
    for category, items in ITEM_CATEGORIES.items():
        if item_name in items:
            return category
    return "miscellaneous"


def get_item_effect(item_name):
    """
    Get the effect of using an item.
    
    Args:
        item_name (str): The name of the item
    
    Returns:
        dict: The item effects or None if the item has no effects
    """
    return ITEM_EFFECTS.get(item_name)


def is_item_usable(item_name):
    """
    Check if an item can be used.
    
    Args:
        item_name (str): The name of the item
    
    Returns:
        bool: True if the item can be used, False otherwise
    """
    return item_name in ITEM_EFFECTS or get_item_category(item_name) in ["weapon", "tool", "magical"]


def get_all_items_in_category(category):
    """
    Get all items in a specific category.
    
    Args:
        category (str): The category name
    
    Returns:
        list: List of items in the category or empty list if category not found
    """
    return ITEM_CATEGORIES.get(category, [])

