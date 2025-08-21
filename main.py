from game.actions import perform_action
from game.player import create_player, get_player_status
from game.world import get_current_location, initialize_world
from utils.save_load import list_save_files, load_game, save_game
from utils.text_formatting import print_help, print_welcome_message


def main():
    print_welcome_message()

    # Add load game option
    load_option = input("Do you want to load a saved game? (y/n): ").lower()
    if load_option == 'y':
        save_files = list_save_files()
        if save_files:
            print("Available save files:")
            for i, file in enumerate(save_files, 1):
                print(f"{i}. {file}")
            try:
                choice = int(input("Enter the number of the save file to load: "))
                player, world = load_game(save_files[choice - 1])
                if player is None or world is None:
                    print("Failed to load game. Starting a new game.")
                    player = create_player("Kevin")
                    world = initialize_world()
            except (ValueError, IndexError):
                print("Invalid choice. Starting a new game.")
                player = create_player("Kevin")
                world = initialize_world()
        else:
            print("No save files found. Starting a new game.")
            player = create_player("Kevin")
            world = initialize_world()
    else:
        player = create_player("Kevin")
        world = initialize_world()

    # Main game loop
    while True:
        current_location = get_current_location(world)
        print(f"\nYou are in the {current_location}.")
        print(get_player_status(player))

        action = input("What would you like to do? ").strip()
        
        if not action:
            print("Please enter a command. Type 'help' for available commands.")
            continue

        # Use the new action system
        result = perform_action(player, world, action)
        
        if result.message:
            print(result.message)
        
        if not result.should_continue:
            break

if __name__ == "__main__":
    main()

