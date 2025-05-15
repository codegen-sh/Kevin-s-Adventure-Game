"""
Command processor for handling player input.
"""
from typing import Dict, List, Optional, Callable, Any


class CommandProcessor:
    """Processes player commands and executes the appropriate actions."""

    def __init__(self, game):
        """Initialize the command processor with a reference to the game."""
        self.game = game
        self.commands = {
            "quit": self._quit,
            "help": self._help,
            "look": self._look,
            "inventory": self._inventory,
            "status": self._status,
            "move": self._move,
            "go": self._move,  # Alias for move
            "pickup": self._pickup,
            "take": self._pickup,  # Alias for pickup
            "drop": self._drop,
            "use": self._use,
            "examine": self._examine,
            "interact": self._interact,
        }

    def process(self, command_text: str) -> bool:
        """
        Process a command string and execute the appropriate action.
        
        Args:
            command_text: The command text entered by the player
            
        Returns:
            bool: True if the command was processed successfully, False otherwise
        """
        if not command_text:
            self.game.ui.display_message("Please enter a command.")
            return False

        # Split the command into the action and arguments
        parts = command_text.strip().lower().split(maxsplit=1)
        action = parts[0]
        args = parts[1] if len(parts) > 1 else ""

        # Execute the command if it exists
        if action in self.commands:
            return self.commands[action](args)
        else:
            self.game.ui.display_message(f"Unknown command: {action}. Type 'help' for a list of commands.")
            return False

    def _quit(self, args: str) -> bool:
        """Quit the game."""
        self.game.quit()
        return True

    def _help(self, args: str) -> bool:
        """Display help information."""
        self.game.ui.display_help()
        return True

    def _look(self, args: str) -> bool:
        """Look around the current location."""
        current_location = self.game.world.get_current_location()
        self.game.ui.display_message(current_location.get_description())
        
        # Show available items
        items = current_location.get_items()
        if items:
            self.game.ui.display_message("You can see the following items:")
            for item in items:
                self.game.ui.display_message(f"- {item.name}")
        
        # Show available exits
        connections = current_location.get_connections()
        if connections:
            self.game.ui.display_message("You can go to:")
            for connection in connections:
                self.game.ui.display_message(f"- {connection}")
        
        return True

    def _inventory(self, args: str) -> bool:
        """Display the player's inventory."""
        self.game.ui.display_message(f"Inventory: {self.game.player.format_inventory()}")
        return True

    def _status(self, args: str) -> bool:
        """Display the player's status."""
        self.game.ui.display_message(self.game.player.get_status())
        return True

    def _move(self, args: str) -> bool:
        """Move to a new location."""
        if not args:
            self.game.ui.display_message("Move where? Please specify a location.")
            return False
        
        destination = args.capitalize()
        if self.game.world.is_location_accessible(destination):
            self.game.world.change_location(destination)
            self.game.player.move(destination)
            self.game.ui.display_message(f"You moved to: {destination}")
            return True
        else:
            self.game.ui.display_message(f"You can't go to {destination} from here.")
            return False

    def _pickup(self, args: str) -> bool:
        """Pick up an item from the current location."""
        if not args:
            self.game.ui.display_message("Pick up what? Please specify an item.")
            return False
        
        item_name = args.lower()
        current_location = self.game.world.get_current_location()
        item = current_location.get_item(item_name)
        
        if item:
            self.game.player.add_item(item)
            current_location.remove_item(item_name)
            self.game.ui.display_message(f"You picked up: {item.name}")
            return True
        else:
            self.game.ui.display_message(f"There is no {item_name} here.")
            return False

    def _drop(self, args: str) -> bool:
        """Drop an item from the player's inventory."""
        if not args:
            self.game.ui.display_message("Drop what? Please specify an item.")
            return False
        
        item_name = args.lower()
        item = self.game.player.get_item(item_name)
        
        if item:
            current_location = self.game.world.get_current_location()
            self.game.player.remove_item(item_name)
            current_location.add_item(item)
            self.game.ui.display_message(f"You dropped: {item.name}")
            return True
        else:
            self.game.ui.display_message(f"You don't have {item_name} in your inventory.")
            return False

    def _use(self, args: str) -> bool:
        """Use an item from the player's inventory."""
        if not args:
            self.game.ui.display_message("Use what? Please specify an item.")
            return False
        
        item_name = args.lower()
        item = self.game.player.get_item(item_name)
        
        if item:
            return item.use(self.game.player, self.game.world)
        else:
            self.game.ui.display_message(f"You don't have {item_name} in your inventory.")
            return False

    def _examine(self, args: str) -> bool:
        """Examine an item in the player's inventory or in the current location."""
        if not args:
            self.game.ui.display_message("Examine what? Please specify an item.")
            return False
        
        item_name = args.lower()
        
        # Check inventory first
        item = self.game.player.get_item(item_name)
        if not item:
            # If not in inventory, check current location
            current_location = self.game.world.get_current_location()
            item = current_location.get_item(item_name)
        
        if item:
            self.game.ui.display_message(item.get_description())
            return True
        else:
            self.game.ui.display_message(f"You don't see {item_name} anywhere.")
            return False

    def _interact(self, args: str) -> bool:
        """Interact with the current location."""
        current_location = self.game.world.get_current_location()
        return current_location.interact(self.game.player, self.game.world)

