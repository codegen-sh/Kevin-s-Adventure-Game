"""
Configuration module for Kevin's Adventure Game.
This module handles loading and accessing game configuration.
"""
import json
import logging
import os
from pathlib import Path

# Set up logger
logger = logging.getLogger(__name__)

# Default configuration
DEFAULT_CONFIG = {
    "player": {
        "default_name": "Kevin",
        "starting_health": 100,
        "starting_gold": 100,
        "starting_location": "Village",
        "starting_inventory": [],
    },
    "game": {
        "save_directory": "saves",
        "random_event_chance": 0.3,
        "max_inventory_size": 10,
    },
    "display": {
        "text_width": 80,
        "show_health_bar": True,
        "show_gold": True,
    },
}

# Configuration singleton
_config = None


def get_config_dir():
    """Get the configuration directory."""
    # Use platform-appropriate config directory
    if os.name == "nt":  # Windows
        config_dir = Path(os.environ.get("APPDATA", "")) / "KevinAdventureGame"
    else:  # Unix/Linux/Mac
        config_dir = Path.home() / ".config" / "kevin_adventure_game"
    
    # Create directory if it doesn't exist
    config_dir.mkdir(parents=True, exist_ok=True)
    return config_dir


def get_config_file():
    """Get the configuration file path."""
    return get_config_dir() / "config.json"


def load_config():
    """Load configuration from file or create default."""
    global _config
    
    if _config is not None:
        return _config
    
    config_file = get_config_file()
    
    # If config file exists, load it
    if config_file.exists():
        try:
            with open(config_file, "r") as f:
                loaded_config = json.load(f)
            logger.info(f"Loaded configuration from {config_file}")
            
            # Merge with default config to ensure all keys exist
            merged_config = DEFAULT_CONFIG.copy()
            for section, values in loaded_config.items():
                if section in merged_config:
                    merged_config[section].update(values)
                else:
                    merged_config[section] = values
            
            _config = merged_config
        except Exception as e:
            logger.error(f"Error loading config: {e}")
            logger.info("Using default configuration")
            _config = DEFAULT_CONFIG
    else:
        # Create default config file
        try:
            with open(config_file, "w") as f:
                json.dump(DEFAULT_CONFIG, f, indent=4)
            logger.info(f"Created default configuration at {config_file}")
            _config = DEFAULT_CONFIG
        except Exception as e:
            logger.error(f"Error creating config file: {e}")
            _config = DEFAULT_CONFIG
    
    return _config


def save_config(config=None):
    """Save configuration to file."""
    if config is None:
        config = _config if _config is not None else DEFAULT_CONFIG
    
    config_file = get_config_file()
    
    try:
        with open(config_file, "w") as f:
            json.dump(config, f, indent=4)
        logger.info(f"Saved configuration to {config_file}")
        return True
    except Exception as e:
        logger.error(f"Error saving config: {e}")
        return False


def get_config_value(section, key, default=None):
    """Get a specific configuration value."""
    config = load_config()
    
    try:
        return config[section][key]
    except KeyError:
        if default is not None:
            return default
        # If no default provided, try to get from DEFAULT_CONFIG
        try:
            return DEFAULT_CONFIG[section][key]
        except KeyError:
            logger.warning(f"Config value {section}.{key} not found")
            return None


def set_config_value(section, key, value):
    """Set a specific configuration value."""
    config = load_config()
    
    # Create section if it doesn't exist
    if section not in config:
        config[section] = {}
    
    # Set value
    config[section][key] = value
    
    # Save config
    return save_config(config)

