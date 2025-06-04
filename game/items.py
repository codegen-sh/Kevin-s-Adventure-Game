import random

from config import config, ITEM_EFFECTS, TRADING_VALUES
from game.player import (
    add_item_to_inventory,
    damage_player,
    heal_player,
    move_player,
    remove_item_from_inventory,
)
from game.world import change_location, get_all_locations, get_available_locations
from utils.random_events import generate_random_event


def get_item_description(item):
    """Get description for an item from configuration."""
    return config.get_item_description(item)


def use_item(player, item, world):
    """
    Use an item from the player's inventory.
    
    Args:
        player (dict): Player state dictionary
        item (str): Name of the item to use
        world (dict): World state dictionary
        
    Returns:
        bool: True if item was used successfully, False otherwise
    """
    if item not in player["inventory"]:
        print(f"You don't have {item} in your inventory.")
        return False

    # Delegate to specific item handlers
    item_handlers = {
        "map": _use_map,
        "bread": _use_bread,
        "stick": _use_stick,
        "berries": _use_berries,
        "torch": _use_torch,
        "gemstone": _use_gemstone,
        "rope": _use_rope,
        "pickaxe": _use_pickaxe,
        "mushrooms": _use_mushrooms,
        "mountain_herbs": _use_mountain_herbs,
        "ancient_coin": _use_ancient_coin,
        "hermit's_blessing": _use_hermits_blessing,
        "sword": _use_sword,
        "gold_coin": _use_gold_coin,
        "silver_necklace": _use_silver_necklace,
        "ancient_artifact": _use_ancient_artifact,
    }
    
    handler = item_handlers.get(item)
    if handler:
        return handler(player, world)
    else:
        print(f"You're not sure how to use the {item}.")
        return False


def _use_map(player, world):
    """Use the map to show available locations."""
    print("You consult the map. It shows the following locations you can go to:")
    available_locations = get_available_locations(world)
    for location in available_locations:
        print(f"- {location}")
    return True


def _use_bread(player, world):
    """Use bread to restore health."""
    print("You eat the bread. It's delicious and restores some health.")
    heal_player(player, 20)
    remove_item_from_inventory(player, "bread")
    return True


def _use_stick(player, world):
    """Use the stick, with special effects in the forest."""
    print("You wave the stick around. It makes a satisfying swoosh sound.")
    if world["current_location"] == "Forest":
        print("A nearby bird is startled and drops a shiny object!")
        add_item_to_inventory(player, "gold_coin")
    return True


def _use_berries(player, world):
    """Use berries with random healing or poison effect."""
    print("You eat the berries. They're sweet and juicy.")
    if generate_random_event(events=[("heal", 70), ("poison", 30)]) == "heal":
        print("You feel refreshed and gain some health.")
        heal_player(player, 10)
    else:
        print("Uh oh, those weren't safe to eat. You lose some health.")
        damage_player(player, 5)
    remove_item_from_inventory(player, "berries")
    return True


def _use_torch(player, world):
    """Use torch to provide light, with special effects in caves."""
    current_location = world["current_location"]
    if current_location == "Cave":
        print("You light the torch, illuminating the dark cave around you.")
        world["locations"]["Cave"]["description"] += " The cave is now well-lit by your torch."
    else:
        print("You light the torch. It provides warmth and light.")
    return True


def _use_gemstone(player, world):
    """Use gemstone, with selling option in village."""
    print("You examine the gemstone closely. It glimmers with an otherworldly light.")
    if world["current_location"] == "Village":
        print("A merchant notices your gemstone and offers to buy it for 50 gold!")
        choice = input("Do you want to sell the gemstone? (y/n): ").lower()
        if choice == 'y':
            player["gold"] += 50
            remove_item_from_inventory(player, "gemstone")
            print("You sold the gemstone for 50 gold.")
        else:
            print("You decide to keep the gemstone.")
    return True


def _use_rope(player, world):
    """Use rope, with special effects on mountain."""
    if world["current_location"] == "Mountain":
        print("You use the rope to safely navigate a treacherous part of the mountain.")
        heal_player(player, 5)
        print("Your climbing technique improves, and you feel more confident.")
    else:
        print("You coil and uncoil the rope. It might be useful in the right situation.")
    return True


def _use_pickaxe(player, world):
    """Use pickaxe for mining."""
    print("You swing the pickaxe, but there's nothing here to mine.")
    return True


