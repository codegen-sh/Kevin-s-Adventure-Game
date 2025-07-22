"""
Cave location module - handles cave exploration and interactions.
"""

from game.mythical import summon_mythical_creature
from game.player import add_item_to_inventory, damage_player, heal_player
from game.state import update_world_state
from utils.random_events import generate_random_event


def explore_cave(world, player):
    """Main cave exploration function."""
    print("You enter the dark, mysterious cave. Water drips from stalactites above, and the air is cool and damp.")
    print("Your footsteps echo in the darkness.")

    while True:
        print("\nWhat would you like to do in the cave?")
        print("1. Explore deeper into the cave")
        print("2. Search for treasure")
        print("3. Examine the cave walls")
        print("4. Rest in a safe alcove")
        print("5. Leave the cave")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            explore_deeper(world, player)
        elif choice == "2":
            search_for_treasure(world, player)
        elif choice == "3":
            examine_walls(world, player)
        elif choice == "4":
            rest_in_alcove(world, player)
        elif choice == "5":
            print("You carefully make your way back to the cave entrance.")
            break
        else:
            print("Invalid choice. Please try again.")


def explore_deeper(world, player):
    """Explore deeper into the cave with random encounters."""
    print("You venture deeper into the cave, your torch casting dancing shadows on the walls.")
    
    event = generate_random_event(events=[
        ("find_chamber", 25),
        ("encounter_bats", 20),
        ("discover_underground_stream", 15),
        ("find_ancient_paintings", 10),
        ("encounter_danger", 15),
        (None, 15)
    ])

    if event == "find_chamber":
        print("You discover a large chamber with glittering crystals embedded in the ceiling!")
        print("The natural beauty takes your breath away.")
        if generate_random_event(events=[("find_gem", 40), (None, 60)]) == "find_gem":
            add_item_to_inventory(player, "crystal_shard")
            print("You carefully extract a beautiful crystal shard.")
    
    elif event == "encounter_bats":
        print("A colony of bats suddenly erupts from the darkness, startling you!")
        if player.get("health", 0) > 10:
            damage_player(player, 5)
            print("You stumble and scrape yourself on the rough cave floor.")
        else:
            print("You duck quickly and avoid any harm.")
    
    elif event == "discover_underground_stream":
        print("You hear the sound of running water and discover a clear underground stream.")
        print("The water looks pure and refreshing.")
        heal_player(player, 15)
        print("Drinking the cool water restores your energy.")
    
    elif event == "find_ancient_paintings":
        print("You discover ancient cave paintings depicting mysterious rituals and creatures.")
        print("The artwork seems to tell a story of an ancient civilization.")
        add_item_to_inventory(player, "ancient_knowledge")
        print("You feel you've gained valuable knowledge from studying the paintings.")
    
    elif event == "encounter_danger":
        print("You hear a low growling sound echoing from the depths...")
        print("Something dangerous lurks in the darkness ahead.")
        if "torch" in player.get("inventory", []):
            print("Your torch helps you spot the danger and avoid it safely.")
        else:
            print("Without proper light, you stumble into danger!")
            damage_player(player, 15)
    
    else:
        print("You explore the winding passages but find nothing of particular interest.")
        print("The cave seems to go on forever in all directions.")


def search_for_treasure(world, player):
    """Search for treasure in the cave."""
    print("You carefully search the cave floor and crevices for anything valuable.")
    
    event = generate_random_event(events=[
        ("find_gold", 30),
        ("find_gemstone", 20),
        ("find_artifact", 15),
        ("find_nothing", 25),
        ("trigger_trap", 10)
    ])

    if event == "find_gold":
        gold_found = generate_random_event(events=[(10, 30), (20, 40), (50, 30)])
        player["gold"] = player.get("gold", 0) + gold_found
        print(f"You find {gold_found} gold coins hidden in a small crevice!")
    
    elif event == "find_gemstone":
        add_item_to_inventory(player, "cave_gemstone")
        print("You discover a beautiful gemstone embedded in the cave wall!")
    
    elif event == "find_artifact":
        add_item_to_inventory(player, "mysterious_artifact")
        print("You uncover a strange, ancient artifact partially buried in the cave floor.")
    
    elif event == "trigger_trap":
        print("You accidentally trigger an old trap! Rocks fall from above!")
        damage_player(player, 20)
        print("You manage to dodge most of the falling rocks but still get hurt.")
    
    else:
        print("Despite your thorough search, you don't find anything valuable.")
        print("The cave keeps its secrets well hidden.")


def examine_walls(world, player):
    """Examine the cave walls for interesting features."""
    print("You run your hands along the rough cave walls, looking for anything unusual.")
    
    event = generate_random_event(events=[
        ("find_minerals", 35),
        ("discover_passage", 20),
        ("find_fossils", 25),
        (None, 20)
    ])

    if event == "find_minerals":
        print("You notice interesting mineral formations in the rock.")
        print("The walls sparkle with various colored veins of ore.")
        if "pickaxe" in player.get("inventory", []):
            print("Using your pickaxe, you extract some valuable minerals!")
            add_item_to_inventory(player, "rare_minerals")
        else:
            print("You would need a pickaxe to extract these minerals.")
    
    elif event == "discover_passage":
        print("You discover a narrow passage hidden behind some loose rocks!")
        print("It looks like it might lead to another part of the cave system.")
        # This could be expanded to lead to new areas in the future
        print("The passage is too narrow to explore safely right now.")
    
    elif event == "find_fossils":
        print("You spot what appear to be ancient fossils embedded in the cave wall.")
        print("These creatures must have lived here millions of years ago.")
        add_item_to_inventory(player, "ancient_fossil")
        print("You carefully extract a small fossil as a keepsake.")
    
    else:
        print("The walls are rough and weathered, but you don't find anything special.")


def rest_in_alcove(world, player):
    """Rest in a safe alcove to recover health."""
    print("You find a dry, sheltered alcove and decide to rest for a while.")
    print("The cave is quiet except for the distant sound of dripping water.")
    
    if player.get("health", 0) < 100:
        heal_amount = min(25, 100 - player.get("health", 0))
        heal_player(player, heal_amount)
        print("The rest helps you recover your strength.")
    else:
        print("You're already at full health, but the rest is still refreshing.")
    
    # Small chance of random event while resting
    if generate_random_event(events=[("peaceful_rest", 80), ("disturbed", 20)]) == "disturbed":
        print("Your rest is interrupted by strange sounds echoing through the cave.")
        print("You decide it's best to stay alert and move on.")
    else:
        print("You have a peaceful rest and feel ready to continue exploring.")
