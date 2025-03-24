from game.player import add_item_to_inventory, heal_player
from utils.random_events import generate_random_event


def explore_cave(world, player):
    print("You enter a dark, mysterious cave. The air is cool and damp, and you can hear water dripping somewhere.")

    while True:
        print("\nWhat would you like to do in the cave?")
        print("1. Explore deeper")
        print("2. Look for minerals")
        print("3. Listen to the cave")
        print("4. Rest in the cave")
        print("5. Leave the cave")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            explore_deeper(world, player)
        elif choice == "2":
            look_for_minerals(world, player)
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
    print("You venture deeper into the cave, your torch illuminating the path ahead.")
    event = generate_random_event(events=[("find_passage", 20), ("encounter_bats", 30), ("underground_lake", 15), (None, 35)])

    if event == "find_passage":
        print("You discover a narrow passage that seems to lead to a hidden chamber!")
        print("You squeeze through and find an ancient chest with some valuable items.")
        add_item_to_inventory(player, "ancient coin")
        print("You've added 'ancient coin' to your inventory.")
    elif event == "encounter_bats":
        print("A swarm of bats suddenly flies past you, startled by your presence!")
        print("You duck down and cover your head until they pass.")
        heal_player(player, -2)
        print("The encounter was frightening (-2 health).")
    elif event == "underground_lake":
        print("You come across a serene underground lake with crystal-clear water.")
        print("The sight is breathtaking and fills you with a sense of wonder.")
        heal_player(player, 4)
        print("You feel rejuvenated (+4 health).")
    else:
        print("Your exploration yields nothing of note this time.")

def look_for_minerals(world, player):
    print("You examine the cave walls, looking for interesting minerals and gems.")
    event = generate_random_event(events=[("find_gemstone", 25), ("find_crystal", 30), ("find_gold", 10), (None, 35)])

    if event == "find_gemstone":
        print("You find a beautiful, sparkling gemstone embedded in the rock!")
        add_item_to_inventory(player, "gemstone")
        print("You've added 'gemstone' to your inventory.")
    elif event == "find_crystal":
        print("You discover a cluster of quartz crystals growing from the cave wall.")
        add_item_to_inventory(player, "quartz crystal")
        print("You've added 'quartz crystal' to your inventory.")
    elif event == "find_gold":
        print("You spot a vein of gold running through the rock!")
        add_item_to_inventory(player, "gold nugget")
        print("You've added 'gold nugget' to your inventory.")
    else:
        print("You don't find anything valuable this time.")

def listen_to_cave(world, player):
    print("You stand still and listen carefully to the sounds of the cave.")
    event = generate_random_event(events=[("water_sound", 40), ("strange_whispers", 20), ("distant_rumble", 15), (None, 25)])

    if event == "water_sound":
        print("You hear the sound of running water. There might be an underground stream nearby.")
    elif event == "strange_whispers":
        print("You hear what sounds like whispers echoing through the cave...")
        print("It's probably just the wind, but it sends a chill down your spine.")
    elif event == "distant_rumble":
        print("You hear a distant rumbling sound. It could be a sign of unstable cave sections.")
        print("You should be careful while exploring.")
    else:
        print("You hear nothing but the occasional drip of water.")

def rest_in_cave(world, player):
    print("You find a relatively comfortable spot and sit down to rest.")
    print("The quiet solitude of the cave is peaceful in its own way.")
    heal_player(player, 5)
    print("You feel refreshed after your rest (+5 health).")
