"""
Game actions module - handles user input and command processing
"""

from game.player import (
    add_item_to_inventory, 
    remove_item_from_inventory, 
    move_player, 
    heal_player,
    damage_player
)
from game.world import (
    get_current_location, 
    get_location_description, 
    get_available_locations,
    change_location,
    interact_with_location,
    is_location_accessible
)
from utils.text_formatting import format_inventory


def perform_action(player, world, action):
    """
    Process user actions and update game state accordingly
    
    Args:
        player (dict): Player data structure
        world (dict): World data structure  
        action (str): User input action
    """
    action = action.lower().strip()
    
    # Parse action into command and arguments
    parts = action.split()
    command = parts[0] if parts else ""
    args = parts[1:] if len(parts) > 1 else []
    
    # Movement commands
    if command in ["go", "move", "travel", "walk"]:
        handle_movement(player, world, args)
    
    # Inventory commands
    elif command in ["inventory", "inv", "i"]:
        show_inventory(player)
    
    elif command in ["take", "get", "pick", "pickup"]:
        handle_take_item(player, world, args)
    
    elif command in ["drop", "leave"]:
        handle_drop_item(player, args)
    
    elif command in ["use"]:
        handle_use_item(player, world, args)
    
    # Location interaction commands
    elif command in ["look", "examine", "inspect"]:
        handle_look(player, world, args)
    
    elif command in ["interact", "talk", "enter"]:
        interact_with_location(world, player)
    
    # Status commands
    elif command in ["status", "stats", "health"]:
        show_player_status(player)
    
    elif command in ["locations", "map"]:
        show_available_locations(world)
    
    # Help command
    elif command in ["help", "commands"]:
        show_help()
    
    else:
        print(f"Unknown command: '{action}'. Type 'help' for available commands.")


def handle_movement(player, world, args):
    """Handle player movement between locations"""
    if not args:
        print("Where would you like to go? Available locations:")
        show_available_locations(world)
        return
    
    destination = " ".join(args).title()
    
    if is_location_accessible(world, destination):
        if change_location(world, destination):
            move_player(player, destination)
            print(f"\n{get_location_description(world, destination)}")
        else:
            print(f"You cannot go to {destination} from here.")
    else:
        print(f"'{destination}' is not a valid location or is not accessible from here.")
        show_available_locations(world)


def handle_take_item(player, world, args):
    """Handle taking items from the current location"""
    if not args:
        print("What would you like to take?")
        return
    
    item_name = " ".join(args).lower()
    current_location = get_current_location(world)
    location_items = world["locations"][current_location].get("items", [])
    
    if item_name in location_items:
        location_items.remove(item_name)
        add_item_to_inventory(player, item_name)
    else:
        print(f"There is no '{item_name}' here to take.")
        if location_items:
            print(f"Available items: {', '.join(location_items)}")


def handle_drop_item(player, args):
    """Handle dropping items from inventory"""
    if not args:
        print("What would you like to drop?")
        return
    
    item_name = " ".join(args).lower()
    remove_item_from_inventory(player, item_name)


def handle_use_item(player, world, args):
    """Handle using items from inventory"""
    if not args:
        print("What would you like to use?")
        return
    
    item_name = " ".join(args).lower()
    
    if item_name not in player["inventory"]:
        print(f"You don't have '{item_name}' in your inventory.")
        return
    
    # Item-specific usage logic
    if item_name == "bread":
        player["inventory"].remove(item_name)
        heal_player(player, 20)
        print("You ate the bread and feel refreshed.")
    
    elif item_name == "torch":
        print("The torch provides light in dark places.")
        # Could add logic for dark locations
    
    elif item_name == "map":
        print("The map shows the layout of the world:")
        show_world_map(world)
    
    elif item_name == "rope":
        current_location = get_current_location(world)
        if current_location == "Mountain":
            print("The rope helps you climb more safely on the mountain.")
        else:
            print("The rope might be useful for climbing.")
    
    elif item_name == "sword":
        print("You brandish your sword. You feel more confident in combat.")
        # Could add combat bonus logic
    
    else:
        print(f"You're not sure how to use the {item_name}.")


def handle_look(player, world, args):
    """Handle looking at the environment or specific objects"""
    if not args:
        # Look around current location
        current_location = get_current_location(world)
        print(f"\n{get_location_description(world, current_location)}")
        
        location_items = world["locations"][current_location].get("items", [])
        if location_items:
            print(f"You can see: {', '.join(location_items)}")
        
        available_locations = get_available_locations(world)
        if available_locations:
            print(f"You can go to: {', '.join(available_locations)}")
    else:
        # Look at specific object
        target = " ".join(args).lower()
        print(f"You examine the {target}.")
        # Could add specific object descriptions


def show_inventory(player):
    """Display player's inventory"""
    inventory = player.get("inventory", [])
    if inventory:
        print(f"Inventory: {format_inventory(inventory)}")
    else:
        print("Your inventory is empty.")


def show_player_status(player):
    """Display detailed player status"""
    print(f"Name: {player['name']}")
    print(f"Health: {player['health']}/100")
    print(f"Gold: {player['gold']}")
    print(f"Location: {player['location']}")
    show_inventory(player)


def show_available_locations(world):
    """Display locations accessible from current position"""
    available = get_available_locations(world)
    if available:
        print(f"Available locations: {', '.join(available)}")
    else:
        print("No locations available from here.")


def show_world_map(world):
    """Display a simple world map"""
    print("\n=== WORLD MAP ===")
    for location, data in world["locations"].items():
        connections = ", ".join(data["connections"])
        print(f"{location}: connects to {connections}")


def show_help():
    """Display available commands"""
    print("\n=== AVAILABLE COMMANDS ===")
    print("Movement:")
    print("  go <location>     - Move to a location")
    print("  locations         - Show available locations")
    print("")
    print("Inventory:")
    print("  inventory         - Show your inventory")
    print("  take <item>       - Take an item")
    print("  drop <item>       - Drop an item")
    print("  use <item>        - Use an item")
    print("")
    print("Interaction:")
    print("  look              - Look around")
    print("  look <object>     - Examine an object")
    print("  interact          - Interact with current location")
    print("")
    print("Information:")
    print("  status            - Show player status")
    print("  help              - Show this help")
    print("  quit              - Save and quit game")
