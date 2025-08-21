"""
Module for handling items in the game.
"""

import random
from enum import Enum, auto

from game.player import add_item_to_inventory, damage_player, heal_player, move_player
from game.world import change_location, get_all_locations, get_available_locations
from utils.random_events import generate_random_event


class ItemType(Enum):
    """Enum for item types."""
    WEAPON = auto()
    ARMOR = auto()
    POTION = auto()
    FOOD = auto()
    TOOL = auto()
    TREASURE = auto()
    KEY = auto()
    QUEST = auto()
    MISC = auto()


class Item:
    """
    A class to represent an item in the game.
    
    Attributes:
        name (str): The name of the item
        description (str): A description of the item
        item_type (ItemType): The type of item
        value (int): The value of the item in gold
        usable (bool): Whether the item can be used
        consumable (bool): Whether the item is consumed on use
        durability (int): The durability of the item (if applicable)
        effects (dict): The effects of using the item
    """
    
    def __init__(self, name, description, item_type=ItemType.MISC, value=0, usable=True, consumable=False, durability=None, effects=None):
        """
        Initialize a new Item.
        
        Args:
            name (str): The name of the item
            description (str): A description of the item
            item_type (ItemType, optional): The type of item. Defaults to ItemType.MISC.
            value (int, optional): The value of the item in gold. Defaults to 0.
            usable (bool, optional): Whether the item can be used. Defaults to True.
            consumable (bool, optional): Whether the item is consumed on use. Defaults to False.
            durability (int, optional): The durability of the item. Defaults to None.
            effects (dict, optional): The effects of using the item. Defaults to None.
        """
        self.name = name
        self.description = description
        self.item_type = item_type
        self.value = value
        self.usable = usable
        self.consumable = consumable
        self.durability = durability
        self.effects = effects if effects is not None else {}
    
    def use(self, player, world):
        """
        Use the item.
        
        Args:
            player: The player using the item
            world: The world state
        
        Returns:
            bool: True if the item was used successfully, False otherwise
        """
        if not self.usable:
            print(f"You can't use the {self.name}.")
            return False
        
        print(f"You use the {self.name}.")
        
        # Apply effects
        for effect, value in self.effects.items():
            if effect == "heal":
                heal_player(player, value)
            elif effect == "damage":
                damage_player(player, value)
            elif effect == "teleport" and value in get_all_locations(world):
                change_location(world, value)
                move_player(player, value)
        
        # Reduce durability if applicable
        if self.durability is not None:
            self.durability -= 1
            if self.durability <= 0:
                print(f"The {self.name} breaks from use.")
                self.usable = False
        
        # Remove if consumable
        if self.consumable:
            return True  # Signal that the item should be removed
        
        return False  # Signal that the item should not be removed
    
    def to_dict(self):
        """
        Convert the item to a dictionary for saving.
        
        Returns:
            dict: A dictionary representation of the item
        """
        return {
            "name": self.name,
            "description": self.description,
            "item_type": self.item_type.name,
            "value": self.value,
            "usable": self.usable,
            "consumable": self.consumable,
            "durability": self.durability,
            "effects": self.effects
        }
    
    @classmethod
    def from_dict(cls, data):
        """
        Create an Item from a dictionary.
        
        Args:
            data (dict): A dictionary representation of an item
        
        Returns:
            Item: A new Item instance
        """
        try:
            item_type = ItemType[data["item_type"]]
        except (KeyError, ValueError):
            item_type = ItemType.MISC
        
        return cls(
            name=data.get("name", "Unknown"),
            description=data.get("description", ""),
            item_type=item_type,
            value=data.get("value", 0),
            usable=data.get("usable", True),
            consumable=data.get("consumable", False),
            durability=data.get("durability"),
            effects=data.get("effects", {})
        )


