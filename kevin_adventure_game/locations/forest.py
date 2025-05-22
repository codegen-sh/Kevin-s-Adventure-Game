from kevin_adventure_game.game.player import add_item_to_inventory, heal_player
from kevin_adventure_game.utils.random_events import generate_random_event


def enter_forest(world, player):
    print(
        "You enter the lush, green forest. The air is filled with the sounds of birds and rustling leaves."
    )

    while True:
        print("\nWhat would you like to do in the forest?")
        print("1. Explore deeper")
        print("2. Climb a tree")
        print("3. Listen to the forest")
        print("4. Forage for food")
        print("5. Leave the forest")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            explore_forest(world, player)
        elif choice == "2":
            climb_tree(world, player)
        elif choice == "3":
            listen_to_forest(world, player)
        elif choice == "4":
            forage_for_food(world, player)
        elif choice == "5":
            print("You decide to leave the forest.")
            break
        else:
            print("Invalid choice. Please try again.")


def explore_forest(world, player):
    print("You decide to explore deeper into the forest.")
    event = generate_random_event(
        events=[
            ("find_berries", 40),
            ("encounter_animal", 25),
            ("discover_clearing", 10),
            (None, 25),
        ]
    )

    if event == "find_berries":
        print("You stumble upon a bush full of ripe berries!")
        add_item_to_inventory(player, "berries")
    elif event == "encounter_animal":
        print("You encounter a friendly deer. It allows you to approach and pet it.")
        heal_player(player, 5)
        print("The peaceful interaction leaves you feeling refreshed.")
    elif event == "discover_clearing":
        print("You discover a beautiful clearing with a small pond.")
        # summon_mythical_creature(world, player, "unicorn")
        # update_world_state(world, "add_clearing")
    else:
        print("Your exploration yields nothing of note this time.")


def climb_tree(world, player):
    print("You climb a tall tree to get a better view of the surrounding area.")
    print(
        "From up here, you can see the mountain peaks in the distance and what looks like the entrance to a cave."
    )


def listen_to_forest(world, player):
    print("You stop and listen carefully to the sounds of the forest.")
    print(
        "You hear a faint sound of rushing water in the distance. There might be a river nearby."
    )
    # TODO: Implement this
    # if generate_random_event(events = [("discover_river", 20), (None, 80)]) == "discover_river":
    #     print("You've discovered a river!")
    #     update_world_state(world, "add_river")
    # else:
    #     print("You don't find anything of note this time.")


def forage_for_food(world, player):
    print("You search the forest floor for edible plants and mushrooms.")
    if (
        generate_random_event(events=[("find_mushrooms", 30), (None, 70)])
        == "find_mushrooms"
    ):
        print("You find some edible mushrooms!")
        add_item_to_inventory(player, "mushrooms")
    else:
        print("You don't find anything edible this time.")
