from game.actions import perform_action
from game.player import create_player, get_player_status
from game.world import get_current_location, initialize_world
from utils.save_load import (
    list_save_files, load_game, save_game, list_save_slots, 
    save_to_slot, load_from_slot, start_auto_save, stop_auto_save,
    get_save_statistics, backup_save_slot
)
from utils.text_formatting import print_help, print_welcome_message


def display_save_slots():
    """Display available save slots with metadata."""
    slots = list_save_slots()
    print("\n=== Save Slots ===")
    
    for slot in slots:
        if slot["exists"]:
            metadata = slot["metadata"]
            print(f"Slot {slot['slot_id']}: {metadata.get('player_name', 'Unknown')} - "
                  f"Level {metadata.get('player_level', 0)} - "
                  f"Location: {metadata.get('location', 'Unknown')} - "
                  f"Gold: {metadata.get('gold', 0)}")
            if slot["is_current"]:
                print("  (Current)")
        else:
            print(f"Slot {slot['slot_id']}: [Empty]")
    print("==================")


def save_menu(player, world):
    """Display save menu and handle save operations."""
    while True:
        print("\n=== Save Menu ===")
        print("1. Quick Save (current slot)")
        print("2. Save to specific slot")
        print("3. View save slots")
        print("4. Backup current slot")
        print("5. View save statistics")
        print("6. Back to game")
        
        choice = input("Choose an option: ").strip()
        
        if choice == "1":
            if save_game(player, world):
                print("Quick save completed!")
            break
        elif choice == "2":
            display_save_slots()
            try:
                slot_id = int(input("Enter slot number (1-10): "))
                if 1 <= slot_id <= 10:
                    if save_to_slot(slot_id, player, world):
                        print(f"Game saved to slot {slot_id}!")
                    break
                else:
                    print("Invalid slot number. Please enter 1-10.")
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "3":
            display_save_slots()
        elif choice == "4":
            display_save_slots()
            try:
                slot_id = int(input("Enter slot number to backup (1-10): "))
                if 1 <= slot_id <= 10:
                    backup_save_slot(slot_id)
                else:
                    print("Invalid slot number. Please enter 1-10.")
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "5":
            stats = get_save_statistics()
            print("\n=== Save Statistics ===")
            print(f"Total slots used: {stats.get('total_slots', 0)}/{stats.get('max_slots', 10)}")
            print(f"Total size: {stats.get('total_size_mb', 0)} MB")
            print(f"Auto-save enabled: {stats.get('auto_save_enabled', False)}")
            if stats.get('auto_save_enabled'):
                print(f"Auto-save interval: {stats.get('auto_save_interval_minutes', 5)} minutes")
            backup_stats = stats.get('backup_stats', {})
            print(f"Total backups: {backup_stats.get('total_backups', 0)}")
            print(f"Backup size: {backup_stats.get('total_size_mb', 0)} MB")
            print("=======================")
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")


def load_menu():
    """Display load menu and handle load operations."""
    while True:
        print("\n=== Load Menu ===")
        print("1. Load from save slot")
        print("2. Load legacy save file")
        print("3. View save slots")
        print("4. Start new game")
        
        choice = input("Choose an option: ").strip()
        
        if choice == "1":
            display_save_slots()
            try:
                slot_id = int(input("Enter slot number to load (1-10): "))
                if 1 <= slot_id <= 10:
                    player, world = load_from_slot(slot_id)
                    if player and world:
                        return player, world
                    else:
                        print("Failed to load from that slot.")
                else:
                    print("Invalid slot number. Please enter 1-10.")
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "2":
            save_files = list_save_files()
            legacy_files = [f for f in save_files if f.endswith('.json')]
            
            if legacy_files:
                print("Available legacy save files:")
                for i, file in enumerate(legacy_files, 1):
                    print(f"{i}. {file}")
                try:
                    choice_idx = int(input("Enter the number of the save file to load: "))
                    if 1 <= choice_idx <= len(legacy_files):
                        player, world = load_game(legacy_files[choice_idx - 1])
                        if player and world:
                            return player, world
                        else:
                            print("Failed to load game.")
                    else:
                        print("Invalid choice.")
                except ValueError:
                    print("Please enter a valid number.")
            else:
                print("No legacy save files found.")
        elif choice == "3":
            display_save_slots()
        elif choice == "4":
            return None, None
        else:
            print("Invalid choice. Please try again.")


def main():
    print_welcome_message()

    # Enhanced load game option
    load_option = input("Do you want to load a saved game? (y/n): ").lower()
    if load_option == 'y':
        player, world = load_menu()
        if player is None or world is None:
            print("Starting a new game.")
            player = create_player("Kevin")
            world = initialize_world()
    else:
        player = create_player("Kevin")
        world = initialize_world()

    # Ask about auto-save
    auto_save_option = input("Enable auto-save? (y/n): ").lower()
    if auto_save_option == 'y':
        try:
            interval = int(input("Auto-save interval in minutes (default 5): ") or "5")
            start_auto_save(player, world, interval)
        except ValueError:
            start_auto_save(player, world, 5)  # Default to 5 minutes

    print("\nGame started! Type 'help' for available commands.")
    print("New commands: 'save' (save menu), 'stats' (save statistics)")

    while True:
        current_location = get_current_location(world)
        print(f"\nYou are in the {current_location}.")
        print(get_player_status(player))

        action = input("What would you like to do? ").lower()

        if action == "quit":
            # Stop auto-save before quitting
            stop_auto_save()
            
            # Offer to save before quitting
            save_option = input("Save before quitting? (y/n): ").lower()
            if save_option == 'y':
                save_menu(player, world)
            
            print("Thanks for playing!")
            break
        elif action == "help":
            print_help()
            print("\nAdvanced save commands:")
            print("- 'save': Open save menu")
            print("- 'stats': View save statistics")
        elif action == "save":
            save_menu(player, world)
        elif action == "stats":
            stats = get_save_statistics()
            print("\n=== Save Statistics ===")
            print(f"Total slots used: {stats.get('total_slots', 0)}/{stats.get('max_slots', 10)}")
            print(f"Total size: {stats.get('total_size_mb', 0)} MB")
            print(f"Auto-save enabled: {stats.get('auto_save_enabled', False)}")
            if stats.get('auto_save_enabled'):
                print(f"Auto-save interval: {stats.get('auto_save_interval_minutes', 5)} minutes")
            print("=======================")
        else:
            perform_action(player, world, action)

if __name__ == "__main__":
    main()
