"""
Game actions module for Kevin's Adventure Game.
Handles all player actions and game interactions.
"""

from game.player import (
    add_item_to_inventory, 
    remove_item_from_inventory, 
    move_player, 
    heal_player, 
    damage_player,
    get_player_status
)
from game.world import (
    get_current_location, 
    get_location_description, 
    get_available_locations, 
    change_location,
    interact_with_location,
    get_all_locations
)
from utils.text_formatting import format_inventory, print_help


def perform_action(player, world, action):
    """
    Main action handler that processes player commands.
    Returns a message describing the result of the action.
    """
    action = action.lower().strip()
    
    # Basic commands
    if action in ["help", "h"]:
        return handle_help()
    
    elif action in ["status", "stat", "s"]:
        return handle_status(player, world)
    
    elif action in ["inventory", "inv", "i"]:
        return handle_inventory(player)
    
    elif action in ["look", "l"]:
        return handle_look(player, world)
    
    elif action in ["quit", "exit", "q"]:
        return "Game ended. Thanks for playing!"
    
    # Movement commands
    elif action.startswith("go ") or action.startswith("move "):
        destination = action.split(" ", 1)[1] if " " in action else ""
        return handle_movement(player, world, destination)
    
    elif action in ["north", "south", "east", "west", "n", "s", "e", "w"]:
        return handle_direction_movement(player, world, action)
    
    # Item commands
    elif action.startswith("take ") or action.startswith("get ") or action.startswith("pick "):
        item = action.split(" ", 1)[1] if " " in action else ""
        return handle_take_item(player, world, item)
    
    elif action.startswith("drop ") or action.startswith("leave "):
        item = action.split(" ", 1)[1] if " " in action else ""
        return handle_drop_item(player, item)
    
    elif action.startswith("use "):
        item = action.split(" ", 1)[1] if " " in action else ""
        return handle_use_item(player, world, item)
    
    # Interaction commands
    elif action in ["explore", "search"]:
        return handle_explore(player, world)
    
    elif action in ["rest", "sleep"]:
        return handle_rest(player)
    
    elif action in ["talk", "speak"]:
        return handle_talk(player, world)
    
    elif action in ["shop", "buy", "trade"]:
        return handle_shop(player, world)
    
    # Location-specific actions
    elif action in ["hunt", "fish"]:
        return handle_hunt(player, world)
    
    elif action in ["gather", "collect"]:
        return handle_gather(player, world)
    
    elif action in ["climb", "mine"]:
        return handle_climb_mine(player, world)
    
    else:
        return f"I don't understand '{action}'. Type 'help' for available commands."


def handle_help():
    """Return help text"""
    return """
Available commands:
- help/h: Show this help message
- status/stat/s: Show your current status
- inventory/inv/i: Show your inventory
- look/l: Look around your current location
- go <location>: Move to a specific location
- take/get <item>: Pick up an item
- drop <item>: Drop an item from inventory
- use <item>: Use an item from inventory
- explore/search: Explore your current location
- rest: Rest to recover health
- talk: Talk to people in your location
- shop: Visit shops (if available)
- quit/exit: End the game

Location-specific actions:
- hunt/fish: Hunt for food (in appropriate locations)
- gather: Gather resources
- climb/mine: Climb or mine (in mountains)
"""


def handle_status(player, world):
    """Show player status and current location"""
    location = get_current_location(world)
    status = get_player_status(player)
    return f"Current location: {location}\n{status}"


def handle_inventory(player):
    """Show player inventory"""
    if not player['inventory']:
        return "Your inventory is empty."
    return f"Inventory: {format_inventory(player['inventory'])}"


def handle_look(player, world):
    """Look around current location"""
    location = get_current_location(world)
    description = get_location_description(world, location)
    available_locations = get_available_locations(world)
    
    result = f"You are in {location}.\n{description}\n"
    
    if available_locations:
        result += f"You can go to: {', '.join(available_locations)}\n"
    
    # Show available items in location
    location_data = world["locations"].get(location, {})
    items = location_data.get("items", [])
    if items:
        result += f"You see: {', '.join(items)}"
    
    return result


def handle_movement(player, world, destination):
    """Handle movement to a specific location"""
    if not destination:
        return "Where do you want to go? Available locations: " + ", ".join(get_available_locations(world))
    
    destination = destination.title()  # Capitalize first letter
    
    if change_location(world, destination):
        move_player(player, destination)
        return f"You moved to {destination}.\n" + handle_look(player, world)
    else:
        available = get_available_locations(world)
        return f"You can't go to {destination} from here. Available locations: {', '.join(available)}"