def _use_mushrooms(player, world):
    """Use mushrooms with random healing or poison effect."""
    print("You decide to eat the mushrooms.")
    if generate_random_event(events=[("heal", 50), ("poison", 50)]) == "heal":
        print("The mushrooms were edible and restore some health.")
        heal_player(player, 20)
    else:
        print("The mushrooms were poisonous! You feel sick.")
        damage_player(player, 10)
    remove_item_from_inventory(player, "mushrooms")
    return True


def _use_mountain_herbs(player, world):
    """Use mountain herbs for healing."""
    print("You brew a tea with the mountain herbs and drink it.")
    heal_player(player, 30)
    print("You feel invigorated and ready for more adventures!")
    remove_item_from_inventory(player, "mountain_herbs")
    return True


def _use_ancient_coin(player, world):
    """Use ancient coin with magical teleportation or revelation effects."""
    print("You flip the ancient coin. As it spins in the air, you feel a strange energy...")
    if generate_random_event(events=[("teleport", 50), ("reveal_secret", 50)]) == "teleport":
        new_location = random.choice(get_all_locations(world))
        change_location(world, new_location)
        move_player(player, new_location)
        print(f"The coin vanishes and you find yourself teleported to {new_location}!")
    else:
        print("The coin glows and reveals a secret about your current location!")
        # You might want to add some location-specific secrets here
    remove_item_from_inventory(player, "ancient_coin")
    return True


def _use_hermits_blessing(player, world):
    """Use hermit's blessing for significant healing."""
    print("You invoke the hermit's blessing. A warm, comforting light envelops you.")
    heal_player(player, 50)
    print("You feel completely refreshed and your mind is clear.")
    remove_item_from_inventory(player, "hermit's_blessing")
    return True


def _use_sword(player, world):
    """Use sword for combat practice, with special effects in forest."""
    print("You swing the sword, practicing your combat moves.")
    if world["current_location"] == "Forest":
        print("Your sword slices through some thick vines, revealing a hidden path!")
        # update_world_state(world, "reveal_hidden_path")
    return True


def _use_gold_coin(player, world):
    """Use gold coin, with trading option in village."""
    print("You flip the gold coin. It catches the light, shimmering brilliantly.")
    if world["current_location"] == "Village":
        print("A street vendor notices your coin and offers you a mysterious potion in exchange.")
        choice = input("Do you want to trade the gold coin for the potion? (y/n): ").lower()
        if choice == 'y':
            remove_item_from_inventory(player, "gold_coin")
            add_item_to_inventory(player, "mysterious_potion")
            print("You traded the gold coin for a mysterious potion.")
        else:
            print("You decide to keep the gold coin.")
    return True


def _use_silver_necklace(player, world):
    """Use silver necklace, with special effects on mountain."""
    print("You hold up the silver necklace, admiring its craftsmanship.")
    if world["current_location"] == "Mountain":
        print("The necklace begins to glow, revealing hidden runes on nearby rocks!")
        print("You discover a secret path leading to a hidden cave.")
        # update_player_knowledge(player, "ancient_history")
    else:
        print("The necklace sparkles beautifully, but nothing else happens.")
    return True


def _use_ancient_artifact(player, world):
    """Use ancient artifact with random wisdom, curse, or no effect."""
    print("You examine the ancient artifact closely, turning it over in your hands.")
    event = generate_random_event(events=[("wisdom", 40), ("curse", 30), ("nothing", 30)])
    
    if event == "wisdom":
        print("Suddenly, knowledge of the ancient world floods your mind!")
        print("You gain insight into the history of this land.")
        # update_player_knowledge(player, "ancient_history")
    elif event == "curse":
        print("A dark energy emanates from the artifact, making you feel weak.")
        damage_player(player, 10)
        print("You quickly put the artifact away, feeling drained.")
    else:
        print("Despite its age, the artifact remains inert and mysterious.")
    return True


def get_available_items(world, location):
    return world["locations"][location]["items"]

def add_item_to_world(world, location, item):
    if item not in world["locations"][location]["items"]:
        world["locations"][location]["items"].append(item)
        print(f"A {item} has been added to {location}.")
    else:
        print(f"There's already a {item} in {location}.")

def remove_item_from_world(world, location, item):
    if item in world["locations"][location]["items"]:
        world["locations"][location]["items"].remove(item)
        return True
    return False

def transfer_item(player, world, item, from_inventory_to_world=True):
    current_location = world["current_location"]

    if from_inventory_to_world:
        if remove_item_from_inventory(player, item):
            add_item_to_world(world, current_location, item)
            return True
    else:
        if remove_item_from_world(world, current_location, item):
            add_item_to_inventory(player, item)
            return True

    return False
