import random
from game.player import add_item_to_inventory, damage_player, heal_player

def explore_cave(world, player):
    """
    Handle player interactions with the cave location.
    
    Args:
        world (dict): The world state
        player (dict): The player's state
    """
    print("\nYou explore the dark, mysterious cave...")
    
    # Check if player has a torch
    has_torch = "torch" in player["inventory"]
    
    if not has_torch:
        print("It's very dark in here. You can barely see anything.")
        # Higher chance of taking damage without a torch
        if random.random() < 0.4:
            damage = random.randint(5, 15)
            print("You stumble in the darkness and hurt yourself!")
            damage_player(player, damage)
            return
    else:
        print("Your torch illuminates the cave, revealing glittering minerals and ancient cave paintings.")
    
    # Random cave events
    event = random.randint(1, 5)
    
    if event == 1:
        # Find treasure
        if "gemstone" not in player["inventory"] and random.random() < 0.3:
            print("You discover a beautiful gemstone embedded in the cave wall!")
            add_item_to_inventory(player, "gemstone")
        else:
            gold_amount = random.randint(10, 30)
            print(f"You find a small pouch containing {gold_amount} gold coins!")
            player["gold"] += gold_amount
    
    elif event == 2:
        # Encounter bats
        print("A swarm of bats suddenly flies past you!")
        if not has_torch:
            damage = random.randint(5, 10)
            print("The bats startle you, causing you to fall!")
            damage_player(player, damage)
        else:
            print("Your torch keeps the bats at bay.")
    
    elif event == 3:
        # Find underground spring
        print("You discover a small underground spring with crystal clear water.")
        heal_amount = random.randint(10, 20)
        print("You take a drink and feel refreshed.")
        heal_player(player, heal_amount)
    
    elif event == 4:
        # Cave paintings
        print("You notice ancient cave paintings depicting a mythical creature guarding a treasure.")
        print("Perhaps there's more to discover deeper in the cave system...")
        
        # Small chance to find a special item
        if random.random() < 0.2 and "ancient amulet" not in player["inventory"]:
            print("Something glints behind a rock... you find an ancient amulet!")
            add_item_to_inventory(player, "ancient amulet")
    
    elif event == 5:
        # Cave-in threat
        print("You hear ominous rumbling from above. The cave doesn't seem stable here.")
        if random.random() < 0.3:
            damage = random.randint(10, 20)
            print("Small rocks fall from the ceiling, hitting you!")
            damage_player(player, damage)
        else:
            print("You quickly move to a safer part of the cave.")
    
    # Chance to find additional items
    if has_torch and random.random() < 0.3:
        if "crystal" not in player["inventory"]:
            print("Your torch light reflects off something in a crevice... you find a beautiful crystal!")
            add_item_to_inventory(player, "crystal")
        elif "old coin" not in player["inventory"]:
            print("You spot something metallic on the ground... an old coin!")
            add_item_to_inventory(player, "old coin")

