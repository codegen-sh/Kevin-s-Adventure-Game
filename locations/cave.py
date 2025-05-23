"""
Cave location module for Kevin's Adventure Game.
Handles all cave-specific interactions and events.
"""

from typing import Dict, Any
from game.player import add_item_to_inventory, damage_player, heal_player
from game.config import get_random_event_probabilities, get_healing_value, get_damage_value
from utils.random_events import generate_random_event


def explore_cave(world: Dict[str, Any], player: Dict[str, Any]) -> None:
    """
    Main function for cave exploration with various activities.
    
    Args:
        world: The game world state
        player: The player's current state
    """
    print("You enter the dark, mysterious cave. Water drips from the ceiling and your footsteps echo.")
    
    while True:
        print("\nWhat would you like to do in the cave?")
        print("1. Search for treasure")
        print("2. Examine the cave walls")
        print("3. Listen for sounds")
        print("4. Light a torch (if you have one)")
        print("5. Mine for minerals")
        print("6. Exit the cave")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == "1":
            search_for_treasure(world, player)
        elif choice == "2":
            examine_cave_walls(world, player)
        elif choice == "3":
            listen_for_sounds(world, player)
        elif choice == "4":
            light_torch_in_cave(world, player)
        elif choice == "5":
            mine_for_minerals(world, player)
        elif choice == "6":
            print("You carefully make your way out of the cave.")
            break
        else:
            print("Invalid choice. Please try again.")


def search_for_treasure(world: Dict[str, Any], player: Dict[str, Any]) -> None:
    """Search the cave for hidden treasure."""
    print("You search the dark corners of the cave for hidden treasure...")
    
    # Check if player has a torch for better searching
    has_torch = "torch" in player["inventory"]
    search_bonus = 20 if has_torch else 0
    
    event_probs = get_random_event_probabilities("cave_treasure")
    # Adjust probabilities based on torch
    adjusted_probs = []
    for event_name, prob in event_probs:
        if event_name == "find_treasure":
            adjusted_probs.append((event_name, prob + search_bonus))
        elif event_name == "find_nothing":
            adjusted_probs.append((event_name, prob - search_bonus))
        else:
            adjusted_probs.append((event_name, prob))
    
    event = generate_random_event(events=adjusted_probs)
    
    if event == "find_treasure":
        treasure_type = generate_random_event(events=[
            ("gemstone", 40),
            ("gold_coin", 30),
            ("ancient_artifact", 20),
            ("magic_ring", 10)
        ])
        
        print(f"You discover a hidden {treasure_type}!")
        add_item_to_inventory(player, treasure_type)
        
        if has_torch:
            print("Your torch helped you spot the treasure more easily.")
    
    elif event == "find_danger":
        print("You accidentally disturb a colony of bats!")
        damage_player(player, get_damage_value("cave_bats"))
        print("The bats swarm around you before settling back down.")
    
    else:
        print("You search thoroughly but find nothing of value.")
        if not has_torch:
            print("It's quite dark in here. A torch might help you see better.")


def examine_cave_walls(world: Dict[str, Any], player: Dict[str, Any]) -> None:
    """Examine the cave walls for interesting features."""
    print("You examine the cave walls closely...")
    
    event_probs = get_random_event_probabilities("cave_walls")
    event = generate_random_event(events=event_probs)
    
    if event == "find_paintings":
        print("You discover ancient cave paintings depicting mysterious creatures!")
        print("The artwork seems to tell a story of brave adventurers.")
        heal_player(player, 10)
        print("The inspiring artwork fills you with determination.")
    
    elif event == "find_minerals":
        print("You notice beautiful mineral formations glittering in the cave walls.")
        if "pickaxe" in player["inventory"]:
            print("You use your pickaxe to carefully extract some valuable minerals.")
            add_item_to_inventory(player, "gemstone")
        else:
            print("You would need a pickaxe to extract these minerals.")
    
    elif event == "find_passage":
        print("You discover a narrow passage leading deeper into the cave system.")
        print("It looks dangerous but might lead to greater treasures...")
        # This could be expanded to add new cave areas
    
    else:
        print("The cave walls are rough and unremarkable.")


