"""
Plugin registry system for managing and organizing plugins.

This module provides registries for different types of plugins and handles
plugin discovery, registration, and retrieval.
"""

from typing import Dict, List, Type, Optional, Any
import logging
from .base import BasePlugin, BaseLocation, BaseAction, BaseGameMechanic

logger = logging.getLogger(__name__)


class PluginRegistry:
    """
    Base registry for managing plugins.
    
    Provides common functionality for plugin registration and retrieval.
    """
    
    def __init__(self):
        self._plugins: Dict[str, BasePlugin] = {}
        self._enabled_plugins: Dict[str, BasePlugin] = {}
    
    def register(self, plugin: BasePlugin) -> bool:
        """
        Register a plugin.
        
        Args:
            plugin: The plugin instance to register
            
        Returns:
            bool: True if registration was successful, False otherwise.
        """
        if not isinstance(plugin, BasePlugin):
            logger.error(f"Plugin must inherit from BasePlugin: {type(plugin)}")
            return False
        
        # Validate plugin
        errors = plugin.validate()
        if errors:
            logger.error(f"Plugin validation failed for {plugin.metadata.name}: {errors}")
            return False
        
        name = plugin.metadata.name
        
        if name in self._plugins:
            logger.warning(f"Plugin {name} is already registered, replacing...")
        
        self._plugins[name] = plugin
        
        if plugin.enabled:
            self._enabled_plugins[name] = plugin
        
        logger.info(f"Registered plugin: {name} v{plugin.metadata.version}")
        return True
    
    def unregister(self, name: str) -> bool:
        """
        Unregister a plugin.
        
        Args:
            name: Name of the plugin to unregister
            
        Returns:
            bool: True if unregistration was successful, False otherwise.
        """
        if name not in self._plugins:
            logger.warning(f"Plugin {name} is not registered")
            return False
        
        plugin = self._plugins[name]
        plugin.cleanup()
        
        del self._plugins[name]
        if name in self._enabled_plugins:
            del self._enabled_plugins[name]
        
        logger.info(f"Unregistered plugin: {name}")
        return True
    
    def get(self, name: str) -> Optional[BasePlugin]:
        """Get a plugin by name."""
        return self._plugins.get(name)
    
    def get_enabled(self, name: str) -> Optional[BasePlugin]:
        """Get an enabled plugin by name."""
        return self._enabled_plugins.get(name)
    
    def list_all(self) -> List[str]:
        """List all registered plugin names."""
        return list(self._plugins.keys())
    
    def list_enabled(self) -> List[str]:
        """List all enabled plugin names."""
        return list(self._enabled_plugins.keys())
    
    def enable_plugin(self, name: str) -> bool:
        """Enable a plugin."""
        if name not in self._plugins:
            logger.error(f"Plugin {name} is not registered")
            return False
        
        plugin = self._plugins[name]
        plugin.enable()
        self._enabled_plugins[name] = plugin
        return True
    
    def disable_plugin(self, name: str) -> bool:
        """Disable a plugin."""
        if name not in self._plugins:
            logger.error(f"Plugin {name} is not registered")
            return False
        
        plugin = self._plugins[name]
        plugin.disable()
        if name in self._enabled_plugins:
            del self._enabled_plugins[name]
        return True
    
    def initialize_all(self) -> Dict[str, bool]:
        """
        Initialize all enabled plugins.
        
        Returns:
            Dict[str, bool]: Results of initialization for each plugin.
        """
        results = {}
        for name, plugin in self._enabled_plugins.items():
            try:
                success = plugin.initialize()
                results[name] = success
                if success:
                    plugin._initialized = True
                    logger.info(f"Initialized plugin: {name}")
                else:
                    logger.error(f"Failed to initialize plugin: {name}")
            except Exception as e:
                logger.error(f"Error initializing plugin {name}: {e}")
                results[name] = False
        
        return results
    
    def cleanup_all(self) -> None:
        """Clean up all plugins."""
        for plugin in self._plugins.values():
            try:
                plugin.cleanup()
            except Exception as e:
                logger.error(f"Error cleaning up plugin {plugin.metadata.name}: {e}")


class LocationRegistry(PluginRegistry):
    """Registry specifically for location plugins."""
    
    def register(self, plugin: BaseLocation) -> bool:
        """Register a location plugin."""
        if not isinstance(plugin, BaseLocation):
            logger.error(f"Plugin must inherit from BaseLocation: {type(plugin)}")
            return False
        
        return super().register(plugin)
    
    def get_location_data(self) -> Dict[str, Dict[str, Any]]:
        """
        Get location data for all enabled location plugins.
        
        Returns:
            Dict mapping location names to their data structures.
        """
        location_data = {}
        for name, plugin in self._enabled_plugins.items():
            try:
                location_data[name] = plugin.get_location_data()
            except Exception as e:
                logger.error(f"Error getting location data for {name}: {e}")
        
        return location_data
    
    def handle_location_entry(self, location_name: str, world: Dict[str, Any], 
                            player: Dict[str, Any]) -> bool:
        """
        Handle player entering a location.
        
        Args:
            location_name: Name of the location being entered
            world: Game world state
            player: Player state
            
        Returns:
            bool: True if location was handled by a plugin, False otherwise.
        """
        plugin = self.get_enabled(location_name)
        if plugin:
            try:
                plugin.enter_location(world, player)
                return True
            except Exception as e:
                logger.error(f"Error handling location entry for {location_name}: {e}")
        
        return False


