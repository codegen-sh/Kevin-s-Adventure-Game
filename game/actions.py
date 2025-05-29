from game.world import (
    get_current_location, 
    get_available_locations, 
    change_location, 
    interact_with_location,
    get_location_description
)
from game.player import (
    get_player_status,
    add_item_to_inventory,
    remove_item_from_inventory,
    use_item
)
from utils.text_formatting import print_help


def perform_action(player, world, action):
    """
    Main action handler that processes player input and executes corresponding actions.
    """
    action = action.lower().strip()
    
    # Movement actions
    if action in ["go", "move", "travel"]:
        handle_movement_menu(player, world)
    elif action.startswith("go "):
        destination = action[3:].title()
        handle_movement(player, world, destination)
    elif action in ["north", "n"]:
        handle_directional_movement(player, world, "north")
    elif action in ["south", "s"]:
        handle_directional_movement(player, world, "south")
    elif action in ["east", "e"]:
        handle_directional_movement(player, world, "east")
    elif action in ["west", "w"]:
        handle_directional_movement(player, world, "west")
    
    # Location interaction
    elif action in ["explore", "interact", "look around", "examine"]:
        interact_with_location(world, player)
    elif action in ["look", "l", "describe"]:
        describe_current_location(world)
    
    # Inventory actions
    elif action in ["inventory", "inv", "i"]:
        show_inventory(player)
    elif action.startswith("use "):
        item = action[4:]
        handle_use_item(player, world, item)
    elif action.startswith("drop "):
        item = action[5:]
        handle_drop_item(player, world, item)
    
    # Status and help
    elif action in ["status", "stats", "health"]:
        print(get_player_status(player))
    elif action in ["help", "h", "?"]:
        print_help()
    elif action in ["locations", "map"]:
        show_available_locations(world)
    
    # Default case
    else:
        print(f"I don't understand '{action}'. Type 'help' for available commands.")


def handle_movement_menu(player, world):
    """Display available locations and let player choose where to go."""
    available_locations = get_available_locations(world)
    current_location = get_current_location(world)
    
    print(f"\nYou are currently in: {current_location}")
    print("Available locations:")
    for i, location in enumerate(available_locations, 1):
        print(f"{i}. {location}")
    
    try:
        choice = int(input("Where would you like to go? (Enter number): "))
        if 1 <= choice <= len(available_locations):
            destination = available_locations[choice - 1]
            handle_movement(player, world, destination)
        else:
            print("Invalid choice.")
    except ValueError:
        print("Please enter a valid number.")


def handle_movement(player, world, destination):
    """Handle movement to a specific location."""
    if change_location(world, destination):
        player["location"] = destination
        print(f"\nYou travel to {destination}.")
        describe_current_location(world)
    else:
        print(f"You can't go to {destination} from here.")


def handle_directional_movement(player, world, direction):
    """Handle directional movement (north, south, east, west)."""
    # This is a simplified directional system
    # In a more complex game, you'd have a proper coordinate system
    available_locations = get_available_locations(world)
    
    direction_map = {
        "north": 0,
        "south": 1, 
        "east": 2,
        "west": 3
    }
    
    if direction in direction_map and available_locations:
        index = direction_map[direction] % len(available_locations)
        destination = available_locations[index]
        handle_movement(player, world, destination)
    else:
        print(f"You can't go {direction} from here.")


def describe_current_location(world):
    """Describe the current location to the player."""
    current_location = get_current_location(world)
    description = get_location_description(world, current_location)
    print(f"\n{description}")
    
    # Show available exits
    available_locations = get_available_locations(world)
    if available_locations:
        print(f"You can go to: {', '.join(available_locations)}")


def show_inventory(player):
    """Display the player's inventory."""
    inventory = player.get("inventory", [])
    if inventory:
        print("Your inventory contains:")
        for item in inventory:
            print(f"- {item}")
    else:
        print("Your inventory is empty.")


def handle_use_item(player, world, item):
    """Handle using an item from inventory."""
    if item in player.get("inventory", []):
        # Import here to avoid circular imports
        from game.player import use_item
        use_item(player, item)
    else:
        print(f"You don't have '{item}' in your inventory.")


def handle_drop_item(player, world, item):
    """Handle dropping an item from inventory."""
    if item in player.get("inventory", []):
        remove_item_from_inventory(player, item)
        
        # Add item to current location
        current_location = get_current_location(world)
        if "items" not in world["locations"][current_location]:
            world["locations"][current_location]["items"] = []
        world["locations"][current_location]["items"].append(item)
        
        print(f"You dropped '{item}' here.")
    else:
        print(f"You don't have '{item}' to drop.")


def show_available_locations(world):
    """Show all available locations from current position."""
    current_location = get_current_location(world)
    available_locations = get_available_locations(world)
    
    print(f"\nFrom {current_location}, you can travel to:")
    for location in available_locations:
        print(f"- {location}")

