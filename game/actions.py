"""
Game actions module - handles all player actions in the game.
"""
from game.player import add_item_to_inventory, damage_player, heal_player, move_player, remove_item_from_inventory
from game.world import change_location, get_available_locations, get_current_location, interact_with_location
from utils.random_events import trigger_random_event


def perform_action(player, world, action):
    """
    Process player actions and execute the appropriate game logic.
    
    Args:
        player (dict): The player's state
        world (dict): The game world state
        action (str): The action input by the player
    
    Returns:
        None
    """
    # Split the action into command and target
    parts = action.strip().split(" ", 1)
    command = parts[0]
    target = parts[1] if len(parts) > 1 else ""
    
    # Process different commands
    if command == "go" or command == "move":
        handle_movement(player, world, target)
    elif command == "look" or command == "examine":
        handle_look(world, target)
    elif command == "take" or command == "pickup":
        handle_take(player, world, target)
    elif command == "drop":
        handle_drop(player, target)
    elif command == "inventory" or command == "inv":
        handle_inventory(player)
    elif command == "interact" or command == "use":
        handle_interact(player, world, target)
    elif command == "status":
        handle_status(player)
    elif command == "locations":
        handle_locations(world)
    else:
        print(f"I don't understand '{action}'. Type 'help' for a list of commands.")
    
    # Chance for random events after each action
    trigger_random_event(player, world)


def handle_movement(player, world, location):
    """Handle player movement between locations."""
    if not location:
        print("Where do you want to go? Available locations:")
        for loc in get_available_locations(world):
            print(f"- {loc}")
        return
    
    if change_location(world, location):
        move_player(player, location)
    else:
        print(f"You can't go to {location} from here.")
        print("Available locations:")
        for loc in get_available_locations(world):
            print(f"- {loc}")


def handle_look(world, target):
    """Handle examining the surroundings or specific items."""
    current_location = get_current_location(world)
    
    if not target or target == "around":
        # Look at the current location
        print(world["locations"][current_location]["description"])
        print("\nYou can see:")
        for item in world["locations"][current_location]["items"]:
            print(f"- {item}")
        return
    
    # Look at a specific item in the location
    if target in world["locations"][current_location]["items"]:
        # In a full implementation, items would have descriptions
        print(f"You see a {target}. It looks useful.")
    else:
        print(f"You don't see any {target} here.")


def handle_take(player, world, item):
    """Handle picking up items."""
    if not item:
        print("What do you want to take?")
        return
    
    current_location = get_current_location(world)
    if item in world["locations"][current_location]["items"]:
        add_item_to_inventory(player, item)
        world["locations"][current_location]["items"].remove(item)
    else:
        print(f"There is no {item} here to take.")


def handle_drop(player, item):
    """Handle dropping items from inventory."""
    if not item:
        print("What do you want to drop?")
        return
    
    if remove_item_from_inventory(player, item):
        # Add the item to the current location
        current_location = player["location"]
        world["locations"][current_location]["items"].append(item)


def handle_inventory(player):
    """Display the player's inventory."""
    if not player["inventory"]:
        print("Your inventory is empty.")
    else:
        print("Your inventory contains:")
        for item in player["inventory"]:
            print(f"- {item}")


def handle_interact(player, world, target):
    """Handle interaction with the current location or items."""
    if not target:
        # Interact with the location itself
        interact_with_location(world, player)
    elif target in player["inventory"]:
        # Use an item from inventory
        print(f"You use the {target}.")
        # In a full implementation, items would have effects when used
    else:
        print(f"You don't have a {target} to use.")


def handle_status(player):
    """Display detailed player status."""
    print(f"Name: {player['name']}")
    print(f"Health: {player['health']}/100")
    print(f"Gold: {player['gold']}")
    print(f"Current location: {player['location']}")
    handle_inventory(player)


def handle_locations(world):
    """Show available locations to travel to."""
    current_location = get_current_location(world)
    print(f"You are currently in {current_location}.")
    print("You can travel to:")
    for location in get_available_locations(world):
        print(f"- {location}")

