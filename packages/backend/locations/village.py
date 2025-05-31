from game.mythical import summon_mythical_creature
from game.player import add_item_to_inventory, heal_player
from game.state import update_world_state
from utils.random_events import generate_random_event


def visit_village(world, player):
    print("You enter the bustling village. Villagers go about their daily lives around you.")

    while True:
        print("\nWhat would you like to do in the village?")
        print("1. Visit the shop")
        print("2. Talk to villagers")
        print("3. Visit the inn")
        print("4. Check for quests")
        print("5. Leave the village")
        # print("6. Check on the village dragon")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            visit_shop(world, player)
        elif choice == "2":
            talk_to_villagers(world, player)
        elif choice == "3":
            visit_inn(world, player)
        elif choice == "4":
            perform_quest(world, player)
        elif choice == "5":
            print("You decide to leave the village.")
            break
        # elif choice == "6":
        #     summon_mythical_creature(world, player, "dragon")
        else:
            print("Invalid choice. Please try again.")

def visit_shop(world, player):
    print("You enter the village shop. The shopkeeper greets you warmly.")
    print("Available items: bread (5 gold), torch (10 gold), rope (15 gold), sword (50 gold)")

    while True:
        choice = input("What would you like to buy? (or 'exit' to leave): ").lower()
        if choice == 'exit':
            break
        elif choice == 'bread' and player.get("gold", 0) >= 5:
            player["gold"] -= 5
            add_item_to_inventory(player, "bread")
            print("You bought a loaf of bread.")
        elif choice == 'torch' and player.get("gold", 0) >= 10:
            player["gold"] -= 10
            add_item_to_inventory(player, "torch")
            print("You bought a torch.")
        elif choice == 'rope' and player.get("gold", 0) >= 15:
            player["gold"] -= 15
            add_item_to_inventory(player, "rope")
            print("You bought a coil of rope.")
        elif choice == 'sword' and player.get("gold", 0) >= 50:
            player["gold"] -= 50
            add_item_to_inventory(player, "sword")
            print("You bought a sturdy sword.")
        else:
            print("Invalid choice or not enough gold.")

def talk_to_villagers(world, player):
    print("You approach a group of villagers to chat.")
    event = generate_random_event(events = [("hear_rumor", 40), ("receive_advice", 30), (None, 30)])

    if event == "hear_rumor":
        print("You overhear an interesting rumor about treasure hidden in the nearby cave.")
    elif event == "receive_advice":
        print("An old villager gives you advice about surviving in the forest.")
        heal_player(player, 10)
        print("Their wisdom makes you feel more prepared for your adventures.")
    else:
        print("You have a pleasant but uneventful conversation with the villagers.")

def visit_inn(world, player):
    print("You enter the cozy village inn.")
    if player.get("gold", 0) >= 10:
        choice = input("Would you like to rest for the night? (10 gold) [y/n]: ").lower()
        if choice == 'y':
            player["gold"] -= 10
            heal_player(player, 50)
            print("You have a good night's rest and feel rejuvenated.")
        else:
            print("You decide not to stay the night.")
    else:
        print("You don't have enough gold to stay the night.")

def perform_quest(world, player):
    print("You check the village quest board.")
    if generate_random_event(events = [("receive_quest", 30), (None, 70)]) == "receive_quest":
        print("You accept a quest to deliver a package to a hermit living on the mountain.")
        add_item_to_inventory(player, "mysterious_package")
        print("Complete this quest by reaching the mountain peak.")
    else:
        print("There are no available quests at the moment.")
