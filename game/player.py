from utils.text_formatting import format_inventory, print_game_over
from config import config


def create_player(name):
    """Create a new player with configuration-based starting values."""
    game_settings = config.get_game_settings()
    player_config = game_settings["player"]
    
    return {
        "name": name,
        "health": player_config["starting_health"],
        "inventory": player_config["starting_inventory"].copy(),
        "location": player_config["starting_location"],
        "gold": player_config["starting_gold"]
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
    game_settings = config.get_game_settings()
    max_health = game_settings["player"]["max_health"]
    
    player['health'] = min(max_health, player['health'] + amount)
    print(f"You healed for {amount} health. Current health: {player['health']}")

def damage_player(player, amount):
    player['health'] = max(0, player['health'] - amount)
    print(f"You took {amount} damage. Current health: {player['health']}")
    if player['health'] == 0:
        print("You have been defeated.")
        print_game_over()
