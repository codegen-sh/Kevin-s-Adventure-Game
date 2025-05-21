"""
Actions module for Kevin's Adventure Game.
Contains functions for handling player actions in the game.
"""
from game.player import (
    add_item_to_inventory, damage_player, heal_player, 
    move_player, remove_item_from_inventory
)
from game.world import (
    change_location, get_available_locations, get_current_location,
    get_location_description, interact_with_location, is_location_accessible
)


def perform_action(player, world, action):
    """
    Parse and perform the player's action.
    
    Args:
        player (dict): The player's state
        world (dict): The world state
        action (str): The action to perform
    """
    action_parts = action.split()
    command = action_parts[0] if action_parts else ""
    
    if command == "move":
        if len(action_parts) < 2:
            print("Move where? Available locations: " + ", ".join(get_available_locations(world)))
            return
        
        destination = action_parts[1].capitalize()
        if is_location_accessible(world, destination):
            if change_location(world, destination):
                move_player(player, destination)
        else:
            print(f"You can't go to {destination} from here.")
            print("Available locations: " + ", ".join(get_available_locations(world)))
    
    elif command == "look":
        current_location = get_current_location(world)
        print(get_location_description(world, current_location))
        items = world["locations"][current_location]["items"]
        if items:
            print(f"You see: {', '.join(items)}")
        else:
            print("You don't see any items here.")
    
    elif command == "inventory":
        if player["inventory"]:
            print(f"Your inventory: {', '.join(player['inventory'])}")
        else:
            print("Your inventory is empty.")
    
    elif command == "pickup" or command == "pick" or command == "take":
        if len(action_parts) < 2:
            print("Pick up what?")
            return
        
        item = action_parts[1].lower()
        current_location = get_current_location(world)
        location_items = world["locations"][current_location]["items"]
        
        if item in location_items:
            add_item_to_inventory(player, item)
            location_items.remove(item)
        else:
            print(f"There is no {item} here.")
    
    elif command == "drop":
        if len(action_parts) < 2:
            print("Drop what?")
            return
        
        item = action_parts[1].lower()
        if remove_item_from_inventory(player, item):
            current_location = get_current_location(world)
            world["locations"][current_location]["items"].append(item)
    
    elif command == "use":
        if len(action_parts) < 2:
            print("Use what?")
            return
        
        item = action_parts[1].lower()
        if item in player["inventory"]:
            use_item(player, world, item)
        else:
            print(f"You don't have {item} in your inventory.")
    
    elif command == "examine":
        if len(action_parts) < 2:
            print("Examine what?")
            return
        
        item = action_parts[1].lower()
        examine_item(player, item)
    
    elif command == "status":
        print(f"Location: {get_current_location(world)}")
        print(f"Health: {player['health']}")
        print(f"Gold: {player['gold']}")
        print(f"Inventory: {', '.join(player['inventory']) if player['inventory'] else 'empty'}")
    
    elif command == "interact":
        interact_with_location(world, player)
    
    else:
        print(f"I don't understand '{action}'. Type 'help' for a list of commands.")


def use_item(player, world, item):
    """
    Use an item from the player's inventory.
    
    Args:
        player (dict): The player's state
        world (dict): The world state
        item (str): The item to use
    """
    if item == "bread":
        heal_player(player, 20)
        player["inventory"].remove(item)
        print("You ate the bread and restored some health.")
    
    elif item == "berries":
        heal_player(player, 10)
        player["inventory"].remove(item)
        print("You ate the berries and restored a little health.")
    
    elif item == "torch":
        print("You light the torch, illuminating the area around you.")
        if get_current_location(world) == "Cave":
            print("The cave's secrets become more visible.")
    
    elif item == "map":
        print("You consult the map.")
        print("Available locations in the world: " + ", ".join(world["locations"].keys()))
    
    elif item == "rope":
        print("You prepare the rope, ready to climb or descend.")
        if get_current_location(world) == "Mountain":
            print("The rope makes climbing much easier.")
    
    elif item == "pickaxe":
        print("You swing the pickaxe.")
        if get_current_location(world) == "Cave":
            print("You mine some valuable minerals!")
            add_item_to_inventory(player, "minerals")
    
    elif item == "stick":
        print("You wave the stick around. It's not very effective.")
    
    elif item == "gemstone":
        print("The gemstone glows with a mysterious light.")
    
    else:
        print(f"You can't figure out how to use the {item}.")


def examine_item(player, item):
    """
    Examine an item to get its description.
    
    Args:
        player (dict): The player's state
        item (str): The item to examine
    """
    item_descriptions = {
        "bread": "A fresh loaf of bread. It looks delicious and would restore some health.",
        "map": "A detailed map of the surrounding area, showing various locations.",
        "stick": "A simple wooden stick. It might be useful for something.",
        "berries": "Small, red berries. They look edible and might restore a little health.",
        "torch": "A wooden torch that can be lit to provide light in dark areas.",
        "gemstone": "A beautiful, sparkling gemstone. It seems valuable.",
        "rope": "A sturdy rope, useful for climbing or descending.",
        "pickaxe": "A sturdy pickaxe, perfect for mining or breaking rocks.",
        "minerals": "Valuable minerals extracted from the cave walls."
    }
    
    if item in player["inventory"]:
        if item in item_descriptions:
            print(item_descriptions[item])
        else:
            print(f"It's a {item}. Nothing special about it.")
    else:
        print(f"You don't have {item} in your inventory.")

