from game.player import add_item_to_inventory, heal_player
from utils.random_events import generate_random_event


def explore_cave(world, player):
    print("You enter the dark, mysterious cave. The air is cool and damp.")
    
    while True:
        print("\\nWhat would you like to do in the cave?")
        print("1. Search for treasure")
        print("2. Examine the walls")
        print("3. Listen for sounds")
        print("4. Use torch (if you have one)")
        print("5. Leave the cave")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            search_for_treasure(world, player)
        elif choice == "2":
            examine_walls(world, player)
        elif choice == "3":
            listen_for_sounds(world, player)
        elif choice == "4":
            use_torch_in_cave(world, player)
        elif choice == "5":
            print("You decide to leave the cave.")
            break
        else:
            print("Invalid choice. Please try again.")


def search_for_treasure(world, player):
    print("You search the cave floor for hidden treasures.")
    if generate_random_event(events=[("find_treasure", 30), (None, 70)]) == "find_treasure":
        print("You find a sparkling gemstone hidden in a crevice!")
        add_item_to_inventory(player, "gemstone")
    else:
        print("You don't find anything valuable this time.")


def examine_walls(world, player):
    print("You examine the cave walls closely.")
    print("The walls are covered in strange mineral formations that glitter in the dim light.")
    if "torch" in player["inventory"]:
        print("With your torch, you can see ancient markings carved into the stone.")


def listen_for_sounds(world, player):
    print("You stop and listen carefully to the sounds in the cave.")
    print("You hear the distant drip of water and the echo of your own breathing.")


def use_torch_in_cave(world, player):
    if "torch" in player["inventory"]:
        print("You light your torch, illuminating the cave around you.")
        print("The flickering light reveals hidden passages and beautiful rock formations.")
        # Update cave description to indicate it's now lit
        if "Cave" in world["locations"]:
            current_desc = world["locations"]["Cave"]["description"]
            if "well-lit" not in current_desc:
                world["locations"]["Cave"]["description"] += " The cave is now well-lit by your torch."
    else:
        print("You don't have a torch to light.")