# Dictionary of predefined items
ITEMS = {
    "map": Item(
        "map",
        "An old, worn map of the surrounding area. It might help you navigate.",
        ItemType.TOOL,
        value=5,
        usable=True,
        consumable=False
    ),
    "bread": Item(
        "bread",
        "A fresh loaf of bread. It looks delicious and nutritious.",
        ItemType.FOOD,
        value=5,
        usable=True,
        consumable=True,
        effects={"heal": 20}
    ),
    "stick": Item(
        "stick",
        "A sturdy wooden stick. It could be used as a simple weapon or tool.",
        ItemType.WEAPON,
        value=2,
        usable=True,
        consumable=False,
        durability=5
    ),
    "berries": Item(
        "berries",
        "A handful of colorful berries. They might be edible... or not.",
        ItemType.FOOD,
        value=3,
        usable=True,
        consumable=True
    ),
    "torch": Item(
        "torch",
        "A flaming torch that provides light in dark areas.",
        ItemType.TOOL,
        value=10,
        usable=True,
        consumable=False,
        durability=10
    ),
    "gemstone": Item(
        "gemstone",
        "A sparkling gemstone. It looks valuable.",
        ItemType.TREASURE,
        value=50,
        usable=True,
        consumable=False
    ),
    "rope": Item(
        "rope",
        "A coil of strong rope. Useful for climbing or tying things.",
        ItemType.TOOL,
        value=15,
        usable=True,
        consumable=False,
        durability=3
    ),
    "pickaxe": Item(
        "pickaxe",
        "A sturdy pickaxe. Perfect for mining or breaking through rocks.",
        ItemType.TOOL,
        value=25,
        usable=True,
        consumable=False,
        durability=5
    ),
    "mushrooms": Item(
        "mushrooms",
        "Some wild mushrooms. They could be edible or poisonous.",
        ItemType.FOOD,
        value=5,
        usable=True,
        consumable=True
    ),
    "mountain_herbs": Item(
        "mountain_herbs",
        "Rare medicinal herbs found on the mountain. They might have healing properties.",
        ItemType.POTION,
        value=20,
        usable=True,
        consumable=True,
        effects={"heal": 30}
    ),
    "ancient_coin": Item(
        "ancient_coin",
        "An old coin with strange markings. It might be valuable to collectors.",
        ItemType.TREASURE,
        value=30,
        usable=True,
        consumable=True
    ),
    "hermit's_blessing": Item(
        "hermit's_blessing",
        "A mystical blessing from the mountain hermit. It fills you with energy.",
        ItemType.MISC,
        value=0,
        usable=True,
        consumable=True,
        effects={"heal": 50}
    ),
    "gold_coin": Item(
        "gold_coin",
        "A shiny gold coin. Standard currency in this realm.",
        ItemType.TREASURE,
        value=1,
        usable=False,
        consumable=False
    ),
    "silver_necklace": Item(
        "silver_necklace",
        "A delicate silver necklace. It could fetch a good price.",
        ItemType.TREASURE,
        value=10,
        usable=True,
        consumable=False
    ),
    "ancient_artifact": Item(
        "ancient_artifact",
        "A mysterious object from a long-lost civilization. Its purpose is unknown.",
        ItemType.TREASURE,
        value=100,
        usable=True,
        consumable=False
    ),
    "magic_ring": Item(
        "magic_ring",
        "A ring imbued with magical properties. Its effects are yet to be discovered.",
        ItemType.TREASURE,
        value=75,
        usable=True,
        consumable=False
    ),
    "mysterious_potion": Item(
        "mysterious_potion",
        "A vial containing a strange, swirling liquid. Its effects are unknown.",
        ItemType.POTION,
        value=25,
        usable=True,
        consumable=True
    ),
    "sword": Item(
        "sword",
        "A well-crafted sword with a sharp blade. Useful for combat and self-defense.",
        ItemType.WEAPON,
        value=50,
        usable=True,
        consumable=False,
        durability=10
    ),
    "unicorn_hair": Item(
        "unicorn_hair",
        "A strand of shimmering hair from a unicorn. It radiates magical energy.",
        ItemType.TREASURE,
        value=100,
        usable=True,
        consumable=True,
        effects={"heal": 40}
    ),
    "dragon_scale": Item(
        "dragon_scale",
        "A tough, iridescent scale from a dragon. It's warm to the touch.",
        ItemType.ARMOR,
        value=150,
        usable=True,
        consumable=False
    ),
    "griffin_feather": Item(
        "griffin_feather",
        "A large, golden feather from a griffin. It's surprisingly light.",
        ItemType.MISC,
        value=75,
        usable=True,
        consumable=False
    ),
    "mermaid_pearl": Item(
        "mermaid_pearl",
        "A lustrous pearl given by a mermaid. It seems to glow with an inner light.",
        ItemType.TREASURE,
        value=200,
        usable=True,
        consumable=False
    ),
    "mysterious_package": Item(
        "mysterious_package",
        "A package that needs to be delivered to the hermit on the mountain.",
        ItemType.QUEST,
        value=0,
        usable=False,
        consumable=False
    )
}


