import random

from game.entity import Entity
from game.player import (
    add_item_to_inventory,
    damage_player,
    heal_player,
    move_player,
    remove_item_from_inventory,
)
from game.world import change_location, get_all_locations, get_available_locations
from utils.random_events import generate_random_event


class Item(Entity):
    """
    Represents an item in the game.
    
    This class handles item attributes and usage effects.
    """
    
    def __init__(self, name, description="", consumable=False):
        """
        Initialize a new Item.
        
        Args:
            name (str): The name of the item
            description (str, optional): A description of the item
            consumable (bool, optional): Whether the item is consumed on use
        """
        super().__init__(name, description)
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
        print(f"You use the {self.name}, but nothing happens.")
        return True


# Dictionary of item descriptions for backward compatibility
ITEM_DESCRIPTIONS = {
    "map": "An old, worn map of the surrounding area. It might help you navigate.",
    "bread": "A fresh loaf of bread. It looks delicious and nutritious.",
    "stick": "A sturdy wooden stick. It could be used as a simple weapon or tool.",
    "berries": "A handful of colorful berries. They might be edible... or not.",
    "torch": "A flaming torch that provides light in dark areas.",
    "gemstone": "A sparkling gemstone. It looks valuable.",
    "rope": "A coil of strong rope. Useful for climbing or tying things.",
    "pickaxe": "A sturdy pickaxe. Perfect for mining or breaking through rocks.",
    "mushrooms": "Some wild mushrooms. They could be edible or poisonous.",
    "mountain_herbs": "Rare medicinal herbs found on the mountain. They might have healing properties.",
    "ancient_coin": "An old coin with strange markings. It might be valuable to collectors.",
    "hermit's_blessing": "A mystical blessing from the mountain hermit. It fills you with energy.",
    "gold_coin": "A shiny gold coin. Standard currency in this realm.",
    "silver_necklace": "A delicate silver necklace. It could fetch a good price.",
    "ancient_artifact": "A mysterious object from a long-lost civilization. Its purpose is unknown.",
    "magic_ring": "A ring imbued with magical properties. Its effects are yet to be discovered.",
    "mysterious_potion": "A vial containing a strange, swirling liquid. Its effects are unknown.",
    "sword": "A well-crafted sword with a sharp blade. Useful for combat and self-defense."
}


def get_item_description(item):
    """Get the description of an item."""
    if isinstance(item, Item):
        return item.description
    return ITEM_DESCRIPTIONS.get(item, "A mysterious item.")


def use_item(player, item, world):
    """Use an item."""
    if isinstance(item, Item):
        return item.use(player, world)
    
    if item not in player["inventory"]:
        print(f"You don't have {item} in your inventory.")
        return False

    if item == "map":
        print("You consult the map. It shows the following locations you can go to:")
        available_locations = get_available_locations(world)
        for location in available_locations:
            print(f"- {location}")
        return True
    elif item == "bread":
        print("You eat the bread. It's delicious and restores some health.")
        heal_player(player, 20)
        remove_item_from_inventory(player, item)
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
        remove_item_from_inventory(player, item)
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
                remove_item_from_inventory(player, item)
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
        remove_item_from_inventory(player, item)
        return True
    elif item == "mountain_herbs":
        print("You brew a tea with the mountain herbs and drink it.")
        heal_player(player, 30)
        print("You feel invigorated and ready for more adventures!")
        remove_item_from_inventory(player, item)
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
        remove_item_from_inventory(player, item)
        return True
    elif item == "hermit's_blessing":
        print("You invoke the hermit's blessing. A warm, comforting light envelops you.")
        heal_player(player, 50)
        print("You feel completely refreshed and your mind is clear.")
        remove_item_from_inventory(player, item)
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
                remove_item_from_inventory(player, item)
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
    """Get a list of items available at a location."""
    if hasattr(world, 'get_location'):
        loc = world.get_location(location)
        return loc.items if loc else []
    return world["locations"][location]["items"]


def add_item_to_world(world, location, item):
    """Add an item to a location in the world."""
    if hasattr(world, 'get_location'):
        loc = world.get_location(location)
        if loc:
            loc.add_item(item)
            print(f"A {item} has been added to {location}.")
        return
    
    if item not in world["locations"][location]["items"]:
        world["locations"][location]["items"].append(item)
        print(f"A {item} has been added to {location}.")
    else:
        print(f"There's already a {item} in {location}.")


def remove_item_from_world(world, location, item):
    """Remove an item from a location in the world."""
    if hasattr(world, 'get_location'):
        loc = world.get_location(location)
        return loc.remove_item(item) if loc else False
    
    if item in world["locations"][location]["items"]:
        world["locations"][location]["items"].remove(item)
        return True
    return False


def transfer_item(player, world, item, from_inventory_to_world=True):
    """Transfer an item between the player's inventory and the world."""
    current_location = world["current_location"] if isinstance(world, dict) else world.get_current_location()

    if from_inventory_to_world:
        if remove_item_from_inventory(player, item):
            add_item_to_world(world, current_location, item)
            return True
    else:
        if remove_item_from_world(world, current_location, item):
            add_item_to_inventory(player, item)
            return True

    return False