class ActionRegistry(PluginRegistry):
    """Registry specifically for action plugins."""
    
    def __init__(self):
        super().__init__()
        self._trigger_map: Dict[str, str] = {}  # trigger -> plugin_name
    
    def register(self, plugin: BaseAction) -> bool:
        """Register an action plugin."""
        if not isinstance(plugin, BaseAction):
            logger.error(f"Plugin must inherit from BaseAction: {type(plugin)}")
            return False
        
        if not super().register(plugin):
            return False
        
        # Register triggers
        try:
            triggers = plugin.get_triggers()
            for trigger in triggers:
                trigger_lower = trigger.lower()
                if trigger_lower in self._trigger_map:
                    logger.warning(f"Trigger '{trigger}' already registered, overriding...")
                self._trigger_map[trigger_lower] = plugin.metadata.name
        except Exception as e:
            logger.error(f"Error registering triggers for {plugin.metadata.name}: {e}")
            return False
        
        return True
    
    def unregister(self, name: str) -> bool:
        """Unregister an action plugin."""
        if name not in self._plugins:
            return False
        
        # Remove triggers
        plugin = self._plugins[name]
        try:
            triggers = plugin.get_triggers()
            for trigger in triggers:
                trigger_lower = trigger.lower()
                if trigger_lower in self._trigger_map:
                    del self._trigger_map[trigger_lower]
        except Exception as e:
            logger.error(f"Error removing triggers for {name}: {e}")
        
        return super().unregister(name)
    
    def find_action(self, command: str) -> Optional[BaseAction]:
        """
        Find an action plugin that handles the given command.
        
        Args:
            command: The command to find an action for
            
        Returns:
            BaseAction plugin that handles the command, or None.
        """
        command_lower = command.lower()
        plugin_name = self._trigger_map.get(command_lower)
        
        if plugin_name:
            return self.get_enabled(plugin_name)
        
        return None
    
    def execute_action(self, command: str, args: List[str], 
                      player: Dict[str, Any], world: Dict[str, Any]) -> bool:
        """
        Execute an action based on the command.
        
        Args:
            command: The command to execute
            args: Additional command arguments
            player: Player state
            world: Game world state
            
        Returns:
            bool: True if action was handled, False otherwise.
        """
        action = self.find_action(command)
        if not action:
            return False
        
        try:
            if not action.can_execute(player, world):
                return False
            
            return action.execute(player, world, command, args)
        except Exception as e:
            logger.error(f"Error executing action {command}: {e}")
            return False
    
    def get_help_text(self) -> Dict[str, str]:
        """
        Get help text for all enabled actions.
        
        Returns:
            Dict mapping action names to their help text.
        """
        help_text = {}
        for name, plugin in self._enabled_plugins.items():
            try:
                help_text[name] = plugin.get_help_text()
            except Exception as e:
                logger.error(f"Error getting help text for {name}: {e}")
        
        return help_text
    
    def list_triggers(self) -> Dict[str, str]:
        """
        List all registered triggers and their associated plugins.
        
        Returns:
            Dict mapping triggers to plugin names.
        """
        return self._trigger_map.copy()


class GameMechanicRegistry(PluginRegistry):
    """Registry specifically for game mechanic plugins."""
    
    def register(self, plugin: BaseGameMechanic) -> bool:
        """Register a game mechanic plugin."""
        if not isinstance(plugin, BaseGameMechanic):
            logger.error(f"Plugin must inherit from BaseGameMechanic: {type(plugin)}")
            return False
        
        return super().register(plugin)
    
    def trigger_game_start(self, player: Dict[str, Any], world: Dict[str, Any]) -> None:
        """Trigger game start event for all enabled mechanics."""
        for plugin in self._enabled_plugins.values():
            try:
                plugin.on_game_start(player, world)
            except Exception as e:
                logger.error(f"Error in game start for {plugin.metadata.name}: {e}")
    
    def trigger_game_load(self, player: Dict[str, Any], world: Dict[str, Any]) -> None:
        """Trigger game load event for all enabled mechanics."""
        for plugin in self._enabled_plugins.values():
            try:
                plugin.on_game_load(player, world)
            except Exception as e:
                logger.error(f"Error in game load for {plugin.metadata.name}: {e}")
    
    def trigger_game_save(self, player: Dict[str, Any], world: Dict[str, Any]) -> Dict[str, Any]:
        """Trigger game save event for all enabled mechanics."""
        save_data = {}
        for name, plugin in self._enabled_plugins.items():
            try:
                plugin_data = plugin.on_game_save(player, world)
                if plugin_data:
                    save_data[name] = plugin_data
            except Exception as e:
                logger.error(f"Error in game save for {name}: {e}")
        
        return save_data
    
    def trigger_turn_start(self, player: Dict[str, Any], world: Dict[str, Any]) -> None:
        """Trigger turn start event for all enabled mechanics."""
        for plugin in self._enabled_plugins.values():
            try:
                plugin.on_turn_start(player, world)
            except Exception as e:
                logger.error(f"Error in turn start for {plugin.metadata.name}: {e}")
    
    def trigger_turn_end(self, player: Dict[str, Any], world: Dict[str, Any]) -> None:
        """Trigger turn end event for all enabled mechanics."""
        for plugin in self._enabled_plugins.values():
            try:
                plugin.on_turn_end(player, world)
            except Exception as e:
                logger.error(f"Error in turn end for {plugin.metadata.name}: {e}")

