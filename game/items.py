"""
Items module for Kevin's Adventure Game.
This module defines the Item class and item-related functionality.
"""


class Item:
    """
    Represents an item in the game.
    
    Attributes:
        name (str): The name of the item
        description (str): A description of the item
        use_effect (callable): A function to call when the item is used
        consumable (bool): Whether the item is consumed on use
    """
    
    def __init__(self, name, description, use_effect=None, consumable=False):
        """
        Initialize a new Item instance.
        
        Args:
            name (str): The name of the item
            description (str): A description of the item
            use_effect (callable, optional): A function to call when the item is used. Defaults to None.
            consumable (bool, optional): Whether the item is consumed on use. Defaults to False.
        """
        self.name = name
        self.description = description
        self.use_effect = use_effect
        self.consumable = consumable
    
    def use(self, player, world):
        """
        Use the item.
        
        Args:
            player: The player using the item
            world: The game world
        
        Returns:
            bool: True if the item was used successfully, False otherwise
        """
        if self.use_effect:
            result = self.use_effect(player, world)
            
            if self.consumable and result:
                player.remove_item(self.name)
            
            return result
        
        print(f"You can't figure out how to use the {self.name}.")
        return False


# Define item use effects
def use_bread(player, world):
    """
    Effect when using bread.
    
    Args:
        player: The player using the item
        world: The game world
    
    Returns:
        bool: True if the item was used successfully
    """
    player.heal(20)
    print("You ate the bread and restored some health.")
    return True


def use_berries(player, world):
    """
    Effect when using berries.
    
    Args:
        player: The player using the item
        world: The game world
    
    Returns:
        bool: True if the item was used successfully
    """
    player.heal(10)
    print("You ate the berries and restored a little health.")
    return True


def use_torch(player, world):
    """
    Effect when using torch.
    
    Args:
        player: The player using the item
        world: The game world
    
    Returns:
        bool: True if the item was used successfully
    """
    print("You light the torch, illuminating the area around you.")
    # No effect yet, but could be used for dark areas
    return True


def use_map(player, world):
    """
    Effect when using map.
    
    Args:
        player: The player using the item
        world: The game world
    
    Returns:
        bool: True if the item was used successfully
    """
    print("You consult the map, showing all known locations.")
    for location_name in world.locations:
        print(f"- {location_name}")
    return True


def use_rope(player, world):
    """
    Effect when using rope.
    
    Args:
        player: The player using the item
        world: The game world
    
    Returns:
        bool: True if the item was used successfully
    """
    print("You prepare the rope. It might help with climbing.")
    # Could be used for specific climbing challenges
    return True


def use_pickaxe(player, world):
    """
    Effect when using pickaxe.
    
    Args:
        player: The player using the item
        world: The game world
    
    Returns:
        bool: True if the item was used successfully
    """
    print("You ready the pickaxe. It could be useful for mining.")
    # Could be used for mining challenges
    return True


def use_gemstone(player, world):
    """
    Effect when using gemstone.
    
    Args:
        player: The player using the item
        world: The game world
    
    Returns:
        bool: True if the item was used successfully
    """
    print("The gemstone glows with a mysterious light, but nothing happens.")
    # Could have magical properties later
    return True


def use_stick(player, world):
    """
    Effect when using stick.
    
    Args:
        player: The player using the item
        world: The game world
    
    Returns:
        bool: True if the item was used successfully
    """
    print("You wave the stick around. It's just a stick.")
    # Could be crafted into something useful later
    return True


# Define all game items
ITEMS = {
    "bread": Item(
        name="bread",
        description="A fresh loaf of bread. It looks delicious and would restore some health.",
        use_effect=use_bread,
        consumable=True
    ),
    "berries": Item(
        name="berries",
        description="Small, red berries. They look edible and might restore a little health.",
        use_effect=use_berries,
        consumable=True
    ),
    "torch": Item(
        name="torch",
        description="A wooden torch that can be lit to provide light in dark areas.",
        use_effect=use_torch,
        consumable=False
    ),
    "map": Item(
        name="map",
        description="A parchment map showing the major locations in the area.",
        use_effect=use_map,
        consumable=False
    ),
    "rope": Item(
        name="rope",
        description="A sturdy rope that could help with climbing or crossing gaps.",
        use_effect=use_rope,
        consumable=False
    ),
    "pickaxe": Item(
        name="pickaxe",
        description="A mining tool that could be used to extract minerals or create passages.",
        use_effect=use_pickaxe,
        consumable=False
    ),
    "gemstone": Item(
        name="gemstone",
        description="A beautiful, glowing gemstone. It seems to have magical properties.",
        use_effect=use_gemstone,
        consumable=False
    ),
    "stick": Item(
        name="stick",
        description="A simple wooden stick. It might be useful for crafting or as a basic weapon.",
        use_effect=use_stick,
        consumable=False
    )
}


def get_item(item_name):
    """
    Get an item by name.
    
    Args:
        item_name (str): The name of the item
    
    Returns:
        Item: The item with the given name, or None if not found
    """
    return ITEMS.get(item_name.lower())


def get_item_description(item_name):
    """
    Get the description of an item.
    
    Args:
        item_name (str): The name of the item
    
    Returns:
        str: The description of the item, or a default message if not found
    """
    item = get_item(item_name)
    if item:
        return item.description
    return f"It's a {item_name}. Nothing special about it."


def use_item(player, world, item_name):
    """
    Use an item.
    
    Args:
        player: The player using the item
        world: The game world
        item_name (str): The name of the item to use
    
    Returns:
        bool: True if the item was used successfully, False otherwise
    """
    item = get_item(item_name)
    if item:
        return item.use(player, world)
    
    print(f"You can't figure out how to use the {item_name}.")
    return False

