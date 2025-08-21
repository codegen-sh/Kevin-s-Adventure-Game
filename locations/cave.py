"""
Cave location for Kevin's Adventure Game.
"""

import random
from game.player import add_item_to_inventory, remove_item_from_inventory
from utils.random_events import apply_random_event


def explore_cave(world, player):
    """
    Handle cave exploration interactions.
    """
    print("\n=== Cave Exploration ===")
    print("You venture deeper into the dark cave...")
    print("The sound of dripping water echoes around you.")
    print("Strange minerals glitter on the cave walls.")
    
    # Random cave events
    event_chance = random.randint(1, 100)
    
    if event_chance <= 30:
        print("\nYou hear a strange noise echoing from deeper in the cave...")
        choice = input("Do you want to investigate? (y/n): ").lower()
        
        if choice == 'y':
            investigate_cave_sound(world, player)
        else:
            print("You decide to stay where it's safer.")
    
    elif event_chance <= 60:
        print("\nYou notice some loose rocks that might contain minerals...")
        choice = input("Do you want to try mining? (y/n): ").lower()
        
        if choice == 'y':
            mine_cave_wall(world, player)
        else:
            print("You leave the rocks undisturbed.")
    
    else:
        print("\nThe cave is peaceful. You take a moment to rest.")
        if player['health'] < 100:
            heal_amount = random.randint(5, 15)
            player['health'] = min(100, player['health'] + heal_amount)
            print(f"The cool cave air refreshes you. You recover {heal_amount} health.")


def investigate_cave_sound(world, player):
    """Handle investigating mysterious cave sounds."""
    print("\nYou cautiously move toward the sound...")
    
    outcome = random.randint(1, 100)
    
    if outcome <= 40:
        # Find treasure
        print("You discover a hidden chamber with ancient treasures!")
        treasure_items = ['ancient_coin', 'crystal_shard', 'cave_painting']
        found_item = random.choice(treasure_items)
        
        if found_item == 'ancient_coin':
            gold_found = random.randint(20, 50)
            player['gold'] += gold_found
            print(f"You found an ancient coin worth {gold_found} gold!")
        elif found_item == 'crystal_shard':
            add_item_to_inventory(player, 'crystal_shard')
            print("You found a beautiful crystal shard!")
        else:
            print("You discover ancient cave paintings that fill you with wonder.")
            player['health'] = min(100, player['health'] + 10)
            print("The inspiring artwork restores 10 health.")
    
    elif outcome <= 70:
        # Encounter danger
        print("You stumble upon a sleeping cave creature!")
        print("You try to back away quietly...")
        
        stealth_check = random.randint(1, 100)
        if stealth_check <= 60:
            print("You successfully sneak away without waking it.")
        else:
            print("You accidentally kick a rock! The creature wakes up and attacks!")
            damage = random.randint(10, 25)
            player['health'] -= damage
            print(f"You take {damage} damage but manage to escape!")
            
            if player['health'] <= 0:
                from utils.text_formatting import print_game_over
                print_game_over()
                return
    
    else:
        # False alarm
        print("The sound was just water dripping from a stalactite.")
        print("You feel a bit foolish but relieved.")


def mine_cave_wall(world, player):
    """Handle mining cave walls for minerals."""
    print("\nYou examine the cave wall for valuable minerals...")
    
    # Check if player has pickaxe
    has_pickaxe = 'pickaxe' in player['inventory']
    
    if has_pickaxe:
        print("You use your pickaxe to carefully extract minerals.")
        success_chance = 80
    else:
        print("You try to break off minerals with your bare hands.")
        success_chance = 30
    
    mining_result = random.randint(1, 100)
    
    if mining_result <= success_chance:
        # Successful mining
        minerals = ['iron_ore', 'copper_ore', 'silver_ore', 'gemstone']
        found_mineral = random.choice(minerals)
        
        if found_mineral == 'gemstone':
            value = random.randint(30, 80)
            player['gold'] += value
            print(f"You found a valuable gemstone worth {value} gold!")
        else:
            add_item_to_inventory(player, found_mineral)
            print(f"You successfully mined some {found_mineral.replace('_', ' ')}!")
    
    else:
        # Mining failure
        if has_pickaxe:
            print("The rock is too hard, even with your pickaxe.")
        else:
            damage = random.randint(2, 8)
            player['health'] -= damage
            print(f"You hurt your hands trying to break the rock. You take {damage} damage.")
            
            if player['health'] <= 0:
                from utils.text_formatting import print_game_over
                print_game_over()
                return
    
    # Chance for random event after mining
    if random.randint(1, 100) <= 25:
        apply_random_event(world, player)


def cave_specific_actions(world, player, action):
    """
    Handle cave-specific actions.
    """
    if action in ['mine', 'dig']:
        mine_cave_wall(world, player)
        return True
    elif action in ['listen', 'hear']:
        print("You listen carefully to the sounds of the cave...")
        print("You hear water dripping, your own breathing, and... something else?")
        return True
    elif action in ['rest', 'sleep']:
        if random.randint(1, 100) <= 70:
            heal_amount = random.randint(10, 20)
            player['health'] = min(100, player['health'] + heal_amount)
            print(f"You rest in the cool cave. You recover {heal_amount} health.")
        else:
            print("The cave is too cold and damp to rest comfortably.")
        return True
    
    return False
