import textwrap


def wrap_text(text, width=80):
    """Wrap text to a specified width."""
    return textwrap.fill(text, width=width)


def print_welcome_message():
    """Print a formatted welcome message for the game."""
    welcome_text = """
╔═══════════════════════════════════════════════════════════════╗
║                 Welcome to Kevin's Adventure Game!            ║
╚═══════════════════════════════════════════════════════════════╝

Explore a world of mystery and danger as you navigate through
forests, caves, villages, and mountains. Collect items, interact
with characters, and uncover the secrets of this magical realm.

Type 'help' at any time to see available commands.

Your journey begins now. Good luck, adventurer!
    """
    print(welcome_text.strip())


def print_help():
    """Print a formatted help message with available commands."""
    help_text = """
╔═══════════════════════════════════════════════════════════════╗
║                       Available Commands                      ║
╚═══════════════════════════════════════════════════════════════╝

Movement:
- go [location] or move [location]: Travel to a connected location
- locations: Show available locations you can travel to

Exploration:
- look or look around: Examine your surroundings
- examine [item] or look [item]: Get a description of an item

Inventory:
- inventory or inv: Check your inventory
- take [item] or pickup [item]: Pick up an item
- drop [item]: Drop an item from your inventory
- use [item] or interact [item]: Use an item from your inventory

Other:
- interact: Interact with your current location
- status: Check your current health, gold, and inventory
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
╔═══════════════════════════════════════════════════════════════╗
║                          GAME OVER                            ║
╚═══════════════════════════════════════════════════════════════╝

Your adventure has come to an end. Thank you for playing!
    """
    print(game_over_text)


def print_success(message):
    """Print a success message with formatting."""
    print(f"\n✅ {message}")


def print_error(message):
    """Print an error message with formatting."""
    print(f"\n❌ {message}")


def print_warning(message):
    """Print a warning message with formatting."""
    print(f"\n⚠️ {message}")


def print_info(message):
    """Print an informational message with formatting."""
    print(f"\n📌 {message}")
