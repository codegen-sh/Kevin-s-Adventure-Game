from game.items import get_available_items, get_item_description, transfer_item, use_item
from game.player import add_item_to_inventory, get_player_status, move_player, remove_item_from_inventory
from game.world import (
    change_location,
    get_available_locations,
    get_current_location,
    get_location_description,
    interact_with_location,
)
from utils.text_formatting import print_help


def perform_action(player, world, action):
    """
    Process player actions and update the game state accordingly.
    
    Args:
        player (dict): The player's current state
        world (dict): The game world state
        action (str): The action to perform
    
    Returns:
        None
    """
    action_parts = action.split()
    command = action_parts[0] if action_parts else ""
    
    if command == "move":
        if len(action_parts) < 2:
            print("Move where? Available locations:")
            for location in get_available_locations(world):
                print(f"- {location}")
            return
        
        destination = action_parts[1].capitalize()
        if change_location(world, destination):
            move_player(player, destination)
        else:
            print(f"You can't go to {destination} from here.")
            print("Available locations:")
            for location in get_available_locations(world):
                print(f"- {location}")
    
    elif command == "look":
        current_location = get_current_location(world)
        print(get_location_description(world, current_location))
        print("You can see the following items here:")
        items = get_available_items(world, current_location)
        if items:
            for item in items:
                print(f"- {item}")
        else:
            print("There are no items here.")
        
        print("\nAvailable locations:")
        for location in get_available_locations(world):
            print(f"- {location}")
    
    elif command == "inventory":
        print(f"Your inventory: {player['inventory']}")
    
    elif command == "pickup" or command == "take":
        if len(action_parts) < 2:
            print("Pick up what?")
            return
        
        item = action_parts[1].lower()
        current_location = get_current_location(world)
        items = get_available_items(world, current_location)
        
        if item in items:
            transfer_item(player, world, item, from_inventory_to_world=False)
        else:
            print(f"There is no {item} here.")
    
    elif command == "drop":
        if len(action_parts) < 2:
            print("Drop what?")
            return
        
        item = action_parts[1].lower()
        transfer_item(player, world, item, from_inventory_to_world=True)
    
    elif command == "use":
        if len(action_parts) < 2:
            print("Use what?")
            return
        
        item = action_parts[1].lower()
        use_item(player, item, world)
    
    elif command == "examine":
        if len(action_parts) < 2:
            print("Examine what?")
            return
        
        item = action_parts[1].lower()
        if item in player["inventory"]:
            print(get_item_description(item))
        else:
            print(f"You don't have {item} in your inventory.")
    
    elif command == "status":
        print(get_player_status(player))
    
    elif command == "interact":
        interact_with_location(world, player)
    
    else:
        print(f"I don't understand '{action}'. Type 'help' for a list of commands.")