def handle_direction_movement(player, world, direction):
    """Handle directional movement (north, south, etc.)"""
    # Simple mapping - in a real game you'd have proper directional logic
    direction_map = {
        "north": "Mountain",
        "n": "Mountain", 
        "south": "Village",
        "s": "Village",
        "east": "Forest",
        "e": "Forest",
        "west": "Cave",
        "w": "Cave"
    }
    
    destination = direction_map.get(direction)
    if destination:
        return handle_movement(player, world, destination)
    else:
        return f"You can't go {direction} from here."


def handle_take_item(player, world, item):
    """Handle taking an item"""
    if not item:
        return "What do you want to take?"
    
    location = get_current_location(world)
    location_data = world["locations"].get(location, {})
    items = location_data.get("items", [])
    
    if item in items:
        add_item_to_inventory(player, item)
        items.remove(item)
        return f"You picked up: {item}"
    else:
        return f"There is no {item} here."


def handle_drop_item(player, item):
    """Handle dropping an item"""
    if not item:
        return "What do you want to drop?"
    
    if remove_item_from_inventory(player, item):
        return f"You dropped: {item}"
    else:
        return f"You don't have {item} in your inventory."


def handle_use_item(player, world, item):
    """Handle using an item"""
    if not item:
        return "What do you want to use?"
    
    if item not in player['inventory']:
        return f"You don't have {item} in your inventory."
    
    # Item-specific logic
    if item == "bread":
        heal_player(player, 20)
        remove_item_from_inventory(player, item)
        return "You ate the bread and feel refreshed!"
    
    elif item == "berries":
        heal_player(player, 10)
        remove_item_from_inventory(player, item)
        return "You ate the berries. They taste sweet!"
    
    elif item == "torch":
        return "The torch illuminates the area, revealing hidden passages."
    
    elif item == "map":
        locations = get_all_locations(world)
        return f"The map shows these locations: {', '.join(locations)}"
    
    elif item == "rope":
        return "The rope might be useful for climbing."
    
    elif item == "pickaxe":
        return "The pickaxe is perfect for mining."
    
    else:
        return f"You can't use {item} right now."


def handle_explore(player, world):
    """Handle exploration of current location"""
    location = get_current_location(world)
    
    # Use the existing location interaction system
    try:
        interact_with_location(world, player)
        return f"You explored {location} and discovered something interesting!"
    except Exception as e:
        return f"You explored {location} but found nothing special."


def handle_rest(player):
    """Handle resting to recover health"""
    if player['health'] >= 100:
        return "You are already at full health."
    
    heal_amount = min(30, 100 - player['health'])
    heal_player(player, heal_amount)
    return f"You rest and recover {heal_amount} health."


def handle_talk(player, world):
    """Handle talking to NPCs"""
    location = get_current_location(world)
    
    if location == "Village":
        return "The villagers greet you warmly and share local gossip."
    elif location == "Forest":
        return "You hear the whispers of forest spirits in the wind."
    elif location == "Mountain":
        return "An old hermit nods at you from his mountain cave."
    else:
        return "There's no one to talk to here."


def handle_shop(player, world):
    """Handle shopping interactions"""
    location = get_current_location(world)
    
    if location == "Village":
        return "The village shop offers: bread (10 gold), rope (25 gold), torch (15 gold)"
    else:
        return "There are no shops here."


def handle_hunt(player, world):
    """Handle hunting actions"""
    location = get_current_location(world)
    
    if location == "Forest":
        import random
        if random.random() < 0.6:  # 60% success rate
            add_item_to_inventory(player, "meat")
            return "You successfully hunted and caught some meat!"
        else:
            return "Your hunting attempt was unsuccessful."
    else:
        return "This is not a good place for hunting."


def handle_gather(player, world):
    """Handle gathering resources"""
    location = get_current_location(world)
    
    if location == "Forest":
        add_item_to_inventory(player, "berries")
        return "You gathered some berries from the forest."
    elif location == "Mountain":
        add_item_to_inventory(player, "stone")
        return "You gathered some stones from the mountain."
    else:
        return "There's nothing to gather here."


def handle_climb_mine(player, world):
    """Handle climbing or mining actions"""
    location = get_current_location(world)
    
    if location == "Mountain":
        if "pickaxe" in player['inventory']:
            add_item_to_inventory(player, "gemstone")
            return "You used your pickaxe to mine a beautiful gemstone!"
        else:
            return "You need a pickaxe to mine here."
    else:
        return "There's nothing to climb or mine here."

