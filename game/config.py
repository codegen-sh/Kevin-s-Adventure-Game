"""
Game Configuration Module
Centralized configuration settings for Kevin's Adventure Game.
"""

# Game Settings
GAME_SETTINGS = {
    'default_player_name': 'Kevin',
    'default_player_health': 100,
    'default_player_gold': 100,
    'max_health': 100,
    'save_directory': 'saves',
    'auto_save_interval': 10,  # turns
}

# Weather Settings
WEATHER_SETTINGS = {
    'weather_change_frequency': 10,  # turns
    'weather_effect_frequency': 3,   # turns
    'weather_conditions': [
        'clear', 'cloudy', 'rainy', 
        'stormy', 'foggy', 'windy'
    ],
    'default_weather': 'clear'
}

# Random Event Settings
EVENT_SETTINGS = {
    'random_event_frequency': 8,     # turns
    'random_event_probability': 0.2, # 20% chance
    'location_event_probability': 0.3, # 30% chance when entering location
}

# Healing Settings
HEALING_SETTINGS = {
    'natural_healing_frequency': 15,  # turns
    'natural_healing_amount': (1, 3), # min, max
    'village_rest_healing': (20, 40), # min, max
    'wilderness_rest_healing': (5, 15), # min, max
}

# Item Settings
ITEM_SETTINGS = {
    'max_inventory_size': 20,
    'search_success_probability': 0.3, # 30% chance to find hidden items
}

# Display Settings
DISPLAY_SETTINGS = {
    'show_weather_frequency': 5,     # turns
    'status_separator': '=' * 50,
    'use_emojis': True,
    'colored_output': False,  # Could be extended for terminal colors
}

# Debug Settings
DEBUG_SETTINGS = {
    'debug_mode': False,
    'verbose_logging': False,
    'show_turn_counter': True,
}


def get_setting(category, key, default=None):
    """
    Get a configuration setting with fallback to default.
    
    Args:
        category (str): Setting category (e.g., 'GAME_SETTINGS')
        key (str): Setting key
        default: Default value if setting not found
    
    Returns:
        The setting value or default
    """
    settings_map = {
        'game': GAME_SETTINGS,
        'weather': WEATHER_SETTINGS,
        'events': EVENT_SETTINGS,
        'healing': HEALING_SETTINGS,
        'items': ITEM_SETTINGS,
        'display': DISPLAY_SETTINGS,
        'debug': DEBUG_SETTINGS,
    }
    
    category_settings = settings_map.get(category.lower(), {})
    return category_settings.get(key, default)


def update_setting(category, key, value):
    """
    Update a configuration setting.
    
    Args:
        category (str): Setting category
        key (str): Setting key
        value: New value
    """
    settings_map = {
        'game': GAME_SETTINGS,
        'weather': WEATHER_SETTINGS,
        'events': EVENT_SETTINGS,
        'healing': HEALING_SETTINGS,
        'items': ITEM_SETTINGS,
        'display': DISPLAY_SETTINGS,
        'debug': DEBUG_SETTINGS,
    }
    
    category_settings = settings_map.get(category.lower())
    if category_settings is not None:
        category_settings[key] = value
        return True
    return False


def get_all_settings():
    """
    Get all configuration settings.
    
    Returns:
        dict: All settings organized by category
    """
    return {
        'game': GAME_SETTINGS,
        'weather': WEATHER_SETTINGS,
        'events': EVENT_SETTINGS,
        'healing': HEALING_SETTINGS,
        'items': ITEM_SETTINGS,
        'display': DISPLAY_SETTINGS,
        'debug': DEBUG_SETTINGS,
    }


def reset_to_defaults():
    """
    Reset all settings to their default values.
    """
    global GAME_SETTINGS, WEATHER_SETTINGS, EVENT_SETTINGS
    global HEALING_SETTINGS, ITEM_SETTINGS, DISPLAY_SETTINGS, DEBUG_SETTINGS
    
    # Reset to original values
    GAME_SETTINGS.update({
        'default_player_name': 'Kevin',
        'default_player_health': 100,
        'default_player_gold': 100,
        'max_health': 100,
        'save_directory': 'saves',
        'auto_save_interval': 10,
    })
    
    WEATHER_SETTINGS.update({
        'weather_change_frequency': 10,
        'weather_effect_frequency': 3,
        'weather_conditions': ['clear', 'cloudy', 'rainy', 'stormy', 'foggy', 'windy'],
        'default_weather': 'clear'
    })
    
    EVENT_SETTINGS.update({
        'random_event_frequency': 8,
        'random_event_probability': 0.2,
        'location_event_probability': 0.3,
    })
    
    HEALING_SETTINGS.update({
        'natural_healing_frequency': 15,
        'natural_healing_amount': (1, 3),
        'village_rest_healing': (20, 40),
        'wilderness_rest_healing': (5, 15),
    })
    
    ITEM_SETTINGS.update({
        'max_inventory_size': 20,
        'search_success_probability': 0.3,
    })
    
    DISPLAY_SETTINGS.update({
        'show_weather_frequency': 5,
        'status_separator': '=' * 50,
        'use_emojis': True,
        'colored_output': False,
    })
    
    DEBUG_SETTINGS.update({
        'debug_mode': False,
        'verbose_logging': False,
        'show_turn_counter': True,
    })

