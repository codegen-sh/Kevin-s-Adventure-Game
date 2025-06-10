"""
Mountain location module for Kevin's Adventure Game.
"""
from typing import Dict, List, Optional

from kevin_adventure.core.player import Player
from kevin_adventure.core.world import World
from kevin_adventure.locations.location import Location
from kevin_adventure.utils.random_events import generate_random_event


class Mountain(Location):
    """
    Mountain location class.
    """

    def __init__(self):
        """
        Initialize a new Mountain location.
        """
        super().__init__(
            "Mountain",
            "A tall, snow-capped mountain with treacherous paths and breathtaking views.",
            ["Village"],
            ["rope", "pickaxe"]
        )

    def interact(self, player: Player, world: World) -> None:
        """
        Interact with the mountain.

        Args:
            player: The player interacting with the mountain
            world: The game world
        """
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
                self.check_weather(player, world)
            elif choice == "2":
                self.use_climbing_gear(player, world)
            elif choice == "3":
                self.search_for_herbs(player, world)
            elif choice == "4":
                self.reach_peak(player, world)
            elif choice == "5":
                self.explore_mountain_cave(player, world)
            elif choice == "6":
                print("You decide to descend the mountain.")
                break
            else:
                print("Invalid choice. Please try again.")

    def check_weather(self, player: Player, world: World) -> None:
        """
        Check the weather on the mountain.

        Args:
            player: The player checking the weather
            world: The game world
        """
        print("You pause to check the weather conditions.")
        event = generate_random_event(events=[("clear_skies", 50), ("incoming_storm", 50)])

        if event == "clear_skies":
            print("The skies are clear, offering a breathtaking view of the surrounding lands.")
        elif event == "incoming_storm":
            print("You notice dark clouds gathering. A storm might be approaching.")
        else:
            print("The weather seems stable for now.")

    def use_climbing_gear(self, player: Player, world: World) -> None:
        """
        Use climbing gear on the mountain.

        Args:
            player: The player using climbing gear
            world: The game world
        """
        if "rope" in player.inventory:
            print("You use your rope to safely navigate a particularly treacherous part of the path.")
            player.heal(5)
            print("Your careful climbing technique leaves you feeling confident.")
        else:
            print("This part of the path looks dangerous. A rope would be useful here.")
            player.damage(10)
            print("You slip and take some damage while climbing. Be more careful!")

    def search_for_herbs(self, player: Player, world: World) -> None:
        """
        Search for herbs on the mountain.

        Args:
            player: The player searching for herbs
            world: The game world
        """
        print("You search the mountainside for rare herbs.")
        if generate_random_event(events=[("find_herbs", 30), (None, 70)]) == "find_herbs":
            print("You find some rare medicinal herbs!")
            player.add_item("mountain_herbs")
        else:
            print("You don't find any useful herbs this time.")

    def reach_peak(self, player: Player, world: World) -> None:
        """
        Reach the peak of the mountain.

        Args:
            player: The player reaching the peak
            world: The game world
        """
        print("You finally reach the mountain peak!")
        if "mysterious_package" in player.inventory:
            print("You find the hermit's hut and deliver the mysterious package.")
            player.remove_item("mysterious_package")
            player.add_item("hermit's_blessing")
            print("The hermit thanks you and gives you their blessing, which fills you with energy.")
            player.heal(100)
            # Future implementation: Add mythical creature encounter

        print("The view from the top is spectacular. You can see the entire game world spread out before you.")

    def explore_mountain_cave(self, player: Player, world: World) -> None:
        """
        Explore a cave on the mountain.

        Args:
            player: The player exploring the cave
            world: The game world
        """
        print("You discover a small cave entrance on the mountainside.")
        if "torch" in player.inventory:
            print("You use your torch to explore the mountain cave.")
            if generate_random_event(events=[("find_treasure", 20), (None, 80)]) == "find_treasure":
                print("You discover an old treasure chest hidden in the cave!")
                player.add_item("ancient_coin")
            else:
                print("The cave is empty, but it provides good shelter from the elements.")
        else:
            print("It's too dark to explore the cave without a torch.")

