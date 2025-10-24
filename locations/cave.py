"""
Cave location for Kevin's Adventure Game.
"""

from game.player import add_item_to_inventory, damage_player, heal_player
from utils.random_events import generate_random_event


def explore_cave(world, player):
    """Explore the mysterious cave."""
    print("You enter the dark, damp cave. Water drips from the ceiling and your footsteps echo.")
    
    while True:
        print("\nWhat would you like to do in the cave?")
        print("1. Search for treasure")
        print("2. Examine the walls")
        print("3. Go deeper into the cave")
        print("4. Rest by the entrance")
        print("5. Leave the cave")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            search_for_treasure(world, player)
        elif choice == "2":
            examine_walls(world, player)
        elif choice == "3":
            go_deeper(world, player)
        elif choice == "4":
            rest_in_cave(world, player)
        elif choice == "5":
            print("You decide to leave the cave and return to the forest.")
            break
        else:
            print("Invalid choice. Please try again.")


def search_for_treasure(world, player):
    """Search for treasure in the cave."""
    print("You carefully search the cave floor and crevices...")
    
    event = generate_random_event(events=[
        ("find_gold", 30),
        ("find_gemstone", 20),
        ("find_nothing", 40),
        ("encounter_danger", 10)
    ])
    
    if event == "find_gold":
        gold_found = generate_random_event(events=[(10, 30), (20, 40), (50, 30)])
        player["gold"] += gold_found
        print(f"You found {gold_found} gold coins hidden in a small crevice!")
    elif event == "find_gemstone":
        add_item_to_inventory(player, "gemstone")
        print("You discover a beautiful gemstone glinting in the torchlight!")
    elif event == "find_nothing":
        print("Despite your thorough search, you find nothing of value.")
    elif event == "encounter_danger":
        print("You disturb a sleeping bat colony! They swarm around you.")
        damage_player(player, 15)


def examine_walls(world, player):
    """Examine the cave walls for interesting features."""
    print("You hold up your torch and examine the cave walls closely...")
    
    event = generate_random_event(events=[
        ("ancient_paintings", 25),
        ("mineral_deposits", 35),
        ("hidden_passage", 15),
        ("nothing_special", 25)
    ])
    
    if event == "ancient_paintings":
        print("You discover ancient cave paintings depicting mysterious creatures and symbols.")
        print("The knowledge fills you with wonder and restores some of your energy.")
        heal_player(player, 10)
    elif event == "mineral_deposits":
        print("You notice interesting mineral deposits in the rock.")
        if "pickaxe" in player["inventory"]:
            print("Using your pickaxe, you extract some valuable minerals!")
            add_item_to_inventory(player, "rare_minerals")
        else:
            print("You would need a pickaxe to extract them.")
    elif event == "hidden_passage":
        print("You notice what might be a hidden passage, but it's too narrow to explore safely.")
        print("Perhaps with the right equipment, you could investigate further.")
    else:
        print("The walls appear to be ordinary cave rock, worn smooth by time.")


def go_deeper(world, player):
    """Venture deeper into the cave."""
    print("You venture deeper into the cave, where the darkness grows thicker...")
    
    if "torch" not in player["inventory"]:
        print("Without a torch, it's too dangerous to go deeper. You turn back.")
        damage_player(player, 5)
        return
    
    event = generate_random_event(events=[
        ("underground_lake", 30),
        ("crystal_chamber", 25),
        ("dangerous_creature", 20),
        ("dead_end", 25)
    ])
    
    if event == "underground_lake":
        print("You discover a beautiful underground lake with crystal-clear water.")
        print("The peaceful sight restores your spirit.")
        heal_player(player, 20)
    elif event == "crystal_chamber":
        print("You enter a magnificent chamber filled with glowing crystals!")
        add_item_to_inventory(player, "magic_crystal")
        print("You carefully take one of the smaller crystals.")
    elif event == "dangerous_creature":
        print("You encounter a hostile cave creature! It attacks you!")
        damage_player(player, 25)
        if "sword" in player["inventory"]:
            print("You fight back with your sword and drive it away!")
            print("You find some gold that the creature was hoarding.")
            player["gold"] += 30
        else:
            print("Without a weapon, you can only flee back to safety.")
    else:
        print("The passage leads to a dead end. You turn back, disappointed.")


def rest_in_cave(world, player):
    """Rest near the cave entrance."""
    print("You sit down near the cave entrance and rest for a while.")
    print("The cool air and quiet atmosphere help you recover some energy.")
    heal_player(player, 15)
    print("You feel refreshed and ready to continue exploring.")

