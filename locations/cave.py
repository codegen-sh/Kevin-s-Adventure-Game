"""
Cave location module for Kevin's Adventure Game.
Handles interactions and events specific to the cave location.
"""

from game.player import add_item_to_inventory, damage_player, heal_player
from game.state import update_world_state
from utils.random_events import generate_random_event
import random


def explore_cave(world, player):
    """
    Handle cave exploration interactions.
    
    Args:
        world: World state dictionary
        player: Player data dictionary
    """
    print("You enter the dark, mysterious cave. Water drips from stalactites above,")
    print("and you can hear the echo of your footsteps. The air is cool and damp.")
    
    while True:
        print("\nWhat would you like to do in the cave?")
        print("1. Venture deeper into the cave")
        print("2. Search for minerals and gems")
        print("3. Light a torch (if you have one)")
        print("4. Listen for sounds")
        print("5. Rest in the cave")
        print("6. Leave the cave")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == "1":
            _venture_deeper(world, player)
        elif choice == "2":
            _search_for_minerals(world, player)
        elif choice == "3":
            _light_torch(world, player)
        elif choice == "4":
            _listen_for_sounds(world, player)
        elif choice == "5":
            _rest_in_cave(world, player)
        elif choice == "6":
            print("You carefully make your way back to the cave entrance.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")
        
        # Random event chance
        if random.random() < 0.3:
            generate_random_event(world, player, "cave")


def _venture_deeper(world, player):
    """Handle venturing deeper into the cave."""
    print("You carefully navigate deeper into the cave's winding passages.")
    
    encounter_chance = random.random()
    
    if encounter_chance < 0.3:
        print("You discover a hidden chamber filled with ancient cave paintings!")
        print("The paintings seem to tell the story of ancient civilizations.")
        add_item_to_inventory(player, "ancient_scroll")
        update_world_state(world, "cave_paintings_discovered", True)
    elif encounter_chance < 0.5:
        print("You stumble in the darkness and scrape your knee on a sharp rock.")
        damage_player(player, 5)
    elif encounter_chance < 0.7:
        print("You find a small underground stream with crystal-clear water.")
        print("Drinking from it refreshes you.")
        heal_player(player, 10)
    else:
        print("The passage leads to a dead end, but you notice some interesting rock formations.")


def _search_for_minerals(world, player):
    """Handle searching for minerals and gems."""
    print("You carefully examine the cave walls, looking for valuable minerals.")
    
    if "pickaxe" in player["inventory"]:
        print("Using your pickaxe, you chip away at the rock face.")
        find_chance = random.random()
        
        if find_chance < 0.4:
            gems = ["ruby", "sapphire", "emerald", "quartz_crystal", "amethyst"]
            found_gem = random.choice(gems)
            print(f"You successfully extract a beautiful {found_gem}!")
            add_item_to_inventory(player, found_gem)
            player["gold"] += random.randint(20, 50)
        elif find_chance < 0.7:
            print("You find some common minerals, but nothing particularly valuable.")
            add_item_to_inventory(player, "iron_ore")
        else:
            print("Despite your efforts, you don't find anything of value this time.")
    else:
        print("Without proper tools, you can only collect small pebbles and common stones.")
        if random.random() < 0.3:
            add_item_to_inventory(player, "smooth_pebble")


def _light_torch(world, player):
    """Handle lighting a torch."""
    if "torch" in player["inventory"]:
        print("You light your torch, illuminating the cave with a warm, flickering glow.")
        print("The light reveals intricate mineral formations and hidden passages.")
        
        # Torch provides temporary benefits for cave exploration
        world.setdefault("temp_effects", {})["torch_lit"] = True
        
        # Chance to discover something with better visibility
        if random.random() < 0.4:
            discoveries = [
                ("hidden_passage", "You notice a narrow passage you hadn't seen before!"),
                ("bat_colony", "Your light disturbs a colony of bats that flutter overhead."),
                ("underground_lake", "The torchlight reflects off a small underground lake."),
                ("fossil", "You spot what appears to be an ancient fossil embedded in the wall.")
            ]
            discovery, description = random.choice(discoveries)
            print(description)
            
            if discovery == "fossil":
                add_item_to_inventory(player, "ancient_fossil")
    else:
        print("You don't have a torch to light. The cave remains shrouded in darkness.")


def _listen_for_sounds(world, player):
    """Handle listening for sounds in the cave."""
    print("You stand perfectly still and listen carefully to the cave's sounds...")
    
    sounds = [
        "You hear the steady drip of water echoing through the chambers.",
        "A faint whistling sound suggests there might be another entrance somewhere.",
        "You hear the distant flutter of bat wings deeper in the cave.",
        "The sound of your own breathing seems amplified in the silence.",
        "You detect a faint rumbling that might be an underground stream.",
        "Strange clicking sounds echo from the depths - perhaps falling pebbles?"
    ]
    
    print(random.choice(sounds))
    
    # Small chance of discovering something through careful listening
    if random.random() < 0.2:
        print("Your careful listening pays off - you notice a loose rock that might hide something!")
        if random.random() < 0.5:
            add_item_to_inventory(player, "hidden_key")
            print("Behind the rock, you find an old, mysterious key!")


def _rest_in_cave(world, player):
    """Handle resting in the cave."""
    print("You find a relatively dry spot and sit down to rest.")
    
    if player["health"] < 100:
        rest_healing = random.randint(5, 15)
        heal_player(player, rest_healing)
        print("The cool, quiet environment helps you recover some energy.")
    else:
        print("You feel refreshed after your brief rest.")
    
    # Small chance of a peaceful encounter while resting
    if random.random() < 0.2:
        encounters = [
            "A small, friendly cave creature approaches and seems curious about you.",
            "You notice beautiful mineral formations glittering in the dim light.",
            "The sound of dripping water creates a soothing, rhythmic melody."
        ]
        print(random.choice(encounters))


def get_cave_items(world):
    """
    Get available items in the cave.
    
    Args:
        world: World state dictionary
        
    Returns:
        list: Available items in the cave
    """
    return world["locations"]["Cave"].get("items", [])


def add_cave_item(world, item):
    """
    Add an item to the cave location.
    
    Args:
        world: World state dictionary
        item: Item to add to the cave
    """
    world["locations"]["Cave"].setdefault("items", []).append(item)


def remove_cave_item(world, item):
    """
    Remove an item from the cave location.
    
    Args:
        world: World state dictionary
        item: Item to remove from the cave
        
    Returns:
        bool: True if item was removed, False if not found
    """
    cave_items = world["locations"]["Cave"].get("items", [])
    if item in cave_items:
        cave_items.remove(item)
        return True
    return False

