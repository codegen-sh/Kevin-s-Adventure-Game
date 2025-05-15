"""
Registry for item use handlers and descriptions.
"""
import random
from typing import Dict, Callable, Any, Optional, Tuple, List

# Type alias for item use handlers
ItemUseHandler = Callable[['Item', Any, Any], bool]


# Dictionary of item descriptions
ITEM_DESCRIPTIONS: Dict[str, str] = {
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
    "mysterious_package": "A package wrapped in brown paper. It's addressed to the hermit on the mountain.",
}


# Dictionary to store item use handlers
_item_use_handlers: Dict[str, ItemUseHandler] = {}


def register_item_use_handler(item_name: str, handler: ItemUseHandler) -> None:
    """Register a use handler for an item type."""
    _item_use_handlers[item_name.lower()] = handler


def get_item_use_handler(item_name: str) -> Optional[ItemUseHandler]:
    """Get the use handler for an item type."""
    return _item_use_handlers.get(item_name.lower())


def get_item_description(item_name: str) -> str:
    """Get the description for an item type."""
    return ITEM_DESCRIPTIONS.get(item_name.lower(), "A mysterious item.")


# Define item use handlers

def use_map(item, player, world) -> bool:
    """Handler for using a map."""
    from kevin_adventure.ui.text_ui import TextUI
    ui = TextUI()
    
    ui.display_message("You consult the map. It shows the following locations you can go to:")
    available_locations = world.get_available_locations()
    for location in available_locations:
        ui.display_message(f"- {location}")
    return True


def use_bread(item, player, world) -> bool:
    """Handler for using bread."""
    from kevin_adventure.ui.text_ui import TextUI
    ui = TextUI()
    
    ui.display_message("You eat the bread. It's delicious and restores some health.")
    player.heal(20)
    player.remove_item(item.name)
    return True


def use_berries(item, player, world) -> bool:
    """Handler for using berries."""
    from kevin_adventure.ui.text_ui import TextUI
    from kevin_adventure.utils.random_events import generate_random_event
    ui = TextUI()
    
    ui.display_message("You eat the berries. They're sweet and juicy.")
    if generate_random_event(events=[("heal", 70), ("poison", 30)]) == "heal":
        ui.display_message("You feel refreshed and gain some health.")
        player.heal(10)
    else:
        ui.display_message("Uh oh, those weren't safe to eat. You lose some health.")
        player.damage(5)
    player.remove_item(item.name)
    return True


def use_torch(item, player, world) -> bool:
    """Handler for using a torch."""
    from kevin_adventure.ui.text_ui import TextUI
    ui = TextUI()
    
    current_location = world.get_current_location()
    if current_location.name == "Cave":
        ui.display_message("You light the torch, illuminating the dark cave around you.")
        current_location.description += " The cave is now well-lit by your torch."
        return True
    else:
        ui.display_message("You light the torch. It provides warmth and light.")
        return True


def use_gemstone(item, player, world) -> bool:
    """Handler for using a gemstone."""
    from kevin_adventure.ui.text_ui import TextUI
    ui = TextUI()
    
    ui.display_message("You examine the gemstone closely. It glimmers with an otherworldly light.")
    current_location = world.get_current_location()
    if current_location.name == "Village":
        ui.display_message("A merchant notices your gemstone and offers to buy it for 50 gold!")
        choice = ui.get_input("Do you want to sell the gemstone? (y/n): ").lower()
        if choice == 'y':
            player.gold += 50
            player.remove_item(item.name)
            ui.display_message("You sold the gemstone for 50 gold.")
        else:
            ui.display_message("You decide to keep the gemstone.")
    return True


# Register all item use handlers
register_item_use_handler("map", use_map)
register_item_use_handler("bread", use_bread)
register_item_use_handler("berries", use_berries)
register_item_use_handler("torch", use_torch)
register_item_use_handler("gemstone", use_gemstone)
# Add more handlers for other items as needed


def create_item(name: str) -> 'Item':
    """Create an item with the specified name."""
    from kevin_adventure.entities.item import Item
    
    description = get_item_description(name)
    use_handler = get_item_use_handler(name)
    
    return Item(name=name, description=description, use_handler=use_handler)

