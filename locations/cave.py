"""
Cave location module for Kevin's Adventure Game.
Contains functions for handling player interactions in the cave.
"""
import random
from game.player import add_item_to_inventory, damage_player, heal_player


def explore_cave(world, player):
    """
    Handle player interaction with the cave location.
    
    Args:
        world (dict): The world state
        player (dict): The player's state
    """
    print("You explore the dark, mysterious cave...")
    
    # Check if player has a torch
    has_torch = "torch" in player["inventory"]
    
    if not has_torch:
        print("It's very dark in here. You can barely see anything.")
        print("You stumble around in the darkness.")
        
        # 30% chance of taking damage when exploring without a torch
        if random.random() < 0.3:
            damage = random.randint(5, 15)
            print(f"You trip over a rock and hurt yourself!")
            damage_player(player, damage)
            return
    else:
        print("Your torch illuminates the cave, revealing glittering minerals and ancient drawings on the walls.")
    
    # Random events in the cave
    event = random.randint(1, 5)
    
    if event == 1:
        print("You discover a hidden chest!")
        if "gemstone" not in player["inventory"]:
            print("Inside, you find a valuable gemstone!")
            add_item_to_inventory(player, "gemstone")
        else:
            print("Inside, you find 50 gold coins!")
            player["gold"] += 50
            print(f"You now have {player['gold']} gold.")
    
    elif event == 2:
        print("You find a small underground spring with crystal clear water.")
        print("The water seems to have healing properties.")
        heal_amount = random.randint(10, 25)
        heal_player(player, heal_amount)
    
    elif event == 3:
        if has_torch and "pickaxe" in player["inventory"]:
            print("You notice a vein of valuable minerals in the wall.")
            print("Using your pickaxe, you extract some minerals!")
            add_item_to_inventory(player, "minerals")
        else:
            print("You notice a vein of valuable minerals in the wall, but you need a pickaxe to extract them.")
    
    elif event == 4:
        print("You hear strange echoes deeper in the cave...")
        if random.random() < 0.5:
            print("Suddenly, a swarm of bats flies toward you!")
            if has_torch:
                print("You wave your torch, and the bats disperse.")
            else:
                print("The bats swarm around you, disorienting you!")
                damage = random.randint(5, 10)
                damage_player(player, damage)
    
    elif event == 5:
        print("You find ancient cave drawings depicting a legendary treasure hidden somewhere in the world.")
        print("The drawings suggest the treasure is located in a place where 'the earth meets the sky'.")
        print("Could it be referring to the mountain?")
        
    # Add the cave exploration to the world state
    if "explored_locations" not in world:
        world["explored_locations"] = []
    
    if "Cave" not in world["explored_locations"]:
        world["explored_locations"].append("Cave")
        print("You've successfully explored the cave! This location has been added to your explored locations.")

