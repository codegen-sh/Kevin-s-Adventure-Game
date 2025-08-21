"""
Cave location module for Kevin's Adventure Game.

This module contains functions for handling player interactions in the cave location.
"""
from game.mythical import summon_mythical_creature
from game.player import add_item_to_inventory, damage_player, heal_player
from game.state import update_world_state
from utils.random_events import generate_random_event


def explore_cave(world, player):
    """
    Handle player interactions in the cave location.

    Args:
        world (dict): The game world state
        player (dict): The player's current state

    Returns:
        None
    """
    print("You enter a dark, mysterious cave. The air is damp and cool, and you can hear water dripping somewhere.")

    while True:
        print("\nWhat would you like to do in the cave?")
        print("1. Explore deeper")
        print("2. Search for minerals")
        print("3. Listen to the echoes")
        print("4. Rest in the cave")
        print("5. Leave the cave")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            explore_deeper(world, player)
        elif choice == "2":
            search_for_minerals(world, player)
        elif choice == "3":
            listen_to_echoes(world, player)
        elif choice == "4":
            rest_in_cave(world, player)
        elif choice == "5":
            print("You decide to leave the cave.")
            break
        else:
            print("Invalid choice. Please try again.")


def explore_deeper(world, player):
    """Explore deeper into the cave."""
    print("You venture deeper into the cave, your footsteps echoing off the walls.")
    
    if "torch" in player["inventory"]:
        print("Your torch illuminates the path ahead, revealing fascinating rock formations.")
        event = generate_random_event(events=[
            ("find_passage", 30),
            ("encounter_bats", 20),
            ("discover_crystals", 30),
            (None, 20)
        ])
        
        if event == "find_passage":
            print("You discover a hidden passage that seems to lead to an underground lake!")
            update_world_state(world, "discover_underground_lake")
        elif event == "encounter_bats":
            print("A swarm of bats suddenly flies past you, startled by your presence!")
            damage_player(player, 5)
            print("The bats scratch you as they fly by.")
        elif event == "discover_crystals":
            print("You discover a cluster of beautiful glowing crystals!")
            add_item_to_inventory(player, "glowing_crystal")
        else:
            print("Your exploration yields nothing of note this time.")
    else:
        print("It's too dark to see much without a torch. You stumble around and hurt yourself.")
        damage_player(player, 10)
        print("You decide to return to the cave entrance.")


def search_for_minerals(world, player):
    """Search for minerals in the cave."""
    print("You carefully examine the cave walls, looking for valuable minerals.")
    
    if "pickaxe" in player["inventory"]:
        print("With your pickaxe, you're able to extract minerals from the rock.")
        event = generate_random_event(events=[
            ("find_gemstone", 40),
            ("find_ore", 30),
            (None, 30)
        ])
        
        if event == "find_gemstone":
            print("You find a beautiful gemstone embedded in the rock!")
            add_item_to_inventory(player, "gemstone")
        elif event == "find_ore":
            print("You extract some valuable ore from the cave wall!")
            add_item_to_inventory(player, "ore")
        else:
            print("You don't find anything valuable this time.")
    else:
        print("You find some interesting minerals, but without a pickaxe, you can't extract them.")
        if generate_random_event(events=[("find_loose_gemstone", 20), (None, 80)]) == "find_loose_gemstone":
            print("However, you do find a small gemstone that was already loose!")
            add_item_to_inventory(player, "small_gemstone")


def listen_to_echoes(world, player):
    """Listen to the echoes in the cave."""
    print("You stand still and listen carefully to the echoes in the cave.")
    
    event = generate_random_event(events=[
        ("hear_water", 40),
        ("hear_creature", 30),
        ("hear_whispers", 10),
        (None, 20)
    ])
    
    if event == "hear_water":
        print("You hear the sound of running water. There must be an underground stream nearby.")
        update_world_state(world, "discover_underground_stream")
    elif event == "hear_creature":
        print("You hear strange noises deeper in the cave. Something might be living down there.")
        update_world_state(world, "cave_creature_presence")
    elif event == "hear_whispers":
        print("You hear what sounds like whispers coming from deeper in the cave.")
        print("A strange energy fills the air, and you feel a mystical presence.")
        summon_mythical_creature(world, player, "cave_spirit")
    else:
        print("You hear nothing but the dripping of water and your own breathing.")


def rest_in_cave(world, player):
    """Rest in the cave to recover health."""
    print("You find a relatively comfortable spot in the cave and decide to rest for a while.")
    
    if "torch" in player["inventory"]:
        print("Your torch provides warmth and keeps any cave creatures at bay.")
        heal_player(player, 15)
        print("You feel refreshed after your rest.")
    else:
        print("Without a torch, it's cold and a bit scary. Your rest is uneasy.")
        heal_player(player, 5)
        
        if generate_random_event(events=[("creature_approach", 30), (None, 70)]) == "creature_approach":
            print("You hear something approaching in the darkness!")
            damage_player(player, 10)
            print("Something scratches you before retreating back into the darkness.")

