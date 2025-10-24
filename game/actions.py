"""
Game actions for Kevin's Adventure Game.
"""

from game.player import move_player, add_item_to_inventory, remove_item_from_inventory
from game.world import change_location, get_available_locations, interact_with_location


def perform_action(player, world, action):
    """
    Perform a game action based on user input.
    
    Args:
        player: Player data dictionary
        world: World data dictionary
        action: Action string from user input
    """
    action = action.lower().strip()
    
    # Movement actions
    if action in ["go", "move", "travel"]:
        available_locations = get_available_locations(world)
        print(f"Available locations: {', '.join(available_locations)}")
        destination = input("Where would you like to go? ").title()
        
        if change_location(world, destination):
            move_player(player, destination)
        else:
            print(f"You can't go to {destination} from here.")
    
    # Location-specific actions
    elif action in ["explore", "look", "examine"]:
        interact_with_location(world, player)
    
    # Inventory actions
    elif action in ["inventory", "inv", "items"]:
        if player["inventory"]:
            print(f"Inventory: {', '.join(player['inventory'])}")
        else:
            print("Your inventory is empty.")
    
    elif action.startswith("take ") or action.startswith("pick up "):
        item_name = action.replace("take ", "").replace("pick up ", "").strip()
        current_location = world["current_location"]
        available_items = world["locations"][current_location]["items"]
        
        if item_name in available_items:
            available_items.remove(item_name)
            add_item_to_inventory(player, item_name)
        else:
            print(f"There is no {item_name} here.")
    
    elif action.startswith("drop "):
        item_name = action.replace("drop ", "").strip()
        if remove_item_from_inventory(player, item_name):
            current_location = world["current_location"]
            world["locations"][current_location]["items"].append(item_name)
    
    # Status actions
    elif action in ["status", "health", "stats"]:
        print(f"Health: {player['health']}")
        print(f"Gold: {player['gold']}")
        print(f"Location: {player['location']}")
        if player["inventory"]:
            print(f"Inventory: {', '.join(player['inventory'])}")
        else:
            print("Inventory: Empty")
    
    # Unknown action
    else:
        print(f"I don't understand '{action}'. Type 'help' for available commands.")

