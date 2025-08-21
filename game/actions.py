"""
Actions module for Kevin's Adventure Game.
This module handles all player actions and their effects on the game state.
"""

from game.player import (add_item_to_inventory, damage_player, get_player_status,
                        heal_player, move_player, remove_item_from_inventory)
from game.world import (change_location, get_available_locations,
                       get_current_location, get_location_description,
                       interact_with_location, is_location_accessible)
from utils.random_events import apply_random_event
from utils.text_formatting import print_event


def perform_action(player, world, action):
    """
    Parse and perform a player action.
    
    Args:
        player (dict): The player state dictionary
        world (dict): The world state dictionary
        action (str): The action string entered by the player
        
    Returns:
        None
    """
    # Split the action into command and arguments
    parts = action.split()
    command = parts[0] if parts else ""
    args = parts[1:] if len(parts) > 1 else []
    
    # Process the command
    if command == "move":
        handle_move(player, world, args)
    elif command == "look":
        handle_look(player, world)
    elif command == "inventory":
        handle_inventory(player)
    elif command == "pickup":
        handle_pickup(player, world, args)
    elif command == "drop":
        handle_drop(player, args)
    elif command == "use":
        handle_use(player, world, args)
    elif command == "examine":
        handle_examine(player, world, args)
    elif command == "status":
        handle_status(player)
    elif command == "interact":
        handle_interact(player, world)
    else:
        print(f"Unknown command: {command}. Type 'help' for a list of commands.")
    
    # Random events have a chance to occur after any action
    if command not in ["look", "inventory", "examine", "status", "help"]:
        # Only apply random events for actions that change the game state
        apply_random_event(player, world)


def handle_move(player, world, args):
    """Handle the 'move' command."""
    if not args:
        print("Move where? Available locations:")
        available_locations = get_available_locations(world)
        for location in available_locations:
            print(f"- {location}")
        return
    
    destination = " ".join(args)
    available_locations = get_available_locations(world)
    
    # Check if the destination is valid
    if destination.capitalize() in [loc.capitalize() for loc in available_locations]:
        # Find the actual location name with correct capitalization
        for loc in available_locations:
            if loc.capitalize() == destination.capitalize():
                destination = loc
                break
        
        # Move the player
        if change_location(world, destination):
            move_player(player, destination)
            print(get_location_description(world, destination))
    else:
        print(f"You can't go to {destination} from here.")
        print("Available locations:")
        for location in available_locations:
            print(f"- {location}")


def handle_look(player, world):
    """Handle the 'look' command."""
    current_location = get_current_location(world)
    print(get_location_description(world, current_location))
    
    # Show available items at this location
    location_items = world["locations"][current_location].get("items", [])
    if location_items:
        print("You see the following items:")
        for item in location_items:
            print(f"- {item}")
    else:
        print("You don't see any items here.")
    
    # Show available connections
    available_locations = get_available_locations(world)
    print("You can go to:")
    for location in available_locations:
        print(f"- {location}")


def handle_inventory(player):
    """Handle the 'inventory' command."""
    if not player["inventory"]:
        print("Your inventory is empty.")
    else:
        print("Your inventory contains:")
        for item in player["inventory"]:
            print(f"- {item}")


def handle_pickup(player, world, args):
    """Handle the 'pickup' command."""
    if not args:
        print("Pick up what?")
        return
    
    item = " ".join(args)
    current_location = get_current_location(world)
    location_items = world["locations"][current_location].get("items", [])
    
    if item in location_items:
        add_item_to_inventory(player, item)
        location_items.remove(item)
    else:
        print(f"There is no {item} here.")


def handle_drop(player, args):
    """Handle the 'drop' command."""
    if not args:
        print("Drop what?")
        return
    
    item = " ".join(args)
    if remove_item_from_inventory(player, item):
        current_location = player["location"]
        world_location = world["locations"][current_location]
        if "items" not in world_location:
            world_location["items"] = []
        world_location["items"].append(item)


def handle_use(player, world, args):
    """Handle the 'use' command."""
    if not args:
        print("Use what?")
        return
    
    item = " ".join(args)
    if item not in player["inventory"]:
        print(f"You don't have {item} in your inventory.")
        return
    
    # Handle different items
    if item == "potion" or item == "healing_potion":
        print("You drink the healing potion.")
        heal_player(player, 20)
        remove_item_from_inventory(player, item)
    elif item == "map":
        print("You consult your map.")
        print("Available locations in the world:")
        for location in world["locations"]:
            if is_location_accessible(world, location) or location == get_current_location(world):
                print(f"- {location}")
    elif item == "torch":
        print("You light the torch, illuminating the area around you.")
        # Could add special effects for dark areas
    elif item == "bread" or item == "berries" or item == "mushrooms":
        print(f"You eat the {item}. It's delicious!")
        heal_player(player, 10)
        remove_item_from_inventory(player, item)
    else:
        print(f"You're not sure how to use the {item}.")


def handle_examine(player, world, args):
    """Handle the 'examine' command."""
    if not args:
        print("Examine what?")
        return
    
    item = " ".join(args)
    
    # Check if the item is in the player's inventory
    if item in player["inventory"]:
        # Item descriptions
        descriptions = {
            "map": "A weathered map of the surrounding area. It shows the village, forest, cave, and mountain.",
            "bread": "A fresh loaf of bread. It smells delicious and would restore some health if eaten.",
            "stick": "A sturdy wooden stick. It could be used as a simple weapon or tool.",
            "berries": "Plump, juicy berries. They look safe to eat and would restore some health.",
            "torch": "A wooden torch that can be lit to illuminate dark areas.",
            "gemstone": "A sparkling gemstone that seems valuable.",
            "rope": "A coil of strong rope. Useful for climbing or binding things.",
            "pickaxe": "A sturdy pickaxe for mining or breaking rocks.",
            "mushrooms": "Edible mushrooms that would restore some health if eaten.",
            "potion": "A mysterious potion that might have healing properties.",
            "healing_potion": "A potion that will restore a significant amount of health when consumed."
        }
        
        if item in descriptions:
            print(descriptions[item])
        else:
            print(f"It's a {item}. Nothing special about it.")
    else:
        # Check if the item is in the current location
        current_location = get_current_location(world)
        location_items = world["locations"][current_location].get("items", [])
        
        if item in location_items:
            print(f"You see a {item} on the ground. You can pick it up.")
        else:
            print(f"You don't see any {item} here.")


def handle_status(player):
    """Handle the 'status' command."""
    print(get_player_status(player))


def handle_interact(player, world):
    """Handle the 'interact' command."""
    interact_with_location(world, player)

