"""
Actions module for Kevin's Adventure Game.
Contains functions for handling player actions.
"""
from typing import Dict, List, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from src.game.player import Player
    from src.game.world import World


def perform_action(player: 'Player', world: 'World', action: str) -> None:
    """
    Perform a player action.

    Args:
        player: The player performing the action
        world: The game world
        action: The action to perform
    """
    action = action.lower().strip()
    
    if action.startswith("move "):
        move_player(player, world, action[5:])
    elif action == "look":
        look_around(player, world)
    elif action == "inventory":
        check_inventory(player)
    elif action.startswith("pickup ") or action.startswith("pick up "):
        item = action[7:] if action.startswith("pickup ") else action[8:]
        pickup_item(player, world, item)
    elif action.startswith("drop "):
        drop_item(player, world, action[5:])
    elif action.startswith("use "):
        use_item(player, world, action[4:])
    elif action.startswith("examine "):
        examine_item(player, world, action[8:])
    elif action == "status":
        check_status(player)
    elif action == "interact":
        interact_with_location(player, world)
    elif action == "weather":
        check_weather(player, world)
    else:
        print(f"I don't understand '{action}'. Type 'help' for a list of commands.")


def move_player(player: 'Player', world: 'World', location: str) -> None:
    """
    Move the player to a new location.

    Args:
        player: The player to move
        world: The game world
        location: The location to move to
    """
    if not location:
        print("Move where? Type 'move [location]'.")
        return
        
    if world.change_location(location):
        player.move(location)
        current_location = world.get_current_location()
        print(f"You are now in {current_location.name}.")
        print(current_location.description)
    else:
        print(f"You can't go to {location} from here.")
        print(f"Available locations: {', '.join(world.get_available_locations())}")


def look_around(player: 'Player', world: 'World') -> None:
    """
    Look around the current location.

    Args:
        player: The player
        world: The game world
    """
    current_location = world.get_current_location()
    print(current_location.description)
    
    # Show items in the location
    if current_location.items:
        print(f"You can see: {', '.join(current_location.items)}")
    else:
        print("There's nothing of interest here.")
        
    # Show available exits
    if current_location.connections:
        print(f"Exits: {', '.join(current_location.connections)}")
    else:
        print("There are no obvious exits.")


def check_inventory(player: 'Player') -> None:
    """
    Check the player's inventory.

    Args:
        player: The player
    """
    if player.inventory:
        print(f"Inventory: {', '.join(player.inventory)}")
    else:
        print("Your inventory is empty.")


def pickup_item(player: 'Player', world: 'World', item: str) -> None:
    """
    Pick up an item from the current location.

    Args:
        player: The player
        world: The game world
        item: The item to pick up
    """
    if not item:
        print("Pick up what? Type 'pickup [item]'.")
        return
        
    current_location = world.get_current_location()
    if item in current_location.items:
        current_location.remove_item(item)
        player.add_item(item)
    else:
        print(f"There's no {item} here to pick up.")


def drop_item(player: 'Player', world: 'World', item: str) -> None:
    """
    Drop an item from the player's inventory.

    Args:
        player: The player
        world: The game world
        item: The item to drop
    """
    if not item:
        print("Drop what? Type 'drop [item]'.")
        return
        
    if player.remove_item(item):
        current_location = world.get_current_location()
        current_location.add_item(item)


def use_item(player: 'Player', world: 'World', item: str) -> None:
    """
    Use an item from the player's inventory.

    Args:
        player: The player
        world: The game world
        item: The item to use
    """
    if not item:
        print("Use what? Type 'use [item]'.")
        return
        
    if not player.has_item(item):
        print(f"You don't have {item} in your inventory.")
        return
    
    # This is a simplified version. In the full implementation,
    # we would use the ItemRegistry to get the item object and call its use method.
    if item == "map":
        print("You consult the map. It shows the following locations you can go to:")
        available_locations = world.get_available_locations()
        for location in available_locations:
            print(f"- {location}")
    elif item == "bread":
        print("You eat the bread. It's delicious and restores some health.")
        player.heal(20)
        player.remove_item(item)
    elif item == "torch" and world.current_location == "Cave":
        print("You light the torch, illuminating the dark cave around you.")
        current_location = world.get_current_location()
        if hasattr(current_location, 'is_lit'):
            current_location.is_lit = True
            current_location.description += " The cave is now well-lit by your torch."
    else:
        print(f"You're not sure how to use the {item} here.")


def examine_item(player: 'Player', world: 'World', item: str) -> None:
    """
    Examine an item.

    Args:
        player: The player
        world: The game world
        item: The item to examine
    """
    if not item:
        print("Examine what? Type 'examine [item]'.")
        return
    
    # In the full implementation, we would use the ItemRegistry
    # to get the item description.
    item_descriptions = {
        "map": "An old, worn map of the surrounding area. It might help you navigate.",
        "bread": "A fresh loaf of bread. It looks delicious and nutritious.",
        "stick": "A sturdy wooden stick. It could be used as a simple weapon or tool.",
        "berries": "A handful of colorful berries. They might be edible... or not.",
        "torch": "A flaming torch that provides light in dark areas.",
        "gemstone": "A sparkling gemstone. It looks valuable.",
        "rope": "A coil of strong rope. Useful for climbing or tying things.",
        "pickaxe": "A sturdy pickaxe. Perfect for mining or breaking through rocks.",
        "mushrooms": "Some wild mushrooms. They could be edible or poisonous.",
        "mountain_herbs": "Rare medicinal herbs found on the mountain. They might have healing properties.",
        "ancient_coin": "An old coin with strange markings. It might be valuable to collectors.",
        "hermit's_blessing": "A mystical blessing from the mountain hermit. It fills you with energy.",
        "mysterious_package": "A package wrapped in cloth. It's addressed to the hermit on the mountain.",
        "unicorn_hair": "A shimmering strand of hair from a unicorn's mane. It glows with magical energy.",
        "phoenix_feather": "A brilliant red and gold feather that radiates warmth. It never seems to burn out."
    }
    
    description = item_descriptions.get(item, "A mysterious item.")
    print(description)


def check_status(player: 'Player') -> None:
    """
    Check the player's status.

    Args:
        player: The player
    """
    print(player.get_status())


def interact_with_location(player: 'Player', world: 'World') -> None:
    """
    Interact with the current location.

    Args:
        player: The player
        world: The game world
    """
    current_location = world.get_current_location()
    current_location.enter(player, world)


def check_weather(player: 'Player', world: 'World') -> None:
    """
    Check the current weather.

    Args:
        player: The player
        world: The game world
    """
    if hasattr(world, 'weather'):
        print(world.weather.describe_weather())
        world.weather.apply_weather_effects(player)
        print(world.weather.forecast())
    else:
        print("The weather is clear and pleasant.")

