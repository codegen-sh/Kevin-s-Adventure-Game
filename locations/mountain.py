from game.player import add_item_to_inventory, damage_player, heal_player
from game.state import update_world_state
from utils.random_events import generate_random_event
from utils.text_formatting import print_event


def climb_mountain(world, player):
    """
    Handle player exploration of the mountain location.
    
    Args:
        world (dict): The world state
        player (dict): The player's state
    """
    print_event("You begin climbing the tall, snow-capped mountain. The air grows colder as you ascend, but the view becomes increasingly breathtaking.")
    
    while True:
        print("\nWhat would you like to do on the mountain?")
        print("1. Climb higher")
        print("2. Search for resources")
        print("3. Explore a narrow path")
        print("4. Rest and enjoy the view")
        print("5. Descend the mountain")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            climb_higher(world, player)
        elif choice == "2":
            search_for_resources(world, player)
        elif choice == "3":
            explore_narrow_path(world, player)
        elif choice == "4":
            rest_on_mountain(world, player)
        elif choice == "5":
            print("You decide to descend the mountain.")
            break
        else:
            print("Invalid choice. Please try again.")


def climb_higher(world, player):
    """Climb to a higher elevation on the mountain."""
    print("You carefully make your way up the steep mountain path.")
    
    # Check if player has equipment that helps with climbing
    has_climbing_gear = "rope" in player["inventory"]
    
    if has_climbing_gear:
        print("Your rope helps you navigate the difficult sections safely.")
        success_chance = 80  # 80% chance of success with rope
    else:
        print("The path becomes treacherous. Without proper equipment, it's a risky climb.")
        success_chance = 40  # 40% chance of success without rope
    
    event = generate_random_event(events=[
        ("success", success_chance),
        ("fall", 100 - success_chance)
    ])
    
    if event == "success":
        print("You successfully reach a higher elevation!")
        
        # Different discoveries based on how high the player has climbed
        mountain_level = world.get("mountain_level", 0) + 1
        world["mountain_level"] = mountain_level
        
        if mountain_level == 1:
            print("You find a small cave entrance partially hidden by rocks.")
            update_world_state(world, "mountain_cave_discovered")
        elif mountain_level == 2:
            print("You discover an abandoned miner's camp with some supplies.")
            add_item_to_inventory(player, "pickaxe")
            print("You found a pickaxe!")
        elif mountain_level == 3:
            print("You reach a plateau with a stunning view of the entire region.")
            print("From here, you can see all the major landmarks.")
            update_world_state(world, "mountain_viewpoint_reached")
        elif mountain_level >= 4:
            print("You've reached near the summit! The air is thin, and snow covers everything.")
            print("You notice something glinting in the snow...")
            add_item_to_inventory(player, "ancient_artifact")
            print("You found an ancient artifact!")
            update_world_state(world, "mountain_summit_reached")
    
    else:  # fall
        print("You lose your footing and slip!")
        
        if has_climbing_gear:
            print("Fortunately, your rope prevents you from falling far.")
            damage_player(player, 10)
            print("You take some minor damage but are able to continue.")
        else:
            print("With nothing to catch your fall, you tumble down the rocky slope!")
            damage_player(player, 25)
            print("You're badly bruised and scraped from the fall.")
            
            # Reset mountain level
            world["mountain_level"] = max(0, world.get("mountain_level", 0) - 1)


def search_for_resources(world, player):
    """Search for valuable resources on the mountain."""
    print("You search the mountain terrain for useful resources.")
    
    # Different resources available based on elevation
    mountain_level = world.get("mountain_level", 0)
    
    if "pickaxe" in player["inventory"]:
        print("Your pickaxe allows you to extract minerals from the rock.")
        success_chance = 70  # 70% chance with pickaxe
    else:
        print("Without proper tools, you're limited to what you can find on the surface.")
        success_chance = 40  # 40% chance without pickaxe
    
    event = generate_random_event(events=[
        ("find_resources", success_chance),
        (None, 100 - success_chance)
    ])
    
    if event == "find_resources":
        # Resources vary by elevation
        if mountain_level <= 1:
            resources = ["stone", "copper_ore", "herbs"]
        elif mountain_level == 2:
            resources = ["iron_ore", "silver_nugget", "crystal"]
        else:  # level 3+
            resources = ["gold_nugget", "gemstone", "rare_crystal"]
        
        found = resources[generate_random_event(events=[(i, 1) for i in range(len(resources))])]
        
        print(f"You successfully find some {found}!")
        add_item_to_inventory(player, found)
    else:
        print("Despite your efforts, you don't find anything valuable this time.")


