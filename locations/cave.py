"""
Cave location module - handles cave-specific interactions and events.
"""
from typing import Dict, Any
from game.player import add_item_to_inventory, damage_player, heal_player
from utils.random_events import apply_random_event


def explore_cave(world: Dict[str, Any], player: Dict[str, Any]) -> None:
    """
    Handle cave exploration and interactions.
    
    Args:
        world: World state dictionary
        player: Player data dictionary
    """
    print("\n=== Cave Exploration ===")
    print("The cave is dark and mysterious. Water drips from stalactites above.")
    print("You can hear strange echoes in the distance.")
    
    print("\nWhat would you like to do?")
    print("1. Search for treasure")
    print("2. Examine the cave walls")
    print("3. Listen to the echoes")
    print("4. Use torch (if you have one)")
    print("5. Rest in the cave")
    print("6. Leave the cave")
    
    try:
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == "1":
            search_for_treasure(world, player)
        elif choice == "2":
            examine_cave_walls(world, player)
        elif choice == "3":
            listen_to_echoes(world, player)
        elif choice == "4":
            use_torch_in_cave(world, player)
        elif choice == "5":
            rest_in_cave(world, player)
        elif choice == "6":
            print("You carefully make your way back to the cave entrance.")
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")
            
    except (ValueError, KeyboardInterrupt):
        print("Invalid input. Returning to cave entrance.")


def search_for_treasure(world: Dict[str, Any], player: Dict[str, Any]) -> None:
    """Handle treasure searching in the cave."""
    print("You carefully search the cave floor and crevices...")
    
    # Check if player has torch for better searching
    has_torch = "torch" in player["inventory"]
    
    if has_torch:
        print("Your torch illuminates hidden corners of the cave.")
        # Better chance of finding treasure with torch
        import random
        if random.random() < 0.7:  # 70% chance with torch
            treasure_found = random.choice(["gemstone", "gold coins", "ancient artifact"])
            print(f"You discover a {treasure_found} hidden in a small alcove!")
            
            if treasure_found == "gold coins":
                player["gold"] += 50
                print("You gained 50 gold!")
            else:
                add_item_to_inventory(player, treasure_found)
        else:
            print("Despite your thorough search, you find nothing of value.")
    else:
        print("The cave is too dark to search effectively.")
        print("You stumble around blindly and might have missed something valuable.")
        # Small chance of finding something without torch
        import random
        if random.random() < 0.2:  # 20% chance without torch
            print("You accidentally kick something... it's a small gemstone!")
            add_item_to_inventory(player, "small gemstone")
        else:
            # Chance of getting hurt in the dark
            if random.random() < 0.3:
                damage_player(player, 5)
                print("You bump into a sharp rock in the darkness!")


def examine_cave_walls(world: Dict[str, Any], player: Dict[str, Any]) -> None:
    """Handle examining the cave walls."""
    print("You run your hands along the rough cave walls...")
    
    has_torch = "torch" in player["inventory"]
    
    if has_torch:
        print("Your torch reveals ancient cave paintings on the walls!")
        print("The paintings seem to tell a story of ancient adventures.")
        print("You notice symbols that might be a map to hidden treasure.")
        
        # Add knowledge to player (could be used later)
        if "cave_knowledge" not in player:
            player["cave_knowledge"] = []
        player["cave_knowledge"].append("ancient_paintings")
        print("You memorize the symbols for future reference.")
        
    else:
        print("The walls feel rough and damp, but you can't see much in the darkness.")
        print("You sense there might be something interesting here if you had light.")


def listen_to_echoes(world: Dict[str, Any], player: Dict[str, Any]) -> None:
    """Handle listening to cave echoes."""
    print("You stand still and listen carefully to the cave's echoes...")
    
    import random
    echo_events = [
        "You hear the sound of dripping water echoing from deeper in the cave.",
        "A strange whistling sound suggests there might be another entrance.",
        "You hear what sounds like footsteps... but they're just your own echoes.",
        "The echoes reveal the cave is much larger than you initially thought.",
        "You hear a faint rumbling that might indicate underground water."
    ]
    
    echo = random.choice(echo_events)
    print(echo)
    
    # Special event: discover hidden passage
    if random.random() < 0.15:  # 15% chance
        print("\nWait... one of the echoes sounds different!")
        print("You discover a hidden passage behind some loose rocks!")
        
        choice = input("Do you want to explore the hidden passage? (y/n): ").lower()
        if choice == 'y':
            explore_hidden_passage(world, player)


def use_torch_in_cave(world: Dict[str, Any], player: Dict[str, Any]) -> None:
    """Handle using a torch in the cave."""
    if "torch" not in player["inventory"]:
        print("You don't have a torch to use.")
        return
    
    print("You light your torch, illuminating the cave around you!")
    print("The flickering light reveals:")
    print("- Glittering minerals embedded in the walls")
    print("- Ancient stalactites and stalagmites")
    print("- Several passages leading deeper into the cave")
    print("- Strange symbols carved into the rock")
    
    # Update cave description to reflect torch use
    world["locations"]["Cave"]["description"] = (
        "A dark, damp cave with echoing sounds and glittering minerals on the walls. "
        "Your torch illuminates the ancient formations and mysterious symbols."
    )
    
    print("The cave feels less mysterious now that you can see properly.")


def rest_in_cave(world: Dict[str, Any], player: Dict[str, Any]) -> None:
    """Handle resting in the cave."""
    print("You find a dry spot and sit down to rest...")
    
    import random
    if random.random() < 0.6:  # 60% chance of peaceful rest
        heal_amount = random.randint(5, 15)
        heal_player(player, heal_amount)
        print("The cool, quiet cave provides a peaceful rest.")
    else:
        print("Strange sounds in the cave make it difficult to rest properly.")
        print("You feel uneasy and don't recover as much as you hoped.")
        heal_player(player, 2)
    
    # Chance of random event while resting
    if random.random() < 0.3:
        apply_random_event(player, world)


def explore_hidden_passage(world: Dict[str, Any], player: Dict[str, Any]) -> None:
    """Handle exploration of a hidden passage."""
    print("\nYou squeeze through the narrow opening...")
    print("The passage opens into a small chamber!")
    
    import random
    chamber_events = [
        {
            "description": "You find an underground pool with crystal-clear water.",
            "action": lambda: heal_player(player, 20),
            "message": "Drinking the pure water restores your health significantly!"
        },
        {
            "description": "Ancient treasure chests line the walls of this forgotten chamber.",
            "action": lambda: [add_item_to_inventory(player, "ancient key"), 
                             setattr(player, 'gold', player['gold'] + 100)],
            "message": "You find an ancient key and 100 gold pieces!"
        },
        {
            "description": "The chamber contains ancient cave paintings and artifacts.",
            "action": lambda: add_item_to_inventory(player, "ancient scroll"),
            "message": "You carefully take an ancient scroll that might contain valuable knowledge."
        },
        {
            "description": "You discover a sleeping cave bear!",
            "action": lambda: damage_player(player, 15),
            "message": "The bear wakes up and swipes at you before you can escape!"
        }
    ]
    
    event = random.choice(chamber_events)
    print(event["description"])
    
    if callable(event["action"]):
        event["action"]()
    else:
        # Handle multiple actions
        for action in event["action"]:
            if callable(action):
                action()
    
    print(event["message"])
    print("You carefully make your way back to the main cave.")
