"""
Village location module for Kevin's Adventure Game.
"""
from typing import Dict, TYPE_CHECKING

from src.game.location import Location

if TYPE_CHECKING:
    from src.game.player import Player
    from src.game.world import World


class Village(Location):
    """
    Represents the village location in the game.
    """

    def __init__(self):
        """Initialize the village location."""
        super().__init__(
            "Village",
            "A small, peaceful village with thatched-roof houses and friendly inhabitants."
        )
        self.connections = ["Forest", "Mountain"]
        self.items = ["map", "bread"]

    def enter(self, player: 'Player', world: 'World') -> None:
        """
        Handle player entering the village.

        Args:
            player: The player entering the village
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
                self._visit_shop(player, world)
            elif choice == "2":
                self._talk_to_villagers(player, world)
            elif choice == "3":
                self._visit_inn(player, world)
            elif choice == "4":
                self._check_for_quests(player, world)
            elif choice == "5":
                print("You decide to leave the village.")
                break
            else:
                print("Invalid choice. Please try again.")

    def get_available_actions(self) -> Dict[str, str]:
        """
        Get available actions in the village.

        Returns:
            A dictionary of available actions
        """
        actions = super().get_available_actions()
        actions.update({
            "4": "Visit the shop",
            "5": "Talk to villagers",
            "6": "Visit the inn",
            "7": "Check for quests"
        })
        return actions

    def _visit_shop(self, player: 'Player', world: 'World') -> None:
        """
        Handle visiting the village shop.

        Args:
            player: The player
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

    def _talk_to_villagers(self, player: 'Player', world: 'World') -> None:
        """
        Handle talking to villagers.

        Args:
            player: The player
            world: The game world
        """
        from src.utils.random_events import generate_random_event
        
        print("You approach a group of villagers to chat.")
        event = generate_random_event([
            ("hear_rumor", 40),
            ("receive_advice", 30),
            (None, 30)
        ])

        if event == "hear_rumor":
            print("You overhear an interesting rumor about treasure hidden in the nearby cave.")
        elif event == "receive_advice":
            print("An old villager gives you advice about surviving in the forest.")
            player.heal(10)
            print("Their wisdom makes you feel more prepared for your adventures.")
        else:
            print("You have a pleasant but uneventful conversation with the villagers.")

    def _visit_inn(self, player: 'Player', world: 'World') -> None:
        """
        Handle visiting the village inn.

        Args:
            player: The player
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

    def _check_for_quests(self, player: 'Player', world: 'World') -> None:
        """
        Handle checking for quests.

        Args:
            player: The player
            world: The game world
        """
        from src.utils.random_events import generate_random_event
        
        print("You check the village quest board.")
        if generate_random_event([("receive_quest", 30), (None, 70)]) == "receive_quest":
            print("You accept a quest to deliver a package to a hermit living on the mountain.")
            player.add_item("mysterious_package")
            print("Complete this quest by reaching the mountain peak.")
        else:
            print("There are no available quests at the moment.")

