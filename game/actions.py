"""
Actions module for the game.
"""
from game.base import Action
from game.player import add_item_to_inventory, move_player, remove_item_from_inventory
from game.world import change_location, get_available_locations, get_current_location, get_location_description, interact_with_location
from utils.random_events import apply_random_event


class MoveAction(Action):
    """Action to move the player to a new location."""
    
    def __init__(self):
        super().__init__("move", "Move to a new location")
    
    def execute(self, player, world, *args):
        if not args:
            print("Move where? Available locations:")
            for location in get_available_locations(world):
                print(f"- {location}")
            return
        
        destination = args[0].capitalize()
        if change_location(world, destination):
            move_player(player, destination)
            # 20% chance of a random event when moving
            import random
            if random.random() < 0.2:
                apply_random_event(player, world)
        else:
            print(f"You can't go to {destination} from here.")
            print("Available locations:")
            for location in get_available_locations(world):
                print(f"- {location}")


class LookAction(Action):
    """Action to look around the current location."""
    
    def __init__(self):
        super().__init__("look", "Look around the current location")
    
    def execute(self, player, world, *args):
        current_location = get_current_location(world)
        description = get_location_description(world, current_location)
        print(f"\n{description}")
        
        # Show available connections
        connections = get_available_locations(world)
        if connections:
            print("\nYou can go to:")
            for location in connections:
                print(f"- {location}")
        
        # Show available items
        items = world["locations"][current_location]["items"]
        if items:
            print("\nYou can see:")
            for item in items:
                print(f"- {item}")
        else:
            print("\nThere are no items here.")


class InventoryAction(Action):
    """Action to check the player's inventory."""
    
    def __init__(self):
        super().__init__("inventory", "Check your inventory")
    
    def execute(self, player, world, *args):
        if isinstance(player, dict):
            # Legacy support for dictionary-based player
            if player["inventory"]:
                print("Your inventory contains:")
                for item in player["inventory"]:
                    print(f"- {item}")
            else:
                print("Your inventory is empty.")
        else:
            # Support for Player class
            if player.inventory:
                print("Your inventory contains:")
                for item in player.inventory:
                    print(f"- {item}")
            else:
                print("Your inventory is empty.")


class PickupAction(Action):
    """Action to pick up an item."""
    
    def __init__(self):
        super().__init__("pickup", "Pick up an item")
    
    def execute(self, player, world, *args):
        if not args:
            print("Pick up what?")
            return
        
        item = args[0].lower()
        current_location = get_current_location(world)
        location_items = world["locations"][current_location]["items"]
        
        if item in location_items:
            add_item_to_inventory(player, item)
            location_items.remove(item)
        else:
            print(f"There is no {item} here.")


class DropAction(Action):
    """Action to drop an item."""
    
    def __init__(self):
        super().__init__("drop", "Drop an item")
    
    def execute(self, player, world, *args):
        if not args:
            print("Drop what?")
            return
        
        item = args[0].lower()
        current_location = get_current_location(world)
        
        if remove_item_from_inventory(player, item):
            world["locations"][current_location]["items"].append(item)


class UseAction(Action):
    """Action to use an item."""
    
    def __init__(self):
        super().__init__("use", "Use an item")
    
    def execute(self, player, world, *args):
        if not args:
            print("Use what?")
            return
        
        item = args[0].lower()
        inventory = player["inventory"] if isinstance(player, dict) else player.inventory
        
        if item not in inventory:
            print(f"You don't have {item} in your inventory.")
            return
        
        # Handle different items
        if item == "health_potion":
            print("You drink the health potion and feel rejuvenated.")
            if isinstance(player, dict):
                player["health"] = min(100, player["health"] + 25)
                player["inventory"].remove("health_potion")
            else:
                player.health = min(100, player.health + 25)
                player.inventory.remove("health_potion")
            print(f"Your health is now {player['health'] if isinstance(player, dict) else player.health}.")
        elif item == "map":
            print("You look at the map.")
            print("Available locations:")
            for location in world["locations"].keys():
                print(f"- {location}")
        elif item == "torch":
            print("You light the torch, illuminating the area around you.")
            # Could add special effects for dark areas
        elif item == "mysterious_potion":
            print("You drink the mysterious potion...")
            import random
            effect = random.choice(["health", "damage", "gold"])
            if effect == "health":
                print("You feel invigorated!")
                if isinstance(player, dict):
                    player["health"] = min(100, player["health"] + 30)
                    player["inventory"].remove("mysterious_potion")
                else:
                    player.health = min(100, player.health + 30)
                    player.inventory.remove("mysterious_potion")
                print(f"Your health is now {player['health'] if isinstance(player, dict) else player.health}.")
            elif effect == "damage":
                print("You feel sick!")
                if isinstance(player, dict):
                    player["health"] = max(1, player["health"] - 10)
                    player["inventory"].remove("mysterious_potion")
                else:
                    player.health = max(1, player.health - 10)
                    player.inventory.remove("mysterious_potion")
                print(f"Your health is now {player['health'] if isinstance(player, dict) else player.health}.")
            elif effect == "gold":
                print("You feel lucky!")
                if isinstance(player, dict):
                    player["gold"] += 20
                    player["inventory"].remove("mysterious_potion")
                else:
                    player.gold += 20
                    player.inventory.remove("mysterious_potion")
                print(f"You found 20 gold! Your gold is now {player['gold'] if isinstance(player, dict) else player.gold}.")
        else:
            print(f"You can't use {item} right now.")


