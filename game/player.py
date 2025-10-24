from utils.text_formatting import format_inventory, print_game_over
from game.world import track_gold_earned, track_gold_spent, track_item_collected


def create_player(name):
    return {
        "name": name,
        "health": 100,
        "inventory": [],
        "location": "Village",
        "gold": 100
    }

def get_player_status(player):
    return f"Health: {player['health']} | Inventory: {format_inventory(player['inventory'])} | Gold: {player['gold']}"

def add_item_to_inventory(player, item, world=None):
    player['inventory'].append(item)
    print(f"You picked up: {item}")
    
    # Track item collection for reporting if world is provided
    if world:
        track_item_collected(world, item)

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
    player['health'] = min(100, player['health'] + amount)
    print(f"You healed for {amount} health. Current health: {player['health']}")

def damage_player(player, amount):
    player['health'] = max(0, player['health'] - amount)
    print(f"You took {amount} damage. Current health: {player['health']}")
    if player['health'] == 0:
        print("You have been defeated.")
        print_game_over()

def add_gold(player, amount, world=None):
    """Add gold to the player's inventory and track for reporting."""
    player['gold'] += amount
    print(f"You gained {amount} gold. Current gold: {player['gold']}")
    
    # Track gold earned for reporting if world is provided
    if world:
        track_gold_earned(world, amount)

def spend_gold(player, amount, world=None):
    """Spend gold from the player's inventory and track for reporting."""
    if player['gold'] >= amount:
        player['gold'] -= amount
        print(f"You spent {amount} gold. Current gold: {player['gold']}")
        
        # Track gold spent for reporting if world is provided
        if world:
            track_gold_spent(world, amount)
            
        return True
    else:
        print(f"You don't have enough gold. Current gold: {player['gold']}")
        return False