# Legacy functions for backward compatibility
def get_item_description(item):
    """
    Get the description of an item.
    
    Args:
        item (str): The name of the item
    
    Returns:
        str: The description of the item
    """
    if item in ITEMS:
        return ITEMS[item].description
    return "A mysterious item."

def use_item(player, item, world):
    """
    Use an item.
    
    Args:
        player (dict): The player's state
        item (str): The name of the item to use
        world (dict): The world state
    
    Returns:
        bool: True if the item was used successfully, False otherwise
    """
    if item not in player["inventory"]:
        print(f"You don't have {item} in your inventory.")
        return False
    
    if item in ITEMS:
        item_obj = ITEMS[item]
        should_remove = item_obj.use(player, world)
        if should_remove:
            player["inventory"].remove(item)
        return True
    
    # Legacy item handling for items not in ITEMS dictionary
    if item == "map":
        print("You consult the map. It shows the following locations you can go to:")
        available_locations = get_available_locations(world)
        for location in available_locations:
            print(f"- {location}")
        return True
    elif item == "bread":
        print("You eat the bread. It's delicious and restores some health.")
        heal_player(player, 20)
        player["inventory"].remove(item)
        return True
    elif item == "stick":
        print("You wave the stick around. It makes a satisfying swoosh sound.")
        if world["current_location"] == "Forest":
            print("A nearby bird is startled and drops a shiny object!")
            add_item_to_inventory(player, "gold_coin")
        return True
    elif item == "berries":
        print("You eat the berries. They're sweet and juicy.")
        if generate_random_event(events=[("heal", 70), ("poison", 30)]) == "heal":
            print("You feel refreshed and gain some health.")
            heal_player(player, 10)
        else:
            print("Uh oh, those weren't safe to eat. You lose some health.")
            damage_player(player, 5)
        player["inventory"].remove(item)
        return True
    elif item == "torch":
        current_location = world["current_location"]
        if current_location == "Cave":
            print("You light the torch, illuminating the dark cave around you.")
            world["locations"]["Cave"]["description"] += " The cave is now well-lit by your torch."
            return True
        else:
            print("You light the torch. It provides warmth and light.")
            return True
    elif item == "gemstone":
        print("You examine the gemstone closely. It glimmers with an otherworldly light.")
        if world["current_location"] == "Village":
            print("A merchant notices your gemstone and offers to buy it for 50 gold!")
            choice = input("Do you want to sell the gemstone? (y/n): ").lower()
            if choice == 'y':
                player["gold"] += 50
                player["inventory"].remove(item)
                print("You sold the gemstone for 50 gold.")
            else:
                print("You decide to keep the gemstone.")
        return True
    elif item == "rope":
        if world["current_location"] == "Mountain":
            print("You use the rope to safely navigate a treacherous part of the mountain.")
            heal_player(player, 5)
            print("Your climbing technique improves, and you feel more confident.")
        else:
            print("You coil and uncoil the rope. It might be useful in the right situation.")
        return True
    elif item == "pickaxe":
        print("You swing the pickaxe, but there's nothing here to mine.")
        return True
    elif item == "mushrooms":
        print("You decide to eat the mushrooms.")
        if generate_random_event(events=[("heal", 50), ("poison", 50)]) == "heal":
            print("The mushrooms were edible and restore some health.")
            heal_player(player, 20)
        else:
            print("The mushrooms were poisonous! You feel sick.")
            damage_player(player, 10)
        player["inventory"].remove(item)
        return True
    elif item == "mountain_herbs":
        print("You brew a tea with the mountain herbs and drink it.")
        heal_player(player, 30)
        print("You feel invigorated and ready for more adventures!")
        player["inventory"].remove(item)
        return True
    elif item == "ancient_coin":
        print("You flip the ancient coin. As it spins in the air, you feel a strange energy...")
        if generate_random_event(events=[("teleport", 50), ("reveal_secret", 50)]) == "teleport":
            new_location = random.choice(get_all_locations(world))
            change_location(world, new_location)
            move_player(player, new_location)
            print(f"The coin vanishes and you find yourself teleported to {new_location}!")
        else:
            print("The coin glows and reveals a secret about your current location!")
            # You might want to add some location-specific secrets here
        player["inventory"].remove(item)
        return True
    elif item == "hermit's_blessing":
        print("You invoke the hermit's blessing. A warm, comforting light envelops you.")
        heal_player(player, 50)
        print("You feel completely refreshed and your mind is clear.")
        player["inventory"].remove(item)
        return True
    elif item == "sword":
        print("You swing the sword, practicing your combat moves.")
        if world["current_location"] == "Forest":
            print("Your sword slices through some thick vines, revealing a hidden path!")
            # update_world_state(world, "reveal_hidden_path")
        return True
    elif item == "gold_coin":
        print("You flip the gold coin. It catches the light, shimmering brilliantly.")
        if world["current_location"] == "Village":
            print("A street vendor notices your coin and offers you a mysterious potion in exchange.")
            choice = input("Do you want to trade the gold coin for the potion? (y/n): ").lower()
            if choice == 'y':
                player["inventory"].remove(item)
                add_item_to_inventory(player, "mysterious_potion")
                print("You traded the gold coin for a mysterious potion.")
            else:
                print("You decide to keep the gold coin.")
        return True
    elif item == "silver_necklace":
        print("You hold up the silver necklace, admiring its craftsmanship.")
        if world["current_location"] == "Mountain":
            print("The necklace begins to glow, revealing hidden runes on nearby rocks!")
            print("You discover a secret path leading to a hidden cave.")
            # update_world_state(world, "reveal_hidden_cave")
        else:
            print("The necklace sparkles beautifully, but nothing else happens.")
        return True
    elif item == "ancient_artifact":
        print("You examine the ancient artifact closely, turning it over in your hands.")
        if generate_random_event(events=[("wisdom", 40), ("curse", 30), (None, 30)]) == "wisdom":
            print("Suddenly, knowledge of the ancient world floods your mind!")
            print("You gain insight into the history of this land.")
            # update_player_knowledge(player, "ancient_history")
        elif generate_random_event(events=[("wisdom", 40), ("curse", 30), (None, 30)]) == "curse":
            print("A dark energy emanates from the artifact, making you feel weak.")
            damage_player(player, 10)
            print("You quickly put the artifact away, feeling drained.")
        else:
            print("Despite its age, the artifact remains inert and mysterious.")
        return True
    else:
        print(f"You're not sure how to use the {item}.")
        return False

