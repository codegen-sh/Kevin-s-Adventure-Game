from utils.text_formatting import format_inventory, print_game_over


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
    player['health'] = min(100, player['health'] + amount)
    print(f"You healed for {amount} health. Current health: {player['health']}")

def damage_player(player, amount):
    player['health'] = max(0, player['health'] - amount)
    print(f"You took {amount} damage. Current health: {player['health']}")
    if player['health'] == 0:
        print("You have been defeated.")
        print_game_over()

def use_item(player, item):
    """Use an item from the player's inventory."""
    if item not in player['inventory']:
        print(f"You don't have '{item}' in your inventory.")
        return False
    
    # Define item effects
    item_effects = {
        "bread": lambda: heal_player(player, 20),
        "healing potion": lambda: heal_player(player, 50),
        "berries": lambda: heal_player(player, 10),
        "torch": lambda: print("You light the torch, illuminating the area."),
        "map": lambda: print("You study the map and get a better sense of the area."),
        "rope": lambda: print("You examine the rope. It looks sturdy and useful for climbing."),
        "sword": lambda: print("You brandish your sword. You feel more confident in combat."),
        "pickaxe": lambda: print("You hold the pickaxe. Perfect for mining or breaking rocks."),
        "gemstone": lambda: print("The gemstone glitters beautifully in the light."),
        "glowing crystal": lambda: print("The crystal pulses with a mysterious energy."),
        "ancient artifact": lambda: print("You examine the ancient artifact. It seems to hold great power."),
        "cave pearl": lambda: print("The cave pearl shimmers with an otherworldly beauty."),
        "crystal shard": lambda: print("The crystal shard feels warm to the touch."),
        "ancient coin": lambda: (
            setattr(player, 'gold', player.get('gold', 0) + 10),
            print("You examine the ancient coin and decide to add it to your gold pouch. (+10 gold)")
        )
    }
    
    if item in item_effects:
        item_effects[item]()
        
        # Remove consumable items after use
        consumable_items = ["bread", "healing potion", "berries", "ancient coin"]
        if item in consumable_items:
            remove_item_from_inventory(player, item)
        
        return True
    else:
        print(f"You can't use '{item}' right now.")
        return False
