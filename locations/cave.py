"""
Cave location module for Kevin's Adventure Game.

This module handles all interactions and events specific to the Cave location.
"""

import random
from game.mythical import summon_mythical_creature
from game.player import add_item_to_inventory, damage_player, heal_player
from game.state import update_world_state
from utils.random_events import generate_random_event


def explore_cave(player, world):
    """
    Handle cave exploration events and interactions.
    
    Args:
        player (dict): The player object containing stats and inventory
        world (dict): The world state object
    
    Returns:
        bool: True if exploration was successful
    """
    print("\\nYou enter the dark, mysterious cave...")
    print("The air is cool and damp, and you hear the echo of dripping water.")
    print("Strange minerals glitter on the cave walls in the torchlight.")
    
    # Random cave events
    event_chance = random.randint(1, 100)
    
    if event_chance <= 20:
        _cave_treasure_event(player)
    elif event_chance <= 35:
        _cave_danger_event(player)
    elif event_chance <= 50:
        _cave_mystery_event(player, world)
    elif event_chance <= 65:
        _cave_mining_event(player)
    elif event_chance <= 80:
        _cave_creature_event(player, world)
    else:
        _cave_peaceful_exploration(player)
    
    # Update world state
    update_world_state(world, "cave_visited", True)
    
    # Chance for random event
    if random.randint(1, 100) <= 30:
        generate_random_event(player, world)
    
    return True


def _cave_treasure_event(player):
    """Handle treasure discovery in the cave."""
    treasures = ["gemstone", "ancient_coin", "gold_coin", "ancient_artifact"]
    treasure = random.choice(treasures)
    
    print(f"\\n✨ You discover a hidden alcove containing a {treasure}!")
    add_item_to_inventory(player, treasure)
    
    if treasure == "ancient_artifact":
        print("The artifact pulses with mysterious energy...")
        heal_player(player, 10)


def _cave_danger_event(player):
    """Handle dangerous events in the cave."""
    dangers = [
        ("loose rocks", 15, "Loose rocks fall from the ceiling!"),
        ("slippery floor", 10, "You slip on the wet cave floor!"),
        ("toxic gas", 20, "You encounter a pocket of toxic gas!"),
        ("cave-in", 25, "Part of the cave ceiling collapses!")
    ]
    
    danger, damage, message = random.choice(dangers)
    print(f"\\n⚠️ {message}")
    damage_player(player, damage)
    
    if danger == "toxic gas":
        print("You quickly cover your nose and mouth, but still inhale some fumes.")
    elif danger == "cave-in":
        print("You barely dodge the falling rocks!")


def _cave_mystery_event(player, world):
    """Handle mysterious events in the cave."""
    mysteries = [
        "ancient_paintings",
        "strange_symbols",
        "mysterious_altar",
        "glowing_crystals"
    ]
    
    mystery = random.choice(mysteries)
    
    if mystery == "ancient_paintings":
        print("\\n🎨 You discover ancient cave paintings depicting strange creatures.")
        print("The paintings seem to tell a story of an ancient civilization.")
        update_world_state(world, "cave_paintings_found", True)
        
    elif mystery == "strange_symbols":
        print("\\n📜 You find strange symbols carved into the cave wall.")
        print("They glow faintly with an otherworldly light.")
        if "torch" in player["inventory"]:
            print("Your torch reveals more symbols hidden in the shadows!")
            add_item_to_inventory(player, "mysterious_potion")
            
    elif mystery == "mysterious_altar":
        print("\\n⛩️ You discover an ancient stone altar covered in moss.")
        print("Strange runes are carved around its base.")
        if random.randint(1, 100) <= 50:
            print("You feel a surge of mystical energy!")
            heal_player(player, 30)
        else:
            print("The altar seems dormant and cold.")
            
    elif mystery == "glowing_crystals":
        print("\\n💎 You find a cluster of glowing crystals embedded in the wall.")
        print("They pulse with a soft, blue light.")
        if "pickaxe" in player["inventory"]:
            print("You use your pickaxe to carefully extract a crystal!")
            add_item_to_inventory(player, "magic_crystal")


