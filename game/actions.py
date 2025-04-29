from game.player import add_item_to_inventory, damage_player, heal_player, move_player, remove_item_from_inventory
from game.world import change_location, get_available_locations, get_current_location, interact_with_location
from utils.random_events import trigger_random_event

def perform_action(player, world, action):
    """
    Process player actions and update game state accordingly.
    
    Args:
        player (dict): The player's state
        world (dict): The world state
        action (str): The action input by the player
    """
    # Split the action into command and target
    parts = action.split()
    command = parts[0] if parts else ""
    target = " ".join(parts[1:]) if len(parts) > 1 else ""
    
    # Handle movement
    if command == "go" or command == "move":
        if not target:
            print("Where do you want to go?")
            return
            
        available_locations = get_available_locations(world)
        if target.capitalize() in available_locations:
            if change_location(world, target.capitalize()):
                move_player(player, target.capitalize())
                # Chance for random event when moving
                trigger_random_event(player, world)
            else:
                print(f"You can't go to {target} from here.")
        else:
            print(f"You can't go to {target} from here. Available locations: {', '.join(available_locations)}")
    
    # Handle looking around
    elif command == "look":
        current_location = get_current_location(world)
        location_data = world["locations"][current_location]
        print(f"\n{location_data['description']}")
        
        if location_data["items"]:
            print(f"You can see: {', '.join(location_data['items'])}")
        
        print(f"From here, you can go to: {', '.join(location_data['connections'])}")
    
    # Handle picking up items
    elif command == "take" or command == "pickup":
        if not target:
            print("What do you want to take?")
            return
            
        current_location = get_current_location(world)
        location_items = world["locations"][current_location]["items"]
        
        if target in location_items:
            add_item_to_inventory(player, target)
            location_items.remove(target)
        else:
            print(f"There is no {target} here to take.")
    
    # Handle dropping items
    elif command == "drop":
        if not target:
            print("What do you want to drop?")
            return
            
        if remove_item_from_inventory(player, target):
            current_location = get_current_location(world)
            world["locations"][current_location]["items"].append(target)
    
    # Handle interaction with current location
    elif command == "interact" or command == "explore":
        interact_with_location(world, player)
    
    # Handle using items
    elif command == "use":
        if not target:
            print("What do you want to use?")
            return
            
        if target in player["inventory"]:
            if target == "bread" or target == "berries":
                heal_player(player, 20)
                remove_item_from_inventory(player, target)
            elif target == "torch" and get_current_location(world) == "Cave":
                print("The torch illuminates the dark cave, revealing hidden passages.")
            elif target == "map":
                print("The map shows all locations: Village, Forest, Cave, Mountain")
            else:
                print(f"You're not sure how to use the {target} here.")
        else:
            print(f"You don't have {target} in your inventory.")
    
    # Handle unknown commands
    else:
        print("I don't understand that command. Type 'help' for a list of commands.")

