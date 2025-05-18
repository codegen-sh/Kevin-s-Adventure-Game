from game.player import update_player_inventory
from utils.text_formatting import print_event

def perform_action(player, world, action):
    """Process player actions and update game state accordingly."""
    action_parts = action.split()
    command = action_parts[0] if action_parts else ""
    
    # Handle different commands
    if command == "move":
        if len(action_parts) > 1:
            destination = action_parts[1]
            move_player(player, world, destination)
        else:
            print("Where do you want to move to?")
    
    elif command == "look":
        look_around(world)
    
    elif command == "inventory":
        show_inventory(player)
    
    elif command == "pickup":
        if len(action_parts) > 1:
            item = action_parts[1]
            pickup_item(player, world, item)
        else:
            print("What do you want to pick up?")
    
    elif command == "drop":
        if len(action_parts) > 1:
            item = action_parts[1]
            drop_item(player, world, item)
        else:
            print("What do you want to drop?")
    
    elif command == "use":
        if len(action_parts) > 1:
            item = action_parts[1]
            use_item(player, world, item)
        else:
            print("What do you want to use?")
    
    elif command == "examine":
        if len(action_parts) > 1:
            item = action_parts[1]
            examine_item(player, world, item)
        else:
            print("What do you want to examine?")
    
    elif command == "status":
        show_status(player)
    
    elif command == "interact":
        interact_with_location(player, world)
    
    elif command == "emoji":
        if len(action_parts) > 1:
            emoji_name = action_parts[1]
            display_emoji(emoji_name)
        else:
            print("Available emojis: smile, laugh, sad, heart, star, fire")
            print("Usage: emoji [name]")
    
    else:
        print("I don't understand that command. Type 'help' for a list of commands.")

def move_player(player, world, destination):
    """Move the player to a new location."""
    # This would be implemented with actual game logic
    print(f"Moving to {destination}...")
    
def look_around(world):
    """Describe the current surroundings."""
    # This would be implemented with actual game logic
    print("You look around and see various interesting things.")

def show_inventory(player):
    """Display the player's inventory."""
    inventory = player.get("inventory", [])
    if inventory:
        print("Your inventory contains: " + ", ".join(inventory))
    else:
        print("Your inventory is empty.")

def pickup_item(player, world, item):
    """Pick up an item from the current location."""
    # This would be implemented with actual game logic
    print(f"You picked up the {item}.")
    
def drop_item(player, world, item):
    """Drop an item from the player's inventory."""
    # This would be implemented with actual game logic
    print(f"You dropped the {item}.")

def use_item(player, world, item):
    """Use an item from the player's inventory."""
    # This would be implemented with actual game logic
    print(f"You used the {item}.")

def examine_item(player, world, item):
    """Get a description of an item."""
    # This would be implemented with actual game logic
    print(f"The {item} looks interesting.")

def show_status(player):
    """Show the player's current status."""
    # This would be implemented with actual game logic
    print("You are feeling adventurous!")

def interact_with_location(player, world):
    """Interact with the current location."""
    # This would be implemented with actual game logic
    print("You interact with your surroundings.")

def display_emoji(emoji_name):
    """Display an emoji based on the name provided."""
    emoji_map = {
        "smile": "😊",
        "laugh": "😄",
        "sad": "😢",
        "heart": "❤️",
        "star": "⭐",
        "fire": "🔥"
    }
    
    if emoji_name in emoji_map:
        print(f"Emoji: {emoji_map[emoji_name]}")
        print_event(f"You express yourself with a {emoji_name} {emoji_map[emoji_name]}")
    else:
        print(f"Unknown emoji: {emoji_name}")
        print("Available emojis: smile, laugh, sad, heart, star, fire")

