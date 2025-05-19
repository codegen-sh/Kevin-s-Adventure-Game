"""
Mythical creatures module for Kevin's Adventure Game.
"""
from typing import Dict, List, Optional

from kevin_adventure.core.entity import Entity
from kevin_adventure.core.player import Player
from kevin_adventure.core.world import World


class MythicalCreature(Entity):
    """
    Mythical creature class.
    """

    def __init__(self, name: str, description: str):
        """
        Initialize a new mythical creature.

        Args:
            name: The creature's name
            description: The creature's description
        """
        super().__init__(name)
        self.description = description

    def interact(self, player: Player, world: World) -> None:
        """
        Interact with the creature.

        Args:
            player: The player interacting with the creature
            world: The game world
        """
        print(f"You interact with {self.name}, but nothing special happens.")


class Phoenix(MythicalCreature):
    """
    Phoenix mythical creature class.
    """

    def __init__(self):
        """
        Initialize a new Phoenix creature.
        """
        super().__init__("Phoenix", "A majestic bird with feathers of flame that can be reborn from its ashes.")

    def interact(self, player: Player, world: World) -> None:
        """
        Interact with the Phoenix.

        Args:
            player: The player interacting with the Phoenix
            world: The game world
        """
        print("The phoenix's flames wash over you, but they don't burn. Instead, they heal your wounds.")
        player.heal(50)


class Unicorn(MythicalCreature):
    """
    Unicorn mythical creature class.
    """

    def __init__(self):
        """
        Initialize a new Unicorn creature.
        """
        super().__init__("Unicorn", "A beautiful horse-like creature with a single spiral horn on its forehead.")

    def interact(self, player: Player, world: World) -> None:
        """
        Interact with the Unicorn.

        Args:
            player: The player interacting with the Unicorn
            world: The game world
        """
        print("The unicorn approaches you and allows you to stroke its mane. A single hair falls out.")
        player.add_item("unicorn_hair")


class Dragon(MythicalCreature):
    """
    Dragon mythical creature class.
    """

    def __init__(self):
        """
        Initialize a new Dragon creature.
        """
        super().__init__("Dragon", "A massive reptilian creature with scales, wings, and the ability to breathe fire.")

    def interact(self, player: Player, world: World) -> None:
        """
        Interact with the Dragon.

        Args:
            player: The player interacting with the Dragon
            world: The game world
        """
        print("The dragon regards you with ancient eyes. It sheds a scale, which falls at your feet.")
        player.add_item("dragon_scale")


def summon_mythical_creature(world: World, player: Player, creature_type: str) -> bool:
    """
    Summon a mythical creature to aid the player.

    Args:
        world: The game world
        player: The player summoning the creature
        creature_type: The type of mythical creature to summon

    Returns:
        True if summoning was successful, False otherwise
    """
    if creature_type == "phoenix":
        print("A majestic phoenix appears in a burst of flames!")
        phoenix = Phoenix()
        phoenix.interact(player, world)
    elif creature_type == "unicorn":
        print("A graceful unicorn materializes before you!")
        unicorn = Unicorn()
        unicorn.interact(player, world)
    elif creature_type == "dragon":
        print("A powerful dragon descends from the sky! The dragon is friendly and will help you.")
        dragon = Dragon()
        dragon.interact(player, world)
    else:
        print(f"Unknown creature type: {creature_type}")
        return False

    return True

