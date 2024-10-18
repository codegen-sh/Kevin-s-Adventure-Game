from game.player import add_item_to_inventory, remove_item_from_inventory
from game.state import update_world_state
from utils.random_events import generate_random_event


def explore_cave(world, player):
    print("You cautiously enter the dark, damp cave. Your footsteps echo off the walls.")

    while True:
        print("\nWhat would you like to do in the cave?")
        print("1. Search for minerals")
        print("2. Explore deeper")
        print("3. Listen to the cave")
        print("4. Check for bats")
        print("5. Leave the cave")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            search_for_minerals(world, player)
        elif choice == "2":
            explore_deep_cave(world, player)  # Passing None for world, update as needed
        elif choice == "3":
            listen_to_cave(world, player)
        elif choice == "4":
            check_for_bats(world, player)
        elif choice == "5":
            print("You decide to leave the cave.")
            break
        else:
            print("Invalid choice. Please try again.")

def search_for_minerals(world, player):
    print("You search the cave walls for interesting minerals.")
    if "pickaxe" in player["inventory"]:
        print("Using your pickaxe, you chip away at a promising-looking vein.")
        if generate_random_event(events = [("find_gemstone", 10), (None, 90)]) == "find_gemstone":
            print("You've discovered a beautiful gemstone!")
            add_item_to_inventory(player, "gemstone")
        else:
            print("You find some interesting rocks, but nothing valuable.")
    else:
        print("You spot some interesting minerals, but you need a pickaxe to extract them.")

def explore_deep_cave(world, player):
    if "torch" in player["inventory"]:
        print("With your torch lighting the way, you venture deeper into the cave.")
        if generate_random_event(events = [("discover_underground_lake", 20), (None, 80)]) == "discover_underground_lake":
            print("You discover a magnificent underground lake!")
            # update_world_state(world, "add_underground_lake")
        else:
            print("The cave passages twist and turn, but you find nothing of note.")
    else:
        print("It's too dark to explore deeper without a torch.")

def listen_to_cave(world, player):
    print("You stand still and listen to the sounds of the cave.")
    print("You hear water dripping somewhere in the distance and the faint sound of wind.")

def check_for_bats(world, player):
    print("You look up at the cave ceiling, checking for bats.")
    if generate_random_event(events = [("bat_swarm", 30), (None, 70)]) == "bat_swarm":
        print("Suddenly, a swarm of bats flies past you, startled by your presence!")
        print("In the confusion, you drop something from your inventory.")
        if player["inventory"]:
            dropped_item = player["inventory"][0]
            remove_item_from_inventory(player, dropped_item)
    else:
        print("You see a few bats hanging from the ceiling, but they don't seem bothered by your presence.")
