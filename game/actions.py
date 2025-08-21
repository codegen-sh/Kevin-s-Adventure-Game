"""
Actions module for Kevin's Adventure Game.
Contains functions for handling player actions and commands.
"""
from game.player import add_item_to_inventory, remove_item_from_inventory, move_player
from game.world import (
    change_location, 
    get_available_locations, 
    get_current_location,
    get_location_description,
    interact_with_location
)
from utils.text_formatting import print_help


def perform_action(player, world, action):
    """
    Perform an action based on the player's input.
    
    Args:
        player (dict): The player's current state
        world (dict): The game world state
        action (str): The action to perform
        
    Returns:
        None
    """
    # Split the action into command and arguments
    parts = action.split()
    command = parts[0] if parts else ""
    args = parts[1:] if len(parts) > 1 else []
    
    # Handle different commands
    if command == "move":
        handle_move(player, world, args)
    elif command == "look":
        handle_look(player, world)
    elif command == "inventory":
        handle_inventory(player)
    elif command == "pickup" or command == "take":
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


def handle_move(player, world, args):
    """Handle the 'move' command."""
    if not args:
        print("Move where? Available locations:")
        for location in get_available_locations(world):
            print(f"- {location}")
        return
    
    new_location = args[0].capitalize()
    available_locations = get_available_locations(world)
    
    # Check if the location is valid
    if new_location in available_locations:
        if change_location(world, new_location):
            move_player(player, new_location)
    else:
        print(f"You can't go to {new_location} from here.")
        print("Available locations:")
        for location in available_locations:
            print(f"- {location}")


def handle_look(player, world):
    """Handle the 'look' command."""
    current_location = get_current_location(world)
    description = get_location_description(world, current_location)
    print(description)
    
    # Show available exits
    print("\nAvailable exits:")
    for location in get_available_locations(world):
        print(f"- {location}")
    
    # Show items in the location
    items = world["locations"][current_location].get("items", [])
    if items:
        print("\nYou can see:")
        for item in items:
            print(f"- {item}")


def handle_inventory(player):
    """Handle the 'inventory' command."""
    if not player["inventory"]:
        print("Your inventory is empty.")
    else:
        print("Your inventory contains:")
        for item in player["inventory"]:
            print(f"- {item}")


def handle_pickup(player, world, args):
    """Handle the 'pickup' or 'take' command."""
    if not args:
        print("Pick up what?")
        return
    
    item = args[0].lower()
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
    
    item = args[0].lower()
    remove_item_from_inventory(player, item)


def handle_use(player, world, args):
    """Handle the 'use' command."""
    if not args:
        print("Use what?")
        return
    
    item = args[0].lower()
    if item not in player["inventory"]:
        print(f"You don't have {item} in your inventory.")
        return
    
    # Handle different items
    if item == "bread" or item == "berries" or item == "mushrooms":
        from game.player import heal_player
        heal_player(player, 10)
        player["inventory"].remove(item)
        print(f"You ate the {item} and recovered some health.")
    elif item == "map":
        print("You look at the map. It shows your current location and nearby areas.")
        print("Available locations:")
        for location in world["locations"].keys():
            print(f"- {location}")
    elif item == "torch":
        print("You light the torch. It illuminates the area around you.")
    else:
        print(f"You're not sure how to use the {item}.")


def handle_examine(player, world, args):
    """Handle the 'examine' command."""
    if not args:
        print("Examine what?")
        return
    
    item = args[0].lower()
    
    # Check if the item is in the player's inventory
    if item in player["inventory"]:
        # Item descriptions
        descriptions = {
            "map": "A weathered map showing the village, forest, cave, and mountain.",
            "bread": "A fresh loaf of bread. It smells delicious.",
            "stick": "A sturdy wooden stick. Could be useful for various tasks.",
            "berries": "Plump, juicy berries. They look safe to eat.",
            "torch": "A wooden torch that can be lit to provide light in dark areas.",
            "gemstone": "A sparkling gemstone that catches the light beautifully.",
            "rope": "A coil of strong rope. Useful for climbing or tying things.",
            "pickaxe": "A sturdy pickaxe for mining or breaking rocks.",
            "sword": "A sharp, well-crafted sword. Useful for protection.",
            "mushrooms": "Edible mushrooms that can restore some health.",
            "mysterious_package": "A sealed package addressed to the mountain hermit.",
            "unicorn_hair": "A shimmering strand of unicorn hair. It seems magical.",
            "dragon_scale": "A tough, iridescent dragon scale. It's warm to the touch."
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
            print(f"You see a {item}. You can pick it up with 'pickup {item}'.")
        else:
            print(f"You don't see any {item} here.")


def handle_status(player):
    """Handle the 'status' command."""
    from game.player import get_player_status
    print(get_player_status(player))


def handle_interact(player, world):
    """Handle the 'interact' command."""
    interact_with_location(world, player)

