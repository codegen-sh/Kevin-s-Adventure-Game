from game.mythical import summon_mythical_creature
from game.player import add_item_to_inventory, damage_player, heal_player
from game.state import update_world_state
from utils.random_events import generate_random_event


def explore_cave(world, player):
    """
    Main function for exploring the cave location.
    Provides various activities and interactions within the cave.
    """
    print("You enter the dark, mysterious cave. The air is cool and damp, and you can hear water dripping somewhere in the distance.")
    
    # Check if player has a torch for better exploration
    has_torch = "torch" in player["inventory"]
    if has_torch:
        print("Your torch illuminates the cave walls, revealing glittering minerals and ancient markings.")
    else:
        print("The cave is quite dark. A torch would help you see better.")

    while True:
        print("\nWhat would you like to do in the cave?")
        print("1. Search for treasure")
        print("2. Examine the cave walls")
        print("3. Follow the sound of water")
        print("4. Rest in the cave")
        print("5. Venture deeper into the cave")
        print("6. Leave the cave")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            search_for_treasure(world, player, has_torch)
        elif choice == "2":
            examine_cave_walls(world, player, has_torch)
        elif choice == "3":
            follow_water_sound(world, player)
        elif choice == "4":
            rest_in_cave(world, player)
        elif choice == "5":
            venture_deeper(world, player, has_torch)
        elif choice == "6":
            print("You decide to leave the cave and return to the forest.")
            break
        else:
            print("Invalid choice. Please try again.")


def search_for_treasure(world, player, has_torch):
    """Search for treasure in the cave."""
    print("You search the cave floor and crevices for any valuable items.")
    
    if has_torch:
        # Better chances with a torch
        event = generate_random_event(events=[("find_gemstone", 40), ("find_coin", 30), ("find_nothing", 30)])
    else:
        # Reduced chances without light
        event = generate_random_event(events=[("find_gemstone", 20), ("find_coin", 20), ("find_nothing", 60)])
    
    if event == "find_gemstone":
        print("Your search pays off! You discover a beautiful gemstone embedded in the cave wall.")
        add_item_to_inventory(player, "gemstone")
    elif event == "find_coin":
        print("You find an ancient coin partially buried in the cave floor!")
        add_item_to_inventory(player, "ancient_coin")
    else:
        if has_torch:
            print("Despite your thorough search with the torch, you don't find anything valuable this time.")
        else:
            print("Searching in the dark proves difficult. You don't find anything.")


def examine_cave_walls(world, player, has_torch):
    """Examine the cave walls for interesting features."""
    print("You carefully examine the cave walls.")
    
    if has_torch:
        print("With your torch providing light, you can see ancient cave paintings and strange symbols.")
        event = generate_random_event(events=[("discover_secret", 30), ("learn_history", 40), ("find_minerals", 30)])
        
        if event == "discover_secret":
            print("You notice a hidden passage behind some loose rocks!")
            print("This might lead to a secret area of the cave.")
            # update_world_state(world, "reveal_secret_passage")
        elif event == "learn_history":
            print("The cave paintings tell the story of ancient civilizations that once lived here.")
            print("You feel wiser from this discovery.")
            heal_player(player, 10)
        elif event == "find_minerals":
            print("You spot some valuable minerals in the cave wall.")
            add_item_to_inventory(player, "silver_necklace")
    else:
        print("It's too dark to see much detail on the walls. You can only make out rough shapes.")
        print("A torch would help you see what's really here.")


def follow_water_sound(world, player):
    """Follow the sound of dripping water."""
    print("You follow the sound of dripping water deeper into the cave.")
    
    event = generate_random_event(events=[("find_spring", 50), ("slip_and_fall", 30), ("discover_pool", 20)])
    
    if event == "find_spring":
        print("You discover a natural spring with crystal-clear water!")
        print("You drink from the spring and feel refreshed.")
        heal_player(player, 25)
    elif event == "slip_and_fall":
        print("The cave floor is slippery near the water source. You slip and fall!")
        damage_player(player, 10)
        print("You should be more careful in the dark, damp cave.")
    elif event == "discover_pool":
        print("You find a small underground pool with strange, glowing fish!")
        print("The sight is magical and fills you with wonder.")
        # summon_mythical_creature(world, player, "cave_sprite")


def rest_in_cave(world, player):
    """Rest in the cave to recover."""
    print("You find a dry spot in the cave and sit down to rest.")
    
    if "torch" in player["inventory"]:
        print("Your torch provides warmth and comfort as you rest.")
        heal_player(player, 15)
        print("You feel well-rested and ready to continue exploring.")
    else:
        print("Resting in the cold, dark cave isn't very comfortable.")
        heal_player(player, 5)
        print("You feel slightly better, but the cave isn't ideal for resting.")


def venture_deeper(world, player, has_torch):
    """Venture deeper into the cave system."""
    print("You decide to explore the deeper parts of the cave.")
    
    if has_torch:
        print("Your torch lights the way as you venture into the cave's depths.")
        event = generate_random_event(events=[("find_chamber", 40), ("encounter_bats", 30), ("discover_artifact", 30)])
        
        if event == "find_chamber":
            print("You discover a large underground chamber with stunning rock formations!")
            print("The natural beauty of this hidden place is breathtaking.")
            heal_player(player, 20)
        elif event == "encounter_bats":
            print("You disturb a colony of bats! They fly around you in a panic.")
            print("You duck and cover until they settle down.")
            damage_player(player, 5)
        elif event == "discover_artifact":
            print("In the deepest part of the cave, you find an ancient artifact!")
            add_item_to_inventory(player, "ancient_artifact")
    else:
        print("Venturing deeper without light is dangerous!")
        print("You stumble in the darkness and decide it's too risky to continue.")
        damage_player(player, 15)
        print("You should find a torch before exploring the deeper parts of the cave.")

