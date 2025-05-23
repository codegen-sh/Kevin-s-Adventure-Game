from utils.text_formatting import format_inventory, print_game_over
from game.config import GAME_SETTINGS, PLAYER_DEFAULTS


def create_player(name):
    return {
        "name": name,
        "health": GAME_SETTINGS["starting_health"],
        "inventory": [],
        "location": GAME_SETTINGS["starting_location"],
        "gold": GAME_SETTINGS["starting_gold"],
        "agility": PLAYER_DEFAULTS["agility"],
        "perception": PLAYER_DEFAULTS["perception"],
        "strength": PLAYER_DEFAULTS["strength"]
    }

def get_player_status(player):
    return f"Health: {player['health']} | Inventory: {format_inventory(player['inventory'])} | Gold: {player['gold']}"

def add_item_to_inventory(player, item):
    player['inventory'].append(item)
    print(f"You picked up: {item}")

def remove_item_from_inventory(player, item):
    if item in player['inventory']:
        player['inventory'].remove(item)
        print(f"You dropped: {item}")
        return True
    else:
        print(f"You don't have {item} in your inventory.")

def move_player(player, new_location):
    player['location'] = new_location
    print(f"You moved to: {new_location}")

def heal_player(player, amount):
    player['health'] = min(GAME_SETTINGS["max_health"], player['health'] + amount)
    print(f"You healed for {amount} health. Current health: {player['health']}")

def damage_player(player, amount):
    player['health'] = max(0, player['health'] - amount)
    print(f"You took {amount} damage. Current health: {player['health']}")
    if player['health'] == 0:
        print("You have been defeated.")
        print_game_over()
