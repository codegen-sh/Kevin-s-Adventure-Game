from game.player import add_item_to_inventory, damage_player
from game.state import update_world_state
from utils.random_events import generate_random_event


def explore_cave(world, player):
    """
    Handle player interactions with the cave location.
    
    Args:
        world (dict): The game world state
        player (dict): The player's current state
    
    Returns:
        None
    """
    print("You enter the dark, mysterious cave. The air is cool and damp.")
    
    # Check if player has a torch
    has_torch = "torch" in player["inventory"]
    if not has_torch:
        print("It's very dark in here. A torch would be helpful.")
        damage_player(player, 5)
        print("You stumble in the darkness and hurt yourself.")
    
    while True:
        print("\nWhat would you like to do in the cave?")
        print("1. Explore deeper")
        print("2. Search for minerals")
        print("3. Listen to the cave")
        print("4. Rest in the cave")
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
    """
    Handle exploring deeper into the cave.
    
    Args:
        world (dict): The game world state
        player (dict): The player's current state
        has_torch (bool): Whether the player has a torch
    
    Returns:
        None
    """
    print("You venture deeper into the cave.")
    
    if not has_torch:
        print("It's too dark to see much without a torch.")
        damage_player(player, 10)
        print("You trip over rocks and hurt yourself in the darkness.")
        return
    
    event = generate_random_event(events=[
        ("find_gemstone", 30),
        ("encounter_bats", 20),
        ("discover_underground_lake", 10),
        (None, 40)
    ])
    
    if event == "find_gemstone":
        print("You discover a sparkling gemstone embedded in the cave wall!")
        add_item_to_inventory(player, "gemstone")
    elif event == "encounter_bats":
        print("A swarm of bats suddenly flies past you, startled by your presence!")
        damage_player(player, 5)
        print("The bats scratch you as they fly by.")
    elif event == "discover_underground_lake":
        print("You discover a beautiful underground lake with crystal-clear water.")
        # update_world_state(world, "add_underground_lake")
    else:
        print("You explore for a while but find nothing of interest.")


def search_for_minerals(world, player, has_torch):
    """
    Handle searching for minerals in the cave.
    
    Args:
        world (dict): The game world state
        player (dict): The player's current state
        has_torch (bool): Whether the player has a torch
    
    Returns:
        None
    """
    print("You search the cave walls for valuable minerals.")
    
    if not has_torch:
        print("It's too dark to see anything without a torch.")
        return
    
    if "pickaxe" in player["inventory"]:
        print("You use your pickaxe to carefully extract minerals from the cave wall.")
        event = generate_random_event(events=[
            ("find_gemstone", 40),
            ("find_gold", 20),
            (None, 40)
        ])
        
        if event == "find_gemstone":
            print("You extract a beautiful gemstone from the rock!")
            add_item_to_inventory(player, "gemstone")
        elif event == "find_gold":
            print("You find a small gold nugget!")
            player["gold"] += 20
            print(f"You now have {player['gold']} gold.")
        else:
            print("You mine for a while but don't find anything valuable.")
    else:
        print("You could extract minerals more effectively with a pickaxe.")
        event = generate_random_event(events=[
            ("find_gemstone", 10),
            (None, 90)
        ])
        
        if event == "find_gemstone":
            print("You manage to pry a small gemstone loose with your hands!")
            add_item_to_inventory(player, "gemstone")
        else:
            print("You search for a while but don't find anything you can extract without tools.")


def listen_to_cave(world, player):
    """
    Handle listening to sounds in the cave.
    
    Args:
        world (dict): The game world state
        player (dict): The player's current state
    
    Returns:
        None
    """
    print("You stand still and listen carefully to the sounds of the cave.")
    print("You hear water dripping and the occasional echo.")
    
    event = generate_random_event(events=[
        ("hear_creature", 20),
        ("hear_wind", 30),
        (None, 50)
    ])
    
    if event == "hear_creature":
        print("You hear a strange growling sound deeper in the cave. It might be dangerous to explore further.")
    elif event == "hear_wind":
        print("You hear the faint sound of wind coming from somewhere. There might be another entrance to the cave.")
        # update_world_state(world, "reveal_secret_exit")
    else:
        print("You don't hear anything unusual.")


def rest_in_cave(world, player):
    """
    Handle resting in the cave.
    
    Args:
        world (dict): The game world state
        player (dict): The player's current state
    
    Returns:
        None
    """
    print("You find a relatively comfortable spot and rest for a while.")
    
    if "torch" in player["inventory"]:
        print("Your torch provides warmth and light, making your rest more comfortable.")
        player["health"] = min(100, player["health"] + 10)
        print(f"You recover some health. Current health: {player['health']}")
    else:
        print("It's cold and dark, making it difficult to rest properly.")
        player["health"] = min(100, player["health"] + 5)
        print(f"You recover a little health. Current health: {player['health']}")

