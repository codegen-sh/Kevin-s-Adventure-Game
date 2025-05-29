"""
Game Engine - Core game loop and state management for Kevin's Adventure Game
"""
from game.player import create_player, get_player_status
from game.world import initialize_world, get_current_location
from game.actions import perform_action
from utils.save_load import save_game, load_game, list_save_files
from utils.text_formatting import print_welcome_message, print_help


class GameEngine:
    """Main game engine that manages the game loop and state."""
    
    def __init__(self):
        self.player = None
        self.world = None
        self.running = False
    
    def start_new_game(self, player_name="Kevin"):
        """Start a new game with the given player name."""
        self.player = create_player(player_name)
        self.world = initialize_world()
        self.running = True
        print(f"Welcome, {player_name}! Your adventure begins...")
    
    def load_existing_game(self):
        """Load an existing game from save files."""
        save_files = list_save_files()
        if not save_files:
            print("No save files found. Starting a new game.")
            self.start_new_game()
            return
        
        print("Available save files:")
        for i, file in enumerate(save_files, 1):
            print(f"{i}. {file}")
        
        try:
            choice = int(input("Enter the number of the save file to load: "))
            if 1 <= choice <= len(save_files):
                self.player, self.world = load_game(save_files[choice - 1])
                if self.player is None or self.world is None:
                    print("Failed to load game. Starting a new game.")
                    self.start_new_game()
                else:
                    self.running = True
                    print("Game loaded successfully!")
            else:
                print("Invalid choice. Starting a new game.")
                self.start_new_game()
        except (ValueError, IndexError):
            print("Invalid input. Starting a new game.")
            self.start_new_game()
    
    def save_current_game(self):
        """Save the current game state."""
        if self.player and self.world:
            save_game(self.player, self.world)
            print("Game saved successfully!")
        else:
            print("No game to save.")
    
    def run_game_loop(self):
        """Main game loop."""
        if not self.running:
            print("No game is currently running. Start a new game first.")
            return
        
        while self.running:
            try:
                self.display_game_state()
                action = self.get_player_input()
                self.process_action(action)
            except KeyboardInterrupt:
                print("\nGame interrupted. Saving...")
                self.save_current_game()
                break
            except Exception as e:
                print(f"An error occurred: {e}")
                print("The game will continue...")
    
    def display_game_state(self):
        """Display the current game state to the player."""
        current_location = get_current_location(self.world)
        print(f"\n{'='*50}")
        print(f"You are in the {current_location}.")
        print(get_player_status(self.player))
        print(f"{'='*50}")
    
    def get_player_input(self):
        """Get and validate player input."""
        return input("What would you like to do? ").strip()
    
    def process_action(self, action):
        """Process the player's action."""
        action = action.lower()
        
        # Handle special game commands
        if action in ["quit", "exit", "q"]:
            self.quit_game()
        elif action in ["save"]:
            self.save_current_game()
        elif action in ["help", "h", "?"]:
            print_help()
        else:
            # Delegate to the action system
            perform_action(self.player, self.world, action)
    
    def quit_game(self):
        """Quit the game with save option."""
        save_choice = input("Do you want to save before quitting? (y/n): ").lower()
        if save_choice in ['y', 'yes']:
            self.save_current_game()
        
        print("Thanks for playing Kevin's Adventure Game!")
        self.running = False
    
    def is_game_over(self):
        """Check if the game should end (player death, etc.)."""
        return self.player and self.player.get('health', 0) <= 0


def main():
    """Main entry point for the game."""
    print_welcome_message()
    
    engine = GameEngine()
    
    # Ask if player wants to load a saved game
    load_option = input("Do you want to load a saved game? (y/n): ").lower()
    if load_option in ['y', 'yes']:
        engine.load_existing_game()
    else:
        player_name = input("Enter your character's name (or press Enter for 'Kevin'): ").strip()
        if not player_name:
            player_name = "Kevin"
        engine.start_new_game(player_name)
    
    # Run the main game loop
    engine.run_game_loop()


if __name__ == "__main__":
    main()

