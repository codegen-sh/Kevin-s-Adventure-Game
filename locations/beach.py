from game.player import add_item_to_inventory, heal_player
from game.state import update_world_state
from utils.random_events import generate_random_event


def visit_beach(world, player):
    print("You arrive at a beautiful sandy beach. The waves crash gently on the shore and a cool breeze blows from the ocean.")

    while True:
        print("\nWhat would you like to do at the beach?")
        print("1. Explore the shoreline")
        print("2. Swim in the ocean")
        print("3. Build a sand castle")
        print("4. Search for seashells")
        print("5. Leave the beach")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            explore_shoreline(world, player)
        elif choice == "2":
            swim_in_ocean(world, player)
        elif choice == "3":
            build_sand_castle(world, player)
        elif choice == "4":
            search_for_seashells(world, player)
        elif choice == "5":
            print("You decide to leave the beach.")
            break
        else:
            print("Invalid choice. Please try again.")

def explore_shoreline(world, player):
    print("You walk along the shoreline, feeling the sand between your toes.")
    event = generate_random_event(events=[("find_bottle", 30), ("encounter_crab", 25), ("discover_cave", 15), (None, 30)])

    if event == "find_bottle":
        print("You find a bottle with a message inside!")
        add_item_to_inventory(player, "message in a bottle")
        print("You've added 'message in a bottle' to your inventory.")
    elif event == "encounter_crab":
        print("You encounter a small crab scuttling across the sand. It seems friendly.")
        print("Watching the crab's antics makes you smile and lifts your spirits.")
        heal_player(player, 3)
        print("You feel refreshed (+3 health).")
    elif event == "discover_cave":
        print("You discover a small cave entrance hidden among the rocks!")
        print("It might be worth exploring later when you're better prepared.")
        update_world_state(world, "discovered_beach_cave")
    else:
        print("Your exploration yields nothing of note this time.")

def swim_in_ocean(world, player):
    print("You wade into the cool, refreshing water and start swimming.")
    event = generate_random_event(events=[("find_coral", 25), ("see_fish", 40), ("strong_current", 15), (None, 20)])

    if event == "find_coral":
        print("You swim over a beautiful coral reef teeming with colorful fish!")
        heal_player(player, 5)
        print("The beauty of nature rejuvenates you (+5 health).")
    elif event == "see_fish":
        print("A school of colorful fish swims around you, creating a magical moment.")
        heal_player(player, 2)
        print("You feel at peace with nature (+2 health).")
    elif event == "strong_current":
        print("You get caught in a strong current and struggle to swim back to shore!")
        print("You manage to make it back, but you're exhausted from the effort.")
        heal_player(player, -3)
        print("You've lost 3 health points.")
    else:
        print("You enjoy a pleasant swim in the ocean and return to shore.")

def build_sand_castle(world, player):
    print("You start gathering wet sand to build a sand castle.")
    event = generate_random_event(events=[("masterpiece", 20), ("decent_castle", 50), ("wave_destroys", 30)])

    if event == "masterpiece":
        print("You create a magnificent sand castle with towers, moats, and intricate details!")
        print("A few other beachgoers stop to admire your work.")
        heal_player(player, 4)
        print("You feel proud of your creation (+4 health).")
    elif event == "decent_castle":
        print("You build a decent sand castle. It's not a masterpiece, but it's still fun.")
        heal_player(player, 2)
        print("The creative activity makes you feel good (+2 health).")
    elif event == "wave_destroys":
        print("Just as you're finishing your castle, a large wave comes and washes it away!")
        print("All that work for nothing... but that's life at the beach.")
    else:
        print("You spend some time building in the sand and enjoy yourself.")

def search_for_seashells(world, player):
    print("You search the beach for interesting seashells and treasures.")
    event = generate_random_event(events=[("rare_shell", 15), ("common_shells", 40), ("shiny_object", 10), (None, 35)])

    if event == "rare_shell":
        print("You find a rare, perfectly intact spiral shell with beautiful colors!")
        add_item_to_inventory(player, "rare seashell")
        print("You've added 'rare seashell' to your inventory.")
    elif event == "common_shells":
        print("You collect a handful of common but pretty seashells.")
        add_item_to_inventory(player, "seashells")
        print("You've added 'seashells' to your inventory.")
    elif event == "shiny_object":
        print("Something shiny catches your eye in the sand...")
        print("It's a gold coin! It looks very old and might be from a shipwreck.")
        add_item_to_inventory(player, "gold coin")
        print("You've added 'gold coin' to your inventory.")
    else:
        print("You don't find anything interesting this time.")