def get_available_items(world, location):
    """
    Get the items available at a location.
    
    Args:
        world (dict): The world state
        location (str): The location to get items from
    
    Returns:
        list: A list of items at the location
    """
    return world["locations"][location]["items"]

def add_item_to_world(world, location, item):
    """
    Add an item to a location in the world.
    
    Args:
        world (dict): The world state
        location (str): The location to add the item to
        item (str): The item to add
    """
    if item not in world["locations"][location]["items"]:
        world["locations"][location]["items"].append(item)
        print(f"A {item} has been added to {location}.")
    else:
        print(f"There's already a {item} in {location}.")

def remove_item_from_world(world, location, item):
    """
    Remove an item from a location in the world.
    
    Args:
        world (dict): The world state
        location (str): The location to remove the item from
        item (str): The item to remove
    
    Returns:
        bool: True if the item was removed, False otherwise
    """
    if item in world["locations"][location]["items"]:
        world["locations"][location]["items"].remove(item)
        return True
    return False

def transfer_item(player, world, item, from_inventory_to_world=True):
    """
    Transfer an item between the player's inventory and the world.
    
    Args:
        player (dict): The player's state
        world (dict): The world state
        item (str): The item to transfer
        from_inventory_to_world (bool, optional): Whether to transfer from inventory to world. Defaults to True.
    
    Returns:
        bool: True if the item was transferred, False otherwise
    """
    current_location = world["current_location"]
    
    if from_inventory_to_world:
        if item in player["inventory"]:
            player["inventory"].remove(item)
            add_item_to_world(world, current_location, item)
            print(f"You dropped: {item}")
            return True
    else:
        if remove_item_from_world(world, current_location, item):
            player["inventory"].append(item)
            print(f"You picked up: {item}")
            return True
    
    return False

