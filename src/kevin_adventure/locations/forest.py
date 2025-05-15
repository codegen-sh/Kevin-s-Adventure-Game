"""
Forest location interaction handler.
"""
from typing import Any

from kevin_adventure.entities.item_registry import create_item
from kevin_adventure.ui.text_ui import TextUI
from kevin_adventure.utils.random_events import generate_random_event


def interact_with_forest(location: Any, player: Any, world: Any) -> bool:
    """
    Interact with the forest location.
    
    Args:
        location: The forest location
        player: The player
        world: The game world
        
    Returns:
        bool: True if the interaction was successful, False otherwise
    """
    ui = TextUI()
    ui.display_message("You enter the lush, green forest. The air is filled with the sounds of birds and rustling leaves.")

    while True:
        ui.display_message("\nWhat would you like to do in the forest?")
        ui.display_message("1. Explore deeper")
        ui.display_message("2. Climb a tree")
        ui.display_message("3. Listen to the forest")
        ui.display_message("4. Forage for food")
        ui.display_message("5. Leave the forest")

        choice = ui.get_input("Enter your choice (1-5): ")

        if choice == "1":
            explore_forest(player, world, ui)
        elif choice == "2":
            climb_tree(world, ui)
        elif choice == "3":
            listen_to_forest(world, ui)
        elif choice == "4":
            forage_for_food(player, ui)
        elif choice == "5":
            ui.display_message("You decide to leave the forest.")
            break
        else:
            ui.display_message("Invalid choice. Please try again.")
    
    return True


def explore_forest(player: Any, world: Any, ui: TextUI) -> None:
    """Explore deeper into the forest."""
    ui.display_message("You decide to explore deeper into the forest.")
    event = generate_random_event(events=[("find_berries", 40), ("encounter_animal", 25), ("discover_clearing", 10), (None, 25)])

    if event == "find_berries":
        ui.display_message("You stumble upon a bush full of ripe berries!")
        player.add_item(create_item("berries"))
    elif event == "encounter_animal":
        ui.display_message("You encounter a friendly deer. It allows you to approach and pet it.")
        player.heal(5)
        ui.display_message("The peaceful interaction leaves you feeling refreshed.")
    elif event == "discover_clearing":
        ui.display_message("You discover a beautiful clearing with a small pond.")
        # Future enhancement: Add mythical creature encounter
        # world.update_state("forest_clearing_discovered", True)
    else:
        ui.display_message("Your exploration yields nothing of note this time.")


def climb_tree(world: Any, ui: TextUI) -> None:
    """Climb a tree to get a better view."""
    ui.display_message("You climb a tall tree to get a better view of the surrounding area.")
    ui.display_message("From up here, you can see the mountain peaks in the distance and what looks like the entrance to a cave.")


def listen_to_forest(world: Any, ui: TextUI) -> None:
    """Listen to the sounds of the forest."""
    ui.display_message("You stop and listen carefully to the sounds of the forest.")
    ui.display_message("You hear a faint sound of rushing water in the distance. There might be a river nearby.")
    # Future enhancement: Add river discovery
    # if generate_random_event(events=[("discover_river", 20), (None, 80)]) == "discover_river":
    #     ui.display_message("You've discovered a river!")
    #     world.update_state("forest_river_discovered", True)


def forage_for_food(player: Any, ui: TextUI) -> None:
    """Forage for food in the forest."""
    ui.display_message("You search the forest floor for edible plants and mushrooms.")
    if generate_random_event(events=[("find_mushrooms", 30), (None, 70)]) == "find_mushrooms":
        ui.display_message("You find some edible mushrooms!")
        player.add_item(create_item("mushrooms"))
    else:
        ui.display_message("You don't find anything edible this time.")

