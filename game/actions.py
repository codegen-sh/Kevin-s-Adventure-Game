"""
Action system for Kevin's Adventure Game.
Provides a comprehensive action registry and core game actions.
"""

from typing import Dict, List, Any, Optional
from abc import ABC, abstractmethod


class ActionResult:
    """Represents the result of an action execution."""
    
    def __init__(self, success: bool = True, message: str = "", should_continue: bool = True):
        self.success = success
        self.message = message
        self.should_continue = should_continue


class Action(ABC):
    """Base class for all game actions."""
    
    def __init__(self, name: str, aliases: List[str] = None, description: str = ""):
        self.name = name
        self.aliases = aliases or []
        self.description = description
    
    @abstractmethod
    def execute(self, player: Dict[str, Any], world: Dict[str, Any], args: List[str]) -> ActionResult:
        """Execute the action with the given context and arguments."""
        pass


class ActionRegistry:
    """Registry for managing game actions."""
    
    def __init__(self):
        self._actions: Dict[str, Action] = {}
        self._aliases: Dict[str, str] = {}
    
    def register(self, action: Action):
        """Register an action and its aliases."""
        self._actions[action.name] = action
        for alias in action.aliases:
            self._aliases[alias] = action.name
    
    def get_action(self, command: str) -> Optional[Action]:
        """Get an action by name or alias."""
        command = command.lower()
        if command in self._actions:
            return self._actions[command]
        if command in self._aliases:
            return self._actions[self._aliases[command]]
        return None
    
    def list_actions(self) -> List[Action]:
        """Get all registered actions."""
        return list(self._actions.values())


# Core Actions
class LookAction(Action):
    def __init__(self):
        super().__init__("look", ["l", "examine"], "Look around the current location")
    
    def execute(self, player: Dict[str, Any], world: Dict[str, Any], args: List[str]) -> ActionResult:
        from game.world import get_current_location_info
        location_info = get_current_location_info(world)
        return ActionResult(message=location_info)


class InventoryAction(Action):
    def __init__(self):
        super().__init__("inventory", ["i", "inv"], "Show your inventory")
    
    def execute(self, player: Dict[str, Any], world: Dict[str, Any], args: List[str]) -> ActionResult:
        from utils.text_formatting import format_inventory
        inventory_text = format_inventory(player['inventory'])
        return ActionResult(message=f"Inventory: {inventory_text}")


class HelpAction(Action):
    def __init__(self):
        super().__init__("help", ["h", "?"], "Show available commands")
    
    def execute(self, player: Dict[str, Any], world: Dict[str, Any], args: List[str]) -> ActionResult:
        from game.parser import CommandParser
        parser = CommandParser()
        help_text = parser.get_help_text()
        return ActionResult(message=help_text)


class QuitAction(Action):
    def __init__(self):
        super().__init__("quit", ["q", "exit"], "Quit the game")
    
    def execute(self, player: Dict[str, Any], world: Dict[str, Any], args: List[str]) -> ActionResult:
        from utils.save_load import save_game
        save_game(player, world)
        return ActionResult(
            message="Thanks for playing! Your progress has been saved.",
            should_continue=False
        )


class MoveAction(Action):
    def __init__(self):
        super().__init__("go", ["move", "travel"], "Move to another location")
    
    def execute(self, player: Dict[str, Any], world: Dict[str, Any], args: List[str]) -> ActionResult:
        if not args:
            return ActionResult(success=False, message="Where do you want to go?")
        
        destination = args[0].title()
        from game.world import get_current_location_connections, move_to_location
        
        connections = get_current_location_connections(world)
        if destination in connections:
            move_to_location(world, destination)
            from game.player import move_player
            move_player(player, destination)
            return ActionResult(message=f"You moved to: {destination}")
        else:
            available = ", ".join(connections)
            return ActionResult(
                success=False, 
                message=f"You can't go to {destination}. Available locations: {available}"
            )


