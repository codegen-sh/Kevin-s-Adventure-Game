"""
Plugin loader for automatic discovery and loading of plugins.

This module handles the discovery, loading, and validation of plugins
from the filesystem and provides hot-reloading capabilities.
"""

import os
import sys
import importlib
import importlib.util
from pathlib import Path
from typing import List, Dict, Any, Optional, Type
import logging
import json
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from .base import BasePlugin, BaseLocation, BaseAction, BaseGameMechanic
from .registry import LocationRegistry, ActionRegistry, GameMechanicRegistry

logger = logging.getLogger(__name__)


class PluginFileHandler(FileSystemEventHandler):
    """File system event handler for hot-reloading plugins."""
    
    def __init__(self, loader: 'PluginLoader'):
        self.loader = loader
        self.last_reload = {}
    
    def on_modified(self, event):
        """Handle file modification events."""
        if event.is_directory:
            return
        
        if not event.src_path.endswith('.py'):
            return
        
        # Debounce rapid file changes
        now = time.time()
        if event.src_path in self.last_reload:
            if now - self.last_reload[event.src_path] < 1.0:  # 1 second debounce
                return
        
        self.last_reload[event.src_path] = now
        
        logger.info(f"Plugin file modified: {event.src_path}")
        self.loader.reload_plugin_file(event.src_path)


