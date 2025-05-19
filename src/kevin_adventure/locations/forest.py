"""
Forest location module for Kevin's Adventure Game.
"""
from typing import Dict, List, Optional

from kevin_adventure.core.player import Player
from kevin_adventure.core.world import World
from kevin_adventure.locations.location import Location
from kevin_adventure.utils.random_events import generate_random_event


class Forest(Location):
    """
    Forest location class.
    """

    def __init__(self):
        """
        Initialize a new Forest location.
        """
        super().__init__(
            "Forest",
            "A dense, mysterious forest with towering trees and the sound of rustling leaves.",
            ["Village", "Cave"],
            ["stick", "berries"]
        )

    def interact(self, player: Player, world: World) -> None:
        """
        Interact with the forest.

        Args:
            player: The player interacting with the forest
            world: The game world
        """
        print("You enter the lush, green forest. The air is filled with the sounds of birds and rustling leaves.")

        while True:
            print("\nWhat would you like to do in the forest?")
            print("1. Explore deeper")
            print("2. Climb a tree")
            print("3. Listen to the forest")
            print("4. Forage for food")
            print("5. Leave the forest")

            choice = input("Enter your choice (1-5): ")

            if choice == "1":
                self.explore_forest(player, world)
            elif choice == "2":
                self.climb_tree(player, world)
            elif choice == "3":
                self.listen_to_forest(player, world)
            elif choice == "4":
                self.forage_for_food(player, world)
            elif choice == "5":
                print("You decide to leave the forest.")
                break
            else:
                print("Invalid choice. Please try again.")

    def explore_forest(self, player: Player, world: World) -> None:
        """
        Explore the forest.

        Args:
            player: The player exploring the forest
            world: The game world
        """
        print("You decide to explore deeper into the forest.")
        event = generate_random_event(events=[("find_berries", 40), ("encounter_animal", 25), ("discover_clearing", 10), (None, 25)])

        if event == "find_berries":
            print("You stumble upon a bush full of ripe berries!")
            player.add_item("berries")
        elif event == "encounter_animal":
            print("You encounter a friendly deer. It allows you to approach and pet it.")
            player.heal(5)
            print("The peaceful interaction leaves you feeling refreshed.")
        elif event == "discover_clearing":
            print("You discover a beautiful clearing with a small pond.")
            # Future implementation: Add mythical creature encounter
        else:
            print("Your exploration yields nothing of note this time.")

    def climb_tree(self, player: Player, world: World) -> None:
        """
        Climb a tree in the forest.

        Args:
            player: The player climbing the tree
            world: The game world
        """
        print("You climb a tall tree to get a better view of the surrounding area.")
        print("From up here, you can see the mountain peaks in the distance and what looks like the entrance to a cave.")

    def listen_to_forest(self, player: Player, world: World) -> None:
        """
        Listen to the forest.

        Args:
            player: The player listening to the forest
            world: The game world
        """
        print("You stop and listen carefully to the sounds of the forest.")
        print("You hear a faint sound of rushing water in the distance. There might be a river nearby.")

    def forage_for_food(self, player: Player, world: World) -> None:
        """
        Forage for food in the forest.

        Args:
            player: The player foraging for food
            world: The game world
        """
        print("You search the forest floor for edible plants and mushrooms.")
        if generate_random_event(events=[("find_mushrooms", 30), (None, 70)]) == "find_mushrooms":
            print("You find some edible mushrooms!")
            player.add_item("mushrooms")
        else:
            print("You don't find anything edible this time.")

