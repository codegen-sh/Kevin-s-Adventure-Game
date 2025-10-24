#!/usr/bin/env python3
"""
Simple test script to verify the configuration system works correctly.
"""

import sys
import os

# Add the project root to the Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_configuration_system():
    """Test the configuration system functionality."""
    print("Testing Configuration System...")
    
    try:
        from config import config
        
        # Test game settings
        print("\n1. Testing game settings...")
        game_settings = config.get_game_settings()
        print(f"   Starting health: {game_settings['player']['starting_health']}")
        print(f"   Starting gold: {game_settings['player']['starting_gold']}")
        print(f"   Starting location: {game_settings['player']['starting_location']}")
        
        # Test items configuration
        print("\n2. Testing items configuration...")
        items_config = config.get_items_config()
        print(f"   Total items defined: {len(items_config['items'])}")
        
        # Test specific item
        sword_data = config.get_item_data("sword")
        print(f"   Sword description: {sword_data['description'][:50]}...")
        
        # Test shop configuration
        print("\n3. Testing shop configuration...")
        shop_config = config.get_shop_config("village_shop")
        print(f"   Shop name: {shop_config['name']}")
        print(f"   Items for sale: {len(shop_config['inventory'])}")
        
        # Test world configuration
        print("\n4. Testing world configuration...")
        world_config = config.get_world_config()
        locations = world_config["world"]["locations"]
        print(f"   Total locations: {len(locations)}")
        print(f"   Starting location: {world_config['world']['starting_location']}")
        
        # Test location data
        village_data = config.get_location_data("Village")
        print(f"   Village connections: {village_data['connections']}")
        
        # Test events configuration
        print("\n5. Testing events configuration...")
        events_config = config.get_events_config()
        encounters = events_config["random_events"]["encounters"]
        print(f"   Total encounters defined: {len(encounters)}")
        
        # Test validation
        print("\n6. Testing configuration validation...")
        is_valid = config.validate_configuration()
        print(f"   Configuration valid: {is_valid}")
        
        # Test configuration info
        print("\n7. Configuration manager info...")
        info = config.get_config_info()
        print(f"   Config directory: {info['config_dir']}")
        print(f"   Environment: {info['environment']}")
        print(f"   Loaded files: {len(info['loaded_files'])}")
        
        print("\n✅ All configuration tests passed!")
        return True
        
    except Exception as e:
        print(f"\n❌ Configuration test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_game_integration():
    """Test that the game can use the configuration system."""
    print("\nTesting Game Integration...")
    
    try:
        # Test player creation with config
        from game.player import create_player
        player = create_player("TestPlayer")
        print(f"   Created player with {player['health']} health and {player['gold']} gold")
        
        # Test world initialization with config
        from game.world import initialize_world
        world = initialize_world()
        print(f"   Initialized world with {len(world['locations'])} locations")
        print(f"   Starting location: {world['current_location']}")
        
        # Test item description loading
        from game.items import get_item_description
        bread_desc = get_item_description("bread")
        print(f"   Bread description: {bread_desc[:50]}...")
        
        print("\n✅ Game integration tests passed!")
        return True
        
    except Exception as e:
        print(f"\n❌ Game integration test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    print("Kevin's Adventure Game - Configuration System Test")
    print("=" * 50)
    
    # Run tests
    config_test_passed = test_configuration_system()
    integration_test_passed = test_game_integration()
    
    # Summary
    print("\n" + "=" * 50)
    if config_test_passed and integration_test_passed:
        print("🎉 All tests passed! Configuration system is working correctly.")
        sys.exit(0)
    else:
        print("💥 Some tests failed. Please check the configuration system.")
        sys.exit(1)

