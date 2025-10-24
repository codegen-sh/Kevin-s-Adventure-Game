"""
Cave location for Kevin's Adventure Game.
Provides cave-specific interactions and events.
"""
import random
from typing import Dict, Any
from game.player import add_item_to_inventory, heal_player, damage_player
from utils.random_events import generate_random_event


def explore_cave(world: Dict[str, Any], player: Dict[str, Any]) -> None:
    """
    Handle cave exploration.
    
    Args:
        world: World state dictionary
        player: Player state dictionary
    """
    print("\n=== Exploring the Cave ===")
    print("You venture deeper into the dark, mysterious cave.")
    print("The sound of dripping water echoes around you.")
    
    # Check if player has a torch
    has_torch = "torch" in player.get("inventory", [])
    
    if has_torch:
        print("Your torch illuminates the cave walls, revealing ancient drawings.")
        print("The light helps you navigate safely through the cave.")
        
        # Better outcomes with torch
        event = generate_random_event(events=[
            ("find_treasure", 40),
            ("discover_passage", 30),
            ("find_crystals", 20),
            ("nothing", 10)
        ])
        
        if event == "find_treasure":
            print("Your torch reveals a hidden alcove containing a valuable gemstone!")
            add_item_to_inventory(player, "ancient_artifact")
        elif event == "discover_passage":
            print("The torchlight reveals a hidden passage leading deeper into the mountain.")
            print("You mark its location for future exploration.")
            # Could add a new location or connection here
        elif event == "find_crystals":
            print("Beautiful crystals glitter in your torchlight!")
            add_item_to_inventory(player, "gemstone")
        else:
            print("You explore thoroughly but find nothing new.")
    
    else:
        print("The cave is very dark. You stumble around carefully.")
        print("It's difficult to see anything without a light source.")
        
        # Riskier outcomes without torch
        event = generate_random_event(events=[
            ("trip_and_fall", 30),
            ("find_something", 25),
            ("get_lost", 20),
            ("nothing", 25)
        ])
        
        if event == "trip_and_fall":
            print("You trip over something in the darkness and hurt yourself!")
            damage_player(player, 10)
            print("You should find a torch before exploring further.")
        elif event == "find_something":
            print("You feel around in the dark and find something!")
            items = ["torch", "rope", "ancient_coin"]
            found_item = random.choice(items)
            add_item_to_inventory(player, found_item)
        elif event == "get_lost":
            print("You become disoriented in the darkness!")
            print("After some time, you manage to find your way back to the entrance.")
            damage_player(player, 5)
        else:
            print("You carefully explore but find nothing in the darkness.")
    
    # Cave-specific actions
    print("\nWhat would you like to do in the cave?")
    print("1. Search for minerals")
    print("2. Listen for sounds")
    print("3. Look for cave paintings")
    print("4. Return to entrance")
    
    try:
        choice = input("Choose an action (1-4): ").strip()
        
        if choice == "1":
            search_for_minerals(world, player)
        elif choice == "2":
            listen_in_cave(world, player)
        elif choice == "3":
            examine_cave_paintings(world, player)
        elif choice == "4":
            print("You make your way back to the cave entrance.")
        else:
            print("You decide to just look around for a moment.")
    
    except (ValueError, KeyboardInterrupt):
        print("You decide to just look around for a moment.")


def search_for_minerals(world: Dict[str, Any], player: Dict[str, Any]) -> None:
    """
    Search for minerals in the cave.
    
    Args:
        world: World state dictionary
        player: Player state dictionary
    """
    print("\nYou search the cave walls for valuable minerals...")
    
    # Check if player has pickaxe
    has_pickaxe = "pickaxe" in player.get("inventory", [])
    
    if has_pickaxe:
        print("You use your pickaxe to carefully extract minerals from the rock.")
        
        event = generate_random_event(events=[
            ("find_gems", 50),
            ("find_ore", 30),
            ("break_pickaxe", 10),
            ("nothing", 10)
        ])
        
        if event == "find_gems":
            print("You successfully extract some beautiful gemstones!")
            add_item_to_inventory(player, "gemstone")
            add_item_to_inventory(player, "ancient_coin")
        elif event == "find_ore":
            print("You find some valuable ore deposits!")
            add_item_to_inventory(player, "ancient_artifact")
        elif event == "break_pickaxe":
            print("Your pickaxe breaks against the hard rock!")
            if "pickaxe" in player.get("inventory", []):
                player["inventory"].remove("pickaxe")
            print("You'll need a new pickaxe to continue mining.")
        else:
            print("The rock is too hard to extract anything useful.")
    
    else:
        print("You try to chip away at the rock with your hands.")
        print("Without proper tools, you can't extract much.")
        
        event = generate_random_event(events=[
            ("small_find", 30),
            ("hurt_hands", 40),
            ("nothing", 30)
        ])
        
        if event == "small_find":
            print("You manage to find a small, loose gemstone!")
            add_item_to_inventory(player, "gemstone")
        elif event == "hurt_hands":
            print("You scrape your hands on the rough rock!")
            damage_player(player, 5)
        else:
            print("You can't make any progress without proper mining tools.")


