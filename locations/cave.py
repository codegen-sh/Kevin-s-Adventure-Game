"""
Cave location module for Kevin's Adventure Game.
Contains functions for exploring the cave.
"""
from game.mythical import summon_mythical_creature
from game.player import add_item_to_inventory, damage_player
from game.state import update_world_state
from utils.random_events import generate_random_event


def explore_cave(world, player):
    """
    Handle player interactions with the cave location.
    
    Args:
        world (dict): The game world state
        player (dict): The player's current state
    """
    print("You enter the dark, mysterious cave. The air is cool and damp, and you hear water dripping somewhere.")
    
    # Check if player has a torch
    if "torch" not in player["inventory"]:
        print("It's very dark in here. A torch would be helpful.")
        damage_player(player, 5)
        print("You stumble in the darkness and hurt yourself.")
    
    while True:
        print("\nWhat would you like to do in the cave?")
        print("1. Explore deeper")
        print("2. Search for minerals")
        print("3. Listen to the cave")
        print("4. Rest in a safe corner")
        print("5. Leave the cave")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            explore_deeper(world, player)
        elif choice == "2":
            search_for_minerals(world, player)
        elif choice == "3":
            listen_to_cave(world, player)
        elif choice == "4":
            rest_in_cave(world, player)
        elif choice == "5":
            print("You decide to leave the cave.")
            break
        else:
            print("Invalid choice. Please try again.")


def explore_deeper(world, player):
    """Explore deeper into the cave."""
    print("You venture deeper into the cave.")
    
    # Check if player has a torch
    if "torch" not in player["inventory"]:
        print("It's too dark to see anything. You should come back with a torch.")
        damage_player(player, 10)
        print("You trip over rocks and hurt yourself in the darkness.")
        return
    
    event = generate_random_event(events=[
        ("find_gemstone", 30),
        ("encounter_bat", 20),
        ("discover_underground_lake", 15),
        (None, 35)
    ])
    
    if event == "find_gemstone":
        print("You find a sparkling gemstone embedded in the cave wall!")
        add_item_to_inventory(player, "gemstone")
    elif event == "encounter_bat":
        print("A swarm of bats suddenly flies past you, startling you!")
        damage_player(player, 5)
    elif event == "discover_underground_lake":
        print("You discover a beautiful underground lake with crystal-clear water.")
        print("The water seems to have healing properties.")
        from game.player import heal_player
        heal_player(player, 15)
    else:
        print("Your exploration yields nothing of interest this time.")


def search_for_minerals(world, player):
    """Search for minerals in the cave."""
    print("You search the cave walls for interesting minerals.")
    
    # Check if player has a pickaxe
    if "pickaxe" in player["inventory"]:
        print("You use your pickaxe to carefully extract minerals from the cave wall.")
        event = generate_random_event(events=[
            ("find_gemstone", 40),
            ("find_gold_nugget", 20),
            ("find_crystal", 15),
            (None, 25)
        ])
        
        if event == "find_gemstone":
            print("You find a valuable gemstone!")
            add_item_to_inventory(player, "gemstone")
        elif event == "find_gold_nugget":
            print("You find a small gold nugget!")
            add_item_to_inventory(player, "gold_nugget")
            player["gold"] = player.get("gold", 0) + 20
        elif event == "find_crystal":
            print("You find a beautiful crystal!")
            add_item_to_inventory(player, "crystal")
        else:
            print("Your search yields nothing of value this time.")
    else:
        print("You find some interesting minerals, but you need a pickaxe to extract them properly.")
        if generate_random_event(events=[("find_small_gemstone", 20), (None, 80)]) == "find_small_gemstone":
            print("You manage to find a small gemstone that was already loose!")
            add_item_to_inventory(player, "small_gemstone")


def listen_to_cave(world, player):
    """Listen to the sounds in the cave."""
    print("You stand still and listen carefully to the sounds in the cave.")
    print("You hear water dripping, the occasional echo, and the faint sound of wind.")
    
    event = generate_random_event(events=[
        ("hear_creature", 20),
        ("hear_whispers", 10),
        (None, 70)
    ])
    
    if event == "hear_creature":
        print("You hear a strange creature moving deeper in the cave.")
        print("It doesn't sound threatening, but rather... magical.")
        choice = input("Do you want to investigate the sound? (y/n): ").lower()
        if choice == 'y':
            print("You follow the sound and find...")
            summon_mythical_creature(world, player, "phoenix")
    elif event == "hear_whispers":
        print("You hear mysterious whispers echoing through the cave.")
        print("They seem to be guiding you to a hidden treasure.")
        print("Following the whispers, you discover a small hidden alcove.")
        add_item_to_inventory(player, "ancient_amulet")
        print("You found an ancient amulet with strange inscriptions!")
    else:
        print("You don't hear anything unusual.")


def rest_in_cave(world, player):
    """Rest in a safe corner of the cave."""
    print("You find a dry, comfortable corner of the cave to rest in.")
    
    # Check if player has a torch
    if "torch" in player["inventory"]:
        print("Your torch provides warmth and keeps any cave creatures at bay.")
        from game.player import heal_player
        heal_player(player, 20)
        print("You feel refreshed after your rest.")
    else:
        print("It's cold and a bit scary without a light source.")
        from game.player import heal_player
        heal_player(player, 10)
        print("You get some rest, but it's not very comfortable.")