class TakeAction(Action):
    def __init__(self):
        super().__init__("take", ["get", "pick", "pickup", "grab"], "Take an item")
    
    def execute(self, player: Dict[str, Any], world: Dict[str, Any], args: List[str]) -> ActionResult:
        if not args:
            return ActionResult(success=False, message="What do you want to take?")
        
        item_name = args[0].lower()
        from game.world import get_current_location
        current_location = get_current_location(world)
        location_data = world["locations"][current_location]
        
        # Check if item exists at location
        available_items = [item.lower() for item in location_data["items"]]
        if item_name not in available_items:
            available = ", ".join(location_data["items"]) if location_data["items"] else "nothing"
            return ActionResult(
                success=False, 
                message=f"There's no {item_name} here. Available items: {available}"
            )
        
        # Add to player inventory
        from game.player import add_item_to_inventory
        # Find the actual item name (with proper capitalization)
        actual_item = None
        for item in location_data["items"]:
            if item.lower() == item_name:
                actual_item = item
                break
        
        if actual_item:
            add_item_to_inventory(player, actual_item)
            location_data["items"].remove(actual_item)
            return ActionResult(message=f"You picked up: {actual_item}")
        
        return ActionResult(success=False, message="Couldn't take that item.")


class DropAction(Action):
    def __init__(self):
        super().__init__("drop", ["put", "place", "leave"], "Drop an item")
    
    def execute(self, player: Dict[str, Any], world: Dict[str, Any], args: List[str]) -> ActionResult:
        if not args:
            return ActionResult(success=False, message="What do you want to drop?")
        
        item_name = args[0].lower()
        
        # Check if player has the item
        player_items = [item.lower() for item in player["inventory"]]
        if item_name not in player_items:
            inventory_text = ", ".join(player["inventory"]) if player["inventory"] else "nothing"
            return ActionResult(
                success=False, 
                message=f"You don't have {item_name}. You have: {inventory_text}"
            )
        
        # Remove from player inventory and add to location
        from game.player import remove_item_from_inventory
        from game.world import get_current_location
        
        # Find actual item name
        actual_item = None
        for item in player["inventory"]:
            if item.lower() == item_name:
                actual_item = item
                break
        
        if actual_item and remove_item_from_inventory(player, actual_item):
            current_location = get_current_location(world)
            world["locations"][current_location]["items"].append(actual_item)
            return ActionResult(message=f"You dropped: {actual_item}")
        
        return ActionResult(success=False, message="Couldn't drop that item.")


class UseAction(Action):
    def __init__(self):
        super().__init__("use", ["utilize", "employ"], "Use an item")
    
    def execute(self, player: Dict[str, Any], world: Dict[str, Any], args: List[str]) -> ActionResult:
        if not args:
            return ActionResult(success=False, message="What do you want to use?")
        
        item_name = args[0].lower()
        
        # Check if player has the item
        player_items = [item.lower() for item in player["inventory"]]
        if item_name not in player_items:
            return ActionResult(
                success=False, 
                message=f"You don't have {item_name} to use."
            )
        
        # Handle specific item usage
        if item_name == "map":
            return ActionResult(message="The map shows the surrounding areas: Village, Forest, Cave, and Mountain.")
        elif item_name == "bread":
            if player["health"] < 100:
                heal_amount = 20
                player["health"] = min(100, player["health"] + heal_amount)
                from game.player import remove_item_from_inventory
                remove_item_from_inventory(player, "bread")
                return ActionResult(message=f"You ate the bread and recovered {heal_amount} health!")
            else:
                return ActionResult(message="You're already at full health.")
        elif item_name == "torch":
            from game.world import get_current_location
            current_location = get_current_location(world)
            if current_location == "Cave":
                return ActionResult(message="The torch illuminates the cave, revealing hidden passages and sparkling minerals.")
            else:
                return ActionResult(message="The torch provides light, but there's nothing special to see here.")
        elif item_name == "pickaxe":
            from game.world import get_current_location
            current_location = get_current_location(world)
            if current_location == "Cave" or current_location == "Mountain":
                return ActionResult(message="You could use this to mine for minerals. Try exploring the area!")
            else:
                return ActionResult(message="There's nothing to mine here.")
        else:
            return ActionResult(message=f"You're not sure how to use the {item_name}.")


