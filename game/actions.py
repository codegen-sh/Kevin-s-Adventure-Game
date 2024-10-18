from game.items import (
    get_available_items,
    get_item_description,
    transfer_item,
    use_item,
)
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
    action_word = action.split()[0].lower() if action.split() else ""
    if action_word == "move":
        move(player, world, action)
    elif action_word == "look":
        look(player, world, action)
    elif action_word == "inventory":
        check_inventory(player, world, action)
    elif action_word == "pickup":
        pick_up(player, world, action)
    elif action_word == "drop":
        drop(player, world, action)
    elif action_word == "use":
        use(player, world, action)
    elif action_word == "examine":
        examine(player, world, action)
    elif action_word == "status":
        status(player, world, action)
    elif action_word == "interact":
        interact(player, world, action)
    else:
        print("I don't understand that action. Type 'help' for a list of commands.")

def move(player, world, action):
    destination = " ".join(action.split()[1:])  # SUS
    available_locations = get_available_locations(world)

    if destination.capitalize() in available_locations:
        if change_location(world, destination.capitalize()):
            move_player(player, destination.capitalize())
            look(player, world, "")
            apply_random_event(player, world)
            # TODO: Implement weather system
            # apply_weather_effects(player, world)
    else:
        print(f"You can't go to {destination}. Available locations: {', '.join(available_locations)}")

def look(player, world, action):
    current_location = get_current_location(world)
    print(get_location_description(world, current_location))
    items = get_available_items(world, current_location)
    if items:
        print(f"You see the following items: {', '.join(items)}")
    else:
        print("You don't see any items here.")

def check_inventory(player, world, action):
    if player["inventory"]:
        print("You are carrying:")
        for item in player["inventory"]:
            print(f"- {item}")
    else:
        print("Your inventory is empty.")

def pick_up(player, world, action):
    item = " ".join(action.split()[1:])
    current_location = get_current_location(world)
    available_items = get_available_items(world, current_location)

    if item in available_items:
        transfer_item(player, world, item, from_inventory_to_world=False)
    else:
        print(f"There's no {item} here to pick up.")

def drop(player, world, action):
    item = " ".join(action.split()[1:])
    if item in player["inventory"]:
        transfer_item(player, world, item, from_inventory_to_world=True)
    else:
        print(f"You don't have a {item} to drop.")

def use(player, world, action):
    item = " ".join(action.split()[1:])
    if use_item(player, item, world):
        print(f"You used the {item}.")
    else:
        print(f"You can't use the {item} right now.")

def examine(player, world, action):
    item = " ".join(action.split()[1:])
    if item in player["inventory"] or item in get_available_items(world, get_current_location(world)):
        print(get_item_description(item))
    else:
        print(f"You don't see a {item} to examine.")

def status(player, world, action):
    print(get_player_status(player))

def interact(player, world, action):
    interact_with_location(world, player)
