"""
Village location module for Kevin's Adventure Game.
"""
from typing import Dict, List, Optional

from kevin_adventure.core.player import Player
from kevin_adventure.core.world import World
from kevin_adventure.locations.location import Location
from kevin_adventure.utils.random_events import generate_random_event


class Village(Location):
    """
    Village location class.
    """

    def __init__(self):
        """
        Initialize a new Village location.
        """
        super().__init__(
            "Village",
            "A small, peaceful village with thatched-roof houses and friendly inhabitants.",
            ["Forest", "Mountain"],
            ["map", "bread"]
        )

    def interact(self, player: Player, world: World) -> None:
        """
        Interact with the village.

        Args:
            player: The player interacting with the village
            world: The game world
        """
        print("You enter the bustling village. Villagers go about their daily lives around you.")

        while True:
            print("\nWhat would you like to do in the village?")
            print("1. Visit the shop")
            print("2. Talk to villagers")
            print("3. Visit the inn")
            print("4. Check for quests")
            print("5. Leave the village")

            choice = input("Enter your choice (1-5): ")

            if choice == "1":
                self.visit_shop(player, world)
            elif choice == "2":
                self.talk_to_villagers(player, world)
            elif choice == "3":
                self.visit_inn(player, world)
            elif choice == "4":
                self.perform_quest(player, world)
            elif choice == "5":
                print("You decide to leave the village.")
                break
            else:
                print("Invalid choice. Please try again.")

    def visit_shop(self, player: Player, world: World) -> None:
        """
        Visit the village shop.

        Args:
            player: The player visiting the shop
            world: The game world
        """
        print("You enter the village shop. The shopkeeper greets you warmly.")
        print("Available items: bread (5 gold), torch (10 gold), rope (15 gold), sword (50 gold)")

        while True:
            choice = input("What would you like to buy? (or 'exit' to leave): ").lower()
            if choice == 'exit':
                break
            elif choice == 'bread' and player.gold >= 5:
                player.gold -= 5
                player.add_item("bread")
                print("You bought a loaf of bread.")
            elif choice == 'torch' and player.gold >= 10:
                player.gold -= 10
                player.add_item("torch")
                print("You bought a torch.")
            elif choice == 'rope' and player.gold >= 15:
                player.gold -= 15
                player.add_item("rope")
                print("You bought a coil of rope.")
            elif choice == 'sword' and player.gold >= 50:
                player.gold -= 50
                player.add_item("sword")
                print("You bought a sturdy sword.")
            else:
                print("Invalid choice or not enough gold.")

    def talk_to_villagers(self, player: Player, world: World) -> None:
        """
        Talk to the villagers.

        Args:
            player: The player talking to the villagers
            world: The game world
        """
        print("You approach a group of villagers to chat.")
        event = generate_random_event(events=[("hear_rumor", 40), ("receive_advice", 30), (None, 30)])

        if event == "hear_rumor":
            print("You overhear an interesting rumor about treasure hidden in the nearby cave.")
        elif event == "receive_advice":
            print("An old villager gives you advice about surviving in the forest.")
            player.heal(10)
            print("Their wisdom makes you feel more prepared for your adventures.")
        else:
            print("You have a pleasant but uneventful conversation with the villagers.")

    def visit_inn(self, player: Player, world: World) -> None:
        """
        Visit the village inn.

        Args:
            player: The player visiting the inn
            world: The game world
        """
        print("You enter the cozy village inn.")
        if player.gold >= 10:
            choice = input("Would you like to rest for the night? (10 gold) [y/n]: ").lower()
            if choice == 'y':
                player.gold -= 10
                player.heal(50)
                print("You have a good night's rest and feel rejuvenated.")
            else:
                print("You decide not to stay the night.")
        else:
            print("You don't have enough gold to stay the night.")

    def perform_quest(self, player: Player, world: World) -> None:
        """
        Perform a quest.

        Args:
            player: The player performing the quest
            world: The game world
        """
        print("You check the village quest board.")
        if generate_random_event(events=[("receive_quest", 30), (None, 70)]) == "receive_quest":
            print("You accept a quest to deliver a package to a hermit living on the mountain.")
            player.add_item("mysterious_package")
            print("Complete this quest by reaching the mountain peak.")