def explore_narrow_path(world, player):
    """Explore a narrow, hidden path on the mountain."""
    print("You notice a narrow path winding around the mountain that you hadn't seen before.")
    print("Curious, you decide to follow it and see where it leads.")
    
    paths = [
        "hidden_cave",
        "abandoned_shrine",
        "mountain_spring",
        "eagle_nest",
        "dead_end"
    ]
    
    path = paths[generate_random_event(events=[(i, 1) for i in range(len(paths))])]
    
    if path == "hidden_cave":
        print("The path leads to a hidden cave entrance!")
        print("The cave appears to go deep into the mountain.")
        
        explore = input("Do you want to explore the cave? (y/n): ").lower()
        if explore == "y":
            print("You enter the dark cave, using your torch to light the way.")
            print("Inside, you find ancient carvings on the walls and a small chest.")
            add_item_to_inventory(player, "ancient_artifact")
            print("You found an ancient artifact in the chest!")
            update_world_state(world, "mountain_hidden_cave_explored")
        else:
            print("You decide not to enter the cave right now, but make a mental note of its location.")
            update_world_state(world, "mountain_hidden_cave_discovered")
    
    elif path == "abandoned_shrine":
        print("The path leads to an abandoned shrine built into the mountainside.")
        print("It appears to be very old, dedicated to some forgotten mountain deity.")
        
        pray = input("Do you want to pray at the shrine? (y/n): ").lower()
        if pray == "y":
            print("You kneel and offer a prayer at the ancient shrine.")
            print("A sense of peace washes over you, and you feel rejuvenated.")
            heal_player(player, 30)
            update_world_state(world, "mountain_shrine_blessing_received")
        else:
            print("You examine the shrine but decide not to disturb it.")
            print("You find a small offering left by a previous visitor.")
            add_item_to_inventory(player, "silver_nugget")
            print("You found a silver nugget!")
    
    elif path == "mountain_spring":
        print("The path leads to a small spring bubbling up from the mountain rock.")
        print("The water looks crystal clear and refreshing.")
        
        drink = input("Do you want to drink from the spring? (y/n): ").lower()
        if drink == "y":
            print("You cup your hands and drink the cool mountain water.")
            print("It's the most refreshing water you've ever tasted!")
            heal_player(player, 20)
            print("You feel revitalized.")
            
            # Fill water flask if player has one
            if "water_flask" in player["inventory"]:
                print("You fill your water flask with the spring water.")
                # This could be implemented as a special item
                update_world_state(world, "mountain_spring_water_collected")
        else:
            print("You decide not to drink the water, but it's a nice spot to rest.")
    
    elif path == "eagle_nest":
        print("The path takes you near a large eagle's nest built on a rocky outcrop.")
        print("The magnificent bird watches you warily from its perch.")
        
        approach = input("Do you want to approach the nest? (y/n): ").lower()
        if approach == "y":
            print("You carefully approach the eagle's nest.")
            
            if generate_random_event(events=[("friendly", 30), ("hostile", 70)]) == "friendly":
                print("The eagle seems to accept your presence and doesn't attack.")
                print("You notice something shiny in the nest that isn't part of it.")
                add_item_to_inventory(player, "golden_feather")
                print("You found a golden feather! It must be valuable.")
            else:
                print("The eagle screeches and dives at you, protecting its territory!")
                print("You shield yourself but still get scratched by its talons.")
                damage_player(player, 15)
                print("You retreat quickly, leaving the eagle in peace.")
        else:
            print("You decide to admire the eagle from a distance, respecting its territory.")
    
    elif path == "dead_end":
        print("The path winds around for a while but ultimately leads to a dead end.")
        print("There's nothing particularly interesting here.")
        
        if generate_random_event(events=[("find_something", 30), (None, 70)]) == "find_something":
            print("As you turn to leave, you notice something half-buried in the ground.")
            add_item_to_inventory(player, "old_coin")
            print("You found an old coin! It might be valuable to a collector.")
        else:
            print("You return the way you came, a bit disappointed.")


def rest_on_mountain(world, player):
    """Rest and enjoy the view from the mountain."""
    print("You find a relatively flat rock and sit down to rest, enjoying the spectacular view.")
    
    # Basic healing from resting
    heal_amount = 10
    
    # Additional healing if player has certain items
    if "bedroll" in player["inventory"]:
        heal_amount += 5
        print("Your bedroll makes resting more comfortable.")
    
    heal_player(player, heal_amount)
    print(f"The rest rejuvenates you. (Recovered {heal_amount} health)")
    
    # Chance to spot something interesting
    if generate_random_event(events=[("spot_something", 40), (None, 60)]) == "spot_something":
        print("As you rest, you notice something interesting in the distance.")
        
        discoveries = [
            "You spot what looks like ruins in the forest below.",
            "You notice a hidden path that might lead to a new area.",
            "You see smoke rising from an unexpected location.",
            "You observe strange lights in the sky that seem to be moving with purpose."
        ]
        
        discovery = discoveries[generate_random_event(events=[(i, 1) for i in range(len(discoveries))])]
        print(discovery)
        
        # This could unlock new locations or quests
        update_world_state(world, f"mountain_discovery_{discoveries.index(discovery)}")

