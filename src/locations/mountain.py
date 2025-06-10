"""
Mountain location module for Kevin's Adventure Game.
"""
from typing import Dict, TYPE_CHECKING

from src.game.location import Location

if TYPE_CHECKING:
    from src.game.player import Player
    from src.game.world import World


class Mountain(Location):
    """
    Represents the mountain location in the game.
    """

    def __init__(self):
        """Initialize the mountain location."""
        super().__init__(
            "Mountain",
            "A tall, snow-capped mountain with treacherous paths and breathtaking views."
        )
        self.connections = ["Village"]
        self.items = ["rope", "pickaxe"]

    def enter(self, player: 'Player', world: 'World') -> None:
        """
        Handle player entering the mountain.

        Args:
            player: The player entering the mountain
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
                self._check_weather(player, world)
            elif choice == "2":
                self._use_climbing_gear(player, world)
            elif choice == "3":
                self._search_for_herbs(player, world)
            elif choice == "4":
                self._reach_peak(player, world)
            elif choice == "5":
                self._explore_mountain_cave(player, world)
            elif choice == "6":
                print("You decide to descend the mountain.")
                break
            else:
                print("Invalid choice. Please try again.")

    def get_available_actions(self) -> Dict[str, str]:
        """
        Get available actions on the mountain.

        Returns:
            A dictionary of available actions
        """
        actions = super().get_available_actions()
        actions.update({
            "4": "Check weather",
            "5": "Use climbing gear",
            "6": "Search for herbs",
            "7": "Try to reach the peak",
            "8": "Explore mountain cave"
        })
        return actions

    def _check_weather(self, player: 'Player', world: 'World') -> None:
        """
        Handle checking the weather on the mountain.

        Args:
            player: The player
            world: The game world
        """
        from src.utils.random_events import generate_random_event
        
        print("You pause to check the weather conditions.")
        
        # Use the weather system if available
        if hasattr(world, 'weather'):
            print(world.weather.describe_weather())
            print(world.weather.forecast())
        else:
            # Fallback if weather system is not available
            event = generate_random_event([
                ("clear_skies", 50),
                ("incoming_storm", 50)
            ])

            if event == "clear_skies":
                print("The skies are clear, offering a breathtaking view of the surrounding lands.")
                world.update_state("improve_visibility")
            elif event == "incoming_storm":
                print("You notice dark clouds gathering. A storm might be approaching.")
                world.update_state("approaching_storm")
            else:
                print("The weather seems stable for now.")

    def _use_climbing_gear(self, player: 'Player', world: 'World') -> None:
        """
        Handle using climbing gear on the mountain.

        Args:
            player: The player
            world: The game world
        """
        if player.has_item("rope"):
            print("You use your rope to safely navigate a particularly treacherous part of the path.")
            player.heal(5)
            print("Your careful climbing technique leaves you feeling confident.")
        else:
            print("This part of the path looks dangerous. A rope would be useful here.")
            player.take_damage(10)
            print("You slip and take some damage while climbing. Be more careful!")

    def _search_for_herbs(self, player: 'Player', world: 'World') -> None:
        """
        Handle searching for herbs on the mountain.

        Args:
            player: The player
            world: The game world
        """
        from src.utils.random_events import generate_random_event
        
        print("You search the mountainside for rare herbs.")
        if generate_random_event([("find_herbs", 30), (None, 70)]) == "find_herbs":
            print("You find some rare medicinal herbs!")
            player.add_item("mountain_herbs")
        else:
            print("You don't find any useful herbs this time.")

    def _reach_peak(self, player: 'Player', world: 'World') -> None:
        """
        Handle reaching the mountain peak.

        Args:
            player: The player
            world: The game world
        """
        print("You finally reach the mountain peak!")
        if player.has_item("mysterious_package"):
            print("You find the hermit's hut and deliver the mysterious package.")
            player.remove_item("mysterious_package")
            player.add_item("hermit's_blessing")
            print("The hermit thanks you and gives you their blessing, which fills you with energy.")
            player.heal(100)
            
            # Mythical creature encounter
            print("As you turn to leave, a majestic phoenix appears in a burst of flames!")
            player.add_item("phoenix_feather")
            print("The phoenix leaves behind a glowing feather before flying away.")

        print("The view from the top is spectacular. You can see the entire game world spread out before you.")
        world.update_state("map_revealed")

    def _explore_mountain_cave(self, player: 'Player', world: 'World') -> None:
        """
        Handle exploring a cave on the mountain.

        Args:
            player: The player
            world: The game world
        """
        from src.utils.random_events import generate_random_event
        
        print("You discover a small cave entrance on the mountainside.")
        if player.has_item("torch"):
            print("You use your torch to explore the mountain cave.")
            if generate_random_event([("find_treasure", 20), (None, 80)]) == "find_treasure":
                print("You discover an old treasure chest hidden in the cave!")
                player.add_item("ancient_coin")
            else:
                print("The cave is empty, but it provides good shelter from the elements.")
        else:
            print("It's too dark to explore the cave without a torch.")

