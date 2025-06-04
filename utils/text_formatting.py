import textwrap


def wrap_text(text, width=80):
    """Wrap text to a specified width."""
    return textwrap.fill(text, width=width)

def print_welcome_message():
    """Print a formatted welcome message for the game."""
    welcome_text = """
Welcome to Kevin's Adventure Game!

Explore a world of mystery and danger as you navigate through
forests, caves, villages, and mountains. Collect items, interact
with characters, and uncover the secrets of this magical realm.

Type 'help' at any time to see available commands.

Your journey begins now. Good luck, adventurer!
    """
    print(welcome_text.strip())

def print_help():
    """Print a formatted help message with available commands."""
    print("\\n=== Kevin's Adventure Game - Help ===")
    print("Available commands:")
    print("  help - Show this help message")
    print("  quit - Save and exit the game")
    print("  go/move/travel - Show available locations")
    print("  <location name> - Travel to a specific location")
    print("  explore/interact/look - Interact with current location")
    print("  inventory/inv/items - Show your inventory")
    print("  status/stats - Show your current status")
    print("  plugins - Show plugin system status")
    print("\\nGame Tips:")
    print("  - Explore different locations to find items and adventures")
    print("  - Keep an eye on your health and gold")
    print("  - Some locations have special interactions")
    print("  - Your progress is automatically saved when you quit")
    print("\\nPlugin Commands:")
    print("  - Additional commands may be available through plugins")
    print("  - Use 'plugins' to see what plugins are loaded")
    print("  - Plugin-specific help will be shown with this command")

def format_inventory(inventory):
    """Format the player's inventory for display."""
    if not inventory:
        return "empty"
    return ", ".join(inventory)

def print_separator(char="-", length=80):
    """Print a separator line."""
    print(char * length)

def print_event(event_text):
    """Print a formatted event message."""
    print_separator()
    print(wrap_text(event_text))
    print_separator()

def print_game_over():
    """Print a formatted game over message."""
    game_over_text = """
    Game Over

    Your adventure has come to an end. Thank you for playing!
    """
    print_separator("=")
    print(game_over_text)
    print_separator("=")
