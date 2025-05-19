"""
Item manager module for Kevin's Adventure Game.
"""
import random
from typing import Dict, List, Optional

from kevin_adventure.core.player import Player
from kevin_adventure.core.world import World
from kevin_adventure.utils.random_events import generate_random_event


def get_item_description(item: str) -> str:
    """
    Get the description of an item.

    Args:
        item: The item to get the description for

    Returns:
        The item's description
    """
    item_descriptions = {
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
        "mysterious_package": "A package wrapped in brown paper and tied with string. It's addressed to the hermit on the mountain.",
        "unicorn_hair": "A shimmering strand of hair from a unicorn. It glows with a faint magical light.",
        "dragon_scale": "A tough, iridescent scale from a dragon. It's warm to the touch."
    }
    return item_descriptions.get(item, "A mysterious item.")


def use_item(player: Player, item: str, world: World) -> bool:
    """
    Use an item.

    Args:
        player: The player using the item
        item: The item to use
        world: The game world

    Returns:
        True if the item was used successfully, False otherwise
    """
    if item not in player.inventory:
        print(f"You don't have {item} in your inventory.")
        return False

    if item == "map":
        print("You consult the map. It shows the following locations you can go to:")
        available_locations = world.get_available_locations()
        for location in available_locations:
            print(f"- {location}")
        return True
    elif item == "bread":
        print("You eat the bread. It's delicious and restores some health.")
        player.heal(20)
        player.remove_item(item)
        return True
    elif item == "stick":
        print("You wave the stick around. It makes a satisfying swoosh sound.")
        if world.current_location == "Forest":
            print("A nearby bird is startled and drops a shiny object!")
            player.add_item("gold_coin")
        return True
    elif item == "berries":
        print("You eat the berries. They're sweet and juicy.")
        if generate_random_event(events=[("heal", 70), ("poison", 30)]) == "heal":
            print("You feel refreshed and gain some health.")
            player.heal(10)
        else:
            print("Uh oh, those weren't safe to eat. You lose some health.")
            player.damage(5)
        player.remove_item(item)
        return True
    elif item == "torch":
        current_location = world.current_location
        if current_location == "Cave":
            print("You light the torch, illuminating the dark cave around you.")
            world.locations[current_location].description += " The cave is now well-lit by your torch."
            return True
        else:
            print("You light the torch. It provides warmth and light.")
            return True
    elif item == "gemstone":
        print("You examine the gemstone closely. It glimmers with an otherworldly light.")
        if world.current_location == "Village":
            print("A merchant notices your gemstone and offers to buy it for 50 gold!")
            choice = input("Do you want to sell the gemstone? (y/n): ").lower()
            if choice == 'y':
                player.gold += 50
                player.remove_item(item)
                print("You sold the gemstone for 50 gold.")
            else:
                print("You decide to keep the gemstone.")
        return True
    elif item == "rope":
        if world.current_location == "Mountain":
            print("You use the rope to safely navigate a treacherous part of the mountain.")
            player.heal(5)
            print("Your climbing technique improves, and you feel more confident.")
        else:
            print("You coil and uncoil the rope. It might be useful in the right situation.")
        return True
    elif item == "pickaxe":
        print("You swing the pickaxe, but there's nothing here to mine.")
        return True
    elif item == "mushrooms":
        print("You decide to eat the mushrooms.")
        if generate_random_event(events=[("heal", 50), ("poison", 50)]) == "heal":
            print("The mushrooms were edible and restore some health.")
            player.heal(20)
        else:
            print("The mushrooms were poisonous! You feel sick.")
            player.damage(10)
        player.remove_item(item)
        return True
    elif item == "mountain_herbs":
        print("You brew a tea with the mountain herbs and drink it.")
        player.heal(30)
        print("You feel invigorated and ready for more adventures!")
        player.remove_item(item)
        return True
    elif item == "ancient_coin":
        print("You flip the ancient coin. As it spins in the air, you feel a strange energy...")
        if generate_random_event(events=[("teleport", 50), ("reveal_secret", 50)]) == "teleport":
            new_location = random.choice(world.get_all_locations())
            world.change_location(new_location)
            player.move(new_location)
            print(f"The coin vanishes and you find yourself teleported to {new_location}!")
        else:
            print("The coin glows and reveals a secret about your current location!")
            # You might want to add some location-specific secrets here
        player.remove_item(item)
        return True
    elif item == "hermit's_blessing":
        print("You invoke the hermit's blessing. A warm, comforting light envelops you.")
        player.heal(50)
        print("You feel completely refreshed and your mind is clear.")
        player.remove_item(item)
        return True
    elif item == "sword":
        print("You swing the sword, practicing your combat moves.")
        if world.current_location == "Forest":
            print("Your sword slices through some thick vines, revealing a hidden path!")
        return True
    elif item == "gold_coin":
        print("You flip the gold coin. It catches the light, shimmering brilliantly.")
        if world.current_location == "Village":
            print("A street vendor notices your coin and offers you a mysterious potion in exchange.")
            choice = input("Do you want to trade the gold coin for the potion? (y/n): ").lower()
            if choice == 'y':
                player.remove_item(item)
                player.add_item("mysterious_potion")
                print("You traded the gold coin for a mysterious potion.")
            else:
                print("You decide to keep the gold coin.")
        return True
    elif item == "silver_necklace":
        print("You hold up the silver necklace, admiring its craftsmanship.")
        if world.current_location == "Mountain":
            print("The necklace begins to glow, revealing hidden runes on nearby rocks!")
            print("You discover a secret path leading to a hidden cave.")
        else:
            print("The necklace sparkles beautifully, but nothing else happens.")
        return True
    elif item == "ancient_artifact":
        print("You examine the ancient artifact closely, turning it over in your hands.")
        event = generate_random_event(events=[("wisdom", 40), ("curse", 30), (None, 30)])
        if event == "wisdom":
            print("Suddenly, knowledge of the ancient world floods your mind!")
            print("You gain insight into the history of this land.")
        elif event == "curse":
            print("A dark energy emanates from the artifact, making you feel weak.")
            player.damage(10)
            print("You quickly put the artifact away, feeling drained.")
        else:
            print("Despite its age, the artifact remains inert and mysterious.")
        return True
    elif item == "mysterious_potion":
        print("You drink the mysterious potion...")
        effect = generate_random_event(events=[("heal", 40), ("damage", 20), ("strength", 20), ("teleport", 20)])
        if effect == "heal":
            print("The potion has a sweet taste and fills you with warmth.")
            player.heal(30)
            print("You feel much better!")
        elif effect == "damage":
            print("The potion tastes bitter and makes your stomach churn.")
            player.damage(15)
            print("That was probably not a good idea...")
        elif effect == "strength":
            print("The potion has a spicy flavor and makes your muscles tingle.")
            print("You feel stronger! Your next combat encounter will be easier.")
            # Future implementation: Add temporary strength boost
        elif effect == "teleport":
            print("The potion fizzes and bubbles. Your vision blurs...")
            new_location = random.choice(world.get_all_locations())
            world.change_location(new_location)
            player.move(new_location)
            print(f"You find yourself teleported to {new_location}!")
        player.remove_item(item)
        return True
    elif item == "mysterious_package":
        if world.current_location == "Mountain":
            print("You should deliver this package to the hermit at the mountain peak.")
        else:
            print("This package is addressed to the hermit who lives on the mountain peak.")
        return True
    elif item == "unicorn_hair":
        print("You examine the unicorn hair. It shimmers with magical energy.")
        player.heal(15)
        print("Just holding it makes you feel better.")
        return True
    elif item == "dragon_scale":
        print("You examine the dragon scale. It's warm to the touch and incredibly tough.")
        print("It might offer some protection in dangerous situations.")
        # Future implementation: Add protection effect
        return True
    else:
        print(f"You're not sure how to use the {item}.")
        return False


