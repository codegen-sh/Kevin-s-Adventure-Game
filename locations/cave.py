"""
Cave location module for Kevin's Adventure Game.
Handles cave exploration and interactions.
"""

from game.items import add_item_to_world, get_available_items
from game.player import add_item_to_inventory, damage_player, heal_player
from utils.random_events import generate_random_event
from utils.text_formatting import print_separator, print_event
import random


def explore_cave(world, player):
    """
    Main cave exploration function.
    
    Args:
        world (dict): World state dictionary
        player (dict): Player state dictionary
    """
    print_separator()
    print("🕳️  CAVE EXPLORATION")
    print_separator()
    
    print("You are in a dark, mysterious cave.")
    print("The air is cool and damp, and you can hear water dripping somewhere in the distance.")
    print("Glittering minerals catch what little light filters in from the entrance.")
    
    # Show available items
    available_items = get_available_items(world, "Cave")
    if available_items:
        print(f"You see: {', '.join(available_items)}")
    
    print("\nWhat would you like to do?")
    print("1. Search for treasure")
    print("2. Examine the walls")
    print("3. Listen carefully")
    print("4. Go deeper into the cave")
    print("5. Rest by the entrance")
    print("6. Leave the cave")
    
    try:
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == "1":
            search_for_treasure(world, player)
        elif choice == "2":
            examine_walls(world, player)
        elif choice == "3":
            listen_in_cave(world, player)
        elif choice == "4":
            go_deeper(world, player)
        elif choice == "5":
            rest_in_cave(world, player)
        elif choice == "6":
            print("You leave the cave and return to the forest.")
        else:
            print("Invalid choice. You decide to look around more carefully.")
            examine_walls(world, player)
            
    except (ValueError, KeyboardInterrupt):
        print("You decide to leave the cave.")


def search_for_treasure(world, player):
    """Search for treasure in the cave."""
    print_event("You carefully search the cave floor and crevices...")
    
    # Random chance of finding treasure
    if random.random() < 0.4:  # 40% chance
        treasures = ["gold coin", "silver ring", "ancient artifact", "precious gem"]
        treasure = random.choice(treasures)
        
        print(f"🎉 You found a {treasure}!")
        add_item_to_inventory(player, treasure)
        
        # Add some gold
        gold_found = random.randint(10, 50)
        player['gold'] += gold_found
        print(f"You also found {gold_found} gold pieces!")
        
    elif random.random() < 0.3:  # 30% chance of finding nothing special
        print("You search thoroughly but find nothing of value.")
        
    else:  # 30% chance of danger
        print("💀 You disturb a sleeping bat colony!")
        print("The bats swarm around you, causing minor injuries.")
        damage_player(player, random.randint(5, 15))


def examine_walls(world, player):
    """Examine the cave walls for interesting features."""
    print_event("You examine the cave walls closely...")
    
    discoveries = [
        "You notice ancient cave paintings depicting hunters and animals.",
        "The walls are covered in beautiful crystalline formations.",
        "You find fossilized remains embedded in the rock.",
        "Strange symbols are carved into the stone - perhaps left by previous explorers.",
        "The walls show signs of mineral veins running through the rock."
    ]
    
    discovery = random.choice(discoveries)
    print(discovery)
    
    # Small chance of finding something useful
    if random.random() < 0.2:  # 20% chance
        items = ["crystal shard", "ancient coin", "carved stone"]
        item = random.choice(items)
        print(f"Hidden in a crevice, you find a {item}!")
        add_item_to_inventory(player, item)


def listen_in_cave(world, player):
    """Listen carefully to the sounds in the cave."""
    print_event("You stand still and listen carefully to the cave sounds...")
    
    sounds = [
        "You hear the steady drip of water echoing through the chambers.",
        "A faint whistling sound suggests there might be another entrance somewhere.",
        "You hear the scurrying of small creatures in the darkness.",
        "The sound of your own breathing seems amplified in the silence.",
        "You detect a faint rumbling that might be an underground stream."
    ]
    
    sound = random.choice(sounds)
    print(sound)
    
    # Chance of discovering something based on what you heard
    if "water" in sound and random.random() < 0.3:
        print("Following the sound of water, you discover a small underground spring!")
        print("The fresh water restores your energy.")
        heal_player(player, random.randint(10, 20))
    elif "creatures" in sound and random.random() < 0.2:
        print("You spot a small cave creature that drops something shiny before scurrying away!")
        add_item_to_inventory(player, "shiny pebble")


def go_deeper(world, player):
    """Venture deeper into the cave."""
    print_event("You venture deeper into the dark cave...")
    
    # Check if player has a torch
    has_light = "torch" in player['inventory'] or "lantern" in player['inventory']
    
    if not has_light:
        print("⚠️  It's too dark to see safely without a light source!")
        print("You stumble in the darkness and hurt yourself.")
        damage_player(player, random.randint(10, 20))
        print("You decide to return to the entrance.")
        return
    
    print("With your light source, you can see deeper into the cave.")
    
    # Random deeper cave events
    events = [
        "You discover a hidden chamber filled with glittering crystals!",
        "You find an underground lake with crystal-clear water.",
        "You encounter a friendly cave hermit who shares wisdom with you.",
        "You discover ancient cave paintings telling a story of treasure.",
        "You find a narrow passage that leads to another part of the cave system."
    ]
    
    event = random.choice(events)
    print(event)
    
    # Rewards for successful deep exploration
    if random.random() < 0.5:  # 50% chance of reward
        rewards = ["rare crystal", "ancient map fragment", "hermit's blessing", "cave mushroom"]
        reward = random.choice(rewards)
        print(f"Your exploration rewards you with: {reward}")
        add_item_to_inventory(player, reward)


def rest_in_cave(world, player):
    """Rest by the cave entrance."""
    print_event("You sit by the cave entrance and rest...")
    
    print("The cool air and peaceful atmosphere help you recover.")
    heal_amount = random.randint(15, 25)
    heal_player(player, heal_amount)
    
    # Small chance of a peaceful encounter
    if random.random() < 0.3:  # 30% chance
        encounters = [
            "A friendly cave owl perches nearby and seems to nod at you.",
            "You notice beautiful cave flowers growing near the entrance.",
            "A gentle breeze carries the scent of fresh air from outside.",
            "You spot a family of harmless cave creatures watching you curiously."
        ]
        encounter = random.choice(encounters)
        print(encounter)


def add_cave_items(world):
    """Add default items to the cave location."""
    cave_items = ["torch", "gemstone", "rope", "cave map"]
    for item in cave_items:
        if item not in get_available_items(world, "Cave"):
            add_item_to_world(world, "Cave", item)

