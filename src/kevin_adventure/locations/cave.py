"""
Cave location module for Kevin's Adventure Game.
"""
from typing import Dict, List, Optional

from kevin_adventure.core.player import Player
from kevin_adventure.core.world import World
from kevin_adventure.locations.location import Location
from kevin_adventure.utils.random_events import generate_random_event


class Cave(Location):
    """
    Cave location class.
    """

    def __init__(self):
        """
        Initialize a new Cave location.
        """
        super().__init__(
            "Cave",
            "A dark, damp cave with echoing sounds and glittering minerals on the walls.",
            ["Forest"],
            ["torch", "gemstone"]
        )

    def interact(self, player: Player, world: World) -> None:
        """
        Interact with the cave.

        Args:
            player: The player interacting with the cave
            world: The game world
        """
        print("You enter the dark, mysterious cave. Water drips from the ceiling and echoes fill the air.")

        # Check if player has a torch
        has_torch = "torch" in player.inventory
        if not has_torch:
            print("It's very dark in here. A torch would be helpful.")
            choice = input("Do you want to continue anyway? (y/n): ").lower()
            if choice != 'y':
                print("You decide to leave the cave.")
                return

        while True:
            print("\nWhat would you like to do in the cave?")
            print("1. Explore deeper")
            print("2. Search for minerals")
            print("3. Listen to the cave")
            print("4. Look for hidden passages")
            print("5. Leave the cave")

            choice = input("Enter your choice (1-5): ")

            if choice == "1":
                self.explore_deeper(player, world, has_torch)
            elif choice == "2":
                self.search_for_minerals(player, world, has_torch)
            elif choice == "3":
                self.listen_to_cave(player, world)
            elif choice == "4":
                self.look_for_hidden_passages(player, world, has_torch)
            elif choice == "5":
                print("You decide to leave the cave.")
                break
            else:
                print("Invalid choice. Please try again.")

    def explore_deeper(self, player: Player, world: World, has_torch: bool) -> None:
        """
        Explore deeper into the cave.

        Args:
            player: The player exploring the cave
            world: The game world
            has_torch: Whether the player has a torch
        """
        print("You venture deeper into the cave.")
        
        # Different outcomes based on having a torch
        if has_torch:
            event = generate_random_event(events=[("find_treasure", 30), ("encounter_bats", 20), ("discover_underground_lake", 20), (None, 30)])
            
            if event == "find_treasure":
                print("Your torch illuminates a small chest hidden in a crevice!")
                player.add_item("ancient_coin")
                print("You found an ancient coin!")
            elif event == "encounter_bats":
                print("Your torch disturbs a colony of bats! They flutter around you in a panic.")
                print("You duck down and they eventually settle back down.")
            elif event == "discover_underground_lake":
                print("You discover a beautiful underground lake with crystal-clear water.")
                print("The torch light reflects off the water, creating a magical atmosphere.")
                player.heal(10)
                print("You feel refreshed just being in this peaceful place.")
            else:
                print("You explore for a while but find nothing of interest.")
        else:
            # Without a torch, more dangerous and less rewarding
            event = generate_random_event(events=[("trip", 40), ("get_lost", 30), (None, 30)])
            
            if event == "trip":
                print("In the darkness, you trip over a rock and fall!")
                player.damage(5)
                print("You should be more careful without a light source.")
            elif event == "get_lost":
                print("Without a light, you lose your sense of direction and wander in circles.")
                print("It takes you a while to find your way back to the cave entrance.")
                player.damage(3)
                print("The experience was exhausting.")
            else:
                print("You fumble around in the darkness but find nothing.")

    def search_for_minerals(self, player: Player, world: World, has_torch: bool) -> None:
        """
        Search for minerals in the cave.

        Args:
            player: The player searching for minerals
            world: The game world
            has_torch: Whether the player has a torch
        """
        print("You search the cave walls for interesting minerals.")
        
        # Different outcomes based on having a torch
        if has_torch:
            if generate_random_event(events=[("find_gemstone", 30), (None, 70)]) == "find_gemstone":
                print("Your torch reveals a sparkling gemstone embedded in the wall!")
                print("You carefully extract it.")
                player.add_item("gemstone")
            else:
                print("You find some interesting rock formations, but nothing valuable.")
        else:
            print("It's too dark to see any minerals clearly. You might need a torch.")

    def listen_to_cave(self, player: Player, world: World) -> None:
        """
        Listen to the sounds in the cave.

        Args:
            player: The player listening to the cave
            world: The game world
        """
        print("You stand still and listen carefully to the sounds of the cave.")
        
        event = generate_random_event(events=[("water_sound", 40), ("creature_sound", 30), (None, 30)])
        
        if event == "water_sound":
            print("You hear the sound of running water deeper in the cave.")
            print("There might be an underground stream or lake nearby.")
        elif event == "creature_sound":
            print("You hear strange rustling and chittering sounds from deeper in the cave.")
            print("Something might be living down here...")
        else:
            print("You hear nothing but the occasional drip of water and your own breathing.")

    def look_for_hidden_passages(self, player: Player, world: World, has_torch: bool) -> None:
        """
        Look for hidden passages in the cave.

        Args:
            player: The player looking for hidden passages
            world: The game world
            has_torch: Whether the player has a torch
        """
        print("You carefully examine the cave walls, looking for hidden passages.")
        
        # Different outcomes based on having a torch
        if has_torch:
            if generate_random_event(events=[("find_passage", 20), (None, 80)]) == "find_passage":
                print("Your torch reveals a narrow crack in the wall that seems to lead somewhere!")
                print("It's too small to explore now, but you make a mental note of its location.")
                # Future implementation: Add new location or special event
            else:
                print("You don't find any hidden passages this time.")
        else:
            print("It's too dark to effectively search for hidden passages. A torch would help.")

