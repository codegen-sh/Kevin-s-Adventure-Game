from game.entity import Entity
from game.player import add_item_to_inventory, heal_player


class MythicalCreature(Entity):
    """
    Represents a mythical creature in the game.
    
    This class handles creature attributes and interactions with the player.
    """
    
    def __init__(self, name, description="", power=0):
        """
        Initialize a new MythicalCreature.
        
        Args:
            name (str): The name of the creature
            description (str, optional): A description of the creature
            power (int, optional): The power level of the creature
        """
        super().__init__(name, description)
        self.power = power
    
    def interact(self, player, world):
        """
        Interact with the player.
        
        Args:
            player: The player interacting with the creature
            world: The game world
            
        Returns:
            bool: True if the interaction was successful, False otherwise
        """
        print(f"You encounter a {self.name}. It watches you curiously.")
        return True


# Dictionary of creature effects for backward compatibility
CREATURE_EFFECTS = {
    "phoenix": lambda player: heal_player(player, 50),
    "unicorn": lambda player: add_item_to_inventory(player, "unicorn_hair"),
    "dragon": lambda player: add_item_to_inventory(player, "dragon_scale")
}


def summon_mythical_creature(world, player, creature_type):
    """
    Summons a mythical creature to aid the player.

    Args:
    world (dict): The game world state
    player (dict): The player's current state
    creature_type (str): The type of mythical creature to summon

    Returns:
    bool: True if summoning was successful, False otherwise
    """
    if creature_type == "phoenix":
        print("A majestic phoenix appears in a burst of flames!")
        heal_player(player, 50)
    elif creature_type == "unicorn":
        print("A graceful unicorn materializes before you!")
        add_item_to_inventory(player, "unicorn_hair")
    elif creature_type == "dragon":
        print("A powerful dragon descends from the sky! The dragon is friendly and will help you.")
        add_item_to_inventory(player, "dragon_scale")
    else:
        print(f"Unknown creature type: {creature_type}")
        return False

    return True
