"""
Forest location module for Kevin's Adventure Game.
This module handles all interactions with the forest location.
"""

import random

from game.player import add_item_to_inventory, heal_player
from game.state import update_world_state
from locations.base import BaseLocation
from utils.random_events import generate_random_event


class Forest(BaseLocation):
    """
    Forest location class.
    Handles all interactions with the forest location.
    """
    
    def __init__(self):
        """Initialize the Forest location."""
        super().__init__(
            name="Forest",
            description="A lush, green forest. The air is filled with the sounds of birds and rustling leaves.",
            options=[
                {"number": "1", "text": "Explore deeper", "action": self.explore_forest},
                {"number": "2", "text": "Climb a tree", "action": self.climb_tree},
                {"number": "3", "text": "Listen to the forest", "action": self.listen_to_forest},
                {"number": "4", "text": "Forage for food", "action": self.forage_for_food}
            ]
        )
    
    def explore_forest(self, world, player):
        """
        Explore deeper into the forest.
        
        Args:
            world: The world object
            player: The player object
        """
        print("You decide to explore deeper into the forest.")
        
        events = [
            ("find_berries", 40),
            ("encounter_animal", 25),
            ("discover_clearing", 10),
            (None, 25)
        ]
        
        event = self.handle_random_event(world, player, events)
        
        if event == "find_berries":
            print("You stumble upon a bush full of ripe berries!")
            self.add_item_to_player(player, "berries")
        elif event == "encounter_animal":
            print("You encounter a friendly deer. It allows you to approach and pet it.")
            self.heal_player(player, 5, "The peaceful interaction leaves you feeling refreshed.")
        elif event == "discover_clearing":
            print("You discover a beautiful clearing with a small pond.")
            # Implement mythical creature encounter
            if hasattr(world, "update_state"):
                world.update_state("add_clearing")
            else:
                update_world_state(world, "add_clearing")
        else:
            print("Your exploration yields nothing of note this time.")
    
    def climb_tree(self, world, player):
        """
        Climb a tree to get a better view.
        
        Args:
            world: The world object
            player: The player object
        """
        print("You climb a tall tree to get a better view of the surrounding area.")
        print("From up here, you can see the mountain peaks in the distance and what looks like the entrance to a cave.")
        
        # Small chance to find a bird's nest
        if random.random() < 0.2:
            print("You spot a bird's nest with a shiny object inside!")
            items = ["gemstone", "gold_coin", "silver_necklace"]
            found_item = random.choice(items)
            self.add_item_to_player(player, found_item, f"You carefully retrieve a {found_item} from the nest.")
        
        # Small chance of falling
        if random.random() < 0.1:
            damage = random.randint(5, 10)
            self.damage_player(player, damage, "You slip while climbing down and fall, taking some damage.")
    
    def listen_to_forest(self, world, player):
        """
        Listen to the sounds of the forest.
        
        Args:
            world: The world object
            player: The player object
        """
        print("You stop and listen carefully to the sounds of the forest.")
        print("You hear a faint sound of rushing water in the distance. There might be a river nearby.")
        
        # Implement river discovery
        if generate_random_event(events=[("discover_river", 20), (None, 80)]) == "discover_river":
            print("Following the sound, you've discovered a river!")
            
            if hasattr(world, "update_state"):
                world.update_state("add_river")
            else:
                update_world_state(world, "add_river")
            
            # Add River location if it doesn't exist
            if hasattr(world, "get_location") and not world.get_location("River"):
                from game.world import Location
                river = Location(
                    name="River",
                    description="A clear, flowing river cutting through the forest. Fish can be seen swimming in the water.",
                    connections=["Forest"],
                    items=["fishing_rod", "water_flask"]
                )
                world.add_location(river)
                
                # Add connection from Forest to River
                forest = world.get_location("Forest")
                if forest and "River" not in forest.connections:
                    forest.add_connection("River")
            elif isinstance(world, dict) and "River" not in world["locations"]:
                world["locations"]["River"] = {
                    "description": "A clear, flowing river cutting through the forest. Fish can be seen swimming in the water.",
                    "connections": ["Forest"],
                    "items": ["fishing_rod", "water_flask"]
                }
                
                # Add connection from Forest to River
                if "River" not in world["locations"]["Forest"]["connections"]:
                    world["locations"]["Forest"]["connections"].append("River")
            
            print("You've marked the river on your map. You can now travel there from the forest.")
        else:
            print("You don't find anything of note this time.")
    
    def forage_for_food(self, world, player):
        """
        Forage for food in the forest.
        
        Args:
            world: The world object
            player: The player object
        """
        print("You search the forest floor for edible plants and mushrooms.")
        
        if generate_random_event(events=[("find_mushrooms", 30), ("find_berries", 20), ("find_herbs", 10), (None, 40)]) == "find_mushrooms":
            print("You find some edible mushrooms!")
            self.add_item_to_player(player, "mushrooms")
        elif generate_random_event(events=[("find_mushrooms", 30), ("find_berries", 20), ("find_herbs", 10), (None, 40)]) == "find_berries":
            print("You find a bush with ripe berries!")
            self.add_item_to_player(player, "berries")
        elif generate_random_event(events=[("find_mushrooms", 30), ("find_berries", 20), ("find_herbs", 10), (None, 40)]) == "find_herbs":
            print("You find some medicinal herbs!")
            self.add_item_to_player(player, "herbs")
        else:
            print("You don't find anything edible this time.")


# Legacy function for backward compatibility
def enter_forest(world, player):
    """
    Enter the forest location.
    
    Args:
        world: The world object
        player: The player object
    """
    forest = Forest()
    forest.enter(world, player)