def listen_in_cave(world: Dict[str, Any], player: Dict[str, Any]) -> None:
    """
    Listen for sounds in the cave.
    
    Args:
        world: World state dictionary
        player: Player state dictionary
    """
    print("\nYou stop and listen carefully to the sounds of the cave...")
    
    sounds = [
        "The steady drip of water echoing from deep within the cave.",
        "A faint whistling sound that might be wind through hidden passages.",
        "The scurrying of small creatures in the darkness.",
        "Your own breathing and heartbeat in the silence.",
        "A distant rumbling that could be underground water.",
        "The settling and creaking of ancient rock formations."
    ]
    
    print(random.choice(sounds))
    
    # Chance for special discovery
    event = generate_random_event(events=[
        ("hear_water", 25),
        ("hear_wind", 20),
        ("hear_nothing", 55)
    ])
    
    if event == "hear_water":
        print("You hear the sound of flowing water nearby!")
        print("Following the sound, you discover a small underground stream.")
        print("The water is crystal clear and refreshing.")
        heal_player(player, 15)
        print("Drinking the pure cave water restores your energy.")
    
    elif event == "hear_wind":
        print("You hear wind coming from a crack in the wall!")
        print("This suggests there might be another chamber or exit nearby.")
        print("You make a mental note to investigate further with proper equipment.")
    
    else:
        print("The cave is mostly silent, with only natural sounds.")


def examine_cave_paintings(world: Dict[str, Any], player: Dict[str, Any]) -> None:
    """
    Examine ancient cave paintings.
    
    Args:
        world: World state dictionary
        player: Player state dictionary
    """
    print("\nYou examine the cave walls for ancient paintings...")
    
    # Check if player has torch for better visibility
    has_torch = "torch" in player.get("inventory", [])
    
    if has_torch:
        print("Your torch illuminates the cave walls clearly.")
        print("You discover ancient paintings depicting:")
        
        paintings = [
            "Hunters pursuing large, extinct animals across vast plains.",
            "Mysterious figures performing rituals around a fire.",
            "Maps showing the locations of hidden treasures.",
            "Symbols that might represent an ancient language.",
            "Scenes of people living in harmony with nature.",
            "Warnings about dangerous creatures that once roamed the land."
        ]
        
        print(f"- {random.choice(paintings)}")
        print(f"- {random.choice(paintings)}")
        
        # Chance to gain knowledge or item
        event = generate_random_event(events=[
            ("gain_knowledge", 40),
            ("find_hidden_item", 30),
            ("nothing_special", 30)
        ])
        
        if event == "gain_knowledge":
            print("\nStudying the paintings gives you insight into the area's history!")
            print("You feel wiser and more connected to this ancient place.")
            # Could add knowledge tracking here
        
        elif event == "find_hidden_item":
            print("\nOne of the paintings seems to point to a hidden cache!")
            print("Following its directions, you find a concealed alcove.")
            add_item_to_inventory(player, "ancient_artifact")
        
        else:
            print("\nThe paintings are beautiful but don't reveal any immediate secrets.")
    
    else:
        print("It's too dark to see any paintings clearly.")
        print("You can make out some faint markings on the walls,")
        print("but you would need a light source to examine them properly.")
        print("You should return with a torch to study them.")


# Additional cave utility functions
def is_cave_lit(player: Dict[str, Any]) -> bool:
    """
    Check if the cave is lit (player has torch).
    
    Args:
        player: Player state dictionary
        
    Returns:
        True if cave is lit, False otherwise
    """
    return "torch" in player.get("inventory", [])


def get_cave_description(player: Dict[str, Any]) -> str:
    """
    Get cave description based on lighting conditions.
    
    Args:
        player: Player state dictionary
        
    Returns:
        Cave description string
    """
    base_desc = "A dark, damp cave with echoing sounds and glittering minerals on the walls."
    
    if is_cave_lit(player):
        return base_desc + " Your torch illuminates ancient paintings and hidden passages."
    else:
        return base_desc + " The darkness makes it difficult to see much detail."

