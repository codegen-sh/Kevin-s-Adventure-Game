from game.items import get_available_items, get_item_description, transfer_item, use_item
from game.player import get_player_status, move_player
from game.world import (
    change_location,
    get_available_locations,
    get_current_location,
    get_location_description,
    interact_with_location,
)
from utils.random_events import apply_random_event


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
    # Split the action into command and target
    parts = action.split(" ", 1)
    command = parts[0]
    target = parts[1] if len(parts) > 1 else ""
    
    # Process the command
    if command == "move":
        if not target:
            print("Move where? Available locations:")
            for location in get_available_locations(world):
                print(f"- {location}")
        elif change_location(world, target):
            move_player(player, target)
            # Random event chance when moving
            if apply_random_event(player, world):
                pass  # Event was applied
        else:
            print(f"You can't move to {target} from here.")
    
    elif command == "look":
        current_location = get_current_location(world)
        print(get_location_description(world, current_location))
        items = get_available_items(world, current_location)
        if items:
            print(f"You see: {', '.join(items)}")
        print("Available exits:")
        for location in get_available_locations(world):
            print(f"- {location}")
    
    elif command == "inventory":
        print(f"Your inventory: {get_player_status(player)}")
    
    elif command == "pickup" or command == "take":
        if not target:
            print("What do you want to pick up?")
        else:
            current_location = get_current_location(world)
            items = get_available_items(world, current_location)
            if target in items:
                transfer_item(player, world, target, from_inventory_to_world=False)
            else:
                print(f"There is no {target} here.")
    
    elif command == "drop":
        if not target:
            print("What do you want to drop?")
        else:
            transfer_item(player, world, target, from_inventory_to_world=True)
    
    elif command == "use":
        if not target:
            print("What do you want to use?")
        else:
            use_item(player, target, world)
    
    elif command == "examine":
        if not target:
            print("What do you want to examine?")
        else:
            if target in player["inventory"]:
                print(get_item_description(target))
            else:
                current_location = get_current_location(world)
                items = get_available_items(world, current_location)
                if target in items:
                    print(get_item_description(target))
                else:
                    print(f"You don't see a {target} here.")
    
    elif command == "status":
        print(get_player_status(player))
    
    elif command == "interact":
        interact_with_location(world, player)
    
    else:
        print(f"I don't understand '{action}'. Type 'help' for a list of commands.")

