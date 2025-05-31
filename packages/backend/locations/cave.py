from game.player import damage_player, add_item_to_inventory
import random

def explore_cave(player, world):
    """
    Explore the mysterious cave.
    
    Args:
    player (dict): The player's current state
    world (dict): The game world state
    
    Returns:
    str: Description of what happened in the cave
    """
    print("You enter a dark, mysterious cave...")
    
    # Random events in the cave
    events = [
        "treasure",
        "monster",
        "empty",
        "crystal"
    ]
    
    event = random.choice(events)
    
    if event == "treasure":
        treasure_items = ["gold_coin", "ancient_scroll", "magic_gem"]
        treasure = random.choice(treasure_items)
        add_item_to_inventory(player, treasure)
        return f"You found a {treasure} hidden in the cave!"
    
    elif event == "monster":
        damage = random.randint(10, 25)
        damage_player(player, damage)
        return f"A cave monster attacks you! You take {damage} damage but manage to escape."
    
    elif event == "crystal":
        add_item_to_inventory(player, "glowing_crystal")
        return "You discover a beautiful glowing crystal that might be useful later."
    
    else:
        return "The cave is empty, but you feel a mysterious presence watching you..."

