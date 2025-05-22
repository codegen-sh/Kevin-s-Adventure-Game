from kevin_adventure_game.game.player import (
    add_item_to_inventory,
    damage_player,
    heal_player,
    remove_item_from_inventory,
)
from kevin_adventure_game.utils.random_events import generate_random_event


def climb_mountain(world, player):
    print("You begin your ascent up the steep mountain path.")

    while True:
        print("\nWhat would you like to do on the mountain?")
        print("1. Check weather")
        print("2. Use climbing gear")
        print("3. Search for herbs")
        print("4. Try to reach the peak")
        print("5. Explore mountain cave")
        print("6. Descend the mountain")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            check_weather(world, player)
        elif choice == "2":
            use_climbing_gear(world, player)
        elif choice == "3":
            search_for_herbs(world, player)
        elif choice == "4":
            reach_peak(world, player)
        elif choice == "5":
            explore_mountain_cave(world, player)
        elif choice == "6":
            print("You decide to descend the mountain.")
            break
        else:
            print("Invalid choice. Please try again.")


def check_weather(world, player):
    print("You pause to check the weather conditions.")
    # TODO: Implement weather system
    # weather = get_current_weather(world)
    event = generate_random_event(events=[("clear_skies", 50), ("incoming_storm", 50)])

    if event == "clear_skies":
        print(
            "The skies are clear, offering a breathtaking view of the surrounding lands."
        )
        # update_world_state(world, "improve_visibility")
    elif event == "incoming_storm":
        print("You notice dark clouds gathering. A storm might be approaching.")
        # update_world_state(world, "approaching_storm")
    else:
        print("The weather seems stable for now.")


def use_climbing_gear(world, player):
    if "rope" in player["inventory"]:
        print(
            "You use your rope to safely navigate a particularly treacherous part of the path."
        )
        heal_player(player, 5)
        print("Your careful climbing technique leaves you feeling confident.")
    else:
        print("This part of the path looks dangerous. A rope would be useful here.")
        damage_player(player, 10)
        print("You slip and take some damage while climbing. Be more careful!")


def search_for_herbs(world, player):
    print("You search the mountainside for rare herbs.")
    if generate_random_event(events=[("find_herbs", 30), (None, 70)]) == "find_herbs":
        print("You find some rare medicinal herbs!")
        add_item_to_inventory(player, "mountain_herbs")
    else:
        print("You don't find any useful herbs this time.")


def reach_peak(world, player):
    print("You finally reach the mountain peak!")
    if "mysterious_package" in player["inventory"]:
        print("You find the hermit's hut and deliver the mysterious package.")
        remove_item_from_inventory(player, "mysterious_package")
        add_item_to_inventory(player, "hermit's_blessing")
        print(
            "The hermit thanks you and gives you their blessing, which fills you with energy."
        )
        heal_player(player, 100)
        # summon_mythical_creature(world, player, "phoenix")

    print(
        "The view from the top is spectacular. You can see the entire game world spread out before you."
    )
    # update_world_state(world, "reveal_map")


def explore_mountain_cave(world, player):
    print("You discover a small cave entrance on the mountainside.")
    if "torch" in player["inventory"]:
        print("You use your torch to explore the mountain cave.")
        if (
            generate_random_event(events=[("find_treasure", 20), (None, 80)])
            == "find_treasure"
        ):
            print("You discover an old treasure chest hidden in the cave!")
            add_item_to_inventory(player, "ancient_coin")
        else:
            print("The cave is empty, but it provides good shelter from the elements.")
    else:
        print("It's too dark to explore the cave without a torch.")