class PluginLoader:
    """
    Plugin loader with automatic discovery and hot-reloading capabilities.
    """
    
    def __init__(self, plugin_dirs: List[str] = None):
        self.plugin_dirs = plugin_dirs or ['plugins/examples', 'plugins/custom']
        self.location_registry = LocationRegistry()
        self.action_registry = ActionRegistry()
        self.mechanic_registry = GameMechanicRegistry()
        
        self._loaded_modules = {}
        self._file_to_plugins = {}  # file_path -> list of plugin names
        self._hot_reload_enabled = False
        self._observer = None
        
        # Ensure plugin directories exist
        for plugin_dir in self.plugin_dirs:
            os.makedirs(plugin_dir, exist_ok=True)
    
    def discover_plugins(self) -> List[str]:
        """
        Discover all plugin files in the plugin directories.
        
        Returns:
            List of plugin file paths.
        """
        plugin_files = []
        
        for plugin_dir in self.plugin_dirs:
            if not os.path.exists(plugin_dir):
                continue
            
            for root, dirs, files in os.walk(plugin_dir):
                for file in files:
                    if file.endswith('.py') and not file.startswith('__'):
                        plugin_files.append(os.path.join(root, file))
        
        return plugin_files
    
    def load_plugin_file(self, file_path: str) -> List[BasePlugin]:
        """
        Load plugins from a single file.
        
        Args:
            file_path: Path to the plugin file
            
        Returns:
            List of loaded plugin instances.
        """
        plugins = []
        
        try:
            # Convert file path to module name
            rel_path = os.path.relpath(file_path)
            module_name = rel_path.replace(os.sep, '.').replace('.py', '')
            
            # Load the module
            spec = importlib.util.spec_from_file_location(module_name, file_path)
            if spec is None or spec.loader is None:
                logger.error(f"Could not load spec for {file_path}")
                return plugins
            
            module = importlib.util.module_from_spec(spec)
            
            # Store reference to avoid garbage collection
            self._loaded_modules[module_name] = module
            
            # Execute the module
            spec.loader.exec_module(module)
            
            # Find plugin classes in the module
            for attr_name in dir(module):
                attr = getattr(module, attr_name)
                
                if (isinstance(attr, type) and 
                    issubclass(attr, BasePlugin) and 
                    attr != BasePlugin and
                    attr not in [BaseLocation, BaseAction, BaseGameMechanic]):
                    
                    try:
                        # Instantiate the plugin
                        plugin_instance = attr()
                        plugins.append(plugin_instance)
                        logger.info(f"Loaded plugin: {plugin_instance.metadata.name}")
                    except Exception as e:
                        logger.error(f"Error instantiating plugin {attr_name}: {e}")
            
            # Track which plugins came from this file
            if plugins:
                plugin_names = [p.metadata.name for p in plugins]
                self._file_to_plugins[file_path] = plugin_names
        
        except Exception as e:
            logger.error(f"Error loading plugin file {file_path}: {e}")
        
        return plugins
    
    def load_all_plugins(self) -> Dict[str, List[BasePlugin]]:
        """
        Load all plugins from all plugin directories.
        
        Returns:
            Dict mapping file paths to lists of loaded plugins.
        """
        all_plugins = {}
        plugin_files = self.discover_plugins()
        
        for file_path in plugin_files:
            plugins = self.load_plugin_file(file_path)
            if plugins:
                all_plugins[file_path] = plugins
        
        return all_plugins
    
    def register_plugins(self, plugins: List[BasePlugin]) -> Dict[str, bool]:
        """
        Register plugins with appropriate registries.
        
        Args:
            plugins: List of plugin instances to register
            
        Returns:
            Dict mapping plugin names to registration success.
        """
        results = {}
        
        for plugin in plugins:
            name = plugin.metadata.name
            success = False
            
            if isinstance(plugin, BaseLocation):
                success = self.location_registry.register(plugin)
            elif isinstance(plugin, BaseAction):
                success = self.action_registry.register(plugin)
            elif isinstance(plugin, BaseGameMechanic):
                success = self.mechanic_registry.register(plugin)
            else:
                logger.warning(f"Unknown plugin type for {name}: {type(plugin)}")
            
            results[name] = success
        
        return results
    
    def load_and_register_all(self) -> Dict[str, Any]:
        """
        Load and register all plugins.
        
        Returns:
            Dict with loading and registration results.
        """
        results = {
            'loaded_files': 0,
            'loaded_plugins': 0,
            'registered_plugins': 0,
            'failed_plugins': [],
            'plugin_details': {}
        }
        
        all_plugins = self.load_all_plugins()
        results['loaded_files'] = len(all_plugins)
        
        for file_path, plugins in all_plugins.items():
            results['loaded_plugins'] += len(plugins)
            
            registration_results = self.register_plugins(plugins)
            
            for plugin_name, success in registration_results.items():
                if success:
                    results['registered_plugins'] += 1
                else:
                    results['failed_plugins'].append(plugin_name)
                
                results['plugin_details'][plugin_name] = {
                    'file': file_path,
                    'registered': success
                }
        
        # Initialize all registered plugins
        init_results = {}
        init_results.update(self.location_registry.initialize_all())
        init_results.update(self.action_registry.initialize_all())
        init_results.update(self.mechanic_registry.initialize_all())
        
        results['initialization_results'] = init_results
        
        return results
    
    def reload_plugin_file(self, file_path: str) -> bool:
        """
        Reload a specific plugin file (for hot-reloading).
        
        Args:
            file_path: Path to the plugin file to reload
            
        Returns:
            bool: True if reload was successful, False otherwise.
        """
        try:
            # Unregister existing plugins from this file
            if file_path in self._file_to_plugins:
                for plugin_name in self._file_to_plugins[file_path]:
                    self.location_registry.unregister(plugin_name)
                    self.action_registry.unregister(plugin_name)
                    self.mechanic_registry.unregister(plugin_name)
                
                del self._file_to_plugins[file_path]
            
            # Reload the module
            rel_path = os.path.relpath(file_path)
            module_name = rel_path.replace(os.sep, '.').replace('.py', '')
            
            if module_name in self._loaded_modules:
                importlib.reload(self._loaded_modules[module_name])
            
            # Load and register plugins from the file
            plugins = self.load_plugin_file(file_path)
            if plugins:
                self.register_plugins(plugins)
                
                # Initialize the new plugins
                for plugin in plugins:
                    if isinstance(plugin, BaseLocation):
                        plugin.initialize()
                    elif isinstance(plugin, BaseAction):
                        plugin.initialize()
                    elif isinstance(plugin, BaseGameMechanic):
                        plugin.initialize()
                
                logger.info(f"Successfully reloaded {len(plugins)} plugins from {file_path}")
                return True
            
        except Exception as e:
            logger.error(f"Error reloading plugin file {file_path}: {e}")
        
        return False
    
    def enable_hot_reload(self) -> bool:
        """
        Enable hot-reloading of plugins.
        
        Returns:
            bool: True if hot-reload was enabled successfully, False otherwise.
        """
        if self._hot_reload_enabled:
            return True
        
        try:
            self._observer = Observer()
            handler = PluginFileHandler(self)
            
            for plugin_dir in self.plugin_dirs:
                if os.path.exists(plugin_dir):
                    self._observer.schedule(handler, plugin_dir, recursive=True)
            
            self._observer.start()
            self._hot_reload_enabled = True
            logger.info("Hot-reload enabled for plugins")
            return True
        
        except Exception as e:
            logger.error(f"Error enabling hot-reload: {e}")
            return False
    
    def disable_hot_reload(self) -> None:
        """Disable hot-reloading of plugins."""
        if self._observer:
            self._observer.stop()
            self._observer.join()
            self._observer = None
        
        self._hot_reload_enabled = False
        logger.info("Hot-reload disabled for plugins")
    
    def create_plugin_template(self, plugin_name: str, plugin_type: str, 
                             output_dir: str = None) -> str:
        """
        Create a template plugin file.
        
        Args:
            plugin_name: Name of the plugin
            plugin_type: Type of plugin ('location', 'action', 'mechanic')
            output_dir: Directory to create the plugin in
            
        Returns:
            str: Path to the created template file.
        """
        if output_dir is None:
            output_dir = self.plugin_dirs[0] if self.plugin_dirs else 'plugins/custom'
        
        os.makedirs(output_dir, exist_ok=True)
        
        file_name = f"{plugin_name.lower().replace(' ', '_')}.py"
        file_path = os.path.join(output_dir, file_name)
        
        if plugin_type == 'location':
            template = self._get_location_template(plugin_name)
        elif plugin_type == 'action':
            template = self._get_action_template(plugin_name)
        elif plugin_type == 'mechanic':
            template = self._get_mechanic_template(plugin_name)
        else:
            raise ValueError(f"Unknown plugin type: {plugin_type}")
        
        with open(file_path, 'w') as f:
            f.write(template)
        
        logger.info(f"Created plugin template: {file_path}")
        return file_path
    
    def _get_location_template(self, plugin_name: str) -> str:
        """Get template for a location plugin."""
        class_name = ''.join(word.capitalize() for word in plugin_name.split())
        return f'''"""
{plugin_name} location plugin for Kevin's Adventure Game.
"""

from plugins.base import BaseLocation, PluginMetadata
from typing import Dict, Any, List


class {class_name}(BaseLocation):
    """A {plugin_name.lower()} location plugin."""
    
    @property
    def metadata(self) -> PluginMetadata:
        return PluginMetadata(
            name="{plugin_name}",
            version="1.0.0",
            description="A {plugin_name.lower()} location for the adventure game",
            author="Plugin Developer"
        )
    
    def initialize(self) -> bool:
        """Initialize the location plugin."""
        return True
    
    def cleanup(self) -> None:
        """Clean up location resources."""
        pass
    
    def get_description(self) -> str:
        """Return the location description."""
        return "A mysterious {plugin_name.lower()} with unknown secrets."
    
    def get_connections(self) -> List[str]:
        """Return list of connected location names."""
        return ["Village"]  # Modify as needed
    
    def get_items(self) -> List[str]:
        """Return list of items available in this location."""
        return []  # Add items as needed
    
    def enter_location(self, world: Dict[str, Any], player: Dict[str, Any]) -> None:
        """Handle player entering this location."""
        print(f"You enter the {{self.get_description()}}")
        
        while True:
            print("\\nWhat would you like to do?")
            print("1. Explore the area")
            print("2. Look around")
            print("3. Leave")
            
            choice = input("Enter your choice (1-3): ")
            
            if choice == "1":
                self._explore_area(world, player)
            elif choice == "2":
                self._look_around(world, player)
            elif choice == "3":
                print("You decide to leave the {plugin_name.lower()}.")
                break
            else:
                print("Invalid choice. Please try again.")
    
    def _explore_area(self, world: Dict[str, Any], player: Dict[str, Any]) -> None:
        """Explore the area."""
        print("You explore the {plugin_name.lower()} and discover...")
        # Add exploration logic here
    
    def _look_around(self, world: Dict[str, Any], player: Dict[str, Any]) -> None:
        """Look around the location."""
        print("Looking around, you see...")
        # Add observation logic here
'''
    
    def _get_action_template(self, plugin_name: str) -> str:
        """Get template for an action plugin."""
        class_name = ''.join(word.capitalize() for word in plugin_name.split())
        return f'''"""
{plugin_name} action plugin for Kevin's Adventure Game.
"""

from plugins.base import BaseAction, PluginMetadata
from typing import Dict, Any, List


class {class_name}Action(BaseAction):
    """A {plugin_name.lower()} action plugin."""
    
    @property
    def metadata(self) -> PluginMetadata:
        return PluginMetadata(
            name="{plugin_name}Action",
            version="1.0.0",
            description="A {plugin_name.lower()} action for the adventure game",
            author="Plugin Developer"
        )
    
    def initialize(self) -> bool:
        """Initialize the action plugin."""
        return True
    
    def cleanup(self) -> None:
        """Clean up action resources."""
        pass
    
    def get_triggers(self) -> List[str]:
        """Return list of command triggers for this action."""
        return ["{plugin_name.lower()}", "{plugin_name.lower()[:3]}"]  # Modify as needed
    
    def execute(self, player: Dict[str, Any], world: Dict[str, Any], 
                command: str, args: List[str]) -> bool:
        """Execute the action."""
        print(f"Executing {{command}} action...")
        
        # Add action logic here
        # Return True if action was handled, False otherwise
        return True
    
    def get_help_text(self) -> str:
        """Return help text for this action."""
        return "{plugin_name.lower()} - Perform a {plugin_name.lower()} action"
    
    def can_execute(self, player: Dict[str, Any], world: Dict[str, Any]) -> bool:
        """Check if this action can be executed."""
        # Add any conditions here
        return True
'''
    
    def _get_mechanic_template(self, plugin_name: str) -> str:
        """Get template for a game mechanic plugin."""
        class_name = ''.join(word.capitalize() for word in plugin_name.split())
        return f'''"""
{plugin_name} game mechanic plugin for Kevin's Adventure Game.
"""

from plugins.base import BaseGameMechanic, PluginMetadata
from typing import Dict, Any


class {class_name}Mechanic(BaseGameMechanic):
    """A {plugin_name.lower()} game mechanic plugin."""
    
    @property
    def metadata(self) -> PluginMetadata:
        return PluginMetadata(
            name="{plugin_name}Mechanic",
            version="1.0.0",
            description="A {plugin_name.lower()} mechanic for the adventure game",
            author="Plugin Developer"
        )
    
    def initialize(self) -> bool:
        """Initialize the mechanic plugin."""
        return True
    
    def cleanup(self) -> None:
        """Clean up mechanic resources."""
        pass
    
    def on_game_start(self, player: Dict[str, Any], world: Dict[str, Any]) -> None:
        """Called when a new game starts."""
        print("{{self.metadata.name}} mechanic activated!")
    
    def on_game_load(self, player: Dict[str, Any], world: Dict[str, Any]) -> None:
        """Called when a game is loaded."""
        pass
    
    def on_game_save(self, player: Dict[str, Any], world: Dict[str, Any]) -> Dict[str, Any]:
        """Called when game is saved."""
        return {{}}  # Return any data to save
    
    def on_turn_start(self, player: Dict[str, Any], world: Dict[str, Any]) -> None:
        """Called at the start of each turn."""
        pass
    
    def on_turn_end(self, player: Dict[str, Any], world: Dict[str, Any]) -> None:
        """Called at the end of each turn."""
        pass
'''
    
    def cleanup(self) -> None:
        """Clean up the plugin loader."""
        self.disable_hot_reload()
        self.location_registry.cleanup_all()
        self.action_registry.cleanup_all()
        self.mechanic_registry.cleanup_all()

