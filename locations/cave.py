from game.player import add_item_to_inventory, damage_player
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
    
    if "torch" not in player["inventory"]:
        print("It's very dark in here. A torch would be helpful.")
        damage_player(player, 5)
        print("You stumble in the darkness and hurt yourself.")
    
    while True:
        print("\nWhat would you like to do in the cave?")
        print("1. Explore deeper")
        print("2. Search for minerals")
        print("3. Listen for sounds")
        print("4. Look for hidden passages")
        print("5. Leave the cave")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            explore_deeper(world, player)
        elif choice == "2":
            search_for_minerals(world, player)
        elif choice == "3":
            listen_for_sounds(world, player)
        elif choice == "4":
            look_for_hidden_passages(world, player)
        elif choice == "5":
            print("You decide to leave the cave.")
            break
        else:
            print("Invalid choice. Please try again.")


def explore_deeper(world, player):
    """Explore deeper into the cave."""
    print("You venture deeper into the cave.")
    
    if "torch" in player["inventory"]:
        event = generate_random_event(events=[
            ("find_treasure", 30),
            ("encounter_bats", 30),
            ("discover_underground_lake", 20),
            (None, 20)
        ])
        
        if event == "find_treasure":
            print("You discover a small treasure chest hidden in a crevice!")
            add_item_to_inventory(player, "ancient_coin")
        elif event == "encounter_bats":
            print("A swarm of bats suddenly flies past you, startled by your presence!")
            damage_player(player, 5)
        elif event == "discover_underground_lake":
            print("You discover a beautiful underground lake with crystal-clear water.")
            print("The ceiling is covered with glowing crystals that reflect in the water.")
        else:
            print("Your exploration yields nothing of note this time.")
    else:
        print("It's too dark to explore deeper without a torch.")
        damage_player(player, 10)
        print("You trip and fall in the darkness, hurting yourself.")


def search_for_minerals(world, player):
    """Search for valuable minerals in the cave."""
    print("You search the cave walls for interesting minerals.")
    
    if "pickaxe" in player["inventory"]:
        event = generate_random_event(events=[
            ("find_gemstone", 40),
            ("find_gold", 20),
            (None, 40)
        ])
        
        if event == "find_gemstone":
            print("You chip away at the wall and discover a beautiful gemstone!")
            add_item_to_inventory(player, "gemstone")
        elif event == "find_gold":
            print("You discover a small vein of gold!")
            player["gold"] = player.get("gold", 0) + 20
            print(f"You now have {player['gold']} gold.")
        else:
            print("You don't find anything valuable this time.")
    else:
        print("You find some interesting rocks, but you need a pickaxe to extract anything valuable.")


def listen_for_sounds(world, player):
    """Listen for sounds in the cave."""
    print("You stand still and listen carefully to the sounds in the cave.")
    print("You hear water dripping somewhere deeper in the cave.")
    
    event = generate_random_event(events=[
        ("hear_creature", 30),
        ("hear_wind", 30),
        (None, 40)
    ])
    
    if event == "hear_creature":
        print("You hear a strange growling sound from deeper in the cave. It might be dangerous to go that way.")
    elif event == "hear_wind":
        print("You hear the sound of wind coming from somewhere. There might be another entrance to the cave.")


def look_for_hidden_passages(world, player):
    """Look for hidden passages in the cave."""
    print("You carefully examine the cave walls, looking for hidden passages.")
    
    if "torch" in player["inventory"]:
        event = generate_random_event(events=[
            ("find_passage", 30),
            (None, 70)
        ])
        
        if event == "find_passage":
            print("You discover a narrow passage hidden behind a rock formation!")
            print("It seems to lead to an unexplored area of the cave.")
            # TODO: Implement hidden areas in the cave
        else:
            print("You don't find any hidden passages this time.")
    else:
        print("It's too dark to effectively search for hidden passages without a torch.")

