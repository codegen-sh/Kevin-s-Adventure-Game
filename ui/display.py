"""
Display module for handling all text output and formatting.
Separates presentation logic from game logic.
"""
from typing import Dict, Any, List, Optional
from game.constants import Colors, GAME_TITLE


class GameDisplay:
    """Handles all game display and formatting operations."""
    
    @staticmethod
    def print_welcome_message() -> None:
        """Print the game welcome message."""
        print("=" * 50)
        print(f"🎮 Welcome to {GAME_TITLE}! 🎮")
        print("=" * 50)
        print("Embark on an epic adventure filled with mystery and wonder!")
        print("Type 'help' at any time to see available commands.")
        print("=" * 50)
    
    @staticmethod
    def print_help() -> None:
        """Print help information."""
        help_text = """
🆘 HELP - Available Commands:

📍 Movement:
  • go, move, travel, walk [location] - Move to a location
  • location, where - Show current location

🎒 Inventory:
  • inventory, inv, i - Show your inventory
  • use [item] - Use an item from inventory
  • take [item], get [item] - Pick up an item
  • drop [item] - Drop an item

🔍 Examination:
  • look, examine, l - Look around current location
  • examine [target] - Examine a specific item or location

💬 Interaction:
  • interact, talk - Interact with current location
  • explore, search - Explore current location thoroughly

📊 Status:
  • status, stats, health - Show player status
  • wait, rest - Rest and recover

🎮 Game:
  • save - Save your progress
  • help - Show this help message
  • quit - Exit the game

💡 Examples:
  • go village
  • use bread
  • take map
  • examine sword
  • look around
        """
        print(help_text)
    
    @staticmethod
    def print_colored(text: str, color: str = Colors.WHITE) -> None:
        """Print colored text (placeholder for future color implementation)."""
        # For now, just print normally. Could be extended with ANSI color codes
        color_prefixes = {
            Colors.RED: "❌ ",
            Colors.GREEN: "✅ ",
            Colors.YELLOW: "⚠️ ",
            Colors.BLUE: "ℹ️ ",
            Colors.PURPLE: "🔮 ",
            Colors.CYAN: "💎 ",
        }
        
        prefix = color_prefixes.get(color, "")
        print(f"{prefix}{text}")
    
    @staticmethod
    def print_event(text: str) -> None:
        """Print a special event message."""
        print(f"🌟 {text}")
    
    @staticmethod
    def print_location_header(location_name: str) -> None:
        """Print a formatted location header."""
        print(f"\n📍 === {location_name} ===")
    
    @staticmethod
    def print_inventory(player: Dict[str, Any]) -> None:
        """Print formatted inventory display."""
        inventory = player.get("inventory", [])
        gold = player.get("gold", 0)
        
        print("\n🎒 === Your Inventory ===")
        if inventory:
            for i, item in enumerate(inventory, 1):
                print(f"  {i}. {item}")
        else:
            print("  Your inventory is empty.")
        print(f"💰 Gold: {gold}")
        print("=" * 25)
    
    @staticmethod
    def print_status(player: Dict[str, Any]) -> None:
        """Print formatted player status."""
        name = player.get("name", "Unknown")
        health = player.get("health", 0)
        gold = player.get("gold", 0)
        location = player.get("location", "Unknown")
        inventory_count = len(player.get("inventory", []))
        
        print(f"\n👤 {name}")
        print(f"❤️  Health: {health}/100")
        print(f"💰 Gold: {gold}")
        print(f"📍 Location: {location}")
        print(f"🎒 Items: {inventory_count}")
    
    @staticmethod
    def print_available_items(items: List[str]) -> None:
        """Print available items in current location."""
        if items:
            print("\n✨ Items you can see:")
            for item in items:
                print(f"  • {item}")
        else:
            print("\n🔍 No items visible here.")
    
    @staticmethod
    def print_available_exits(exits: List[str]) -> None:
        """Print available exits from current location."""
        if exits:
            print(f"\n🚪 You can go to: {', '.join(exits)}")
        else:
            print("\n🚫 No exits available.")
    
    @staticmethod
    def print_game_over() -> None:
        """Print game over message."""
        print("\n" + "=" * 30)
        print("💀 GAME OVER 💀")
        print("Your adventure has come to an end...")
        print("Better luck next time!")
        print("=" * 30)
    
    @staticmethod
    def print_victory() -> None:
        """Print victory message."""
        print("\n" + "=" * 30)
        print("🎉 VICTORY! 🎉")
        print("Congratulations on completing your adventure!")
        print("You are a true hero!")
        print("=" * 30)
    
    @staticmethod
    def print_save_message() -> None:
        """Print save confirmation message."""
        GameDisplay.print_colored("💾 Game saved successfully!", Colors.GREEN)
    
    @staticmethod
    def print_load_message() -> None:
        """Print load confirmation message."""
        GameDisplay.print_colored("📁 Game loaded successfully!", Colors.GREEN)
    
    @staticmethod
    def print_error(message: str) -> None:
        """Print error message."""
        GameDisplay.print_colored(f"Error: {message}", Colors.RED)
    
    @staticmethod
    def print_warning(message: str) -> None:
        """Print warning message."""
        GameDisplay.print_colored(f"Warning: {message}", Colors.YELLOW)
    
    @staticmethod
    def print_info(message: str) -> None:
        """Print info message."""
        GameDisplay.print_colored(message, Colors.BLUE)
    
    @staticmethod
    def format_inventory(inventory: List[str]) -> str:
        """Format inventory as a string."""
        if not inventory:
            return "empty"
        return ", ".join(inventory)
    
    @staticmethod
    def print_separator(char: str = "-", length: int = 40) -> None:
        """Print a separator line."""
        print(char * length)


# Global display instance for easy access
display = GameDisplay()

