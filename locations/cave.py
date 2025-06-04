"""
Cave location module for Kevin's Adventure Game.
Handles all cave-related interactions and events.
"""

from game.player import add_item_to_inventory, damage_player, heal_player
from utils.random_events import generate_random_event


def explore_cave(world, player):
    """Main function for exploring the cave."""
    print("You enter the mysterious cave. The air is cool and damp, and you can hear water dripping in the distance.")
    
    # Check if player has a torch for better exploration
    has_torch = "torch" in player.get("inventory", [])
    
    if has_torch:
        print("Your torch illuminates the cave, revealing ancient drawings on the walls.")
    else:
        print("The cave is quite dark. A torch would help you explore more thoroughly.")
    
    while True:
        print("\nWhat would you like to do in the cave?")
        print("1. Explore deeper into the cave")
        print("2. Examine the cave walls")
        print("3. Search for minerals")
        print("4. Rest in the cave")
        if has_torch:
            print("5. Follow the torch light to hidden passages")
        print("6. Leave the cave")
        
        max_choice = 6 if has_torch else 5
        choice = input(f"Enter your choice (1-{max_choice}): ")
        
        if choice == "1":
            explore_deeper(world, player, has_torch)
        elif choice == "2":
            examine_walls(world, player, has_torch)
        elif choice == "3":
            search_minerals(world, player)
        elif choice == "4":
            rest_in_cave(world, player)
        elif choice == "5" and has_torch:
            explore_hidden_passages(world, player)
        elif choice == "6" or (choice == "5" and not has_torch):
            print("You leave the cave and return to the outside world.")
            break
        else:
            print("Invalid choice. Please try again.")


def explore_deeper(world, player, has_torch):
    """Explore deeper into the cave."""
    if has_torch:
        print("You venture deeper into the cave, your torch casting dancing shadows on the walls.")
        
        # Random events when exploring with light
        event = generate_random_event(events=[("treasure", 30), ("danger", 20), ("discovery", 25), ("nothing", 25)])
        
        if event == "treasure":
            print("You discover a hidden alcove containing ancient treasures!")
            treasures = ["ancient_coin", "gemstone", "silver_necklace"]
            found_treasure = generate_random_event(events=[(t, 33) for t in treasures])
            add_item_to_inventory(player, found_treasure)
            print(f"You found a {found_treasure}!")
            
        elif event == "danger":
            print("You accidentally disturb a colony of bats! They swarm around you.")
            damage_player(player, 5)
            print("You manage to protect yourself but suffer some minor injuries.")
            
        elif event == "discovery":
            print("You find ancient cave paintings depicting mysterious rituals.")
            print("The knowledge fills you with wisdom and inner peace.")
            heal_player(player, 10)
            
    else:
        print("You try to explore deeper, but it's too dark to see safely.")
        print("You hear strange sounds echoing from the depths...")
        
        # Higher chance of danger without light
        if generate_random_event(events=[("danger", 60), ("safe", 40)]) == "danger":
            print("You stumble in the darkness and hurt yourself!")
            damage_player(player, 10)


def examine_walls(world, player, has_torch):
    """Examine the cave walls for interesting features."""
    if has_torch:
        print("Your torch reveals intricate cave paintings and strange symbols carved into the rock.")
        print("The artwork seems to tell the story of ancient civilizations.")
        
        # Chance to find hidden items
        if generate_random_event(events=[("find_item", 40), ("nothing", 60)]) == "find_item":
            print("Behind one of the paintings, you discover a hidden compartment!")
            add_item_to_inventory(player, "ancient_artifact")
            print("You found an ancient artifact!")
    else:
        print("You run your hands along the rough cave walls.")
        print("You can feel carved patterns, but it's too dark to see what they depict.")


def search_minerals(world, player):
    """Search for valuable minerals in the cave."""
    print("You search the cave floor and walls for valuable minerals.")
    
    # Check if player has pickaxe for better mining
    has_pickaxe = "pickaxe" in player.get("inventory", [])
    
    if has_pickaxe:
        print("You use your pickaxe to carefully extract minerals from the cave walls.")
        success_chance = 70
    else:
        print("You search with your bare hands, looking for loose gems and minerals.")
        success_chance = 30
    
    if generate_random_event(events=[("success", success_chance), ("failure", 100 - success_chance)]) == "success":
        minerals = ["gemstone", "ancient_coin", "gold_coin"]
        found_mineral = generate_random_event(events=[(m, 33) for m in minerals])
        add_item_to_inventory(player, found_mineral)
        print(f"You successfully found a {found_mineral}!")
    else:
        print("Despite your efforts, you don't find any valuable minerals this time.")


def rest_in_cave(world, player):
    """Rest in the cave to recover health."""
    print("You find a dry spot in the cave and rest for a while.")
    print("The cool, quiet environment helps you recover your strength.")
    heal_player(player, 15)
    
    # Small chance of being disturbed
    if generate_random_event(events=[("disturbed", 20), ("peaceful", 80)]) == "disturbed":
        print("Your rest is interrupted by strange noises echoing through the cave.")
        print("You feel uneasy but manage to get some rest anyway.")


def explore_hidden_passages(world, player):
    """Explore hidden passages that can only be found with a torch."""
    print("Following your torch light, you notice a narrow passage hidden behind a rock formation.")
    print("You squeeze through the passage and discover a secret chamber!")
    
    # Special rewards for thorough exploration
    event = generate_random_event(events=[("treasure_chamber", 40), ("underground_spring", 30), ("ancient_shrine", 30)])
    
    if event == "treasure_chamber":
        print("You've discovered an ancient treasure chamber!")
        print("Gold coins and precious gems are scattered across the floor.")
        player["gold"] = player.get("gold", 0) + 50
        add_item_to_inventory(player, "magic_ring")
        print("You collected 50 gold and found a magic ring!")
        
    elif event == "underground_spring":
        print("You find a crystal-clear underground spring.")
        print("The water has magical healing properties!")
        heal_player(player, 30)
        print("You feel completely refreshed and energized.")
        
    elif event == "ancient_shrine":
        print("You discover an ancient shrine dedicated to forgotten gods.")
        print("Touching the shrine fills you with mystical energy.")
        add_item_to_inventory(player, "hermit's_blessing")
        print("You received a hermit's blessing!")

