"""
Plugin manager for coordinating all plugin operations.

This module provides a high-level interface for managing the entire plugin system,
including loading, registration, and integration with the game.
"""

import logging
from typing import Dict, Any, List, Optional
import json
import os

from .loader import PluginLoader
from .registry import LocationRegistry, ActionRegistry, GameMechanicRegistry
from .base import BasePlugin

logger = logging.getLogger(__name__)


class PluginManager:
    """
    High-level plugin manager that coordinates all plugin operations.
    
    This class provides a unified interface for the plugin system and handles
    integration with the main game loop.
    """
    
    def __init__(self, plugin_dirs: List[str] = None, config_file: str = None):
        self.config_file = config_file or 'plugins/config.json'
        self.loader = PluginLoader(plugin_dirs)
        self.config = self._load_config()
        
        # Quick access to registries
        self.locations = self.loader.location_registry
        self.actions = self.loader.action_registry
        self.mechanics = self.loader.mechanic_registry
        
        self._initialized = False
    
    def initialize(self) -> Dict[str, Any]:
        """
        Initialize the plugin system.
        
        Returns:
            Dict with initialization results and statistics.
        """
        if self._initialized:
            logger.warning("Plugin manager already initialized")
            return {'status': 'already_initialized'}
        
        logger.info("Initializing plugin system...")
        
        # Load and register all plugins
        results = self.loader.load_and_register_all()
        
        # Apply configuration
        self._apply_config()
        
        # Enable hot-reload if configured
        if self.config.get('hot_reload', False):
            self.loader.enable_hot_reload()
        
        self._initialized = True
        
        logger.info(f"Plugin system initialized: {results['registered_plugins']} plugins registered")
        return results
    
    def shutdown(self) -> None:
        """Shutdown the plugin system and clean up resources."""
        if not self._initialized:
            return
        
        logger.info("Shutting down plugin system...")
        
        self.loader.cleanup()
        self._initialized = False
        
        logger.info("Plugin system shutdown complete")
    
    def integrate_with_world(self, world: Dict[str, Any]) -> None:
        """
        Integrate plugin locations with the game world.
        
        Args:
            world: The game world dictionary to modify.
        """
        if not self._initialized:
            logger.warning("Plugin manager not initialized")
            return
        
        # Add plugin locations to the world
        plugin_locations = self.locations.get_location_data()
        
        if 'locations' not in world:
            world['locations'] = {}
        
        for location_name, location_data in plugin_locations.items():
            if location_name not in world['locations']:
                world['locations'][location_name] = location_data
                logger.info(f"Added plugin location: {location_name}")
            else:
                logger.warning(f"Location {location_name} already exists in world")
    
    def handle_action(self, command: str, player: Dict[str, Any], 
                     world: Dict[str, Any]) -> bool:
        """
        Handle a player action using the plugin system.
        
        Args:
            command: The command entered by the player
            player: Player state dictionary
            world: Game world dictionary
            
        Returns:
            bool: True if action was handled by a plugin, False otherwise.
        """
        if not self._initialized:
            return False
        
        # Parse command and arguments
        parts = command.strip().split()
        if not parts:
            return False
        
        main_command = parts[0].lower()
        args = parts[1:] if len(parts) > 1 else []
        
        # Try to execute the action
        return self.actions.execute_action(main_command, args, player, world)
    
    def handle_location_entry(self, location_name: str, player: Dict[str, Any], 
                            world: Dict[str, Any]) -> bool:
        """
        Handle player entering a location using the plugin system.
        
        Args:
            location_name: Name of the location being entered
            player: Player state dictionary
            world: Game world dictionary
            
        Returns:
            bool: True if location was handled by a plugin, False otherwise.
        """
        if not self._initialized:
            return False
        
        return self.locations.handle_location_entry(location_name, world, player)
    
    def trigger_game_events(self, event_type: str, player: Dict[str, Any], 
                          world: Dict[str, Any]) -> Any:
        """
        Trigger game events for all relevant mechanics.
        
        Args:
            event_type: Type of event ('start', 'load', 'save', 'turn_start', 'turn_end')
            player: Player state dictionary
            world: Game world dictionary
            
        Returns:
            Any: Event-specific return value (e.g., save data for 'save' event).
        """
        if not self._initialized:
            return None
        
        if event_type == 'start':
            self.mechanics.trigger_game_start(player, world)
        elif event_type == 'load':
            self.mechanics.trigger_game_load(player, world)
        elif event_type == 'save':
            return self.mechanics.trigger_game_save(player, world)
        elif event_type == 'turn_start':
            self.mechanics.trigger_turn_start(player, world)
        elif event_type == 'turn_end':
            self.mechanics.trigger_turn_end(player, world)
        else:
            logger.warning(f"Unknown event type: {event_type}")
    
    def get_help_text(self) -> str:
        """
        Get help text for all available plugin actions.
        
        Returns:
            str: Formatted help text.
        """
        if not self._initialized:
            return "Plugin system not initialized."
        
        help_texts = self.actions.get_help_text()
        
        if not help_texts:
            return "No plugin actions available."
        
        lines = ["Available plugin actions:"]
        for action_name, help_text in help_texts.items():
            lines.append(f"  {help_text}")
        
        return "\\n".join(lines)
    
    def get_status(self) -> Dict[str, Any]:
        """
        Get current status of the plugin system.
        
        Returns:
            Dict with plugin system status information.
        """
        status = {
            'initialized': self._initialized,
            'hot_reload_enabled': self.loader._hot_reload_enabled,
            'plugin_counts': {
                'locations': len(self.locations.list_enabled()),
                'actions': len(self.actions.list_enabled()),
                'mechanics': len(self.mechanics.list_enabled())
            },
            'enabled_plugins': {
                'locations': self.locations.list_enabled(),
                'actions': self.actions.list_enabled(),
                'mechanics': self.mechanics.list_enabled()
            }
        }
        
        return status
    
    def enable_plugin(self, plugin_name: str) -> bool:
        """
        Enable a specific plugin.
        
        Args:
            plugin_name: Name of the plugin to enable
            
        Returns:
            bool: True if plugin was enabled successfully, False otherwise.
        """
        success = (self.locations.enable_plugin(plugin_name) or
                  self.actions.enable_plugin(plugin_name) or
                  self.mechanics.enable_plugin(plugin_name))
        
        if success:
            self._save_config()
        
        return success
    
    def disable_plugin(self, plugin_name: str) -> bool:
        """
        Disable a specific plugin.
        
        Args:
            plugin_name: Name of the plugin to disable
            
        Returns:
            bool: True if plugin was disabled successfully, False otherwise.
        """
        success = (self.locations.disable_plugin(plugin_name) or
                  self.actions.disable_plugin(plugin_name) or
                  self.mechanics.disable_plugin(plugin_name))
        
        if success:
            self._save_config()
        
        return success
    
    def create_plugin(self, plugin_name: str, plugin_type: str, 
                     output_dir: str = None) -> str:
        """
        Create a new plugin template.
        
        Args:
            plugin_name: Name of the plugin
            plugin_type: Type of plugin ('location', 'action', 'mechanic')
            output_dir: Directory to create the plugin in
            
        Returns:
            str: Path to the created plugin file.
        """
        return self.loader.create_plugin_template(plugin_name, plugin_type, output_dir)
    
    def reload_plugin(self, file_path: str) -> bool:
        """
        Reload a specific plugin file.
        
        Args:
            file_path: Path to the plugin file to reload
            
        Returns:
            bool: True if reload was successful, False otherwise.
        """
        return self.loader.reload_plugin_file(file_path)
    
    def _load_config(self) -> Dict[str, Any]:
        """Load plugin configuration from file."""
        default_config = {
            'hot_reload': False,
            'enabled_plugins': [],
            'disabled_plugins': [],
            'plugin_settings': {}
        }
        
        if not os.path.exists(self.config_file):
            return default_config
        
        try:
            with open(self.config_file, 'r') as f:
                config = json.load(f)
                # Merge with defaults
                for key, value in default_config.items():
                    if key not in config:
                        config[key] = value
                return config
        except Exception as e:
            logger.error(f"Error loading plugin config: {e}")
            return default_config
    
    def _save_config(self) -> None:
        """Save plugin configuration to file."""
        try:
            # Update config with current state
            self.config['enabled_plugins'] = (
                self.locations.list_enabled() +
                self.actions.list_enabled() +
                self.mechanics.list_enabled()
            )
            
            os.makedirs(os.path.dirname(self.config_file), exist_ok=True)
            
            with open(self.config_file, 'w') as f:
                json.dump(self.config, f, indent=2)
        except Exception as e:
            logger.error(f"Error saving plugin config: {e}")
    
    def _apply_config(self) -> None:
        """Apply configuration settings to plugins."""
        # Disable plugins that are in the disabled list
        for plugin_name in self.config.get('disabled_plugins', []):
            self.disable_plugin(plugin_name)
        
        # Apply plugin-specific settings
        plugin_settings = self.config.get('plugin_settings', {})
        for plugin_name, settings in plugin_settings.items():
            plugin = (self.locations.get(plugin_name) or
                     self.actions.get(plugin_name) or
                     self.mechanics.get(plugin_name))
            
            if plugin and hasattr(plugin, 'apply_settings'):
                try:
                    plugin.apply_settings(settings)
                except Exception as e:
                    logger.error(f"Error applying settings to {plugin_name}: {e}")


# Global plugin manager instance
_plugin_manager: Optional[PluginManager] = None


def get_plugin_manager() -> PluginManager:
    """Get the global plugin manager instance."""
    global _plugin_manager
    if _plugin_manager is None:
        _plugin_manager = PluginManager()
    return _plugin_manager


def initialize_plugins(plugin_dirs: List[str] = None) -> Dict[str, Any]:
    """
    Initialize the global plugin system.
    
    Args:
        plugin_dirs: List of directories to search for plugins
        
    Returns:
        Dict with initialization results.
    """
    manager = get_plugin_manager()
    if plugin_dirs:
        manager.loader.plugin_dirs = plugin_dirs
    return manager.initialize()


def shutdown_plugins() -> None:
    """Shutdown the global plugin system."""
    global _plugin_manager
    if _plugin_manager:
        _plugin_manager.shutdown()
        _plugin_manager = None

