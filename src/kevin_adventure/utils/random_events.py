"""
Random event utilities for Kevin's Adventure Game.
"""
import random
from typing import Dict, List, Optional, Tuple, Union

from kevin_adventure.core.player import Player
from kevin_adventure.core.world import World
from kevin_adventure.utils.text_formatting import print_event


def generate_random_event(events: List[Tuple[Optional[str], int]]) -> Optional[str]:
    """
    Generate a random event based on probabilities.

    Args:
        events: A list of tuples containing the event name and its probability

    Returns:
        The selected event name, or None if no event was selected
    """
    return random.choices(
        [event[0] for event in events],
        weights=[event[1] for event in events]
    )[0]


def handle_random_encounter(player: Player, world: World) -> None:
    """
    Handle a random encounter event.

    Args:
        player: The player encountering the event
        world: The game world
    """
    encounters = [
        "friendly_traveler",
        "merchant",
        "lost_child",
        "wild_animal",
        "bandit"
    ]
    encounter = random.choice(encounters)

    if encounter == "friendly_traveler":
        print_event("You meet a friendly traveler who shares some of their supplies with you.")
        player.heal(10)
    elif encounter == "merchant":
        print_event("A wandering merchant offers to sell you a mysterious potion.")
        if player.gold >= 20:
            choice = input("Do you want to buy the potion for 20 gold? (y/n): ").lower()
            if choice == 'y':
                player.gold -= 20
                player.add_item("mysterious_potion")
                print("You bought the mysterious potion.")
            else:
                print("You decline the offer.")
        else:
            print("You don't have enough gold to buy the potion.")
    elif encounter == "lost_child":
        print_event("You find a lost child. After helping them return to their village, the grateful parents reward you.")
        player.gold += 15
    elif encounter == "wild_animal":
        print_event("A wild animal attacks you!")
        player.damage(15)
    elif encounter == "bandit":
        print_event("A bandit tries to rob you!")
        if "sword" in player.inventory:
            print("You use your sword to fend off the bandit.")
        elif player.gold > 0:
            stolen_gold = min(player.gold, 10)
            player.gold -= stolen_gold
            print(f"The bandit steals {stolen_gold} gold from you.")
        else:
            print("The bandit finds nothing of value and leaves you alone.")


def find_treasure(player: Player) -> None:
    """
    Handle finding a treasure.

    Args:
        player: The player finding the treasure
    """
    treasures = [
        ("gold_coin", 5),
        ("silver_necklace", 10),
        ("ancient_artifact", 20),
        ("magic_ring", 30)
    ]
    treasure, value = random.choice(treasures)
    print_event(f"You found a {treasure} worth {value} gold!")
    player.add_item(treasure)
    player.gold += value


def weather_event(world: World) -> None:
    """
    Handle a weather change event.

    Args:
        world: The game world
    """
    weathers = ["sunny", "rainy", "windy", "foggy", "stormy"]
    new_weather = random.choice(weathers)
    print_event(f"The weather changes to {new_weather}.")
    world.weather = new_weather


def trap_event(player: Player) -> None:
    """
    Handle a trap event.

    Args:
        player: The player triggering the trap
    """
    traps = ["pitfall", "snare", "poison_dart"]
    trap = random.choice(traps)
    print_event(f"You've triggered a {trap} trap!")
    damage = random.randint(5, 15)
    player.damage(damage)


def special_discovery(player: Player, world: World) -> None:
    """
    Handle a special discovery event.

    Args:
        player: The player making the discovery
        world: The game world
    """
    discoveries = [
        "hidden_cave",
        "ancient_ruins",
        "magical_spring",
        "abandoned_camp"
    ]
    discovery = random.choice(discoveries)
    print_event(f"You've discovered a {discovery.replace('_', ' ')}!")

    if discovery == "hidden_cave":
        print("You mark the location of the hidden cave on your map.")
    elif discovery == "ancient_ruins":
        player.add_item("ancient_artifact")
        print("You find an ancient artifact among the ruins.")
    elif discovery == "magical_spring":
        player.heal(30)
        print("You drink from the magical spring and feel rejuvenated.")
    elif discovery == "abandoned_camp":
        items = ["rope", "torch", "map"]
        found_item = random.choice(items)
        player.add_item(found_item)
        print(f"You search the abandoned camp and find a {found_item}.")


def apply_random_event(player: Player, world: World) -> None:
    """
    Apply a random event to the game state.

    Args:
        player: The player experiencing the event
        world: The game world
    """
    event = generate_random_event(events=[
        ("nothing", 20),
        ("find_item", 20),
        ("encounter", 20),
        ("weather_change", 10),
        ("trap", 10),
        ("special_discovery", 20)
    ])

    if event == "nothing":
        return  # No event occurs
    elif event == "find_item":
        find_treasure(player)
    elif event == "encounter":
        handle_random_encounter(player, world)
    elif event == "weather_change":
        weather_event(world)
    elif event == "trap":
        trap_event(player)
    elif event == "special_discovery":
        special_discovery(player, world)

