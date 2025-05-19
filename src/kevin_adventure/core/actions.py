"""
Actions module for Kevin's Adventure Game.
"""
from typing import Dict, List, Optional

from kevin_adventure.core.player import Player
from kevin_adventure.core.world import World
from kevin_adventure.items.item_manager import get_item_description, use_item


def perform_action(player: Player, world: World, action: str) -> None:
    """
    Perform an action based on user input.

    Args:
        player: The player performing the action
        world: The game world
        action: The action to perform
    """
    action_parts = action.split()
    command = action_parts[0] if action_parts else ""
    
    if command == "move":
        if len(action_parts) > 1:
            location = " ".join(action_parts[1:])
            if world.is_location_accessible(location):
                world.change_location(location)
                player.move(location)
            else:
                print(f"You can't go to {location} from here.")
        else:
            print("Where do you want to move to?")
            available_locations = world.get_available_locations()
            print(f"Available locations: {', '.join(available_locations)}")
    
    elif command == "look":
        current_location = world.get_current_location()
        print(world.get_location_description(current_location))
        print(f"You can go to: {', '.join(world.get_available_locations())}")
        
        # Show items in the location
        location_obj = world.locations[current_location]
        if location_obj.items:
            print(f"You can see: {', '.join(location_obj.items)}")
        else:
            print("There are no items here.")
    
    elif command == "inventory":
        if player.inventory:
            print(f"Your inventory: {', '.join(player.inventory)}")
        else:
            print("Your inventory is empty.")
    
    elif command == "pickup" or command == "take":
        if len(action_parts) > 1:
            item = " ".join(action_parts[1:])
            current_location = world.get_current_location()
            location_obj = world.locations[current_location]
            
            if item in location_obj.items:
                player.add_item(item)
                location_obj.items.remove(item)
            else:
                print(f"There is no {item} here.")
        else:
            print("What do you want to pick up?")
    
    elif command == "drop":
        if len(action_parts) > 1:
            item = " ".join(action_parts[1:])
            if player.remove_item(item):
                current_location = world.get_current_location()
                world.locations[current_location].items.append(item)
        else:
            print("What do you want to drop?")
    
    elif command == "use":
        if len(action_parts) > 1:
            item = " ".join(action_parts[1:])
            use_item(player, item, world)
        else:
            print("What do you want to use?")
    
    elif command == "examine":
        if len(action_parts) > 1:
            item = " ".join(action_parts[1:])
            if item in player.inventory:
                print(get_item_description(item))
            else:
                print(f"You don't have {item} in your inventory.")
        else:
            print("What do you want to examine?")
    
    elif command == "status":
        print(player.get_status())
    
    elif command == "interact":
        world.interact_with_location(player)
    
    else:
        print(f"I don't understand '{action}'. Type 'help' for a list of commands.")

