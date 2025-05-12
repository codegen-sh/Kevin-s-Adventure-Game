from game.player import add_item_to_inventory, damage_player, heal_player
from game.state import update_world_state
from utils.random_events import generate_random_event
from utils.text_formatting import print_event


def explore_cave(world, player):
    """
    Handle player exploration of the cave location.
    
    Args:
        world (dict): The world state
        player (dict): The player's state
    """
    print_event("You enter a dark, mysterious cave. The air is cool and damp, and you can hear water dripping somewhere in the distance.")
    
    while True:
        print("\nWhat would you like to do in the cave?")
        print("1. Explore deeper")
        print("2. Search for minerals")
        print("3. Investigate strange sounds")
        print("4. Rest in a safe corner")
        print("5. Leave the cave")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            explore_deeper(world, player)
        elif choice == "2":
            search_for_minerals(world, player)
        elif choice == "3":
            investigate_sounds(world, player)
        elif choice == "4":
            rest_in_cave(world, player)
        elif choice == "5":
            print("You decide to leave the cave.")
            break
        else:
            print("Invalid choice. Please try again.")


def explore_deeper(world, player):
    """Explore deeper into the cave."""
    print("You venture deeper into the cave, your footsteps echoing off the walls.")
    
    event = generate_random_event(events=[
        ("find_treasure", 20),
        ("encounter_bats", 30),
        ("discover_underground_lake", 15),
        ("trap", 20),
        (None, 15)
    ])
    
    if event == "find_treasure":
        print("You discover a small chest hidden behind some rocks!")
        add_item_to_inventory(player, "gemstone")
        player["gold"] = player.get("gold", 0) + 25
        print("You found a valuable gemstone and 25 gold coins!")
    
    elif event == "encounter_bats":
        print("A swarm of bats suddenly flies toward you, startled by your presence!")
        if "torch" in player["inventory"]:
            print("You wave your torch, and the bats disperse, avoiding the flames.")
        else:
            print("The bats swarm around you, disorienting and scratching you.")
            damage_player(player, 10)
    
    elif event == "discover_underground_lake":
        print("You discover a serene underground lake with crystal-clear water.")
        print("The water seems to have healing properties.")
        heal_player(player, 15)
        # update_world_state(world, "discovered_underground_lake")
    
    elif event == "trap":
        print("You step on a loose stone, triggering a trap!")
        damage_player(player, 15)
        print("Sharp rocks fall from the ceiling, hitting you.")
    
    else:
        print("You explore for a while but find nothing of interest.")


def search_for_minerals(world, player):
    """Search for valuable minerals in the cave."""
    print("You carefully examine the cave walls, looking for valuable minerals.")
    
    if "pickaxe" in player["inventory"]:
        print("Using your pickaxe, you efficiently chip away at promising spots in the rock.")
        success_chance = 70  # 70% chance with pickaxe
    else:
        print("Without proper tools, you're limited to what you can find with your bare hands.")
        success_chance = 30  # 30% chance without pickaxe
    
    event = generate_random_event(events=[
        ("find_minerals", success_chance),
        (None, 100 - success_chance)
    ])
    
    if event == "find_minerals":
        minerals = ["copper_ore", "iron_ore", "silver_nugget", "gold_nugget", "gemstone"]
        found = minerals[min(len(minerals) - 1, player.get("mining_skill", 0) // 10)]
        
        print(f"You successfully extract some {found.replace('_', ' ')}!")
        add_item_to_inventory(player, found)
        
        # Increase mining skill
        player["mining_skill"] = player.get("mining_skill", 0) + 1
        if player.get("mining_skill", 0) % 5 == 0:
            print(f"Your mining skill has improved to level {player['mining_skill'] // 5}!")
    else:
        print("Despite your efforts, you don't find any valuable minerals this time.")


def investigate_sounds(world, player):
    """Investigate strange sounds in the cave."""
    print("You follow the strange sounds deeper into the cave...")
    
    event = generate_random_event(events=[
        ("friendly_creature", 20),
        ("hostile_creature", 30),
        ("water_source", 25),
        ("cave_in", 15),
        (None, 10)
    ])
    
    if event == "friendly_creature":
        print("You discover a small, friendly cave creature that seems curious about you.")
        print("It leads you to a hidden stash of supplies!")
        add_item_to_inventory(player, "torch")
        heal_player(player, 10)
    
    elif event == "hostile_creature":
        print("You encounter a hostile cave creature protecting its territory!")
        if "sword" in player["inventory"]:
            print("You defend yourself with your sword, driving the creature away.")
        else:
            print("Without a weapon, you're forced to retreat, getting injured in the process.")
            damage_player(player, 20)
    
    elif event == "water_source":
        print("The sounds lead you to a small underground spring with fresh water.")
        print("You drink from the spring and feel refreshed.")
        heal_player(player, 15)
    
    elif event == "cave_in":
        print("Suddenly, the ceiling begins to collapse! You need to escape quickly!")
        damage_player(player, 15)
        print("You barely escape the cave-in, suffering some injuries.")
    
    else:
        print("The sounds fade away, and you find nothing unusual.")


def rest_in_cave(world, player):
    """Rest in a safe corner of the cave."""
    print("You find a relatively safe corner of the cave and decide to rest for a while.")
    
    # Basic healing from resting
    heal_amount = 10
    
    # Additional healing if player has certain items
    if "bedroll" in player["inventory"]:
        heal_amount += 10
        print("Your bedroll provides extra comfort, making your rest more effective.")
    
    heal_player(player, heal_amount)
    print(f"You feel refreshed after resting. (Recovered {heal_amount} health)")
    
    # Small chance of being disturbed
    if generate_random_event(events=[("disturbed", 20), (None, 80)]) == "disturbed":
        print("Your rest is disturbed by strange noises. Something is moving in the darkness...")
        # This could lead to an encounter, but we'll keep it simple for now
        print("Fortunately, whatever it was moves away without bothering you further.")

