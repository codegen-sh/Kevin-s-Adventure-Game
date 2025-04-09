from game.player import add_to_inventory, drop_from_inventory, get_player_status, use_item
from game.world import get_current_location, move_to_location
from locations.cave import explore_cave
from locations.forest import explore_forest
from locations.mountain import explore_mountain
from locations.village import explore_village
from utils.text_formatting import print_event

def perform_action(player, world, action):
    """Process player actions and update game state accordingly."""
    action_parts = action.split()
    command = action_parts[0] if action_parts else ""
    
    # Handle movement
    if command == "move":
        if len(action_parts) > 1:
            destination = action_parts[1]
            move_to_location(world, destination)
        else:
            print("Where do you want to move to?")
    
    # Handle looking around
    elif command == "look":
        location = get_current_location(world)
        location_info = world["locations"].get(location, {})
        print(location_info.get("description", "There's nothing special here."))
        
        # Show available items
        items = location_info.get("items", [])
        if items:
            print(f"You see: {', '.join(items)}")
        
        # Show available exits
        exits = location_info.get("exits", [])
        if exits:
            print(f"You can go to: {', '.join(exits)}")
    
    # Handle inventory
    elif command == "inventory":
        inventory = player.get("inventory", [])
        if inventory:
            print(f"You are carrying: {', '.join(inventory)}")
        else:
            print("Your inventory is empty.")
    
    # Handle picking up items
    elif command == "pickup":
        if len(action_parts) > 1:
            item = action_parts[1]
            location = get_current_location(world)
            location_info = world["locations"].get(location, {})
            items = location_info.get("items", [])
            
            if item in items:
                add_to_inventory(player, item)
                location_info["items"].remove(item)
                print(f"You picked up the {item}.")
            else:
                print(f"There is no {item} here.")
        else:
            print("What do you want to pick up?")
    
    # Handle dropping items
    elif command == "drop":
        if len(action_parts) > 1:
            item = action_parts[1]
            if drop_from_inventory(player, item):
                location = get_current_location(world)
                location_info = world["locations"].get(location, {})
                if "items" not in location_info:
                    location_info["items"] = []
                location_info["items"].append(item)
                print(f"You dropped the {item}.")
            else:
                print(f"You don't have a {item} in your inventory.")
        else:
            print("What do you want to drop?")
    
    # Handle using items
    elif command == "use":
        if len(action_parts) > 1:
            item = action_parts[1]
            use_item(player, world, item)
        else:
            print("What do you want to use?")
    
    # Handle examining items
    elif command == "examine":
        if len(action_parts) > 1:
            item = action_parts[1]
            inventory = player.get("inventory", [])
            
            if item in inventory:
                # Get item description from world items
                item_info = world.get("items", {}).get(item, {})
                description = item_info.get("description", f"A {item}. Nothing special about it.")
                print(description)
            else:
                print(f"You don't have a {item} in your inventory.")
        else:
            print("What do you want to examine?")
    
    # Handle status check
    elif command == "status":
        print(get_player_status(player))
    
    # Handle interaction with current location
    elif command == "interact":
        location = get_current_location(world)
        
        if location == "village":
            explore_village(world, player)
        elif location == "forest":
            explore_forest(world, player)
        elif location == "cave":
            explore_cave(world, player)
        elif location == "mountain":
            explore_mountain(world, player)
        else:
            print("There's nothing to interact with here.")
    
    # Handle unknown commands
    else:
        print(f"I don't understand '{action}'. Type 'help' for a list of commands.")
