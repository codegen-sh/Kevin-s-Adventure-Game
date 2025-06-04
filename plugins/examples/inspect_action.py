"""
Inspect action plugin - Example action plugin for Kevin's Adventure Game.
"""

from plugins.base import BaseAction, PluginMetadata
from game.world import get_current_location
from typing import Dict, Any, List


class InspectAction(BaseAction):
    """An inspect action plugin that allows detailed examination of items and locations."""
    
    @property
    def metadata(self) -> PluginMetadata:
        return PluginMetadata(
            name="InspectAction",
            version="1.0.0",
            description="Allows players to inspect items, locations, and objects in detail",
            author="Plugin Developer"
        )
    
    def initialize(self) -> bool:
        """Initialize the inspect action plugin."""
        return True
    
    def cleanup(self) -> None:
        """Clean up inspect action resources."""
        pass
    
    def get_triggers(self) -> List[str]:
        """Return list of command triggers for this action."""
        return ["inspect", "examine", "look at", "check"]
    
    def execute(self, player: Dict[str, Any], world: Dict[str, Any], 
                command: str, args: List[str]) -> bool:
        """Execute the inspect action."""
        if not args:
            print("What would you like to inspect?")
            print("Try: inspect <item>, inspect location, inspect inventory")
            return True
        
        target = " ".join(args).lower()
        
        # Inspect location
        if target in ["location", "area", "here", "around"]:
            self._inspect_location(player, world)
            return True
        
        # Inspect inventory
        if target in ["inventory", "inv", "items", "bag"]:
            self._inspect_inventory(player, world)
            return True
        
        # Inspect specific item in inventory
        if target in [item.lower() for item in player.get("inventory", [])]:
            self._inspect_inventory_item(player, world, target)
            return True
        
        # Inspect player stats
        if target in ["self", "me", "player", "stats"]:
            self._inspect_player(player, world)
            return True
        
        # Inspect location items
        current_location = get_current_location(world)
        location_data = world.get("locations", {}).get(current_location, {})
        location_items = [item.lower() for item in location_data.get("items", [])]
        
        if target in location_items:
            self._inspect_location_item(player, world, target)
            return True
        
        # Default response for unknown targets
        print(f"You don't see '{target}' here to inspect.")
        print("Try inspecting your inventory, the location, or specific items you can see.")
        return True
    
    def get_help_text(self) -> str:
        """Return help text for this action."""
        return "inspect <target> - Examine items, locations, or yourself in detail"
    
    def can_execute(self, player: Dict[str, Any], world: Dict[str, Any]) -> bool:
        """Check if this action can be executed."""
        return True
    
    def _inspect_location(self, player: Dict[str, Any], world: Dict[str, Any]) -> None:
        """Inspect the current location in detail."""
        current_location = get_current_location(world)
        location_data = world.get("locations", {}).get(current_location, {})
        
        print(f"\\n=== Inspecting {current_location} ===")
        print(f"Description: {location_data.get('description', 'No description available.')}")
        
        connections = location_data.get("connections", [])
        if connections:
            print(f"Exits: {', '.join(connections)}")
        else:
            print("Exits: None visible")
        
        items = location_data.get("items", [])
        if items:
            print(f"Items you can see: {', '.join(items)}")
        else:
            print("Items: None visible")
        
        # Add some atmospheric details based on location
        self._add_location_details(current_location)
    
    def _inspect_inventory(self, player: Dict[str, Any], world: Dict[str, Any]) -> None:
        """Inspect the player's inventory in detail."""
        inventory = player.get("inventory", [])
        
        print("\\n=== Inspecting Your Inventory ===")
        if not inventory:
            print("Your inventory is empty.")
            return
        
        print(f"You are carrying {len(inventory)} item(s):")
        for i, item in enumerate(inventory, 1):
            description = self._get_item_description(item)
            print(f"  {i}. {item} - {description}")
    
    def _inspect_inventory_item(self, player: Dict[str, Any], world: Dict[str, Any], item: str) -> None:
        """Inspect a specific item in the player's inventory."""
        # Find the actual item name (case-sensitive)
        actual_item = None
        for inv_item in player.get("inventory", []):
            if inv_item.lower() == item.lower():
                actual_item = inv_item
                break
        
        if not actual_item:
            print(f"You don't have '{item}' in your inventory.")
            return
        
        print(f"\\n=== Inspecting {actual_item} ===")
        description = self._get_item_description(actual_item)
        print(description)
        
        # Add usage hints
        usage = self._get_item_usage(actual_item)
        if usage:
            print(f"Usage: {usage}")
    
    def _inspect_location_item(self, player: Dict[str, Any], world: Dict[str, Any], item: str) -> None:
        """Inspect an item in the current location."""
        current_location = get_current_location(world)
        location_data = world.get("locations", {}).get(current_location, {})
        
        # Find the actual item name
        actual_item = None
        for loc_item in location_data.get("items", []):
            if loc_item.lower() == item.lower():
                actual_item = loc_item
                break
        
        if not actual_item:
            print(f"You don't see '{item}' here.")
            return
        
        print(f"\\n=== Inspecting {actual_item} ===")
        description = self._get_item_description(actual_item)
        print(description)
        print("You could pick this up if you wanted to.")
    
    def _inspect_player(self, player: Dict[str, Any], world: Dict[str, Any]) -> None:
        """Inspect the player's current status."""
        print("\\n=== Inspecting Yourself ===")
        print(f"Name: {player.get('name', 'Unknown')}")
        print(f"Health: {player.get('health', 0)}/100")
        print(f"Gold: {player.get('gold', 0)} coins")
        print(f"Current Location: {get_current_location(world)}")
        
        inventory_count = len(player.get("inventory", []))
        print(f"Carrying: {inventory_count} item(s)")
        
        # Add status-based descriptions
        health = player.get("health", 0)
        if health > 80:
            print("You feel strong and healthy.")
        elif health > 50:
            print("You feel somewhat tired but capable.")
        elif health > 20:
            print("You feel weak and need rest.")
        else:
            print("You feel very weak and in danger.")
    
    def _get_item_description(self, item: str) -> str:
        """Get a detailed description of an item."""
        descriptions = {
            "bread": "A fresh loaf of bread, still warm and fragrant. It would restore some health.",
            "torch": "A wooden torch with oil-soaked cloth. Essential for exploring dark places.",
            "rope": "A sturdy coil of rope. Useful for climbing or securing things.",
            "sword": "A well-balanced steel sword with a sharp edge. A reliable weapon.",
            "map": "A detailed map of the local area showing various locations and paths.",
            "stick": "A sturdy wooden stick. Could be used as a simple weapon or tool.",
            "berries": "A handful of wild berries. They look safe to eat and might restore health.",
            "gemstone": "A beautiful, multifaceted gemstone that catches the light. Quite valuable.",
            "pickaxe": "A heavy mining pickaxe with a sharp metal head. Good for breaking rocks.",
            "mysterious_package": "A wrapped package with unknown contents. Someone wants this delivered.",
            "magic_crystal": "A glowing crystal that pulses with mysterious energy.",
            "rare_minerals": "Valuable minerals extracted from cave walls. Worth good money.",
            "oasis_water": "Crystal-clear water from a desert oasis. Very refreshing.",
            "ancient_coin": "An old coin with strange markings. Might be valuable to collectors.",
            "desert_cloak": "A light but protective cloak designed for desert travel.",
            "water_skin": "A leather container for carrying water. Essential for desert travel.",
            "dried_meat": "Preserved meat that will keep for a long time. Good for sustenance.",
            "cactus_fruit": "Sweet fruit from a desert cactus. Refreshing and nutritious.",
            "sand_crystal": "A beautiful crystal formed in the desert heat. Quite rare.",
            "desert_map": "A specialized map showing desert routes and oasis locations."
        }
        
        return descriptions.get(item.lower(), "An interesting item that might be useful.")
    
    def _get_item_usage(self, item: str) -> str:
        """Get usage information for an item."""
        usage_info = {
            "torch": "Use in dark places like caves to see clearly and avoid dangers.",
            "rope": "Use for climbing steep surfaces or securing items.",
            "sword": "Equip for combat to deal more damage to enemies.",
            "bread": "Eat to restore health when you're injured.",
            "berries": "Eat to restore a small amount of health.",
            "map": "Study to learn about nearby locations and connections.",
            "pickaxe": "Use to mine valuable materials from rock formations.",
            "mysterious_package": "Deliver to the hermit on the mountain peak.",
            "desert_cloak": "Wear to protect against sandstorms in the desert.",
            "water_skin": "Drink from to restore health in hot climates."
        }
        
        return usage_info.get(item.lower(), "")
    
    def _add_location_details(self, location: str) -> None:
        """Add atmospheric details for specific locations."""
        details = {
            "Village": "The village bustles with activity. You can hear the sounds of daily life and smell fresh bread from the bakery.",
            "Forest": "Sunlight filters through the canopy above. You hear birds singing and leaves rustling in the breeze.",
            "Cave": "The air is cool and damp. Water drips somewhere in the darkness, and your voice echoes off the walls.",
            "Mountain": "The air is thin and crisp. You can see for miles in every direction, and the wind is strong.",
            "Desert": "The sun beats down mercilessly. Heat waves shimmer in the distance, and the sand is hot beneath your feet."
        }
        
        detail = details.get(location)
        if detail:
            print(f"Atmosphere: {detail}")

