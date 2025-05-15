"""
Configuration module for the game.
"""
import json
import os


# Default configuration
DEFAULT_CONFIG = {
    "default_player_name": "Kevin",
    "max_health": 100,
    "starting_gold": 100,
    "starting_location": "Village",
    "save_directory": "saves",
    "random_event_chance": 0.2,
    "debug_mode": False
}


class Config:
    """Class for managing game configuration."""
    
    def __init__(self, config_file="config.json"):
        """Initialize the configuration."""
        self.config_file = config_file
        self.config = DEFAULT_CONFIG.copy()
        self.load()
    
    def load(self):
        """Load configuration from file."""
        if os.path.exists(self.config_file):
            try:
                with open(self.config_file, 'r') as f:
                    loaded_config = json.load(f)
                    self.config.update(loaded_config)
                print(f"Configuration loaded from {self.config_file}")
            except json.JSONDecodeError:
                print(f"Error loading configuration from {self.config_file}. Using defaults.")
        else:
            print(f"Configuration file {self.config_file} not found. Using defaults.")
    
    def save(self):
        """Save configuration to file."""
        try:
            with open(self.config_file, 'w') as f:
                json.dump(self.config, f, indent=2)
            print(f"Configuration saved to {self.config_file}")
        except IOError as e:
            print(f"Error saving configuration: {e}")
    
    def get(self, key, default=None):
        """Get a configuration value."""
        return self.config.get(key, default)
    
    def set(self, key, value):
        """Set a configuration value."""
        self.config[key] = value
    
    def reset(self):
        """Reset configuration to defaults."""
        self.config = DEFAULT_CONFIG.copy()
        print("Configuration reset to defaults.")


# Global configuration instance
config = Config()

