"""
Items module for Kevin's Adventure Game.
Contains the Item class and related functions.
"""


class Item:
    """
    Item class representing a game item.
    
    Attributes:
        name (str): The name of the item
        description (str): A description of the item
        portable (bool): Whether the item can be picked up
        value (int): The gold value of the item
        effects (dict): Dictionary of effects the item has when used
    """
    
    def __init__(self, name, description, portable=True, value=0, effects=None):
        """
        Initialize a new Item instance.
        
        Args:
            name (str): The name of the item
            description (str): A description of the item
            portable (bool, optional): Whether the item can be picked up. Defaults to True.
            value (int, optional): The gold value of the item. Defaults to 0.
            effects (dict, optional): Dictionary of effects the item has when used. Defaults to None.
        """
        self.name = name
        self.description = description
        self.portable = portable
        self.value = value
        self.effects = effects or {}
    
    def use(self, player, world):
        """
        Use the item.
        
        Args:
            player: The player using the item
            world: The game world
            
        Returns:
            bool: True if the item was used successfully, False otherwise
        """
        if "heal" in self.effects:
            from game.player import heal_player
            heal_player(player, self.effects["heal"])
            return True
        elif "damage" in self.effects:
            from game.player import damage_player
            damage_player(player, self.effects["damage"])
            return True
        elif "message" in self.effects:
            print(self.effects["message"])
            return True
        else:
            print(f"You're not sure how to use the {self.name}.")
            return False
    
    def examine(self):
        """
        Examine the item.
        
        Returns:
            str: The item's description
        """
        return self.description
    
    def to_dict(self):
        """
        Convert the Item instance to a dictionary.
        
        Returns:
            dict: A dictionary representation of the item
        """
        return {
            "name": self.name,
            "description": self.description,
            "portable": self.portable,
            "value": self.value,
            "effects": self.effects.copy()
        }
    
    @classmethod
    def from_dict(cls, item_dict):
        """
        Create an Item instance from a dictionary.
        
        Args:
            item_dict (dict): A dictionary representation of an item
            
        Returns:
            Item: A new Item instance
        """
        return cls(
            name=item_dict["name"],
            description=item_dict["description"],
            portable=item_dict["portable"],
            value=item_dict["value"],
            effects=item_dict["effects"].copy()
        )


# Create a catalog of standard items
def get_item_catalog():
    """
    Get a catalog of standard items.
    
    Returns:
        dict: A dictionary of Item instances
    """
    return {
        "map": Item(
            name="map",
            description="A weathered map showing the village, forest, cave, and mountain.",
            effects={"message": "You look at the map. It shows your current location and nearby areas."}
        ),
        "bread": Item(
            name="bread",
            description="A fresh loaf of bread. It smells delicious.",
            value=5,
            effects={"heal": 10, "message": "You eat the bread and feel better."}
        ),
        "stick": Item(
            name="stick",
            description="A sturdy wooden stick. Could be useful for various tasks.",
            value=2
        ),
        "berries": Item(
            name="berries",
            description="Plump, juicy berries. They look safe to eat.",
            value=3,
            effects={"heal": 5, "message": "You eat the berries. They're sweet and refreshing."}
        ),
        "torch": Item(
            name="torch",
            description="A wooden torch that can be lit to provide light in dark areas.",
            value=10,
            effects={"message": "You light the torch. It illuminates the area around you."}
        ),
        "gemstone": Item(
            name="gemstone",
            description="A sparkling gemstone that catches the light beautifully.",
            value=30
        ),
        "rope": Item(
            name="rope",
            description="A coil of strong rope. Useful for climbing or tying things.",
            value=15
        ),
        "pickaxe": Item(
            name="pickaxe",
            description="A sturdy pickaxe for mining or breaking rocks.",
            value=20
        ),
        "sword": Item(
            name="sword",
            description="A sharp, well-crafted sword. Useful for protection.",
            value=50
        ),
        "mushrooms": Item(
            name="mushrooms",
            description="Edible mushrooms that can restore some health.",
            value=5,
            effects={"heal": 8, "message": "You eat the mushrooms. They have an earthy flavor."}
        ),
        "mysterious_package": Item(
            name="mysterious_package",
            description="A sealed package addressed to the mountain hermit.",
            value=0,
            effects={"message": "The package is sealed. You should deliver it to the mountain hermit."}
        ),
        "unicorn_hair": Item(
            name="unicorn_hair",
            description="A shimmering strand of unicorn hair. It seems magical.",
            value=100
        ),
        "dragon_scale": Item(
            name="dragon_scale",
            description="A tough, iridescent dragon scale. It's warm to the touch.",
            value=200
        ),
        "gold_nugget": Item(
            name="gold_nugget",
            description="A small nugget of pure gold.",
            value=20
        ),
        "crystal": Item(
            name="crystal",
            description="A beautiful crystal that seems to glow with an inner light.",
            value=25
        ),
        "small_gemstone": Item(
            name="small_gemstone",
            description="A small but valuable gemstone.",
            value=15
        ),
        "ancient_amulet": Item(
            name="ancient_amulet",
            description="An ancient amulet with strange inscriptions. It feels magical.",
            value=150,
            effects={"message": "The amulet glows faintly when you hold it."}
        )
    }


# Get an item by name
def get_item(item_name):
    """
    Get an item by name.
    
    Args:
        item_name (str): The name of the item
        
    Returns:
        Item: The item instance, or None if not found
    """
    catalog = get_item_catalog()
    return catalog.get(item_name.lower())

