"""
Cave location module - handles cave exploration and interactions
"""

from game.player import add_item_to_inventory, damage_player, heal_player
from game.mythical import summon_mythical_creature
from utils.random_events import generate_random_event


def explore_cave(world, player):
    """
    Main function for cave exploration and interactions
    
    Args:
        world (dict): World data structure
        player (dict): Player data structure
    """
    print("You enter the dark, mysterious cave. Water drips from stalactites above.")
    print("The air is cool and damp, and you can hear strange echoes in the distance.")
    
    # Check if player has a torch for better exploration
    has_torch = "torch" in player.get("inventory", [])
    if has_torch:
        print("Your torch illuminates the cave walls, revealing ancient markings.")
    else:
        print("The cave is quite dark. A torch would help you see better.")
    
    while True:
        print("\nWhat would you like to do in the cave?")
        print("1. Search for treasure")
        print("2. Examine the cave walls")
        print("3. Venture deeper into the cave")
        print("4. Rest by the cave entrance")
        print("5. Leave the cave")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            search_for_treasure(world, player, has_torch)
        elif choice == "2":
            examine_cave_walls(world, player, has_torch)
        elif choice == "3":
            venture_deeper(world, player, has_torch)
        elif choice == "4":
            rest_in_cave(world, player)
        elif choice == "5":
            print("You decide to leave the cave and return to the forest.")
            break
        else:
            print("Invalid choice. Please try again.")


def search_for_treasure(world, player, has_torch):
    """Handle treasure searching in the cave"""
    print("You search the cave floor and crevices for valuable items...")
    
    # Better chances with torch
    base_chance = 40 if has_torch else 25
    
    event = generate_random_event(events=[
        ("find_gold", base_chance),
        ("find_gemstone", 20),
        ("find_nothing", 30),
        ("encounter_danger", 10)
    ])
    
    if event == "find_gold":
        gold_found = generate_random_event(events=[(10, 30), (20, 40), (50, 30)])
        player["gold"] += gold_found
        print(f"You found {gold_found} gold coins hidden in a small crevice!")
    
    elif event == "find_gemstone":
        if "gemstone" not in world["locations"]["Cave"]["items"]:
            add_item_to_inventory(player, "gemstone")
            print("You discovered a beautiful gemstone embedded in the cave wall!")
        else:
            print("You find some interesting minerals, but nothing valuable.")
    
    elif event == "find_nothing":
        print("Despite your thorough search, you don't find anything of value.")
    
    elif event == "encounter_danger":
        print("As you search, you accidentally disturb a colony of bats!")
        print("They swarm around you in confusion.")
        damage_player(player, 5)
        print("You manage to calm them down, but not without a few scratches.")


def examine_cave_walls(world, player, has_torch):
    """Handle examining the cave walls and markings"""
    print("You approach the cave walls to examine them more closely...")
    
    if has_torch:
        print("With your torch's light, you can see ancient cave paintings!")
        print("The paintings depict strange creatures and mysterious symbols.")
        
        event = generate_random_event(events=[
            ("learn_secret", 30),
            ("find_hidden_passage", 20),
            ("ancient_wisdom", 25),
            ("nothing_special", 25)
        ])
        
        if event == "learn_secret":
            print("The paintings seem to tell a story about a hidden treasure in the mountain!")
            print("This knowledge might be useful for your future adventures.")
        
        elif event == "find_hidden_passage":
            print("You notice a section of the wall that looks different...")
            print("It might be a hidden passage, but it's too dangerous to explore alone.")
        
        elif event == "ancient_wisdom":
            print("The symbols seem to contain ancient wisdom about survival.")
            heal_player(player, 15)
            print("Studying them makes you feel more prepared and resilient.")
        
        else:
            print("The paintings are beautiful but don't reveal any immediate secrets.")
    
    else:
        print("The cave is too dark to see much detail on the walls.")
        print("You can make out some shapes, but a torch would help you see better.")


