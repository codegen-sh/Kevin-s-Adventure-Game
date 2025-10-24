"""
Plugin system for Kevin's Adventure Game.

This package provides an extensible plugin architecture that allows
easy addition of new locations, actions, and game mechanics.
"""

from .registry import PluginRegistry, ActionRegistry, LocationRegistry
from .base import BasePlugin, BaseLocation, BaseAction
from .loader import PluginLoader
from .manager import PluginManager

__all__ = [
    'PluginRegistry',
    'ActionRegistry', 
    'LocationRegistry',
    'BasePlugin',
    'BaseLocation',
    'BaseAction',
    'PluginLoader',
    'PluginManager'
]

