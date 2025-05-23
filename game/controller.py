"""
Game Controller Module - Central game management and coordination.
Implements the Controller pattern for better game architecture.
"""

from game.player import create_player, get_player_status
from game.world import initialize_world, get_current_location
from game.actions import perform_action
from game.weather import apply_weather_effects, change_weather
from game.config import get_setting
from utils.save_load import save_game, load_game, list_save_files
from utils.text_formatting import print_welcome_message, print_help
import random


class GameController:
    """
    Central game controller that manages the game state and coordinates
    between different game systems.
    """
    
    def __init__(self):
        self.player = None
        self.world = None
        self.game_running = False
        self.turn_counter = 0
        
    def start_new_game(self, player_name=None):
        """Initialize a new game with default settings."""
        if player_name is None:
            player_name = get_setting('game', 'default_player_name', 'Kevin')
            
        self.player = create_player(player_name)
        self.world = initialize_world()
        self.game_running = True
        self.turn_counter = 0
        print(f"🎮 Starting new adventure for {player_name}!")
        
    def load_existing_game(self):
        """Load an existing saved game."""
        save_files = list_save_files()
        
        if not save_files:
            print("No save files found. Starting a new game.")
            return False
            
        print("Available save files:")
        for i, file in enumerate(save_files, 1):
            print(f"{i}. {file}")
            
        try:
            choice = int(input("Enter the number of the save file to load: "))
            if 1 <= choice <= len(save_files):
                self.player, self.world = load_game(save_files[choice - 1])
                
                if self.player is None or self.world is None:
                    print("Failed to load game. Starting a new game.")
                    return False
                    
                self.game_running = True
                print("✅ Game loaded successfully!")
                return True
            else:
                print("Invalid choice. Starting a new game.")
                return False
                
        except (ValueError, IndexError):
            print("Invalid input. Starting a new game.")
            return False
    
    def initialize_game(self):
        """Initialize the game with user choice of new or loaded game."""
        print_welcome_message()
        
        load_option = input("Do you want to load a saved game? (y/n): ").lower()
        
        if load_option == 'y':
            if not self.load_existing_game():
                self.start_new_game()
        else:
            default_name = get_setting('game', 'default_player_name', 'Kevin')
            player_name = input(f"Enter your character's name (or press Enter for '{default_name}'): ").strip()
            if not player_name:
                player_name = default_name
            self.start_new_game(player_name)
    
    def run_game_loop(self):
        """Main game loop that handles turn-based gameplay."""
        if not self.game_running:
            print("Game not initialized. Call initialize_game() first.")
            return
            
        print("\n🌟 Welcome to your adventure!")
        print("Type 'help' at any time to see available commands.")
        print("Type 'quit' to save and exit the game.")
        
        while self.game_running:
            try:
                self.process_turn()
            except KeyboardInterrupt:
                print("\n\n⚠️  Game interrupted. Saving your progress...")
                self.save_and_quit()
                break
            except Exception as e:
                print(f"An error occurred: {e}")
                print("The game will continue, but you may want to save and restart.")
    
    def process_turn(self):
        """Process a single game turn."""
        self.turn_counter += 1
        
        # Apply periodic effects
        self.apply_periodic_effects()
        
        # Display current status
        self.display_turn_info()
        
        # Get and process player input
        action = input("\n🎯 What would you like to do? ").strip()
        
        if action.lower() == "quit":
            self.save_and_quit()
        elif action.lower() == "help":
            print_help()
        elif action:
            perform_action(self.player, self.world, action)
        else:
            print("Please enter a command. Type 'help' for available commands.")
        
        # Check game over conditions
        self.check_game_over()
        
        # Auto-save periodically
        auto_save_interval = get_setting('game', 'auto_save_interval', 10)
        if self.turn_counter % auto_save_interval == 0:
            save_game(self.player, self.world)
            print("💾 Auto-saved game progress.")
    
    def display_turn_info(self):
        """Display current game state information."""
        current_location = get_current_location(self.world)
        separator = get_setting('display', 'status_separator', '=' * 50)
        show_turn_counter = get_setting('debug', 'show_turn_counter', True)
        
        print(f"\n{separator}")
        if show_turn_counter:
            print(f"Turn {self.turn_counter}")
        print(f"📍 Location: {current_location}")
        print(get_player_status(self.player))
        
        # Show weather occasionally
        weather_frequency = get_setting('display', 'show_weather_frequency', 5)
        if self.turn_counter % weather_frequency == 0:
            from game.weather import describe_weather
            print(f"🌤️  {describe_weather(self.world)}")
    
    def apply_periodic_effects(self):
        """Apply effects that happen over time."""
        # Weather changes occasionally
        weather_change_freq = get_setting('weather', 'weather_change_frequency', 10)
        if self.turn_counter % weather_change_freq == 0 and random.random() < 0.3:
            change_weather(self.world)
            from game.weather import describe_weather
            print(f"\n🌦️  The weather changes: {describe_weather(self.world)}")
        
        # Apply weather effects to player
        weather_effect_freq = get_setting('weather', 'weather_effect_frequency', 3)
        if self.turn_counter % weather_effect_freq == 0:
            apply_weather_effects(self.player, self.world)
        
        # Random events occasionally
        event_freq = get_setting('events', 'random_event_frequency', 8)
        event_prob = get_setting('events', 'random_event_probability', 0.2)
        if self.turn_counter % event_freq == 0 and random.random() < event_prob:
            from utils.random_events import generate_random_event
            print("\n✨ Something unexpected happens...")
            generate_random_event(self.world, self.player)
        
        # Natural healing over time (very slow)
        healing_freq = get_setting('healing', 'natural_healing_frequency', 15)
        if self.turn_counter % healing_freq == 0:
            current_health = self.player.get('health', 100)
            max_health = get_setting('game', 'max_health', 100)
            if current_health < max_health:
                heal_range = get_setting('healing', 'natural_healing_amount', (1, 3))
                heal_amount = random.randint(heal_range[0], heal_range[1])
                self.player['health'] = min(max_health, current_health + heal_amount)
                if heal_amount > 0:
                    print(f"🩹 You feel slightly better. (+{heal_amount} health)")
    
    def check_game_over(self):
        """Check if the game should end."""
        if self.player.get('health', 100) <= 0:
            print("\n💀 GAME OVER")
            print("Your adventure has come to an end...")
            print(f"You survived {self.turn_counter} turns.")
            
            restart = input("Would you like to start a new game? (y/n): ").lower()
            if restart == 'y':
                self.start_new_game()
            else:
                self.game_running = False
    
    def save_and_quit(self):
        """Save the game and exit."""
        if self.player and self.world:
            save_game(self.player, self.world)
            print("💾 Game saved successfully!")
        
        print("👋 Thanks for playing Kevin's Adventure Game!")
        print(f"You played for {self.turn_counter} turns.")
        self.game_running = False
    
    def get_game_stats(self):
        """Get current game statistics."""
        if not self.player or not self.world:
            return "No active game."
        
        stats = {
            'player_name': self.player.get('name', 'Unknown'),
            'health': self.player.get('health', 0),
            'gold': self.player.get('gold', 0),
            'inventory_count': len(self.player.get('inventory', [])),
            'current_location': get_current_location(self.world),
            'turns_played': self.turn_counter
        }
        
        return stats
    
    def debug_info(self):
        """Display debug information for development."""
        debug_mode = get_setting('debug', 'debug_mode', False)
        if not debug_mode:
            print("Debug mode is disabled. Enable it in game/config.py")
            return
            
        print("\n🔧 DEBUG INFO:")
        print(f"Game Running: {self.game_running}")
        print(f"Turn Counter: {self.turn_counter}")
        print(f"Player: {self.player}")
        print(f"World State: {self.world}")


def create_game_controller():
    """Factory function to create a new game controller."""
    return GameController()
