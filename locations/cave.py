"""
Cave location module for Kevin's Adventure Game.
This module handles all interactions with the cave location.
"""

import random

from game.player import add_item_to_inventory, damage_player, heal_player
from game.state import update_world_state
from utils.random_events import generate_random_event


def explore_cave(world, player):
    """
    Handle player exploration of the cave location.
    
    Args:
        world (dict): The world state dictionary
        player (dict): The player state dictionary
        
    Returns:
        None
    """
    print("You enter a dark, mysterious cave. The air is cool and damp, and you can hear water dripping somewhere in the distance.")
    
    # Check if player has a torch
    has_torch = "torch" in player["inventory"]
    if not has_torch:
        print("It's very dark in here. A torch would be helpful.")
        # Higher chance of taking damage without a torch
        if random.random() < 0.3:
            print("You stumble in the darkness and hurt yourself.")
            damage_player(player, 5)
    
    while True:
        print("\nWhat would you like to do in the cave?")
        print("1. Explore deeper")
        print("2. Search for minerals")
        print("3. Listen to the cave")
        print("4. Rest in a quiet corner")
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
    print("You venture deeper into the cave...")
    
    # Different events based on whether player has a torch
    if has_torch:
        events = [
            ("find_treasure", 30),
            ("discover_underground_lake", 20),
            ("encounter_bats", 20),
            (None, 30)
        ]
    else:
        # Higher chance of negative events without a torch
        events = [
            ("find_treasure", 15),
            ("discover_underground_lake", 10),
            ("encounter_bats", 40),
            (None, 35)
        ]
    
    event = generate_random_event(events=events)
    
    if event == "find_treasure":
        print("You discover a small treasure chest hidden in a crevice!")
        treasure_items = ["gemstone", "gold_coin", "ancient_artifact", "healing_potion"]
        found_item = random.choice(treasure_items)
        add_item_to_inventory(player, found_item)
        
    elif event == "discover_underground_lake":
        print("You discover a beautiful underground lake with crystal-clear water.")
        print("The water seems to have healing properties.")
        heal_player(player, 15)
        # update_world_state(world, "discovered_underground_lake")
        
    elif event == "encounter_bats":
        print("A swarm of bats suddenly flies at you from the darkness!")
        if has_torch:
            print("Your torch helps keep most of them at bay, but a few still scratch you.")
            damage_player(player, 5)
        else:
            print("In the darkness, you can't see them coming and take several scratches.")
            damage_player(player, 15)
            
    else:
        print("You explore for a while but find nothing of interest.")


def search_for_minerals(world, player, has_torch):
    """Search for minerals in the cave."""
    print("You search the cave walls for interesting minerals...")
    
    # Different probabilities based on torch
    if has_torch:
        success_chance = 0.6
    else:
        success_chance = 0.3
    
    if random.random() < success_chance:
        minerals = ["gemstone", "iron_ore", "gold_nugget", "strange_crystal"]
        found_mineral = random.choice(minerals)
        print(f"You found a {found_mineral}!")
        add_item_to_inventory(player, found_mineral)
    else:
        print("You search for a while but don't find anything valuable.")
        
        # Small chance of injury while searching without proper light
        if not has_torch and random.random() < 0.2:
            print("You cut your hand on a sharp rock while searching in the darkness.")
            damage_player(player, 3)


def listen_to_cave(world, player):
    """Listen to the sounds in the cave."""
    print("You stand still and listen carefully to the sounds of the cave...")
    
    sounds = [
        "dripping water",
        "distant rumbling",
        "wind whistling through tunnels",
        "small rocks falling",
        "strange echoes"
    ]
    
    heard_sound = random.choice(sounds)
    print(f"You hear {heard_sound}.")
    
    # Special discovery chance
    if heard_sound == "strange echoes" and random.random() < 0.5:
        print("Following the strange echoes, you discover a hidden passage!")
        print("The passage seems to lead to a new area.")
        # update_world_state(world, "discovered_hidden_passage")
        
        # Add a new connection if it doesn't exist
        if "Hidden Chamber" not in world["locations"]["Cave"]["connections"]:
            print("You've discovered a path to a Hidden Chamber!")
            world["locations"]["Cave"]["connections"].append("Hidden Chamber")
            
            # Add the Hidden Chamber location if it doesn't exist
            if "Hidden Chamber" not in world["locations"]:
                world["locations"]["Hidden Chamber"] = {
                    "description": "A secret chamber deep within the cave, filled with ancient artifacts and mysterious symbols.",
                    "connections": ["Cave"],
                    "items": ["ancient_scroll", "mysterious_amulet"]
                }


def rest_in_cave(world, player):
    """Rest in a quiet corner of the cave."""
    print("You find a quiet corner of the cave and decide to rest for a while.")
    
    # Healing from rest
    heal_amount = random.randint(5, 10)
    heal_player(player, heal_amount)
    
    # Random event while resting
    if random.random() < 0.3:
        print("While resting, you notice something glinting in the wall nearby.")
        add_item_to_inventory(player, "gemstone")
    else:
        print("Your rest is uneventful but refreshing.")