def listen_for_sounds(world: Dict[str, Any], player: Dict[str, Any]) -> None:
    """Listen carefully for sounds in the cave."""
    print("You stand still and listen carefully to the sounds of the cave...")
    
    event_probs = get_random_event_probabilities("cave_sounds")
    event = generate_random_event(events=event_probs)
    
    if event == "hear_water":
        print("You hear the sound of running water echoing from deeper in the cave.")
        print("There might be an underground stream or pool nearby.")
        # Could lead to discovering a healing spring
    
    elif event == "hear_creatures":
        print("You hear strange chittering and scurrying sounds.")
        print("There are definitely creatures living in this cave.")
        # Small chance of encounter
        if generate_random_event(events=[("encounter", 20), ("safe", 80)]) == "encounter":
            print("A small cave creature scurries past your feet!")
            damage_player(player, 2)
    
    elif event == "hear_wind":
        print("You hear a faint whistling sound - there must be another entrance somewhere.")
        print("The air current might lead to a way out or a hidden chamber.")
    
    else:
        print("The cave is eerily silent except for the occasional drip of water.")
        print("The silence is almost deafening.")


def light_torch_in_cave(world: Dict[str, Any], player: Dict[str, Any]) -> None:
    """Light a torch to illuminate the cave."""
    if "torch" in player["inventory"]:
        print("You light your torch, casting dancing shadows on the cave walls.")
        print("The cave is now much brighter, revealing details you couldn't see before.")
        
        # Update cave description to reflect the lighting
        if "torch_lit" not in world["locations"]["Cave"]:
            world["locations"]["Cave"]["torch_lit"] = True
            world["locations"]["Cave"]["description"] += " Your torch illuminates ancient markings on the walls."
        
        # Bonus exploration opportunity
        print("With better visibility, you notice something interesting...")
        event = generate_random_event(events=[
            ("hidden_alcove", 30),
            ("wall_markings", 40),
            ("nothing_new", 30)
        ])
        
        if event == "hidden_alcove":
            print("You discover a hidden alcove containing a mysterious potion!")
            add_item_to_inventory(player, "mysterious_potion")
        elif event == "wall_markings":
            print("You can now clearly see ancient symbols carved into the walls.")
            print("They seem to be some kind of map or guide.")
        else:
            print("The improved lighting doesn't reveal anything new.")
    
    else:
        print("You don't have a torch to light.")
        print("The cave remains dark and difficult to navigate.")


def mine_for_minerals(world: Dict[str, Any], player: Dict[str, Any]) -> None:
    """Attempt to mine for valuable minerals."""
    if "pickaxe" in player["inventory"]:
        print("You use your pickaxe to chip away at the cave walls...")
        
        event_probs = get_random_event_probabilities("cave_mining")
        event = generate_random_event(events=event_probs)
        
        if event == "find_gems":
            print("You successfully extract some beautiful gemstones!")
            add_item_to_inventory(player, "gemstone")
            add_item_to_inventory(player, "gemstone")
        
        elif event == "find_ore":
            print("You find some valuable metal ore!")
            add_item_to_inventory(player, "ancient_coin")
        
        elif event == "cave_in_risk":
            print("Your mining causes some rocks to fall!")
            damage_player(player, get_damage_value("cave_in"))
            print("You narrowly avoid a cave-in but take some damage.")
        
        else:
            print("You mine for a while but only find worthless rock.")
    
    else:
        print("You need a pickaxe to mine effectively.")
        print("You try to chip at the walls with your hands but make no progress.")


def discover_underground_lake(world: Dict[str, Any], player: Dict[str, Any]) -> None:
    """Special event for discovering a hidden underground lake."""
    print("Following the sound of water, you discover a beautiful underground lake!")
    print("The water is crystal clear and seems to have magical properties.")
    
    choice = input("Do you want to drink from the lake? (y/n): ").lower()
    if choice == 'y':
        event = generate_random_event(events=[
            ("healing", 70),
            ("magical_effect", 20),
            ("nothing", 10)
        ])
        
        if event == "healing":
            print("The water is refreshing and has healing properties!")
            heal_player(player, 30)
        elif event == "magical_effect":
            print("The water glows as you drink it, filling you with magical energy!")
            add_item_to_inventory(player, "magic_ring")
        else:
            print("The water tastes normal but refreshing.")
    else:
        print("You decide not to risk drinking the mysterious water.")
