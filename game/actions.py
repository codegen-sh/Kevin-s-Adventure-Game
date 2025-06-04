"""
Game actions module for Kevin's Adventure Game.
Handles all player actions and coordinates between different game modules.
"""

from game.items import (
    get_available_items, 
    get_item_description, 
    transfer_item, 
    use_item
)
from game.player import (
    add_item_to_inventory,
    get_player_status,
    move_player,
    remove_item_from_inventory
)
from game.world import (
    change_location,
    get_available_locations,
    get_current_location,
    get_location_description,
    interact_with_location,
    is_location_accessible
)
from locations.forest import enter_forest
from locations.mountain import climb_mountain
from locations.village import visit_village
from utils.random_events import apply_random_event
from utils.text_formatting import format_inventory, print_event


def perform_action(player, world, action):
    """
    Main action dispatcher that handles all player actions.
    
    Args:
        player (dict): Player state dictionary
        world (dict): World state dictionary  
        action (str): The action string entered by the player
    """
    action = action.strip().lower()
    
    # Split action into command and arguments
    parts = action.split()
    command = parts[0] if parts else ""
    args = parts[1:] if len(parts) > 1 else []
    
    # Handle movement commands
    if command == "move" or command == "go":
        handle_move_action(player, world, args)
    
    # Handle look/examine commands
    elif command == "look" or command == "examine":
        handle_look_action(player, world, args)
    
    # Handle inventory commands
    elif command == "inventory" or command == "inv":
        handle_inventory_action(player)
    
    # Handle pickup commands
    elif command == "pickup" or command == "take" or command == "get":
        handle_pickup_action(player, world, args)
    
    # Handle drop commands
    elif command == "drop" or command == "leave":
        handle_drop_action(player, world, args)
    
    # Handle use commands
    elif command == "use":
        handle_use_action(player, world, args)
    
    # Handle status command
    elif command == "status":
        print(get_player_status(player))
    
    # Handle interact command
    elif command == "interact":
        handle_interact_action(player, world)
    
    # Handle location-specific actions
    elif command in ["explore", "climb", "visit", "enter"]:
        handle_location_action(player, world, command)
    
    # Handle unknown commands
    else:
        print(f"Unknown command: '{action}'. Type 'help' for available commands.")
        
    # Apply random events after most actions
    if command not in ["status", "inventory", "help", "look"]:
        apply_random_event(player, world)


def handle_move_action(player, world, args):
    """Handle movement to a new location."""
    if not args:
        print("Move where? Available locations:")
        available_locations = get_available_locations(world)
        for location in available_locations:
            print(f"- {location}")
        return
    
    destination = " ".join(args).title()
    available_locations = get_available_locations(world)
    
    # Check if destination is accessible
    if destination not in available_locations:
        print(f"You can't go to {destination} from here.")
        print("Available locations:")
        for location in available_locations:
            print(f"- {location}")
        return
    
    if not is_location_accessible(world, destination):
        print(f"The path to {destination} is blocked or inaccessible.")
        return
    
    # Move to the new location
    change_location(world, destination)
    move_player(player, destination)
    print(f"You travel to {destination}.")
    print(get_location_description(world, destination))


def handle_look_action(player, world, args):
    """Handle looking at surroundings or specific items."""
    if not args:
        # Look around current location
        current_location = get_current_location(world)
        print(f"You are in {current_location}.")
        print(get_location_description(world, current_location))
        
        # Show available items
        available_items = get_available_items(world, current_location)
        if available_items:
            print("You can see the following items:")
            for item in available_items:
                print(f"- {item}")
        else:
            print("There are no items here.")
    else:
        # Look at specific item
        item = " ".join(args).lower()
        current_location = get_current_location(world)
        available_items = get_available_items(world, current_location)
        
        if item in available_items or item in player["inventory"]:
            print(get_item_description(item))
        else:
            print(f"You don't see any '{item}' here.")


def handle_inventory_action(player):
    """Handle inventory display."""
    inventory = player.get("inventory", [])
    if inventory:
        print("Your inventory contains:")
        for item in inventory:
            print(f"- {item}")
    else:
        print("Your inventory is empty.")
    
    # Show gold if player has any
    gold = player.get("gold", 0)
    if gold > 0:
        print(f"Gold: {gold}")


def handle_pickup_action(player, world, args):
    """Handle picking up items."""
    if not args:
        print("Pick up what?")
        return
    
    item = " ".join(args).lower()
    current_location = get_current_location(world)
    available_items = get_available_items(world, current_location)
    
    if item not in available_items:
        print(f"There's no '{item}' here to pick up.")
        return
    
    # Transfer item from world to inventory
    if transfer_item(player, world, item, from_inventory_to_world=False):
        print(f"You picked up the {item}.")
    else:
        print(f"You couldn't pick up the {item}.")


def handle_drop_action(player, world, args):
    """Handle dropping items."""
    if not args:
        print("Drop what?")
        return
    
    item = " ".join(args).lower()
    
    if item not in player.get("inventory", []):
        print(f"You don't have a '{item}' to drop.")
        return
    
    # Transfer item from inventory to world
    if transfer_item(player, world, item, from_inventory_to_world=True):
        print(f"You dropped the {item}.")
    else:
        print(f"You couldn't drop the {item}.")


def handle_use_action(player, world, args):
    """Handle using items."""
    if not args:
        print("Use what?")
        return
    
    item = " ".join(args).lower()
    
    if item not in player.get("inventory", []):
        print(f"You don't have a '{item}' to use.")
        return
    
    # Use the item
    if use_item(player, item, world):
        print_event(f"You used the {item}.")
    else:
        print(f"You can't use the {item} right now.")


def handle_interact_action(player, world):
    """Handle interacting with the current location."""
    current_location = get_current_location(world)
    print(f"You interact with {current_location}...")
    interact_with_location(world, player)


def handle_location_action(player, world, command):
    """Handle location-specific actions like explore, climb, visit."""
    current_location = get_current_location(world)
    
    if command == "explore":
        if current_location == "Forest":
            enter_forest(world, player)
        else:
            print(f"There's nothing special to explore in {current_location}.")
    
    elif command == "climb":
        if current_location == "Mountain":
            climb_mountain(world, player)
        else:
            print("There's nothing to climb here.")
    
    elif command == "visit" or command == "enter":
        if current_location == "Village":
            visit_village(world, player)
        elif current_location == "Forest":
            enter_forest(world, player)
        elif current_location == "Mountain":
            climb_mountain(world, player)
        else:
            print(f"You're already in {current_location}.")