def _cave_mining_event(player):
    """Handle mining opportunities in the cave."""
    print("\\n⛏️ You notice some valuable minerals in the cave wall.")
    
    if "pickaxe" in player["inventory"]:
        print("You use your pickaxe to mine the minerals!")
        minerals = ["iron_ore", "silver_ore", "gemstone", "coal"]
        mineral = random.choice(minerals)
        add_item_to_inventory(player, mineral)
        print(f"You successfully mined: {mineral}")
        
        # Chance for bonus find
        if random.randint(1, 100) <= 25:
            bonus = random.choice(["gold_coin", "ancient_coin"])
            add_item_to_inventory(player, bonus)
            print(f"You also found a {bonus} while mining!")
    else:
        print("You need a pickaxe to mine these minerals.")
        print("You make a mental note to return with proper tools.")


def _cave_creature_event(player, world):
    """Handle creature encounters in the cave."""
    creatures = ["cave_bat", "underground_troll", "crystal_spider", "cave_spirit"]
    creature = random.choice(creatures)
    
    if creature == "cave_bat":
        print("\\n🦇 A swarm of cave bats suddenly flies past you!")
        if random.randint(1, 100) <= 30:
            print("One of the bats scratches you as it flies by.")
            damage_player(player, 5)
        else:
            print("You duck just in time to avoid them.")
            
    elif creature == "underground_troll":
        print("\\n👹 You encounter a grumpy underground troll!")
        print("The troll blocks your path and demands a toll.")
        if "gold_coin" in player["inventory"]:
            print("You give the troll a gold coin and it lets you pass.")
            player["inventory"].remove("gold_coin")
            add_item_to_inventory(player, "troll_blessing")
        else:
            print("You don't have any gold to give the troll.")
            print("The troll grumbles but eventually moves aside.")
            
    elif creature == "crystal_spider":
        print("\\n🕷️ A large crystal spider descends from the ceiling!")
        if "torch" in player["inventory"]:
            print("You wave your torch at the spider and it retreats.")
            print("In its haste, it drops something shiny!")
            add_item_to_inventory(player, "spider_silk")
        else:
            print("The spider bites you before scurrying away!")
            damage_player(player, 12)
            
    elif creature == "cave_spirit":
        print("\\n👻 A mysterious cave spirit appears before you!")
        print("It speaks in an ancient language you don't understand.")
        if random.randint(1, 100) <= 50:
            print("The spirit seems pleased with your presence and blesses you.")
            heal_player(player, 25)
            add_item_to_inventory(player, "spirit_blessing")
        else:
            print("The spirit fades away without a trace.")


def _cave_peaceful_exploration(player):
    """Handle peaceful cave exploration."""
    peaceful_events = [
        "You find a small underground stream with fresh, cool water.",
        "You discover beautiful stalactites and stalagmites formations.",
        "You hear the distant sound of underground wind.",
        "You find a comfortable spot to rest and recover.",
        "You notice interesting rock formations that tell geological history."
    ]
    
    event = random.choice(peaceful_events)
    print(f"\\n🕊️ {event}")
    
    if "fresh water" in event:
        print("You drink some water and feel refreshed.")
        heal_player(player, 10)
    elif "rest" in event:
        print("You take a short rest and recover some energy.")
        heal_player(player, 15)


def get_cave_description():
    """
    Get a detailed description of the cave location.
    
    Returns:
        str: Description of the cave
    """
    return ("A dark, mysterious cave system with winding tunnels and chambers. "
            "The walls are covered with strange minerals that glitter in the light. "
            "You can hear the echo of dripping water and feel a cool breeze from "
            "deeper in the cave. Ancient symbols and paintings can be found on some walls, "
            "hinting at a long-lost civilization that once inhabited this place.")


def get_cave_items():
    """
    Get the list of items typically found in the cave.
    
    Returns:
        list: List of item names available in the cave
    """
    return ["torch", "gemstone", "ancient_coin", "mysterious_potion"]


def get_cave_connections():
    """
    Get the list of locations connected to the cave.
    
    Returns:
        list: List of connected location names
    """
    return ["Forest"]