class ExamineAction(Action):
    """Action to examine an item."""
    
    def __init__(self):
        super().__init__("examine", "Examine an item")
    
    def execute(self, player, world, *args):
        if not args:
            print("Examine what?")
            return
        
        item = args[0].lower()
        inventory = player["inventory"] if isinstance(player, dict) else player.inventory
        current_location = get_current_location(world)
        location_items = world["locations"][current_location]["items"]
        
        # Item descriptions
        descriptions = {
            "map": "A weathered map showing the surrounding areas.",
            "bread": "A fresh loaf of bread. Restores some health when eaten.",
            "stick": "A sturdy wooden stick. Could be useful for crafting.",
            "berries": "Wild berries. They look edible.",
            "torch": "A torch that can be lit to illuminate dark areas.",
            "gemstone": "A sparkling gemstone. It looks valuable.",
            "rope": "A coil of strong rope. Useful for climbing.",
            "pickaxe": "A sturdy pickaxe for mining.",
            "mysterious_potion": "A bubbling potion with unpredictable effects.",
            "health_potion": "A red potion that restores health.",
            "gold_coin": "A shiny gold coin.",
            "silver_necklace": "A beautiful silver necklace.",
            "ancient_artifact": "A mysterious artifact from a forgotten civilization.",
            "magic_ring": "A ring that glows with magical energy."
        }
        
        if item in inventory:
            print(descriptions.get(item, f"A {item}. Nothing special about it."))
        elif item in location_items:
            print(descriptions.get(item, f"A {item}. Nothing special about it."))
        else:
            print(f"You don't see any {item} here.")


class StatusAction(Action):
    """Action to check the player's status."""
    
    def __init__(self):
        super().__init__("status", "Check your status")
    
    def execute(self, player, world, *args):
        if isinstance(player, dict):
            # Legacy support for dictionary-based player
            print(f"Name: {player['name']}")
            print(f"Health: {player['health']}/100")
            print(f"Gold: {player['gold']}")
            print(f"Current location: {player['location']}")
            print(f"Inventory: {', '.join(player['inventory']) if player['inventory'] else 'empty'}")
        else:
            # Support for Player class
            print(f"Name: {player.name}")
            print(f"Health: {player.health}/100")
            print(f"Gold: {player.gold}")
            print(f"Current location: {player.location}")
            print(f"Inventory: {', '.join(player.inventory) if player.inventory else 'empty'}")


class InteractAction(Action):
    """Action to interact with the current location."""
    
    def __init__(self):
        super().__init__("interact", "Interact with the current location")
    
    def execute(self, player, world, *args):
        interact_with_location(world, player)


class HelpAction(Action):
    """Action to show the help message."""
    
    def __init__(self):
        super().__init__("help", "Show help message")
    
    def execute(self, player, world, *args):
        from utils.text_formatting import print_help
        print_help()


class QuitAction(Action):
    """Action to quit the game."""
    
    def __init__(self):
        super().__init__("quit", "Quit the game")
    
    def execute(self, player, world, *args):
        from utils.save_load import save_game
        save_game(player, world)
        print("Thanks for playing! Your progress has been saved.")
        return "QUIT"


# Dictionary of available actions
ACTIONS = {
    "move": MoveAction(),
    "look": LookAction(),
    "inventory": InventoryAction(),
    "pickup": PickupAction(),
    "drop": DropAction(),
    "use": UseAction(),
    "examine": ExamineAction(),
    "status": StatusAction(),
    "interact": InteractAction(),
    "help": HelpAction(),
    "quit": QuitAction()
}


def perform_action(player, world, action_input):
    """Perform an action based on user input."""
    parts = action_input.split()
    action_name = parts[0].lower()
    args = parts[1:] if len(parts) > 1 else []
    
    if action_name in ACTIONS:
        result = ACTIONS[action_name].execute(player, world, *args)
        if result == "QUIT":
            return "QUIT"
    else:
        print(f"Unknown action: {action_name}")
        print("Type 'help' to see available commands.")

