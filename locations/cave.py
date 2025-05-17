"""
Cave location module - handles interactions in the cave location.
"""
import random
from game.player import damage_player, heal_player


def explore_cave(world, player):
    """
    Handle player interactions with the cave location.
    
    Args:
        world (dict): The game world state
        player (dict): The player's state
    
    Returns:
        None
    """
    print("You explore the dark cave...")
    
    # Check if player has a torch
    if "torch" in player["inventory"]:
        print("Your torch illuminates the cave, making it easier to navigate.")
        cave_event_with_torch(player)
    else:
        print("It's very dark. You stumble around blindly.")
        cave_event_without_torch(player)


def cave_event_with_torch(player):
    """Events that can happen in the cave when player has a torch."""
    event = random.randint(1, 3)
    
    if event == 1:
        print("You discover a hidden chest!")
        if "gemstone" not in player["inventory"]:
            print("Inside, you find a valuable gemstone. You take it.")
            player["inventory"].append("gemstone")
        else:
            print("Inside, you find 50 gold coins. You take them.")
            player["gold"] += 50
    elif event == 2:
        print("You find a small underground spring with healing properties.")
        heal_amount = random.randint(10, 25)
        heal_player(player, heal_amount)
    else:
        print("You notice interesting cave paintings depicting an ancient civilization.")
        print("They seem to tell a story about a powerful artifact hidden in the mountains.")


def cave_event_without_torch(player):
    """Events that can happen in the cave when player doesn't have a torch."""
    event = random.randint(1, 3)
    
    if event == 1:
        print("You trip over a rock and hurt yourself.")
        damage_amount = random.randint(5, 15)
        damage_player(player, damage_amount)
    elif event == 2:
        print("You hear strange noises echoing through the cave. It's unsettling.")
        print("You should come back with a torch to explore properly.")
    else:
        print("You feel around in the darkness and touch something slimy.")
        print("Startled, you back away quickly.")
        print("It would be safer to explore with a torch.")

