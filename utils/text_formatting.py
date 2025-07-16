import textwrap


def wrap_text(text, width=80):
    """Wrap text to a specified width."""
    return textwrap.fill(text, width=width)

def print_welcome_message():
    """Print a formatted welcome message for the game."""
    welcome_text = """
🌈 Welcome to Kevin's Adventure Game! 🌈

Explore a world of mystery and danger as you navigate through
forests, caves, villages, and mountains. Collect items, interact
with characters, and uncover the secrets of this magical realm.

Type 'help' at any time to see available commands.

🌈 Your journey begins now. Good luck, adventurer! 🌈
    """
    print(welcome_text.strip())

def print_help():
    """Print a formatted help message with available commands."""
    help_text = """
🌈 Available commands:
- move [location]: Move to a new location
- look: Examine your surroundings
- inventory: Check your inventory
- pickup [item]: Pick up an item
- drop [item]: Drop an item from your inventory
- use [item]: Use an item
- examine [item]: Get a description of an item
- status: Check your current status
- interact: Interact with your current location
- help: Show this help message
- quit: Save and exit the game
    """
    print(help_text.strip())

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
    🌈 Game Over 🌈

    Your adventure has come to an end. Thank you for playing!
    """
    print_separator("=")
    print(game_over_text)
    print_separator("=")
