"""
Configuration package for Kevin's Adventure Game.
Provides centralized access to all game configuration data.
"""

import json
import os
from typing import Dict, Any

from .game_config import (
    GAME_SETTINGS,
    PLAYER_DEFAULTS,
    ITEM_EFFECTS,
    ITEM_PRICES,
    TRADING_VALUES,
    RANDOM_EVENT_WEIGHTS,
    ENCOUNTER_TYPES,
    TREASURE_TYPES,
    WEATHER_TYPES,
    TRAP_TYPES,
    DISCOVERY_TYPES,
    DISPLAY_SETTINGS,
    MESSAGES,
    HELP_TEXT
)


class ConfigManager:
    """Manages all game configuration data."""
    
    def __init__(self):
        self._items_config = None
        self._locations_config = None
        self._config_dir = os.path.dirname(__file__)
    
    @property
    def items(self) -> Dict[str, Any]:
        """Get items configuration data."""
        if self._items_config is None:
            self._items_config = self._load_json_config("items.json")
        return self._items_config
    
    @property
    def locations(self) -> Dict[str, Any]:
        """Get locations configuration data."""
        if self._locations_config is None:
            self._locations_config = self._load_json_config("locations.json")
        return self._locations_config
    
    def _load_json_config(self, filename: str) -> Dict[str, Any]:
        """Load a JSON configuration file."""
        filepath = os.path.join(self._config_dir, filename)
        try:
            with open(filepath, 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Warning: Could not load {filename}: {e}")
            return {}
    
    def get_item_description(self, item: str) -> str:
        """Get description for an item."""
        descriptions = self.items.get("item_descriptions", {})
        return descriptions.get(item, "A mysterious item.")
    
    def get_location_data(self, location: str) -> Dict[str, Any]:
        """Get data for a specific location."""
        locations = self.locations.get("locations", {})
        return locations.get(location, {})
    
    def get_message(self, key: str, **kwargs) -> str:
        """Get a formatted message."""
        message = MESSAGES.get(key, "")
        if kwargs:
            return message.format(**kwargs)
        return message
    
    def get_setting(self, key: str, default=None):
        """Get a game setting value."""
        return GAME_SETTINGS.get(key, default)


# Global configuration manager instance
config = ConfigManager()

# Export commonly used configurations
__all__ = [
    'config',
    'GAME_SETTINGS',
    'PLAYER_DEFAULTS', 
    'ITEM_EFFECTS',
    'ITEM_PRICES',
    'TRADING_VALUES',
    'RANDOM_EVENT_WEIGHTS',
    'ENCOUNTER_TYPES',
    'TREASURE_TYPES',
    'WEATHER_TYPES',
    'TRAP_TYPES',
    'DISCOVERY_TYPES',
    'DISPLAY_SETTINGS',
    'MESSAGES',
    'HELP_TEXT'
]

