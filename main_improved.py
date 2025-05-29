#!/usr/bin/env python3
"""
Kevin's Adventure Game - Improved Version
A text-based adventure game with object-oriented design.
"""

from game.engine import GameEngine
from game.player_class import Player
from game.world_class import create_default_world
from utils.text_formatting import print_welcome_message


def main():
    """Main entry point for the improved version of Kevin's Adventure Game."""
    try:
        # Use the new game engine
        from game.engine import main as engine_main
        engine_main()
    except KeyboardInterrupt:
        print("\n\nGame interrupted by user. Goodbye!")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
        print("Please report this issue if it persists.")


def demo_new_features():
    """Demonstrate the new object-oriented features."""
    print("=== Kevin's Adventure Game - New Features Demo ===\n")
    
    # Create a player using the new class
    player = Player("Kevin", health=100, gold=150)
    print(f"Created player: {player}")
    print(f"Player status: {player.get_status()}\n")
    
    # Create the world using the new class
    world = create_default_world()
    print(f"Created world with {len(world.locations)} locations")
    print(f"Current location: {world.get_current_location()}")
    print(f"World status: {world.get_world_status()}\n")
    
    # Demonstrate player actions
    print("=== Demonstrating Player Actions ===")
    player.add_item("sword")
    player.add_item("healing potion")
    player.show_inventory()
    
    print("\nUsing healing potion...")
    player.take_damage(30)  # Take some damage first
    player.use_item("healing potion")
    
    print(f"\nFinal player status: {player.get_status()}")
    
    # Demonstrate world navigation
    print("\n=== Demonstrating World Navigation ===")
    print(f"Available locations from {world.current_location}: {world.get_available_locations()}")
    
    if world.move_to_location("Forest"):
        print(f"Moved to: {world.current_location}")
        print(f"Location description: {world.get_current_location_description()}")
    
    print(f"\nWorld status: {world.get_world_status()}")


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == "--demo":
        demo_new_features()
    else:
        main()

