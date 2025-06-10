from game.player import (add_item_to_inventory, damage_player, heal_player,
                      move_player, remove_item_from_inventory)
from game.world import (change_location, get_all_locations, get_current_location,
                      get_location_description, interact_with_location,
                      is_location_accessible)
from utils.random_events import apply_random_event
from utils.text_formatting import print_event


def perform_action(player, world, action):
    """
    Process player actions and update game state accordingly.
    
    Args:
        player (dict): The player's state
        world (dict): The world state
        action (str): The action to perform
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
    elif command == "pickup" or command == "get":
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
        print(f"I don't understand '{action}'. Type 'help' for a list of commands.")
    
    # Random events have a chance to occur after any action
    if command not in ["look", "inventory", "examine", "status", "help"]:
        if random.random() < 0.2:  # 20% chance of a random event
            apply_random_event(player, world)


def handle_move(player, world, args):
    """Handle player movement between locations."""
    if not args:
        print("Move where? Available locations:")
        available_locations = get_available_locations(world)
        for location in available_locations:
            print(f"- {location}")
        return
    
    destination = args[0].capitalize()
    
    # Check if the destination is valid
    if not is_location_accessible(world, destination):
        print(f"You can't go to {destination} from here.")
        print("Available locations:")
        available_locations = get_available_locations(world)
        for location in available_locations:
            print(f"- {location}")
        return
    
    # Move the player
    if change_location(world, destination):
        move_player(player, destination)
        print_event(f"You have arrived at {destination}.")
        print(get_location_description(world, destination))
    else:
        print(f"You can't go to {destination} from here.")


def handle_look(player, world):
    """Handle the look command to examine surroundings."""
    current_location = get_current_location(world)
    print(f"You are in the {current_location}.")
    print(get_location_description(world, current_location))
    
    # Show available connections
    print("\nFrom here, you can go to:")
    available_locations = get_available_locations(world)
    for location in available_locations:
        print(f"- {location}")
    
    # Show visible items
    location_items = world["locations"][current_location].get("items", [])
    if location_items:
        print("\nYou can see:")
        for item in location_items:
            print(f"- {item}")
    else:
        print("\nThere are no items visible here.")


def handle_inventory(player):
    """Handle the inventory command to show player's items."""
    if player["inventory"]:
        print("You are carrying:")
        for item in player["inventory"]:
            print(f"- {item}")
    else:
        print("Your inventory is empty.")


def handle_pickup(player, world, args):
    """Handle picking up items from the current location."""
    if not args:
        print("Pick up what?")
        return
    
    item = args[0].lower()
    current_location = get_current_location(world)
    location_items = world["locations"][current_location].get("items", [])
    
    if item in location_items:
        add_item_to_inventory(player, item)
        location_items.remove(item)
        print(f"You picked up the {item}.")
    else:
        print(f"There is no {item} here.")


def handle_drop(player, args):
    """Handle dropping items from inventory."""
    if not args:
        print("Drop what?")
        return
    
    item = args[0].lower()
    if remove_item_from_inventory(player, item):
        current_location = get_current_location(player)
        world["locations"][current_location]["items"].append(item)
        print(f"You dropped the {item}.")


def handle_use(player, world, args):
    """Handle using items from inventory."""
    if not args:
        print("Use what?")
        return
    
    item = args[0].lower()
    if item not in player["inventory"]:
        print(f"You don't have a {item} in your inventory.")
        return
    
    # Handle different items
    if item == "potion" or item == "healing_potion":
        heal_player(player, 20)
        player["inventory"].remove(item)
        print("You used the healing potion and recovered 20 health.")
    elif item == "map":
        print("You consult your map.")
        print("Available locations in the world:")
        for location in get_all_locations(world):
            print(f"- {location}")
    elif item == "torch":
        print("You light the torch, illuminating the area around you.")
        # Could add special effects in dark areas
    elif item == "berries" or item == "mushrooms" or item == "bread":
        heal_player(player, 10)
        player["inventory"].remove(item)
        print(f"You ate the {item} and recovered 10 health.")
    else:
        print(f"You're not sure how to use the {item}.")


def handle_examine(player, world, args):
    """Handle examining items or surroundings."""
    if not args:
        print("Examine what?")
        return
    
    item = args[0].lower()
    
    # Item descriptions
    item_descriptions = {
        "map": "A weathered map showing the major locations in the area.",
        "bread": "A fresh loaf of bread. It smells delicious.",
        "stick": "A sturdy wooden stick. Could be useful for many things.",
        "berries": "Plump, juicy berries. They look safe to eat.",
        "torch": "A wooden torch that can be lit to provide light in dark places.",
        "gemstone": "A beautiful, sparkling gemstone. It might be valuable.",
        "rope": "A coil of strong rope. Useful for climbing or tying things.",
        "pickaxe": "A sturdy pickaxe for mining or breaking rocks.",
        "mushrooms": "Edible mushrooms that can restore some health.",
        "mysterious_potion": "A strange, glowing potion. Who knows what it does?",
        "ancient_artifact": "An ancient artifact with mysterious symbols carved into it."
    }
    
    if item in player["inventory"]:
        if item in item_descriptions:
            print(f"{item.capitalize()}: {item_descriptions[item]}")
        else:
            print(f"It's a {item}. Nothing special about it.")
    elif item in world["locations"][get_current_location(world)].get("items", []):
        if item in item_descriptions:
            print(f"{item.capitalize()}: {item_descriptions[item]}")
        else:
            print(f"It's a {item}. Nothing special about it.")
    else:
        print(f"You don't see a {item} here.")


def handle_status(player):
    """Handle the status command to show player stats."""
    print(f"Name: {player['name']}")
    print(f"Health: {player['health']}/100")
    print(f"Gold: {player['gold']}")
    print(f"Current location: {player['location']}")
    
    if player["inventory"]:
        print("Inventory:")
        for item in player["inventory"]:
            print(f"- {item}")
    else:
        print("Inventory: empty")


def handle_interact(player, world):
    """Handle interaction with the current location."""
    interact_with_location(world, player)


# Import at the end to avoid circular imports
import random
from game.world import get_available_locations

