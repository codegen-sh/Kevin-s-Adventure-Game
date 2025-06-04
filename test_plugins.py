#!/usr/bin/env python3
"""
Test script for the plugin system.
This script tests the basic functionality of the plugin system.
"""

import sys
import os

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from plugins.manager import get_plugin_manager
from game.player import create_player
from game.world import initialize_world


def test_plugin_system():
    """Test the basic plugin system functionality."""
    print("=== Testing Plugin System ===")
    
    # Initialize plugin manager
    manager = get_plugin_manager()
    
    print("1. Initializing plugin system...")
    try:
        results = manager.initialize()
        print(f"   ✓ Initialized successfully")
        print(f"   ✓ Loaded {results.get('loaded_plugins', 0)} plugins")
        print(f"   ✓ Registered {results.get('registered_plugins', 0)} plugins")
        
        if results.get('failed_plugins'):
            print(f"   ⚠ Failed plugins: {results['failed_plugins']}")
    except Exception as e:
        print(f"   ✗ Initialization failed: {e}")
        return False
    
    # Test plugin status
    print("\\n2. Checking plugin status...")
    try:
        status = manager.get_status()
        print(f"   ✓ System initialized: {status['initialized']}")
        print(f"   ✓ Locations: {status['plugin_counts']['locations']}")
        print(f"   ✓ Actions: {status['plugin_counts']['actions']}")
        print(f"   ✓ Mechanics: {status['plugin_counts']['mechanics']}")
    except Exception as e:
        print(f"   ✗ Status check failed: {e}")
        return False
    
    # Test world integration
    print("\\n3. Testing world integration...")
    try:
        world = initialize_world()
        manager.integrate_with_world(world)
        
        original_locations = len(world.get('locations', {}))
        print(f"   ✓ World integration successful")
        print(f"   ✓ Total locations available: {original_locations}")
        
        # Check if plugin locations were added
        plugin_locations = manager.locations.get_location_data()
        if plugin_locations:
            print(f"   ✓ Plugin locations added: {list(plugin_locations.keys())}")
        else:
            print("   ℹ No plugin locations found")
            
    except Exception as e:
        print(f"   ✗ World integration failed: {e}")
        return False
    
    # Test action handling
    print("\\n4. Testing action handling...")
    try:
        player = create_player("TestPlayer")
        
        # Test a plugin action if available
        test_commands = ["inspect", "examine", "plugins", "unknown_command"]
        
        for command in test_commands:
            handled = manager.handle_action(command, player, world)
            print(f"   ✓ Command '{command}': {'handled by plugin' if handled else 'not handled'}")
            
    except Exception as e:
        print(f"   ✗ Action handling test failed: {e}")
        return False
    
    # Test game events
    print("\\n5. Testing game events...")
    try:
        player = create_player("TestPlayer")
        world = initialize_world()
        
        manager.trigger_game_events('start', player, world)
        print("   ✓ Game start event triggered")
        
        save_data = manager.trigger_game_events('save', player, world)
        print(f"   ✓ Game save event triggered, data: {bool(save_data)}")
        
        manager.trigger_game_events('turn_start', player, world)
        print("   ✓ Turn start event triggered")
        
        manager.trigger_game_events('turn_end', player, world)
        print("   ✓ Turn end event triggered")
        
    except Exception as e:
        print(f"   ✗ Game events test failed: {e}")
        return False
    
    # Test plugin creation
    print("\\n6. Testing plugin creation...")
    try:
        test_file = manager.create_plugin("TestLocation", "location", "plugins/custom")
        print(f"   ✓ Plugin template created: {test_file}")
        
        # Clean up test file
        if os.path.exists(test_file):
            os.remove(test_file)
            print("   ✓ Test file cleaned up")
            
    except Exception as e:
        print(f"   ✗ Plugin creation test failed: {e}")
        return False
    
    # Test shutdown
    print("\\n7. Testing shutdown...")
    try:
        manager.shutdown()
        print("   ✓ Plugin system shutdown successful")
    except Exception as e:
        print(f"   ✗ Shutdown failed: {e}")
        return False
    
    print("\\n=== All Tests Passed! ===")
    return True


def test_individual_plugins():
    """Test individual plugin functionality."""
    print("\\n=== Testing Individual Plugins ===")
    
    manager = get_plugin_manager()
    manager.initialize()
    
    # Test Desert location plugin
    print("\\n1. Testing Desert location plugin...")
    desert_plugin = manager.locations.get_enabled("Desert")
    if desert_plugin:
        print("   ✓ Desert plugin loaded")
        print(f"   ✓ Description: {desert_plugin.get_description()[:50]}...")
        print(f"   ✓ Connections: {desert_plugin.get_connections()}")
        print(f"   ✓ Items: {desert_plugin.get_items()}")
    else:
        print("   ℹ Desert plugin not found")
    
    # Test Inspect action plugin
    print("\\n2. Testing Inspect action plugin...")
    inspect_plugin = manager.actions.get_enabled("InspectAction")
    if inspect_plugin:
        print("   ✓ Inspect plugin loaded")
        print(f"   ✓ Triggers: {inspect_plugin.get_triggers()}")
        print(f"   ✓ Help: {inspect_plugin.get_help_text()}")
    else:
        print("   ℹ Inspect plugin not found")
    
    # Test Weather mechanic plugin
    print("\\n3. Testing Weather mechanic plugin...")
    weather_plugin = manager.mechanics.get_enabled("WeatherMechanic")
    if weather_plugin:
        print("   ✓ Weather plugin loaded")
        print(f"   ✓ Current weather: {getattr(weather_plugin, 'current_weather', 'unknown')}")
    else:
        print("   ℹ Weather plugin not found")
    
    manager.shutdown()


if __name__ == "__main__":
    print("Kevin's Adventure Game - Plugin System Test")
    print("=" * 50)
    
    success = test_plugin_system()
    
    if success:
        test_individual_plugins()
        print("\\n🎉 Plugin system is working correctly!")
    else:
        print("\\n❌ Plugin system has issues that need to be addressed.")
        sys.exit(1)

