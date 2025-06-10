"""
Forest location module for Kevin's Adventure Game.
"""
from typing import Dict, TYPE_CHECKING

from src.game.location import Location

if TYPE_CHECKING:
    from src.game.player import Player
    from src.game.world import World


class Forest(Location):
    """
    Represents the forest location in the game.
    """

    def __init__(self):
        """Initialize the forest location."""
        super().__init__(
            "Forest",
            "A dense, mysterious forest with towering trees and the sound of rustling leaves."
        )
        self.connections = ["Village", "Cave"]
        self.items = ["stick", "berries"]

    def enter(self, player: 'Player', world: 'World') -> None:
        """
        Handle player entering the forest.

        Args:
            player: The player entering the forest
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
                self._explore_forest(player, world)
            elif choice == "2":
                self._climb_tree(player, world)
            elif choice == "3":
                self._listen_to_forest(player, world)
            elif choice == "4":
                self._forage_for_food(player, world)
            elif choice == "5":
                print("You decide to leave the forest.")
                break
            else:
                print("Invalid choice. Please try again.")

    def get_available_actions(self) -> Dict[str, str]:
        """
        Get available actions in the forest.

        Returns:
            A dictionary of available actions
        """
        actions = super().get_available_actions()
        actions.update({
            "4": "Explore deeper",
            "5": "Climb a tree",
            "6": "Listen to the forest",
            "7": "Forage for food"
        })
        return actions

    def _explore_forest(self, player: 'Player', world: 'World') -> None:
        """
        Handle exploring deeper into the forest.

        Args:
            player: The player
            world: The game world
        """
        from src.utils.random_events import generate_random_event
        
        print("You decide to explore deeper into the forest.")
        event = generate_random_event([
            ("find_berries", 40),
            ("encounter_animal", 25),
            ("discover_clearing", 10),
            (None, 25)
        ])

        if event == "find_berries":
            print("You stumble upon a bush full of ripe berries!")
            player.add_item("berries")
        elif event == "encounter_animal":
            print("You encounter a friendly deer. It allows you to approach and pet it.")
            player.heal(5)
            print("The peaceful interaction leaves you feeling refreshed.")
        elif event == "discover_clearing":
            print("You discover a beautiful clearing with a small pond.")
            # Implement mythical creature encounter
            if "unicorn_hair" not in player.inventory:
                print("A graceful unicorn appears at the edge of the clearing!")
                print("It approaches you cautiously, then allows you to take a strand of its mane.")
                player.add_item("unicorn_hair")
            world.update_state("clearing_discovered")
        else:
            print("Your exploration yields nothing of note this time.")

    def _climb_tree(self, player: 'Player', world: 'World') -> None:
        """
        Handle climbing a tree in the forest.

        Args:
            player: The player
            world: The game world
        """
        print("You climb a tall tree to get a better view of the surrounding area.")
        print("From up here, you can see the mountain peaks in the distance and what looks like the entrance to a cave.")
        
        # If the player hasn't discovered the cave yet, this is a good way to hint at it
        if "Cave" not in world.get_all_locations():
            print("You notice what appears to be a cave entrance to the east. You mark it on your map.")
            world.update_state("cave_discovered")

    def _listen_to_forest(self, player: 'Player', world: 'World') -> None:
        """
        Handle listening to the forest.

        Args:
            player: The player
            world: The game world
        """
        from src.utils.random_events import generate_random_event
        
        print("You stop and listen carefully to the sounds of the forest.")
        print("You hear a faint sound of rushing water in the distance. There might be a river nearby.")
        
        if generate_random_event([("discover_river", 20), (None, 80)]) == "discover_river":
            print("You've discovered a river!")
            world.update_state("river_discovered")
        else:
            print("You don't find anything of note this time.")

    def _forage_for_food(self, player: 'Player', world: 'World') -> None:
        """
        Handle foraging for food in the forest.

        Args:
            player: The player
            world: The game world
        """
        from src.utils.random_events import generate_random_event
        
        print("You search the forest floor for edible plants and mushrooms.")
        if generate_random_event([("find_mushrooms", 30), (None, 70)]) == "find_mushrooms":
            print("You find some edible mushrooms!")
            player.add_item("mushrooms")
        else:
            print("You don't find anything edible this time.")