class StatusAction(Action):
    def __init__(self):
        super().__init__("status", ["stats", "health"], "Show your current status")
    
    def execute(self, player: Dict[str, Any], world: Dict[str, Any], args: List[str]) -> ActionResult:
        from game.player import get_player_status
        from game.world import get_current_location
        
        status = get_player_status(player)
        location = get_current_location(world)
        
        detailed_status = f"=== Player Status ===\n"
        detailed_status += f"Name: {player['name']}\n"
        detailed_status += f"Location: {location}\n"
        detailed_status += f"{status}"
        
        return ActionResult(message=detailed_status)


class InteractAction(Action):
    def __init__(self):
        super().__init__("interact", ["explore", "search"], "Interact with your current location")
    
    def execute(self, player: Dict[str, Any], world: Dict[str, Any], args: List[str]) -> ActionResult:
        from game.world import interact_with_location
        
        # This will call the location-specific interaction
        interact_with_location(world, player)
        return ActionResult(message="")  # The interaction handles its own output


class SaveAction(Action):
    def __init__(self):
        super().__init__("save", ["s"], "Save your game")
    
    def execute(self, player: Dict[str, Any], world: Dict[str, Any], args: List[str]) -> ActionResult:
        from utils.save_load import save_game
        
        try:
            save_game(player, world)
            return ActionResult(message="Game saved successfully!")
        except Exception as e:
            return ActionResult(success=False, message=f"Failed to save game: {str(e)}")


class LoadAction(Action):
    def __init__(self):
        super().__init__("load", ["l"], "Load a saved game")
    
    def execute(self, player: Dict[str, Any], world: Dict[str, Any], args: List[str]) -> ActionResult:
        from utils.save_load import list_save_files, load_game
        
        save_files = list_save_files()
        if not save_files:
            return ActionResult(success=False, message="No save files found.")
        
        message = "Available save files:\n"
        for i, file in enumerate(save_files, 1):
            message += f"{i}. {file}\n"
        message += "Use 'load [number]' to load a specific save file."
        
        if args:
            try:
                choice = int(args[0]) - 1
                if 0 <= choice < len(save_files):
                    loaded_player, loaded_world = load_game(save_files[choice])
                    if loaded_player and loaded_world:
                        # Update the current game state
                        player.update(loaded_player)
                        world.update(loaded_world)
                        return ActionResult(message=f"Loaded save file: {save_files[choice]}")
                    else:
                        return ActionResult(success=False, message="Failed to load the save file.")
                else:
                    return ActionResult(success=False, message="Invalid save file number.")
            except ValueError:
                return ActionResult(success=False, message="Please provide a valid number.")
        
        return ActionResult(message=message)


# Global action registry
_action_registry = ActionRegistry()

# Register all actions
_action_registry.register(LookAction())
_action_registry.register(InventoryAction())
_action_registry.register(HelpAction())
_action_registry.register(QuitAction())
_action_registry.register(MoveAction())
_action_registry.register(TakeAction())
_action_registry.register(DropAction())
_action_registry.register(UseAction())
_action_registry.register(StatusAction())
_action_registry.register(InteractAction())
_action_registry.register(SaveAction())
_action_registry.register(LoadAction())


def perform_action(player: Dict[str, Any], world: Dict[str, Any], command: str) -> ActionResult:
    """
    Main entry point for executing actions.
    This function maintains compatibility with the existing main.py structure.
    """
    from game.parser import CommandParser
    
    parser = CommandParser()
    action_name, args = parser.parse(command)
    
    if not action_name:
        return ActionResult(success=False, message="Please enter a command.")
    
    action = _action_registry.get_action(action_name)
    if action:
        return action.execute(player, world, args)
    else:
        # Try to suggest a similar command
        suggestion = parser.suggest_command(action_name)
        if suggestion:
            return ActionResult(
                success=False, 
                message=f"Unknown command: {action_name}. Did you mean '{suggestion}'? Type 'help' for available commands."
            )
        else:
            return ActionResult(
                success=False, 
                message=f"Unknown command: {action_name}. Type 'help' for available commands."
            )


def get_action_registry() -> ActionRegistry:
    """Get the global action registry."""
    return _action_registry

