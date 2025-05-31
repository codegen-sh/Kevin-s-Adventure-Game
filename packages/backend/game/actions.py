from game.items import perform_item_action, get_item_description
from game.player import move_player, add_item_to_inventory, remove_item_from_inventory
from game.world import get_current_location, get_available_locations, change_location
from locations.village import visit_village
from locations.forest import enter_forest
from locations.mountain import climb_mountain
from locations.cave import explore_cave

def perform_action(player, world, action):
    """
    Perform a game action based on user input.
    
    Args:
    player (dict): The player's current state
    world (dict): The game world state
    action (str): The action to perform
    
    Returns:
    str: Result message of the action
    """
    action = action.lower().strip()
    current_location = get_current_location(world)
    
    # Movement actions
    if action.startswith("go ") or action.startswith("move ") or action.startswith("travel "):
        destination = action.split()[-1].title()
        available_locations = get_available_locations(world, current_location)
        
        if destination in available_locations:
            change_location(world, destination)
            move_player(player, destination)
            
            # Trigger location-specific events
            if destination == "Village":
                visit_village(player, world)
            elif destination == "Forest":
                enter_forest(player, world)
            elif destination == "Mountain":
                climb_mountain(player, world)
            elif destination == "Cave":
                explore_cave(player, world)
            
            print(f"You travel to the {destination}.")
        else:
            print(f"You can't go to {destination} from here.")
            print(f"Available locations: {', '.join(available_locations)}")
    
    # Item actions
    elif action.startswith("take ") or action.startswith("pick up ") or action.startswith("get "):
        item_name = action.replace("take ", "").replace("pick up ", "").replace("get ", "")
        location_items = world["locations"][current_location].get("items", [])
        
        if item_name in location_items:
            add_item_to_inventory(player, item_name)
            world["locations"][current_location]["items"].remove(item_name)
        else:
            print(f"There is no {item_name} here.")
    
    elif action.startswith("use ") or action.startswith("consume "):
        item_name = action.replace("use ", "").replace("consume ", "")
        if item_name in player.get("inventory", []):
            perform_item_action(player, world, item_name)
        else:
            print(f"You don't have {item_name} in your inventory.")
    
    elif action.startswith("drop "):
        item_name = action.replace("drop ", "")
        if item_name in player.get("inventory", []):
            remove_item_from_inventory(player, item_name)
            world["locations"][current_location].setdefault("items", []).append(item_name)
            print(f"You dropped {item_name}.")
        else:
            print(f"You don't have {item_name} in your inventory.")
    
    # Information actions
    elif action in ["look", "look around", "examine"]:
        location_info = world["locations"][current_location]
        print(f"You are in the {current_location}.")
        print(location_info["description"])
        
        if location_info.get("items"):
            print(f"You see: {', '.join(location_info['items'])}")
        
        available_locations = get_available_locations(world, current_location)
        if available_locations:
            print(f"You can go to: {', '.join(available_locations)}")
    
    elif action in ["inventory", "inv", "items"]:
        inventory = player.get("inventory", [])
        if inventory:
            print(f"Your inventory contains: {', '.join(inventory)}")
            for item in inventory:
                print(f"  - {item}: {get_item_description(item)}")
        else:
            print("Your inventory is empty.")
    
    elif action in ["status", "stats", "health"]:
        print(f"Player: {player['name']}")
        print(f"Health: {player['health']}")
        print(f"Location: {player['location']}")
        print(f"Gold: {player.get('gold', 0)}")
    
    # Unknown action
    else:
        print(f"I don't understand '{action}'. Type 'help' for available commands.")

