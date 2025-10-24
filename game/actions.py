from game.items import get_available_items, transfer_item, use_item
from game.player import add_item_to_inventory, get_player_status
from game.world import (
    change_location,
    get_available_locations,
    get_current_location,
    get_location_description,
    interact_with_location,
)


def perform_action(player, world, action):
    """
    Process user actions and execute the corresponding game logic.
    
    Args:
        player: Player dictionary containing health, inventory, etc.
        world: World dictionary containing locations and game state
        action: String representing the user's action
    """
    action = action.lower().strip()
    
    # Movement actions
    if action.startswith("go ") or action.startswith("move ") or action.startswith("travel "):
        destination = action.split(" ", 1)[1] if " " in action else ""
        move_to_location(player, world, destination)
    
    # Location interaction
    elif action in ["explore", "interact", "look around", "examine"]:
        interact_with_location(world, player)
    
    # Inventory actions
    elif action.startswith("use "):
        item = action.split(" ", 1)[1] if " " in action else ""
        use_item_action(player, world, item)
    
    elif action.startswith("take ") or action.startswith("pick up ") or action.startswith("get "):
        item = action.replace("pick up ", "").replace("take ", "").replace("get ", "")
        take_item_action(player, world, item)
    
    elif action.startswith("drop "):
        item = action.split(" ", 1)[1] if " " in action else ""
        drop_item_action(player, world, item)
    
    # Information actions
    elif action in ["inventory", "inv", "items"]:
        show_inventory(player)
    
    elif action in ["status", "health", "stats"]:
        print(get_player_status(player))
    
    elif action in ["look", "describe", "where am i"]:
        describe_current_location(world)
    
    elif action in ["locations", "where can i go", "exits"]:
        show_available_locations(world)
    
    # Default case for unrecognized actions
    else:
        print(f"I don't understand '{action}'. Type 'help' for available commands.")


def move_to_location(player, world, destination):
    """Handle movement to a new location."""
    if not destination:
        print("Where would you like to go?")
        show_available_locations(world)
        return
    
    destination = destination.title()  # Capitalize first letter
    available_locations = get_available_locations(world)
    
    if destination in available_locations:
        if change_location(world, destination):
            player['location'] = destination
            print(f"You travel to the {destination}.")
            describe_current_location(world)
        else:
            print(f"You cannot travel to {destination} right now.")
    else:
        print(f"You cannot go to '{destination}' from here.")
        show_available_locations(world)


def use_item_action(player, world, item):
    """Handle using an item from inventory."""
    if not item:
        print("What would you like to use?")
        show_inventory(player)
        return
    
    if item in player['inventory']:
        use_item(player, item, world)
    else:
        print(f"You don't have '{item}' in your inventory.")


def take_item_action(player, world, item):
    """Handle taking an item from the current location."""
    if not item:
        print("What would you like to take?")
        show_available_items(world)
        return
    
    current_location = get_current_location(world)
    available_items = get_available_items(world, current_location)
    
    if item in available_items:
        if transfer_item(player, world, item, from_inventory_to_world=False):
            print(f"You picked up the {item}.")
        else:
            print(f"You couldn't pick up the {item}.")
    else:
        print(f"There is no '{item}' here to take.")
        if available_items:
            print("Available items:")
            for available_item in available_items:
                print(f"- {available_item}")


def drop_item_action(player, world, item):
    """Handle dropping an item from inventory."""
    if not item:
        print("What would you like to drop?")
        show_inventory(player)
        return
    
    if item in player['inventory']:
        if transfer_item(player, world, item, from_inventory_to_world=True):
            print(f"You dropped the {item}.")
        else:
            print(f"You couldn't drop the {item}.")
    else:
        print(f"You don't have '{item}' in your inventory.")


def show_inventory(player):
    """Display the player's inventory."""
    if player['inventory']:
        print("Your inventory contains:")
        for item in player['inventory']:
            print(f"- {item}")
    else:
        print("Your inventory is empty.")


def describe_current_location(world):
    """Describe the current location."""
    current_location = get_current_location(world)
    description = get_location_description(world, current_location)
    print(f"You are in the {current_location}.")
    print(description)
    
    # Show available items
    available_items = get_available_items(world, current_location)
    if available_items:
        print("You can see:")
        for item in available_items:
            print(f"- {item}")


def show_available_locations(world):
    """Show where the player can travel from current location."""
    available_locations = get_available_locations(world)
    if available_locations:
        print("You can travel to:")
        for location in available_locations:
            print(f"- {location}")
    else:
        print("There are no available destinations from here.")


def show_available_items(world):
    """Show items available in the current location."""
    current_location = get_current_location(world)
    available_items = get_available_items(world, current_location)
    if available_items:
        print("Available items here:")
        for item in available_items:
            print(f"- {item}")
    else:
        print("There are no items here.")

