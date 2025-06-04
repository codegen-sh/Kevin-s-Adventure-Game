"""
Cave location module - handles cave exploration and interactions.
"""

from game.player import add_item_to_inventory, damage_player, heal_player
from game.state import update_world_state
from utils.random_events import generate_random_event
import random


def explore_cave(world, player):
    """
    Handle cave exploration and interactions.
    
    Args:
        world (dict): World state dictionary
        player (dict): Player state dictionary
    """
    print("You enter the dark, mysterious cave. Water drips from stalactites above.")
    print("The air is cool and damp, and you can hear strange echoes in the distance.")
    
    while True:
        print("\nWhat would you like to do in the cave?")
        print("1. Search for treasure")
        print("2. Explore deeper into the cave")
        print("3. Rest by the cave entrance")
        print("4. Mine for minerals")
        print("5. Leave the cave")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            search_for_treasure(world, player)
        elif choice == "2":
            explore_deeper(world, player)
        elif choice == "3":
            rest_in_cave(world, player)
        elif choice == "4":
            mine_minerals(world, player)
        elif choice == "5":
            print("You decide to leave the cave and return to the forest.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


def search_for_treasure(world, player):
    """Search for treasure in the cave."""
    print("You carefully search the cave walls and floor for hidden treasure...")
    
    # Random chance of finding treasure
    if random.random() < 0.4:  # 40% chance
        treasures = ["gemstone", "gold coin", "ancient artifact", "crystal"]
        treasure = random.choice(treasures)
        add_item_to_inventory(player, treasure)
        
        if treasure == "gold coin":
            gold_amount = random.randint(10, 50)
            player["gold"] += gold_amount
            print(f"You found {gold_amount} gold coins!")
        else:
            print(f"You discovered a valuable {treasure}!")
    else:
        print("You search thoroughly but find nothing of value this time.")
        
        # Small chance of encountering danger
        if random.random() < 0.2:  # 20% chance
            print("As you search, you accidentally disturb a sleeping bat!")
            print("It screeches and scratches you before flying away.")
            damage_player(player, random.randint(5, 15))


def explore_deeper(world, player):
    """Explore deeper into the cave system."""
    print("You venture deeper into the cave, using your torch to light the way...")
    
    # Check if player has a torch
    if "torch" not in player["inventory"]:
        print("It's too dark to explore safely without a torch!")
        print("You stumble in the darkness and hurt yourself.")
        damage_player(player, random.randint(10, 20))
        return
    
    # Random events in the deep cave
    events = [
        "underground_lake",
        "crystal_chamber", 
        "ancient_paintings",
        "cave_monster",
        "hidden_passage"
    ]
    
    event = random.choice(events)
    
    if event == "underground_lake":
        print("You discover a beautiful underground lake with crystal-clear water.")
        print("The water looks refreshing and pure.")
        choice = input("Do you want to drink from the lake? (y/n): ").lower()
        if choice == 'y':
            heal_player(player, random.randint(15, 25))
            print("The water is incredibly refreshing and healing!")
    
    elif event == "crystal_chamber":
        print("You find a magnificent chamber filled with glowing crystals!")
        print("The crystals emit a soft, magical light.")
        add_item_to_inventory(player, "magic crystal")
        
    elif event == "ancient_paintings":
        print("You discover ancient cave paintings on the walls.")
        print("They seem to tell the story of an ancient civilization.")
        print("You feel wiser from studying them.")
        # Could add experience or knowledge points here
        
    elif event == "cave_monster":
        print("A growling sound echoes through the cave!")
        print("A cave troll emerges from the shadows, blocking your path!")
        combat_cave_troll(world, player)
        
    elif event == "hidden_passage":
        print("You notice a hidden passage behind some rocks.")
        print("It leads to a secret chamber with ancient treasures!")
        add_item_to_inventory(player, "ancient treasure")
        player["gold"] += random.randint(50, 100)


def rest_in_cave(world, player):
    """Rest and recover in the cave."""
    print("You find a comfortable spot near the cave entrance to rest.")
    print("The cool air and peaceful atmosphere help you recover.")
    
    # Heal player
    heal_amount = random.randint(10, 20)
    heal_player(player, heal_amount)
    
    # Random chance of a peaceful event
    if random.random() < 0.3:  # 30% chance
        events = [
            "You hear beautiful cave music echoing from deep within.",
            "A friendly cave sprite appears and blesses your journey.",
            "You find a small cache of supplies left by previous explorers."
        ]
        print(random.choice(events))
        
        if "supplies" in events[-1]:
            add_item_to_inventory(player, "travel rations")


def mine_minerals(world, player):
    """Mine for valuable minerals in the cave."""
    print("You begin mining the cave walls for valuable minerals...")
    
    # Check if player has mining equipment
    if "pickaxe" not in player["inventory"]:
        print("You need a pickaxe to mine effectively!")
        print("You try to mine with your bare hands but only hurt yourself.")
        damage_player(player, random.randint(5, 10))
        return
    
    # Mining results
    if random.random() < 0.6:  # 60% chance of success
        minerals = ["iron ore", "copper ore", "silver ore", "gemstone"]
        mineral = random.choice(minerals)
        add_item_to_inventory(player, mineral)
        print(f"You successfully mined some {mineral}!")
        
        # Chance of finding something extra valuable
        if random.random() < 0.1:  # 10% chance
            add_item_to_inventory(player, "rare diamond")
            print("Amazing! You also found a rare diamond!")
    else:
        print("Your mining attempt yields nothing but rock and dust.")
        
        # Small chance of cave-in
        if random.random() < 0.15:  # 15% chance
            print("Your mining causes a small cave-in!")
            print("You're hit by falling rocks!")
            damage_player(player, random.randint(15, 25))


def combat_cave_troll(world, player):
    """Handle combat with a cave troll."""
    print("The cave troll roars and prepares to attack!")
    
    troll_health = 50
    
    while troll_health > 0 and player["health"] > 0:
        print(f"\nTroll Health: {troll_health}")
        print("What do you want to do?")
        print("1. Attack with weapon")
        print("2. Use item")
        print("3. Try to flee")
        
        choice = input("Enter your choice (1-3): ")
        
        if choice == "1":
            # Player attacks
            if "sword" in player["inventory"]:
                damage = random.randint(15, 25)
                print(f"You attack with your sword for {damage} damage!")
            elif "stick" in player["inventory"]:
                damage = random.randint(8, 15)
                print(f"You attack with your stick for {damage} damage!")
            else:
                damage = random.randint(5, 10)
                print(f"You attack with your fists for {damage} damage!")
            
            troll_health -= damage
            
            # Troll attacks back
            if troll_health > 0:
                troll_damage = random.randint(10, 20)
                print(f"The troll attacks you for {troll_damage} damage!")
                damage_player(player, troll_damage)
        
        elif choice == "2":
            print("You don't have any combat items to use right now.")
        
        elif choice == "3":
            if random.random() < 0.5:  # 50% chance to flee
                print("You successfully flee from the cave troll!")
                return
            else:
                print("You failed to escape! The troll blocks your path!")
                troll_damage = random.randint(5, 15)
                damage_player(player, troll_damage)
    
    if troll_health <= 0:
        print("You defeated the cave troll!")
        print("You search its lair and find treasure!")
        add_item_to_inventory(player, "troll treasure")
        player["gold"] += random.randint(30, 80)
    elif player["health"] <= 0:
        print("The cave troll has defeated you...")
        return

