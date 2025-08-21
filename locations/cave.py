"""
Cave location module for Kevin's Adventure Game.
This module handles all interactions in the cave location.
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
    print("You enter a dark, mysterious cave. The air is damp and cool.")
    
    # Check if player has a torch
    has_torch = "torch" in player["inventory"]
    if not has_torch:
        print("It's very dark in here. A torch would be helpful.")
        damage_player(player, 5)
        print("You stumble in the darkness and hurt yourself.")
    
    while True:
        print("\nWhat would you like to do in the cave?")
        print("1. Explore deeper")
        print("2. Search for minerals")
        print("3. Listen to the cave")
        print("4. Rest in the cave")
        print("5. Leave the cave")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            explore_deeper(world, player, has_torch)
        elif choice == "2":
            search_for_minerals(world, player, has_torch)
        elif choice == "3":
            listen_to_cave(world, player)
        elif choice == "4":
            rest_in_cave(world, player)
        elif choice == "5":
            print("You decide to leave the cave.")
            break
        else:
            print("Invalid choice. Please try again.")


def explore_deeper(world, player, has_torch):
    """Explore deeper into the cave."""
    print("You venture deeper into the cave.")
    
    if not has_torch:
        print("It's too dark to see much without a torch.")
        damage_player(player, 10)
        print("You trip over rocks and hurt yourself in the darkness.")
        return
    
    event = generate_random_event(events=[
        ("find_gemstone", 30),
        ("encounter_bat", 20),
        ("discover_underground_lake", 10),
        (None, 40)
    ])
    
    if event == "find_gemstone":
        print("You discover a sparkling gemstone embedded in the cave wall!")
        add_item_to_inventory(player, "gemstone")
    elif event == "encounter_bat":
        print("A swarm of bats suddenly flies past you, startled by your presence.")
        damage_player(player, 5)
        print("Their wings brush against you, causing minor scratches.")
    elif event == "discover_underground_lake":
        print("You discover a beautiful underground lake with crystal-clear water.")
        heal_player(player, 10)
        print("You take a drink from the pristine water and feel refreshed.")
    else:
        print("You explore for a while but find nothing of interest.")


def search_for_minerals(world, player, has_torch):
    """Search for minerals in the cave."""
    print("You search the cave walls for interesting minerals.")
    
    if not has_torch:
        print("It's too dark to find anything without a torch.")
        return
    
    if "pickaxe" in player["inventory"]:
        print("You use your pickaxe to carefully extract minerals from the cave wall.")
        if generate_random_event(events=[("find_valuable_mineral", 60), (None, 40)]) == "find_valuable_mineral":
            print("You find a valuable mineral!")
            add_item_to_inventory(player, "valuable_mineral")
        else:
            print("You extract some common minerals, but nothing of value.")
    else:
        print("You find some interesting minerals, but you need a pickaxe to extract them.")
        if generate_random_event(events=[("find_loose_gemstone", 20), (None, 80)]) == "find_loose_gemstone":
            print("You find a loose gemstone that you can take without tools!")
            add_item_to_inventory(player, "gemstone")


def listen_to_cave(world, player):
    """Listen to the sounds in the cave."""
    print("You stand still and listen carefully to the sounds of the cave.")
    print("You hear water dripping and the occasional echo.")
    
    event = generate_random_event(events=[
        ("hear_whispers", 10),
        ("hear_creature", 20),
        (None, 70)
    ])
    
    if event == "hear_whispers":
        print("You hear strange whispers coming from deeper in the cave...")
        print("They seem to be guiding you toward something.")
        # update_world_state(world, "cave_whispers_heard")
    elif event == "hear_creature":
        print("You hear the sound of something moving in the darkness.")
        print("It might be dangerous to explore deeper without preparation.")
    else:
        print("Nothing unusual stands out among the typical cave sounds.")


def rest_in_cave(world, player):
    """Rest in the cave to recover health."""
    print("You find a relatively comfortable spot in the cave to rest.")
    
    if "torch" in player["inventory"]:
        print("Your torch provides warmth and keeps any cave creatures at bay.")
        heal_player(player, 15)
        print("You feel rested and recover some health.")
    else:
        print("It's cold and dark, making it difficult to rest properly.")
        heal_player(player, 5)
        print("You recover a small amount of health, but remain uneasy in the darkness.")

