"""
Configuration management system for Kevin's Adventure Game.

This module provides centralized configuration management with support for:
- Environment-specific configurations
- JSON schema validation
- Configuration caching and hot reloading
- Easy modding support

Usage:
    from config import config
    
    # Load game settings
    game_settings = config.get_game_settings()
    
    # Load item data
    item_data = config.get_item_data("sword")
    
    # Load location data
    location_data = config.get_location_data("Village")
"""

from .config_manager import ConfigManager

# Create a global configuration manager instance
config = ConfigManager()

__all__ = ['config', 'ConfigManager']

