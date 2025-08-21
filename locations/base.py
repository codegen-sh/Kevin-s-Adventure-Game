"""
Base location module for Kevin's Adventure Game.
This module provides a base class for all locations.
"""

import random

from game.player import add_item_to_inventory, damage_player, heal_player
from utils.random_events import generate_random_event


class BaseLocation:
    """
    Base class for all locations in the game.
    Provides common functionality for location interactions.
    """
    
    def __init__(self, name, description, options=None):
        """
        Initialize a new BaseLocation.
        
        Args:
            name (str): The name of the location
            description (str): A description of the location
            options (list): A list of interaction options for this location
        """
        self.name = name
        self.description = description
        self.options = options or []
        self.default_options = [
            {"number": "5", "text": f"Leave the {name.lower()}", "action": self.leave_location}
        ]
    
    def enter(self, world, player):
        """
        Enter this location and start interaction.
        
        Args:
            world: The world object
            player: The player object
        """
        print(f"You enter {self.name}. {self.description}")
        self.interact(world, player)
    
    def interact(self, world, player):
        """
        Interact with this location.
        
        Args:
            world: The world object
            player: The player object
        """
        while True:
            print(f"\nWhat would you like to do in the {self.name.lower()}?")
            
            # Display options
            all_options = self.options + self.default_options
            for option in all_options:
                print(f"{option['number']}. {option['text']}")
            
            # Get player choice
            choice = input(f"Enter your choice (1-{len(all_options)}): ")
            
            # Find and execute the chosen option
            option_found = False
            for option in all_options:
                if choice == option["number"]:
                    option_found = True
                    result = option["action"](world, player)
                    if result == "exit":
                        return
                    break
            
            if not option_found:
                print("Invalid choice. Please try again.")
    
    def leave_location(self, world, player):
        """
        Leave this location.
        
        Args:
            world: The world object
            player: The player object
            
        Returns:
            str: "exit" to indicate that the player is leaving the location
        """
        print(f"You decide to leave the {self.name.lower()}.")
        return "exit"
    
    def handle_random_event(self, world, player, event_probabilities):
        """
        Handle a random event at this location.
        
        Args:
            world: The world object
            player: The player object
            event_probabilities: A list of tuples (event_name, probability)
            
        Returns:
            str: The name of the event that occurred, or None if no event occurred
        """
        event = generate_random_event(events=event_probabilities)
        return event
    
    def add_item_to_player(self, player, item, message=None):
        """
        Add an item to the player's inventory with an optional custom message.
        
        Args:
            player: The player object
            item (str): The item to add
            message (str): An optional custom message to display
        """
        add_item_to_inventory(player, item)
        if message:
            print(message)
    
    def heal_player(self, player, amount, message=None):
        """
        Heal the player with an optional custom message.
        
        Args:
            player: The player object
            amount (int): The amount to heal
            message (str): An optional custom message to display
        """
        heal_player(player, amount)
        if message:
            print(message)
    
    def damage_player(self, player, amount, message=None):
        """
        Damage the player with an optional custom message.
        
        Args:
            player: The player object
            amount (int): The amount of damage
            message (str): An optional custom message to display
        """
        damage_player(player, amount)
        if message:
            print(message)