def venture_deeper(world, player, has_torch):
    """Handle venturing deeper into the cave"""
    print("You decide to venture deeper into the cave's dark passages...")
    
    if not has_torch:
        print("Without a torch, the deeper cave is treacherous!")
        event = generate_random_event(events=[
            ("stumble", 60),
            ("get_lost", 30),
            ("safe_passage", 10)
        ])
        
        if event == "stumble":
            print("You stumble in the darkness and scrape yourself on the rocky floor.")
            damage_player(player, 10)
        elif event == "get_lost":
            print("You become disoriented in the darkness and have to feel your way back.")
            print("You waste time and energy finding your way to the entrance.")
            damage_player(player, 5)
        else:
            print("Somehow, you manage to navigate safely despite the darkness.")
    
    else:
        print("Your torch lights the way as you explore the deeper passages.")
        
        event = generate_random_event(events=[
            ("underground_lake", 25),
            ("crystal_chamber", 20),
            ("ancient_ruins", 15),
            ("dangerous_creature", 20),
            ("dead_end", 20)
        ])
        
        if event == "underground_lake":
            print("You discover a beautiful underground lake with crystal-clear water.")
            print("The peaceful atmosphere restores your energy.")
            heal_player(player, 20)
        
        elif event == "crystal_chamber":
            print("You find a chamber filled with glowing crystals!")
            if "crystal" not in player.get("inventory", []):
                add_item_to_inventory(player, "crystal")
                print("You carefully extract a small crystal as a memento.")
        
        elif event == "ancient_ruins":
            print("You stumble upon ancient ruins deep within the cave.")
            print("The architecture is unlike anything you've seen before.")
            print("This discovery fills you with wonder and determination.")
            heal_player(player, 10)
        
        elif event == "dangerous_creature":
            print("You encounter a territorial cave creature!")
            handle_cave_creature_encounter(world, player)
        
        else:
            print("The passage leads to a dead end, but the journey was interesting.")


def rest_in_cave(world, player):
    """Handle resting in the cave"""
    print("You find a relatively comfortable spot near the cave entrance to rest.")
    
    event = generate_random_event(events=[
        ("peaceful_rest", 60),
        ("disturbed_rest", 25),
        ("healing_spring", 15)
    ])
    
    if event == "peaceful_rest":
        print("You have a peaceful rest and feel somewhat refreshed.")
        heal_player(player, 10)
    
    elif event == "disturbed_rest":
        print("Your rest is disturbed by strange noises echoing through the cave.")
        print("You don't feel as rested as you hoped.")
        heal_player(player, 5)
    
    elif event == "healing_spring":
        print("You discover a small spring with remarkably pure water!")
        print("Drinking from it makes you feel significantly better.")
        heal_player(player, 25)


def handle_cave_creature_encounter(world, player):
    """Handle encounters with cave creatures"""
    print("A large cave creature blocks your path!")
    print("It doesn't seem immediately hostile, but it's clearly territorial.")
    
    has_sword = "sword" in player.get("inventory", [])
    
    print("\nWhat do you want to do?")
    print("1. Try to scare it away")
    print("2. Offer it food")
    print("3. Back away slowly")
    if has_sword:
        print("4. Brandish your sword")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        success_chance = 40
        if generate_random_event(events=[("success", success_chance), ("failure", 100-success_chance)]) == "success":
            print("You make loud noises and the creature retreats deeper into the cave.")
        else:
            print("The creature is not intimidated and swipes at you!")
            damage_player(player, 15)
    
    elif choice == "2":
        if "bread" in player.get("inventory", []):
            player["inventory"].remove("bread")
            print("You offer the creature some bread. It accepts and allows you to pass.")
        else:
            print("You don't have any food to offer. The creature seems disappointed.")
            damage_player(player, 10)
    
    elif choice == "3":
        print("You slowly back away. The creature watches but doesn't follow.")
        print("You safely return to the main cave area.")
    
    elif choice == "4" and has_sword:
        print("You brandish your sword confidently.")
        print("The creature recognizes the threat and retreats respectfully.")
        print("You feel more confident about cave exploration.")
    
    else:
        print("You hesitate, and the creature takes this as a sign of weakness.")
        damage_player(player, 12)
