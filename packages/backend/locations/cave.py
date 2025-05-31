"""
Cave location module for Kevin's Adventure Game.
"""

import random
from game.player import add_item_to_inventory, damage_player, heal_player


def explore_cave(world, player):
    """
    Handle cave exploration interactions.
    """
    print("You enter the dark, mysterious cave...")
    
    # Random events in the cave
    event = random.choice([
        "treasure", "monster", "crystal", "nothing", "trap"
    ])
    
    if event == "treasure":
        treasure_items = ["gemstone", "gold_coin", "ancient_artifact"]
        item = random.choice(treasure_items)
        add_item_to_inventory(player, item)
        print(f"You discovered a hidden treasure: {item}!")
        
    elif event == "monster":
        print("A cave monster appears!")
        if "torch" in player['inventory']:
            print("Your torch scares the monster away!")
        else:
            damage = random.randint(10, 25)
            damage_player(player, damage)
            print(f"The monster attacks you for {damage} damage!")
            
    elif event == "crystal":
        print("You find a glowing crystal that heals your wounds!")
        heal_player(player, 15)
        
    elif event == "trap":
        print("You step on a pressure plate!")
        if "rope" in player['inventory']:
            print("You use your rope to swing to safety!")
        else:
            damage = random.randint(5, 15)
            damage_player(player, damage)
            print(f"You fall into a pit and take {damage} damage!")
            
    else:
        print("The cave is eerily quiet. You find nothing of interest.")
    
    # Cave-specific interactions
    print("\nThe cave walls glisten with moisture and strange markings.")
    print("You can hear the echo of dripping water in the distance.")


def cave_mining(player):
    """
    Handle mining activities in the cave.
    """
    if "pickaxe" not in player['inventory']:
        return "You need a pickaxe to mine in the cave."
    
    success_rate = 0.7  # 70% chance of finding something
    
    if random.random() < success_rate:
        minerals = ["iron_ore", "gemstone", "crystal", "coal"]
        mineral = random.choice(minerals)
        add_item_to_inventory(player, mineral)
        return f"You successfully mined {mineral}!"
    else:
        return "You swing your pickaxe but only hit solid rock."


def cave_rest(player):
    """
    Handle resting in the cave.
    """
    if "torch" in player['inventory']:
        heal_player(player, 10)
        return "You rest by the light of your torch and feel slightly better."
    else:
        return "It's too dark and scary to rest here without light."

