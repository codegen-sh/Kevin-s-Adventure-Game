"""
Cave location module for Kevin's Adventure Game.
"""
from typing import Dict, TYPE_CHECKING

from src.game.location import Location

if TYPE_CHECKING:
    from src.game.player import Player
    from src.game.world import World


class Cave(Location):
    """
    Represents the cave location in the game.
    """

    def __init__(self):
        """Initialize the cave location."""
        super().__init__(
            "Cave",
            "A dark, damp cave with echoing sounds and glittering minerals on the walls."
        )
        self.connections = ["Forest"]
        self.items = ["torch", "gemstone"]
        self.is_lit = False

    def enter(self, player: 'Player', world: 'World') -> None:
        """
        Handle player entering the cave.

        Args:
            player: The player entering the cave
            world: The game world
        """
        if not self.is_lit and not player.has_item("torch"):
            print("The cave is pitch black. You can barely see anything. A torch would be useful here.")
            choice = input("Do you want to continue anyway? (y/n): ").lower()
            if choice != 'y':
                print("You decide to leave the cave and come back when you have a torch.")
                return
        elif player.has_item("torch") and not self.is_lit:
            print("You light your torch, illuminating the dark cave around you.")
            self.is_lit = True
            self.description += " The cave is now well-lit by your torch."
        
        print("You explore the echoing cave, your footsteps reverberating off the walls.")
        
        while True:
            print("\nWhat would you like to do in the cave?")
            print("1. Explore deeper")
            print("2. Mine for minerals")
            print("3. Listen for sounds")
            print("4. Search for hidden passages")
            print("5. Leave the cave")

            choice = input("Enter your choice (1-5): ")

            if choice == "1":
                self._explore_deeper(player, world)
            elif choice == "2":
                self._mine_for_minerals(player, world)
            elif choice == "3":
                self._listen_for_sounds(player, world)
            elif choice == "4":
                self._search_for_passages(player, world)
            elif choice == "5":
                print("You decide to leave the cave.")
                break
            else:
                print("Invalid choice. Please try again.")

    def get_available_actions(self) -> Dict[str, str]:
        """
        Get available actions in the cave.

        Returns:
            A dictionary of available actions
        """
        actions = super().get_available_actions()
        actions.update({
            "4": "Explore deeper",
            "5": "Mine for minerals",
            "6": "Listen for sounds",
            "7": "Search for hidden passages"
        })
        return actions

    def _explore_deeper(self, player: 'Player', world: 'World') -> None:
        """
        Handle exploring deeper into the cave.

        Args:
            player: The player
            world: The game world
        """
        from src.utils.random_events import generate_random_event
        
        if not self.is_lit and not player.has_item("torch"):
            print("It's too dark to explore deeper without a torch. You might get lost or hurt.")
            player.take_damage(5)
            print("You stumble in the darkness and hurt yourself.")
            return
        
        print("You venture deeper into the cave, the walls narrowing around you.")
        event = generate_random_event([
            ("find_treasure", 30),
            ("encounter_bats", 20),
            ("discover_underground_lake", 15),
            (None, 35)
        ])

        if event == "find_treasure":
            print("You discover a small treasure chest hidden in a crevice!")
            player.add_item("gold_coins")
            player.gold += 20
            print("You found 20 gold coins!")
        elif event == "encounter_bats":
            print("A swarm of bats suddenly flies past you, startled by your presence!")
            if self.is_lit:
                print("Your torch keeps them at bay, and they quickly disappear into the darkness.")
            else:
                print("In the darkness, you panic and get scratched by the bats.")
                player.take_damage(10)
        elif event == "discover_underground_lake":
            print("You discover a beautiful underground lake with crystal-clear water.")
            print("The minerals in the walls reflect in the water, creating a magical atmosphere.")
            player.heal(10)
            print("You feel refreshed just being in this peaceful place.")
            world.update_state("underground_lake_discovered")
        else:
            print("Your exploration yields nothing of note this time.")

    def _mine_for_minerals(self, player: 'Player', world: 'World') -> None:
        """
        Handle mining for minerals in the cave.

        Args:
            player: The player
            world: The game world
        """
        from src.utils.random_events import generate_random_event
        
        if not player.has_item("pickaxe"):
            print("You need a pickaxe to mine effectively. Your hands aren't strong enough to break the rock.")
            return
        
        print("You use your pickaxe to mine the cave walls for valuable minerals.")
        event = generate_random_event([
            ("find_gemstone", 25),
            ("find_gold", 15),
            ("cave_in", 10),
            (None, 50)
        ])

        if event == "find_gemstone":
            print("You discover a beautiful gemstone embedded in the rock!")
            player.add_item("gemstone")
        elif event == "find_gold":
            print("You find a small vein of gold in the rock!")
            player.gold += 15
            print("You extract 15 gold worth of ore.")
        elif event == "cave_in":
            print("Your mining causes a small cave-in! Rocks fall from the ceiling!")
            player.take_damage(15)
            print("You're hit by falling debris.")
        else:
            print("You mine for a while but don't find anything valuable.")

    def _listen_for_sounds(self, player: 'Player', world: 'World') -> None:
        """
        Handle listening for sounds in the cave.

        Args:
            player: The player
            world: The game world
        """
        from src.utils.random_events import generate_random_event
        
        print("You stand still and listen carefully to the sounds in the cave.")
        event = generate_random_event([
            ("hear_water", 40),
            ("hear_creature", 20),
            (None, 40)
        ])

        if event == "hear_water":
            print("You hear the sound of running water somewhere deeper in the cave.")
            if not world.state.get("underground_lake_discovered", False):
                print("There might be an underground lake or river nearby.")
        elif event == "hear_creature":
            print("You hear strange noises coming from deeper in the cave.")
            print("It sounds like some kind of creature, but you can't tell what it is.")
            world.update_state("cave_creature_heard")
        else:
            print("You hear nothing but the occasional drip of water and your own breathing.")

    def _search_for_passages(self, player: 'Player', world: 'World') -> None:
        """
        Handle searching for hidden passages in the cave.

        Args:
            player: The player
            world: The game world
        """
        from src.utils.random_events import generate_random_event
        
        if not self.is_lit and not player.has_item("torch"):
            print("It's too dark to search effectively without a torch.")
            return
        
        print("You carefully search the cave walls for hidden passages or secret chambers.")
        event = generate_random_event([
            ("find_passage", 20),
            ("find_ancient_writing", 15),
            (None, 65)
        ])

        if event == "find_passage":
            print("You discover a narrow passage hidden behind a rock formation!")
            if not world.state.get("hidden_passage_discovered", False):
                print("This passage might lead to unexplored parts of the cave system.")
                world.update_state("hidden_passage_discovered")
                # In a more complex game, this could unlock a new location
        elif event == "find_ancient_writing":
            print("You discover ancient writings carved into the cave wall!")
            print("They appear to be in a language you don't understand, but they seem important.")
            world.update_state("ancient_writing_discovered")
        else:
            print("Your search reveals nothing unusual about the cave walls.")

