"""
Module for handling mythical creatures in the game.
"""

from enum import Enum, auto

from game.player import add_item_to_inventory, heal_player
from game.state import update_world_state


class CreatureType(Enum):
    """Enum for mythical creature types."""
    PHOENIX = auto()
    UNICORN = auto()
    DRAGON = auto()
    GRIFFIN = auto()
    MERMAID = auto()
    CENTAUR = auto()
    MINOTAUR = auto()
    FAIRY = auto()


class MythicalCreature:
    """
    A class to represent a mythical creature in the game.
    
    Attributes:
        creature_type (CreatureType): The type of creature
        name (str): The name of the creature
        description (str): A description of the creature
        friendly (bool): Whether the creature is friendly
        abilities (list): A list of the creature's abilities
    """
    
    def __init__(self, creature_type, name=None, description=None, friendly=True, abilities=None):
        """
        Initialize a new MythicalCreature.
        
        Args:
            creature_type (CreatureType): The type of creature
            name (str, optional): The name of the creature. Defaults to None.
            description (str, optional): A description of the creature. Defaults to None.
            friendly (bool, optional): Whether the creature is friendly. Defaults to True.
            abilities (list, optional): A list of the creature's abilities. Defaults to None.
        """
        self.creature_type = creature_type
        self.name = name if name else self._get_default_name()
        self.description = description if description else self._get_default_description()
        self.friendly = friendly
        self.abilities = abilities if abilities else self._get_default_abilities()
    
    def _get_default_name(self):
        """
        Get the default name for the creature type.
        
        Returns:
            str: The default name
        """
        names = {
            CreatureType.PHOENIX: "Ember",
            CreatureType.UNICORN: "Starlight",
            CreatureType.DRAGON: "Scales",
            CreatureType.GRIFFIN: "Talon",
            CreatureType.MERMAID: "Coral",
            CreatureType.CENTAUR: "Hoofbeats",
            CreatureType.MINOTAUR: "Horns",
            CreatureType.FAIRY: "Twinkle"
        }
        return names.get(self.creature_type, "Unknown Creature")
    
    def _get_default_description(self):
        """
        Get the default description for the creature type.
        
        Returns:
            str: The default description
        """
        descriptions = {
            CreatureType.PHOENIX: "A majestic bird with feathers of flame that can be reborn from its ashes.",
            CreatureType.UNICORN: "A beautiful horse-like creature with a single spiral horn on its forehead.",
            CreatureType.DRAGON: "A massive reptilian creature with scales, wings, and the ability to breathe fire.",
            CreatureType.GRIFFIN: "A creature with the body of a lion and the head and wings of an eagle.",
            CreatureType.MERMAID: "A creature with the upper body of a human and the tail of a fish.",
            CreatureType.CENTAUR: "A creature with the upper body of a human and the lower body of a horse.",
            CreatureType.MINOTAUR: "A creature with the body of a man and the head of a bull.",
            CreatureType.FAIRY: "A tiny humanoid creature with insect-like wings and magical abilities."
        }
        return descriptions.get(self.creature_type, "A mysterious mythical creature.")
    
    def _get_default_abilities(self):
        """
        Get the default abilities for the creature type.
        
        Returns:
            list: The default abilities
        """
        abilities = {
            CreatureType.PHOENIX: ["rebirth", "healing_flame", "flight"],
            CreatureType.UNICORN: ["healing_touch", "purification", "teleportation"],
            CreatureType.DRAGON: ["fire_breath", "flight", "ancient_wisdom"],
            CreatureType.GRIFFIN: ["flight", "enhanced_vision", "strength"],
            CreatureType.MERMAID: ["water_breathing", "enchanting_song", "weather_control"],
            CreatureType.CENTAUR: ["speed", "archery", "navigation"],
            CreatureType.MINOTAUR: ["strength", "maze_navigation", "intimidation"],
            CreatureType.FAIRY: ["flight", "nature_magic", "invisibility"]
        }
        return abilities.get(self.creature_type, [])
    
    def interact(self, player, world):
        """
        Interact with the creature.
        
        Args:
            player: The player
            world: The world state
        
        Returns:
            bool: True if the interaction was successful, False otherwise
        """
        print(f"You encounter {self.name}, a {self.creature_type.name.lower()}!")
        print(self.description)
        
        if not self.friendly:
            print(f"{self.name} seems hostile and might attack!")
            return False
        
        print(f"{self.name} seems friendly and approaches you.")
        
        if self.creature_type == CreatureType.PHOENIX:
            print(f"{self.name} envelops you in a warm, healing flame.")
            heal_player(player, 50)
            return True
        elif self.creature_type == CreatureType.UNICORN:
            print(f"{self.name} touches your hand with its horn, leaving behind a strand of unicorn hair.")
            add_item_to_inventory(player, "unicorn_hair")
            return True
        elif self.creature_type == CreatureType.DRAGON:
            print(f"{self.name} offers you one of its scales as a token of friendship.")
            add_item_to_inventory(player, "dragon_scale")
            return True
        elif self.creature_type == CreatureType.GRIFFIN:
            print(f"{self.name} drops a feather at your feet.")
            add_item_to_inventory(player, "griffin_feather")
            return True
        elif self.creature_type == CreatureType.MERMAID:
            print(f"{self.name} gives you a beautiful pearl from the depths of the ocean.")
            add_item_to_inventory(player, "mermaid_pearl")
            return True
        elif self.creature_type == CreatureType.CENTAUR:
            print(f"{self.name} teaches you about the stars and how to navigate by them.")
            update_world_state(world, "learn_navigation")
            return True
        elif self.creature_type == CreatureType.MINOTAUR:
            print(f"{self.name} shows you a secret path through the area.")
            update_world_state(world, "reveal_secret_path")
            return True
        elif self.creature_type == CreatureType.FAIRY:
            print(f"{self.name} sprinkles fairy dust on you, making you feel lighter and more energetic.")
            heal_player(player, 20)
            return True
        else:
            print(f"You're not sure how to interact with {self.name}.")
            return False
    
    def to_dict(self):
        """
        Convert the creature to a dictionary for saving.
        
        Returns:
            dict: A dictionary representation of the creature
        """
        return {
            "creature_type": self.creature_type.name,
            "name": self.name,
            "description": self.description,
            "friendly": self.friendly,
            "abilities": self.abilities
        }
    
    @classmethod
    def from_dict(cls, data):
        """
        Create a MythicalCreature from a dictionary.
        
        Args:
            data (dict): A dictionary representation of a creature
        
        Returns:
            MythicalCreature: A new MythicalCreature instance
        """
        try:
            creature_type = CreatureType[data["creature_type"]]
        except (KeyError, ValueError):
            creature_type = CreatureType.FAIRY
        
        return cls(
            creature_type=creature_type,
            name=data.get("name"),
            description=data.get("description"),
            friendly=data.get("friendly", True),
            abilities=data.get("abilities")
        )


def summon_mythical_creature(world, player, creature_type_str):
    """
    Summon a mythical creature to aid the player.
    
    Args:
        world (dict): The game world state
        player (dict): The player's current state
        creature_type_str (str): The type of mythical creature to summon
    
    Returns:
        bool: True if summoning was successful, False otherwise
    """
    # Map string creature types to enum values
    creature_type_map = {
        "phoenix": CreatureType.PHOENIX,
        "unicorn": CreatureType.UNICORN,
        "dragon": CreatureType.DRAGON,
        "griffin": CreatureType.GRIFFIN,
        "mermaid": CreatureType.MERMAID,
        "centaur": CreatureType.CENTAUR,
        "minotaur": CreatureType.MINOTAUR,
        "fairy": CreatureType.FAIRY
    }
    
    creature_type = creature_type_map.get(creature_type_str.lower())
    if not creature_type:
        print(f"Unknown creature type: {creature_type_str}")
        return False
    
    creature = MythicalCreature(creature_type)
    return creature.interact(player, world)

