"""
Utility functions for generating random events.
"""
import random
from typing import List, Tuple, Any, Optional


def generate_random_event(events: List[Tuple[Any, int]]) -> Any:
    """
    Generate a random event based on probabilities.
    
    Args:
        events: A list of tuples (event, probability)
        
    Returns:
        The selected event
    """
    return random.choices(
        [event[0] for event in events],
        weights=[event[1] for event in events]
    )[0]


def apply_random_event(player: Any, world: Any) -> None:
    """
    Apply a random event to the game state.
    
    Args:
        player: The player
        world: The game world
    """
    from kevin_adventure.ui.text_ui import TextUI
    ui = TextUI()
    
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
        find_treasure(player, ui)
    elif event == "encounter":
        handle_random_encounter(player, world, ui)
    elif event == "weather_change":
        weather_event(world, ui)
    elif event == "trap":
        trap_event(player, ui)
    elif event == "special_discovery":
        special_discovery(player, world, ui)


def find_treasure(player: Any, ui: TextUI) -> None:
    """
    Handle finding a treasure.
    
    Args:
        player: The player
        ui: The text UI
    """
    from kevin_adventure.entities.item_registry import create_item
    
    treasures = [
        ("gold_coin", 5),
        ("silver_necklace", 10),
        ("ancient_artifact", 20),
        ("magic_ring", 30)
    ]
    treasure, value = random.choice(treasures)
    
    ui.display_message(f"You found a {treasure} worth {value} gold!")
    player.add_item(create_item(treasure))
    player.gold += value


def handle_random_encounter(player: Any, world: Any, ui: TextUI) -> None:
    """
    Handle a random encounter event.
    
    Args:
        player: The player
        world: The game world
        ui: The text UI
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
        ui.display_message("You meet a friendly traveler who shares some of their supplies with you.")
        player.heal(10)
    elif encounter == "merchant":
        ui.display_message("A wandering merchant offers to sell you a mysterious potion.")
        if player.gold >= 20:
            choice = ui.get_input("Do you want to buy the potion for 20 gold? (y/n): ").lower()
            if choice == 'y':
                player.gold -= 20
                player.add_item(create_item("mysterious_potion"))
                ui.display_message("You bought the mysterious potion.")
            else:
                ui.display_message("You decline the offer.")
        else:
            ui.display_message("You don't have enough gold to buy the potion.")
    elif encounter == "lost_child":
        ui.display_message("You find a lost child. After helping them return to their village, the grateful parents reward you.")
        player.gold += 15
    elif encounter == "wild_animal":
        ui.display_message("A wild animal attacks you!")
        player.damage(15)
    elif encounter == "bandit":
        ui.display_message("A bandit tries to rob you!")
        if player.has_item("sword"):
            ui.display_message("You use your sword to fend off the bandit.")
        elif player.gold > 0:
            stolen_gold = min(player.gold, 10)
            player.gold -= stolen_gold
            ui.display_message(f"The bandit steals {stolen_gold} gold from you.")
        else:
            ui.display_message("The bandit finds nothing of value and leaves you alone.")


def weather_event(world: Any, ui: TextUI) -> None:
    """
    Handle a weather change event.
    
    Args:
        world: The game world
        ui: The text UI
    """
    weathers = ["sunny", "rainy", "windy", "foggy", "stormy"]
    new_weather = random.choice(weathers)
    ui.display_message(f"The weather changes to {new_weather}.")
    world.change_weather(new_weather)


def trap_event(player: Any, ui: TextUI) -> None:
    """
    Handle a trap event.
    
    Args:
        player: The player
        ui: The text UI
    """
    traps = ["pitfall", "snare", "poison_dart"]
    trap = random.choice(traps)
    ui.display_message(f"You've triggered a {trap} trap!")
    damage = random.randint(5, 15)
    player.damage(damage)


def special_discovery(player: Any, world: Any, ui: TextUI) -> None:
    """
    Handle a special discovery event.
    
    Args:
        player: The player
        world: The game world
        ui: The text UI
    """
    from kevin_adventure.entities.item_registry import create_item
    
    discoveries = [
        "hidden_cave",
        "ancient_ruins",
        "magical_spring",
        "abandoned_camp"
    ]
    discovery = random.choice(discoveries)
    ui.display_message(f"You've discovered a {discovery.replace('_', ' ')}!")

    if discovery == "hidden_cave":
        world.update_state("hidden_cave_discovered", True)
        ui.display_message("You mark the location of the hidden cave on your map.")
    elif discovery == "ancient_ruins":
        player.add_item(create_item("ancient_artifact"))
        ui.display_message("You find an ancient artifact among the ruins.")
    elif discovery == "magical_spring":
        player.heal(30)
        ui.display_message("You drink from the magical spring and feel rejuvenated.")
    elif discovery == "abandoned_camp":
        items = ["rope", "torch", "map"]
        found_item = random.choice(items)
        player.add_item(create_item(found_item))
        ui.display_message(f"You search the abandoned camp and find a {found_item}.")