def get_available_items(world: World, location: str) -> List[str]:
    """
    Get the available items in a location.

    Args:
        world: The game world
        location: The location to get items for

    Returns:
        A list of available items
    """
    return world.locations[location].items


def add_item_to_world(world: World, location: str, item: str) -> None:
    """
    Add an item to a location in the world.

    Args:
        world: The game world
        location: The location to add the item to
        item: The item to add
    """
    if item not in world.locations[location].items:
        world.locations[location].items.append(item)
        print(f"A {item} has been added to {location}.")
    else:
        print(f"There's already a {item} in {location}.")


def remove_item_from_world(world: World, location: str, item: str) -> bool:
    """
    Remove an item from a location in the world.

    Args:
        world: The game world
        location: The location to remove the item from
        item: The item to remove

    Returns:
        True if the item was removed, False otherwise
    """
    if item in world.locations[location].items:
        world.locations[location].items.remove(item)
        return True
    return False


def transfer_item(player: Player, world: World, item: str, from_inventory_to_world: bool = True) -> bool:
    """
    Transfer an item between the player's inventory and the world.

    Args:
        player: The player transferring the item
        world: The game world
        item: The item to transfer
        from_inventory_to_world: Whether to transfer from inventory to world or vice versa

    Returns:
        True if the item was transferred, False otherwise
    """
    current_location = world.current_location

    if from_inventory_to_world:
        if player.remove_item(item):
            add_item_to_world(world, current_location, item)
            return True
    else:
        if remove_item_from_world(world, current_location, item):
            player.add_item(item)
            return True

    return False

