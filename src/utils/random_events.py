"""
Random events module for Kevin's Adventure Game.
Contains functions for generating and handling random events.
"""
import random
from typing import Any, Dict, List, Optional, Tuple, TYPE_CHECKING

from src.utils.text_formatting import print_event

if TYPE_CHECKING:
    from src.game.player import Player
    from src.game.world import World


def generate_random_event(events: List[Tuple[Optional[str], int]]) -> Optional[str]:
    """
    Generate a random event based on probabilities.

    Args:
        events: A list of tuples (event_name, probability)

    Returns:
        The selected event name, or None if no event was selected
    """
    event_names = [event[0] for event in events]
    probabilities = [event[1] for event in events]
    return random.choices(event_names, weights=probabilities)[0]


class RandomEventHandler:
    """
    Handles random events in the game.
    """

    def __init__(self):
        """Initialize the random event handler."""
        pass

    def handle_random_encounter(self, player: 'Player', world: 'World') -> None:
        """
        Handle a random encounter event.

        Args:
            player: The player
            world: The game world
        """
        encounters = [
            "friendly_traveler",
            "merchant",
            "lost_child",
            "wild_animal",
            "bandit"
        ]
        encounter = random.choice(encounters)

        if encounter == "friendly_traveler":
            print_event("You meet a friendly traveler who shares some of their supplies with you.")
            player.heal(10)
        elif encounter == "merchant":
            print_event("A wandering merchant offers to sell you a mysterious potion.")
            if player.gold >= 20:
                choice = input("Do you want to buy the potion for 20 gold? (y/n): ").lower()
                if choice == 'y':
                    player.gold -= 20
                    player.add_item("mysterious_potion")
                    print("You bought the mysterious potion.")
                else:
                    print("You decline the offer.")
            else:
                print("You don't have enough gold to buy the potion.")
        elif encounter == "lost_child":
            print_event("You find a lost child. After helping them return to their village, the grateful parents reward you.")
            player.gold += 15
        elif encounter == "wild_animal":
            print_event("A wild animal attacks you!")
            player.take_damage(15)
        elif encounter == "bandit":
            print_event("A bandit tries to rob you!")
            if "sword" in player.inventory:
                print("You use your sword to fend off the bandit.")
            elif player.gold > 0:
                stolen_gold = min(player.gold, 10)
                player.gold -= stolen_gold
                print(f"The bandit steals {stolen_gold} gold from you.")
            else:
                print("The bandit finds nothing of value and leaves you alone.")

    def find_treasure(self, player: 'Player') -> None:
        """
        Handle finding a treasure.

        Args:
            player: The player
        """
        treasures = [
            ("gold_coin", 5),
            ("silver_necklace", 10),
            ("ancient_artifact", 20),
            ("magic_ring", 30)
        ]
        treasure, value = random.choice(treasures)
        print_event(f"You found a {treasure} worth {value} gold!")
        player.add_item(treasure)
        player.gold += value

    def weather_event(self, world: 'World') -> None:
        """
        Handle a weather change event.

        Args:
            world: The game world
        """
        from src.game.weather import Weather
        
        weathers = ["clear", "cloudy", "rainy", "stormy", "foggy", "windy"]
        new_weather = random.choice(weathers)
        print_event(f"The weather changes to {new_weather}.")
        
        # Update the weather in the world
        if hasattr(world, 'weather') and isinstance(world.weather, Weather):
            world.weather.current_weather = new_weather

    def trap_event(self, player: 'Player') -> None:
        """
        Handle a trap event.

        Args:
            player: The player
        """
        traps = ["pitfall", "snare", "poison_dart"]
        trap = random.choice(traps)
        print_event(f"You've triggered a {trap} trap!")
        damage = random.randint(5, 15)
        player.take_damage(damage)

    def special_discovery(self, player: 'Player', world: 'World') -> None:
        """
        Handle a special discovery event.

        Args:
            player: The player
            world: The game world
        """
        discoveries = [
            "hidden_cave",
            "ancient_ruins",
            "magical_spring",
            "abandoned_camp"
        ]
        discovery = random.choice(discoveries)
        print_event(f"You've discovered a {discovery.replace('_', ' ')}!")

        if discovery == "hidden_cave":
            world.update_state("hidden_cave_discovered")
            print("You mark the location of the hidden cave on your map.")
        elif discovery == "ancient_ruins":
            player.add_item("ancient_artifact")
            print("You find an ancient artifact among the ruins.")
        elif discovery == "magical_spring":
            player.heal(30)
            print("You drink from the magical spring and feel rejuvenated.")
        elif discovery == "abandoned_camp":
            items = ["rope", "torch", "map"]
            found_item = random.choice(items)
            player.add_item(found_item)
            print(f"You search the abandoned camp and find a {found_item}.")

    def apply_random_event(self, player: 'Player', world: 'World') -> None:
        """
        Apply a random event to the game state.

        Args:
            player: The player
            world: The game world
        """
        event = generate_random_event([
            ("nothing", 20),
            ("find_item", 20),
            ("encounter", 20),
            ("weather_change", 10),
            ("trap", 10),
            ("special_discovery", 20)
        ])

        if event == "nothing":
            return  # No event occurs
        elif event == "find_item":
            self.find_treasure(player)
        elif event == "encounter":
            self.handle_random_encounter(player, world)
        elif event == "weather_change":
            self.weather_event(world)
        elif event == "trap":
            self.trap_event(player)
        elif event == "special_discovery":
            self.special_discovery(player, world)

