"""
Game Actions Module - Handles all player actions and commands.
Implements a command pattern for better organization and extensibility.
"""

from game.player import (
    add_item_to_inventory, 
    remove_item_from_inventory, 
    move_player,
    heal_player,
    get_player_status
)
from game.world import (
    get_current_location, 
    get_location_description, 
    get_available_locations,
    change_location,
    interact_with_location,
    is_location_accessible
)
from game.items import (
    use_item, 
    get_available_items, 
    transfer_item,
    get_item_description
)
from game.weather import (
    get_current_weather, 
    change_weather, 
    describe_weather,
    weather_forecast
)
from locations.forest import enter_forest, explore_forest
from locations.village import visit_village, visit_shop, talk_to_villagers
from locations.mountain import climb_mountain, check_weather as mountain_weather
from locations.cave import explore_cave, search_cave_depths
from utils.save_load import save_game, load_game
from utils.text_formatting import print_help
import random


class ActionHandler:
    """
    Handles all game actions using a command pattern.
    """
    
    def __init__(self):
        self.actions = {
            # Movement actions
            'go': self.go_to_location,
            'move': self.go_to_location,
            'travel': self.go_to_location,
            'enter': self.enter_location,
            
            # Exploration actions
            'explore': self.explore_current_location,
            'look': self.look_around,
            'examine': self.examine,
            'search': self.search_area,
            
            # Inventory actions
            'inventory': self.show_inventory,
            'items': self.show_inventory,
            'use': self.use_item_action,
            'drop': self.drop_item,
            'take': self.take_item,
            'pickup': self.take_item,
            
            # Status actions
            'status': self.show_status,
            'health': self.show_health,
            'stats': self.show_status,
            
            # Weather actions
            'weather': self.check_weather,
            'forecast': self.weather_forecast_action,
            
            # Location-specific actions
            'shop': self.visit_shop_action,
            'talk': self.talk_action,
            'climb': self.climb_action,
            'forest': self.forest_action,
            'cave': self.cave_action,
            
            # Game management
            'save': self.save_game_action,
            'help': self.show_help,
            'commands': self.show_help,
            
            # Rest and healing
            'rest': self.rest_action,
            'sleep': self.rest_action,
        }
    
    def perform_action(self, player, world, action_input):
        """
        Main action dispatcher. Parses input and executes appropriate action.
        """
        if not action_input.strip():
            print("Please enter a command. Type 'help' for available commands.")
            return
        
        # Parse the action input
        parts = action_input.lower().strip().split()
        action = parts[0]
        args = parts[1:] if len(parts) > 1 else []
        
        # Check if action exists
        if action in self.actions:
            try:
                self.actions[action](player, world, args)
            except Exception as e:
                print(f"Error executing action '{action}': {e}")
                print("Type 'help' for available commands.")
        else:
            self.handle_unknown_action(player, world, action, args)
    
    def handle_unknown_action(self, player, world, action, args):
        """
        Handle unknown actions with helpful suggestions.
        """
        suggestions = []
        
        # Suggest similar actions
        for known_action in self.actions.keys():
            if action in known_action or known_action in action:
                suggestions.append(known_action)
        
        if suggestions:
            print(f"Unknown command '{action}'. Did you mean: {', '.join(suggestions[:3])}?")
        else:
            print(f"Unknown command '{action}'. Type 'help' for available commands.")
    
    # Movement Actions
    def go_to_location(self, player, world, args):
        """Handle movement to different locations."""
        if not args:
            available = get_available_locations(world)
            print(f"Where would you like to go? Available locations: {', '.join(available)}")
            return
        
        destination = ' '.join(args).title()
        current_location = get_current_location(world)
        
        if destination.lower() == current_location.lower():
            print(f"You are already in the {current_location}.")
            return
        
        if is_location_accessible(world, destination):
            change_location(world, destination)
            move_player(player, destination)
            print(f"\n🚶 You travel to the {destination}.")
            print(get_location_description(world, destination))
            
            # Trigger location-specific events
            self.trigger_location_events(player, world, destination)
        else:
            available = get_available_locations(world)
            print(f"You cannot go to '{destination}' from here.")
            print(f"Available locations: {', '.join(available)}")
    
    def enter_location(self, player, world, args):
        """Enter and interact with current location."""
        current_location = get_current_location(world)
        print(f"\n🚪 You enter the {current_location}...")
        interact_with_location(world, player)
    
    # Exploration Actions
    def explore_current_location(self, player, world, args):
        """Explore the current location in detail."""
        current_location = get_current_location(world)
        print(f"\n🔍 You explore the {current_location} thoroughly...")
        
        if current_location.lower() == "forest":
            explore_forest(world, player)
        elif current_location.lower() == "cave":
            if args and args[0] == "deep":
                search_cave_depths(world, player)
            else:
                explore_cave(world, player)
        elif current_location.lower() == "mountain":
            climb_mountain(world, player)
        else:
            interact_with_location(world, player)
    
    def look_around(self, player, world, args):
        """Look around the current area."""
        current_location = get_current_location(world)
        print(f"\n👀 You look around the {current_location}:")
        print(get_location_description(world, current_location))
        
        # Show available items
        items = get_available_items(world, current_location)
        if items:
            print(f"You see: {', '.join(items)}")
        
        # Show weather
        print(f"Weather: {describe_weather(world)}")
    
    def examine(self, player, world, args):
        """Examine specific items or areas."""
        if not args:
            print("What would you like to examine?")
            return
        
        target = ' '.join(args).lower()
        current_location = get_current_location(world)
        available_items = get_available_items(world, current_location)
        player_items = player.get('inventory', [])
        
        # Check if examining an item
        all_items = available_items + player_items
        for item in all_items:
            if target in item.lower():
                description = get_item_description(item)
                print(f"\n🔍 {item}: {description}")
                return
        
        print(f"You don't see '{target}' here.")
    
    def search_area(self, player, world, args):
        """Search the current area for hidden items or secrets."""
        current_location = get_current_location(world)
        print(f"\n🔎 You search the {current_location} carefully...")
        
        # Random chance to find something
        if random.random() < 0.3:
            hidden_items = ["coin", "herb", "small_key", "note", "gem"]
            found_item = random.choice(hidden_items)
            add_item_to_inventory(player, found_item)
            print(f"You found a hidden {found_item}!")
        else:
            print("You don't find anything unusual.")
    
    # Inventory Actions
    def show_inventory(self, player, world, args):
        """Display player's inventory."""
        inventory = player.get('inventory', [])
        if inventory:
            print(f"\n🎒 Your inventory: {', '.join(inventory)}")
        else:
            print("\n🎒 Your inventory is empty.")
    
    def use_item_action(self, player, world, args):
        """Use an item from inventory."""
        if not args:
            print("What item would you like to use?")
            return
        
        item_name = ' '.join(args).lower()
        inventory = player.get('inventory', [])
        
        # Find matching item
        for item in inventory:
            if item_name in item.lower():
                use_item(player, item, world)
                return
        
        print(f"You don't have '{item_name}' in your inventory.")
    
    def drop_item(self, player, world, args):
        """Drop an item from inventory."""
        if not args:
            print("What item would you like to drop?")
            return
        
        item_name = ' '.join(args).lower()
        inventory = player.get('inventory', [])
        
        for item in inventory:
            if item_name in item.lower():
                transfer_item(player, world, item, from_inventory_to_world=True)
                print(f"You dropped {item}.")
                return
        
        print(f"You don't have '{item_name}' in your inventory.")
    
    def take_item(self, player, world, args):
        """Take an item from the current location."""
        if not args:
            current_location = get_current_location(world)
            items = get_available_items(world, current_location)
            if items:
                print(f"Available items: {', '.join(items)}")
            else:
                print("There are no items here to take.")
            return
        
        item_name = ' '.join(args).lower()
        current_location = get_current_location(world)
        available_items = get_available_items(world, current_location)
        
        for item in available_items:
            if item_name in item.lower():
                transfer_item(player, world, item, from_inventory_to_world=False)
                print(f"You picked up {item}.")
                return
        
        print(f"There is no '{item_name}' here to take.")
    
    # Status Actions
    def show_status(self, player, world, args):
        """Show player status and current situation."""
        print(f"\n📊 {get_player_status(player)}")
        print(f"📍 Location: {get_current_location(world)}")
        print(f"🌤️  Weather: {describe_weather(world)}")
    
    def show_health(self, player, world, args):
        """Show player health status."""
        health = player.get('health', 100)
        print(f"\n❤️  Health: {health}/100")
        if health < 30:
            print("⚠️  You are in critical condition! Find a way to heal.")
        elif health < 60:
            print("⚠️  You are injured. Consider resting or finding healing items.")
    
    # Weather Actions
    def check_weather(self, player, world, args):
        """Check current weather conditions."""
        print(f"\n🌤️  {describe_weather(world)}")
    
    def weather_forecast_action(self, player, world, args):
        """Get weather forecast."""
        print(f"\n🌦️  {weather_forecast(world)}")
    
    # Location-specific Actions
    def visit_shop_action(self, player, world, args):
        """Visit shop if in village."""
        current_location = get_current_location(world)
        if current_location.lower() == "village":
            visit_shop(world, player)
        else:
            print("There's no shop here. You need to go to the village.")
    
    def talk_action(self, player, world, args):
        """Talk to NPCs if available."""
        current_location = get_current_location(world)
        if current_location.lower() == "village":
            talk_to_villagers(world, player)
        else:
            print("There's no one to talk to here.")
    
    def climb_action(self, player, world, args):
        """Climbing action for mountains or trees."""
        current_location = get_current_location(world)
        if current_location.lower() == "mountain":
            climb_mountain(world, player)
        elif current_location.lower() == "forest":
            from locations.forest import climb_tree
            climb_tree(world, player)
        else:
            print("There's nothing to climb here.")
    
    def forest_action(self, player, world, args):
        """Forest-specific actions."""
        current_location = get_current_location(world)
        if current_location.lower() == "forest":
            enter_forest(world, player)
        else:
            print("You need to be in the forest to do that.")
    
    def cave_action(self, player, world, args):
        """Cave-specific actions."""
        current_location = get_current_location(world)
        if current_location.lower() == "cave":
            if args and args[0] == "deep":
                search_cave_depths(world, player)
            else:
                explore_cave(world, player)
        else:
            print("You need to be in a cave to do that.")
    
    # Game Management Actions
    def save_game_action(self, player, world, args):
        """Save the current game."""
        save_game(player, world)
        print("💾 Game saved successfully!")
    
    def show_help(self, player, world, args):
        """Show help information."""
        print_help()
        print("\n🎮 Available commands:")
        print("Movement: go <location>, enter, explore")
        print("Items: inventory, use <item>, take <item>, drop <item>")
        print("Actions: look, examine <target>, search, talk, shop")
        print("Status: status, health, weather, forecast")
        print("Game: save, help, quit")
    
    def rest_action(self, player, world, args):
        """Rest to recover health."""
        current_location = get_current_location(world)
        
        if current_location.lower() == "village":
            heal_amount = random.randint(20, 40)
            heal_player(player, heal_amount)
            print(f"😴 You rest comfortably in the village and recover {heal_amount} health.")
        else:
            heal_amount = random.randint(5, 15)
            heal_player(player, heal_amount)
            print(f"😴 You rest in the {current_location} and recover {heal_amount} health.")
            
            # Small chance of random event while resting
            if random.random() < 0.2:
                from utils.random_events import generate_random_event
                print("While resting, something happens...")
                generate_random_event(world, player)
    
    def trigger_location_events(self, player, world, location):
        """Trigger location-specific events when entering."""
        # Random chance for events when entering new locations
        if random.random() < 0.3:
            from utils.random_events import generate_random_event
            generate_random_event(world, player)


# Global action handler instance
action_handler = ActionHandler()


def perform_action(player, world, action_input):
    """
    Main function called by the game loop to handle player actions.
    """
    action_handler.perform_action(player, world, action_input)

