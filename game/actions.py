"""
Game actions module - handles all player actions and commands.
"""
from typing import Dict, Any, Tuple
import random

from game.player import (
    get_player_status, 
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
from game.items import (
    use_item,
    get_item_description,
    get_available_items,
    transfer_item
)
from locations.forest import enter_forest, explore_forest
from locations.mountain import climb_mountain
from locations.village import visit_village
from utils.random_events import apply_random_event
from utils.text_formatting import print_colored


def perform_action(player: Dict[str, Any], world: Dict[str, Any], action: str) -> bool:
    """
    Main action dispatcher that handles all player commands.
    
    Args:
        player: Player state dictionary
        world: World state dictionary  
        action: Action string from user input
        
    Returns:
        bool: True if action was valid, False otherwise
    """
    action = action.lower().strip()
    
    # Movement actions
    if action in ["go", "move", "travel", "walk"]:
        return handle_movement(player, world)
    elif action.startswith("go ") or action.startswith("move ") or action.startswith("travel "):
        destination = action.split(" ", 1)[1]
        return handle_movement_to(player, world, destination)
    
    # Inventory actions
    elif action in ["inventory", "inv", "i"]:
        return show_inventory(player)
    elif action.startswith("use "):
        item = action.split(" ", 1)[1]
        return handle_use_item(player, world, item)
    elif action.startswith("drop "):
        item = action.split(" ", 1)[1]
        return handle_drop_item(player, world, item)
    elif action.startswith("take ") or action.startswith("get ") or action.startswith("pick up "):
        item = action.split(" ", 1)[1] if " " in action else ""
        return handle_take_item(player, world, item)
    
    # Examination actions
    elif action in ["look", "examine", "l"]:
        return handle_look(player, world)
    elif action.startswith("look ") or action.startswith("examine "):
        target = action.split(" ", 1)[1]
        return handle_examine(player, world, target)
    
    # Location-specific actions
    elif action in ["explore", "search"]:
        return handle_explore(player, world)
    elif action in ["interact", "talk"]:
        return handle_interact(player, world)
    
    # Status actions
    elif action in ["status", "stats", "health"]:
        print(get_player_status(player))
        return True
    elif action in ["location", "where", "where am i"]:
        current_location = get_current_location(world)
        print(f"You are currently in the {current_location}.")
        print(get_location_description(world, current_location))
        return True
    
    # Game actions
    elif action in ["wait", "rest"]:
        return handle_wait(player, world)
    
    else:
        print_colored("I don't understand that command. Type 'help' for available commands.", "red")
        return False


def handle_movement(player: Dict[str, Any], world: Dict[str, Any]) -> bool:
    """Handle movement when no specific destination is given."""
    available_locations = get_available_locations(world)
    current_location = get_current_location(world)
    
    print("Where would you like to go?")
    for i, location in enumerate(available_locations, 1):
        if location != current_location:
            print(f"{i}. {location}")
    
    try:
        choice = input("Enter your choice (number or name): ").strip()
        if choice.isdigit():
            choice_idx = int(choice) - 1
            available_locs = [loc for loc in available_locations if loc != current_location]
            if 0 <= choice_idx < len(available_locs):
                destination = available_locs[choice_idx]
            else:
                print("Invalid choice.")
                return False
        else:
            destination = choice
        
        return handle_movement_to(player, world, destination)
    except (ValueError, IndexError):
        print("Invalid choice.")
        return False


def handle_movement_to(player: Dict[str, Any], world: Dict[str, Any], destination: str) -> bool:
    """Handle movement to a specific destination."""
    destination = destination.title()  # Normalize case
    current_location = get_current_location(world)
    
    if destination == current_location:
        print("You are already there!")
        return True
    
    if not is_location_accessible(world, destination):
        print(f"You cannot go to {destination} from here.")
        return False
    
    # Move the player
    change_location(world, destination)
    move_player(player, destination)
    
    print(f"You travel to the {destination}.")
    print(get_location_description(world, destination))
    
    # Trigger location-specific entry events
    if destination == "Forest":
        enter_forest(world, player)
    elif destination == "Village":
        visit_village(world, player)
    elif destination == "Mountain":
        climb_mountain(world, player)
    
    # Random event chance
    if random.random() < 0.3:  # 30% chance
        apply_random_event(player, world)
    
    return True


def show_inventory(player: Dict[str, Any]) -> bool:
    """Display player's inventory."""
    inventory = player.get("inventory", [])
    gold = player.get("gold", 0)
    
    print("\n--- Your Inventory ---")
    if inventory:
        for item in inventory:
            description = get_item_description(item)
            print(f"- {item}: {description}")
    else:
        print("Your inventory is empty.")
    
    print(f"Gold: {gold}")
    return True


def handle_use_item(player: Dict[str, Any], world: Dict[str, Any], item: str) -> bool:
    """Handle using an item."""
    item = item.lower().replace(" ", "_")  # Normalize item name
    
    if item not in player.get("inventory", []):
        print(f"You don't have {item} in your inventory.")
        return False
    
    return use_item(player, item, world)


def handle_drop_item(player: Dict[str, Any], world: Dict[str, Any], item: str) -> bool:
    """Handle dropping an item."""
    item = item.lower().replace(" ", "_")  # Normalize item name
    
    if transfer_item(player, world, item, from_inventory_to_world=True):
        print(f"You dropped the {item}.")
        return True
    else:
        print(f"You don't have {item} to drop.")
        return False


def handle_take_item(player: Dict[str, Any], world: Dict[str, Any], item: str) -> bool:
    """Handle taking an item."""
    if not item:
        # Show available items
        current_location = get_current_location(world)
        available_items = get_available_items(world, current_location)
        
        if available_items:
            print("Available items here:")
            for available_item in available_items:
                description = get_item_description(available_item)
                print(f"- {available_item}: {description}")
        else:
            print("There are no items here to take.")
        return True
    
    item = item.lower().replace(" ", "_")  # Normalize item name
    
    if transfer_item(player, world, item, from_inventory_to_world=False):
        print(f"You picked up the {item}.")
        return True
    else:
        print(f"There is no {item} here to take.")
        return False


def handle_look(player: Dict[str, Any], world: Dict[str, Any]) -> bool:
    """Handle looking around the current location."""
    current_location = get_current_location(world)
    print(f"\n--- {current_location} ---")
    print(get_location_description(world, current_location))
    
    # Show available items
    available_items = get_available_items(world, current_location)
    if available_items:
        print("\nItems you can see:")
        for item in available_items:
            description = get_item_description(item)
            print(f"- {item}: {description}")
    
    # Show available exits
    available_locations = get_available_locations(world)
    exits = [loc for loc in available_locations if loc != current_location]
    if exits:
        print(f"\nYou can go to: {', '.join(exits)}")
    
    return True


def handle_examine(player: Dict[str, Any], world: Dict[str, Any], target: str) -> bool:
    """Handle examining a specific target."""
    target = target.lower().replace(" ", "_")
    current_location = get_current_location(world)
    
    # Check if it's an item in inventory
    if target in player.get("inventory", []):
        description = get_item_description(target)
        print(f"You examine your {target}: {description}")
        return True
    
    # Check if it's an item in the current location
    available_items = get_available_items(world, current_location)
    if target in available_items:
        description = get_item_description(target)
        print(f"You examine the {target}: {description}")
        return True
    
    # Check if it's the current location
    if target in current_location.lower():
        print(get_location_description(world, current_location))
        return True
    
    print(f"You don't see any {target} here.")
    return False


def handle_explore(player: Dict[str, Any], world: Dict[str, Any]) -> bool:
    """Handle exploring the current location."""
    current_location = get_current_location(world)
    
    print(f"You explore the {current_location} more thoroughly...")
    
    # Location-specific exploration
    if current_location == "Forest":
        return explore_forest(world, player)
    elif current_location == "Mountain":
        print("You search the rocky terrain for anything interesting.")
        # Random chance to find something
        if random.random() < 0.4:
            apply_random_event(player, world)
    elif current_location == "Village":
        print("You walk around the village, observing the daily life of its inhabitants.")
        if random.random() < 0.3:
            apply_random_event(player, world)
    else:
        print("You don't find anything particularly interesting.")
    
    return True


def handle_interact(player: Dict[str, Any], world: Dict[str, Any]) -> bool:
    """Handle interacting with the current location."""
    return interact_with_location(world, player)


def handle_wait(player: Dict[str, Any], world: Dict[str, Any]) -> bool:
    """Handle waiting/resting."""
    print("You take a moment to rest and gather your thoughts.")
    heal_player(player, 5)  # Small health recovery
    
    # Random event chance while waiting
    if random.random() < 0.2:  # 20% chance
        apply_random_event(player, world)
    
    return True

