"""
Cave location module for Kevin's Adventure Game.
This module handles all interactions with the cave location.
"""
import random
from game.player import add_item_to_inventory, damage_player, heal_player
from utils.text_formatting import print_event


def explore_cave(world, player):
    """
    Handle player interactions with the cave location.
    
    Args:
        world (dict): The world state
        player (dict): The player's state
    
    Returns:
        None
    """
    print("You explore the dark, mysterious cave...")
    
    # Random events that can occur in the cave
    events = [
        cave_find_treasure,
        cave_encounter_bat,
        cave_discover_underground_stream,
        cave_find_glowing_crystals,
        cave_encounter_rockfall
    ]
    
    # Randomly select and execute an event
    random.choice(events)(world, player)


def cave_find_treasure(world, player):
    """
    Event: Player finds treasure in the cave.
    
    Args:
        world (dict): The world state
        player (dict): The player's state
    
    Returns:
        None
    """
    gold_amount = random.randint(10, 50)
    player["gold"] += gold_amount
    
    print_event(f"You discover a small treasure chest hidden behind some rocks! "
                f"Inside, you find {gold_amount} gold coins.")


def cave_encounter_bat(world, player):
    """
    Event: Player encounters bats in the cave.
    
    Args:
        world (dict): The world state
        player (dict): The player's state
    
    Returns:
        None
    """
    damage = random.randint(5, 15)
    damage_player(player, damage)
    
    print_event("A swarm of bats suddenly descends from the ceiling! "
                "They fly around you in a frenzy, their wings beating against your face and arms. "
                f"You swat at them frantically, but not before they cause {damage} damage.")


def cave_discover_underground_stream(world, player):
    """
    Event: Player discovers an underground stream.
    
    Args:
        world (dict): The world state
        player (dict): The player's state
    
    Returns:
        None
    """
    heal_amount = random.randint(10, 20)
    heal_player(player, heal_amount)
    
    print_event("You discover a clear underground stream flowing through the cave. "
                "The water is cool and refreshing. You take a drink and feel revitalized. "
                f"You recover {heal_amount} health.")


def cave_find_glowing_crystals(world, player):
    """
    Event: Player finds glowing crystals.
    
    Args:
        world (dict): The world state
        player (dict): The player's state
    
    Returns:
        None
    """
    if "gemstone" not in player["inventory"] and "gemstone" not in world["locations"]["Cave"]["items"]:
        add_item_to_inventory(player, "gemstone")
        
        print_event("You notice a cluster of crystals embedded in the cave wall, "
                    "glowing with an ethereal blue light. You carefully extract a small gemstone "
                    "that seems to pulse with magical energy.")
    else:
        print_event("You find a beautiful cluster of glowing crystals embedded in the cave wall. "
                    "They illuminate the surrounding area with a soft, blue light. "
                    "They're too firmly embedded to remove, but they're beautiful to look at.")


def cave_encounter_rockfall(world, player):
    """
    Event: Player encounters a rockfall.
    
    Args:
        world (dict): The world state
        player (dict): The player's state
    
    Returns:
        None
    """
    if "pickaxe" in player["inventory"]:
        print_event("You hear a rumbling sound from above. Suddenly, rocks begin to fall from the ceiling! "
                    "Thinking quickly, you use your pickaxe to create a small alcove in the wall, "
                    "protecting yourself from the falling debris.")
    else:
        damage = random.randint(10, 25)
        damage_player(player, damage)
        
        print_event("You hear a rumbling sound from above. Suddenly, rocks begin to fall from the ceiling! "
                    "You try to dodge, but some of the falling debris hits you. "
                    f"You take {damage} damage from the rockfall.")

