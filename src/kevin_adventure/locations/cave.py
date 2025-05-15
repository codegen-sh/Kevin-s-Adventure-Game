"""
Cave location interaction handler.
"""
from typing import Any

from kevin_adventure.entities.item_registry import create_item
from kevin_adventure.ui.text_ui import TextUI
from kevin_adventure.utils.random_events import generate_random_event


def interact_with_cave(location: Any, player: Any, world: Any) -> bool:
    """
    Interact with the cave location.
    
    Args:
        location: The cave location
        player: The player
        world: The game world
        
    Returns:
        bool: True if the interaction was successful, False otherwise
    """
    ui = TextUI()
    ui.display_message("You enter the dark, mysterious cave. The air is cool and damp.")

    # Check if player has a torch
    has_light = player.has_item("torch")
    if not has_light:
        ui.display_message("It's very dark in here. You can barely see anything. A torch would be useful.")

    while True:
        ui.display_message("\nWhat would you like to do in the cave?")
        ui.display_message("1. Explore deeper" + (" (requires torch)" if not has_light else ""))
        ui.display_message("2. Search for minerals")
        ui.display_message("3. Listen to the cave")
        ui.display_message("4. Rest in the cave")
        ui.display_message("5. Leave the cave")

        choice = ui.get_input("Enter your choice (1-5): ")

        if choice == "1":
            if has_light:
                explore_cave(player, world, ui)
            else:
                ui.display_message("It's too dark to explore deeper without a torch.")
        elif choice == "2":
            search_for_minerals(player, ui)
        elif choice == "3":
            listen_to_cave(world, ui)
        elif choice == "4":
            rest_in_cave(player, ui)
        elif choice == "5":
            ui.display_message("You decide to leave the cave.")
            break
        else:
            ui.display_message("Invalid choice. Please try again.")
    
    return True


def explore_cave(player: Any, world: Any, ui: TextUI) -> None:
    """Explore deeper into the cave."""
    ui.display_message("You venture deeper into the cave, your torch illuminating the way.")
    event = generate_random_event(events=[
        ("find_treasure", 30), 
        ("encounter_bats", 20), 
        ("discover_underground_lake", 10), 
        (None, 40)
    ])

    if event == "find_treasure":
        ui.display_message("You discover a small treasure chest hidden in a crevice!")
        if generate_random_event(events=[("gold", 60), ("gemstone", 40)]) == "gold":
            ui.display_message("Inside, you find some gold coins!")
            player.gold += 25
        else:
            ui.display_message("Inside, you find a sparkling gemstone!")
            player.add_item(create_item("gemstone"))
    elif event == "encounter_bats":
        ui.display_message("A swarm of bats suddenly flies past you, startled by your presence!")
        if generate_random_event(events=[("take_damage", 30), (None, 70)]) == "take_damage":
            ui.display_message("You're disoriented by the bats and stumble, hurting yourself.")
            player.damage(5)
        else:
            ui.display_message("You duck just in time to avoid the swarm.")
    elif event == "discover_underground_lake":
        ui.display_message("You discover a beautiful underground lake with crystal-clear water.")
        ui.display_message("The water seems to have healing properties.")
        player.heal(15)
        # world.update_state("cave_lake_discovered", True)
    else:
        ui.display_message("You explore for a while but find nothing of interest.")


def search_for_minerals(player: Any, ui: TextUI) -> None:
    """Search for valuable minerals in the cave."""
    ui.display_message("You search the cave walls for valuable minerals.")
    if player.has_item("pickaxe"):
        ui.display_message("You use your pickaxe to chip away at promising spots in the rock.")
        if generate_random_event(events=[("find_gemstone", 40), (None, 60)]) == "find_gemstone":
            ui.display_message("Your efforts are rewarded! You find a valuable gemstone embedded in the rock!")
            player.add_item(create_item("gemstone"))
        else:
            ui.display_message("Despite your efforts, you don't find anything valuable this time.")
    else:
        ui.display_message("You examine the cave walls but can't extract anything without proper tools.")
        if generate_random_event(events=[("find_loose_gemstone", 10), (None, 90)]) == "find_loose_gemstone":
            ui.display_message("However, you spot a loose gemstone that you can pick up without tools!")
            player.add_item(create_item("gemstone"))


def listen_to_cave(world: Any, ui: TextUI) -> None:
    """Listen to the sounds of the cave."""
    ui.display_message("You stand still and listen carefully to the sounds of the cave.")
    event = generate_random_event(events=[
        ("dripping_water", 40), 
        ("distant_rumbling", 30), 
        ("strange_whispers", 10), 
        (None, 20)
    ])

    if event == "dripping_water":
        ui.display_message("You hear the steady drip of water echoing through the cave.")
        ui.display_message("Following the sound might lead to a water source.")
    elif event == "distant_rumbling":
        ui.display_message("You hear a distant rumbling sound. It might be an underground river or a cave-in.")
        ui.display_message("It might be wise to proceed with caution.")
    elif event == "strange_whispers":
        ui.display_message("You hear strange, whispered voices that seem to come from deeper in the cave.")
        ui.display_message("It's probably just the wind... right?")
        # world.update_state("cave_whispers_heard", True)
    else:
        ui.display_message("The cave is eerily silent except for the occasional drip of water.")


def rest_in_cave(player: Any, ui: TextUI) -> None:
    """Rest in the cave to recover health."""
    ui.display_message("You find a relatively comfortable spot and decide to rest for a while.")
    player.heal(10)
    ui.display_message("The rest has restored some of your energy.")
    
    # Random event while resting
    if generate_random_event(events=[("strange_dream", 20), (None, 80)]) == "strange_dream":
        ui.display_message("While resting, you have a strange dream about a hidden treasure deeper in the cave.")
        ui.display_message("When you wake up, you feel oddly refreshed and more perceptive.")
        player.modify_attribute("perception", 2)

