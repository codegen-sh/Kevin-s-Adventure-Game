"""
Cave location module.
"""
import random

from game.player import add_item_to_inventory, damage_player
from utils.text_formatting import print_event


def explore_cave(world, player):
    """Explore the cave location."""
    print("You explore the dark, damp cave...")
    
    # Random cave events
    events = [
        "find_treasure",
        "encounter_bat",
        "discover_underground_river",
        "find_ancient_inscription",
        "cave_in"
    ]
    
    event = random.choice(events)
    
    if event == "find_treasure":
        print_event("You discover a hidden treasure chest tucked away in a corner of the cave!")
        treasures = ["gold_coin", "gemstone", "ancient_artifact", "magic_ring"]
        treasure = random.choice(treasures)
        add_item_to_inventory(player, treasure)
        
    elif event == "encounter_bat":
        print_event("A swarm of bats suddenly flies at you from the darkness!")
        if "torch" in (player["inventory"] if isinstance(player, dict) else player.inventory):
            print("You wave your torch to keep the bats at bay.")
        else:
            print("The bats swarm around you, disorienting you and causing minor injuries.")
            damage_player(player, 5)
            
    elif event == "discover_underground_river":
        print_event("You discover an underground river flowing through the cave.")
        print("The water looks clean and refreshing.")
        choice = input("Do you want to drink from the river? (y/n): ").lower()
        if choice == 'y':
            if random.random() < 0.7:
                print("The water is refreshing and rejuvenating.")
                if isinstance(player, dict):
                    player["health"] = min(100, player["health"] + 10)
                else:
                    player.health = min(100, player.health + 10)
                print(f"Your health is now {player['health'] if isinstance(player, dict) else player.health}.")
            else:
                print("The water makes you feel sick.")
                damage_player(player, 5)
        else:
            print("You decide not to risk drinking the water.")
            
    elif event == "find_ancient_inscription":
        print_event("You find ancient inscriptions carved into the cave wall.")
        print("They depict a story of a powerful artifact hidden somewhere in these lands.")
        print("You make a mental note of the locations mentioned in the inscriptions.")
        # Could unlock a new location or quest
        
    elif event == "cave_in":
        print_event("You hear a rumbling sound from above!")
        print("Small rocks begin to fall from the ceiling.")
        choice = input("Do you want to run deeper into the cave or back toward the entrance? (deeper/entrance): ").lower()
        if choice == "deeper":
            print("You run deeper into the cave, avoiding the falling rocks.")
            print("You discover a new passage that wasn't visible before.")
            # Could unlock a new area
        else:
            print("You run toward the entrance, but some rocks hit you on the way out.")
            damage_player(player, 10)
            print("You make it outside safely, but decide to wait before venturing back in.")

