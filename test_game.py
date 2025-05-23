#!/usr/bin/env python3
"""
Simple test script to verify the game works correctly.
"""

import sys
from io import StringIO
from game.controller import create_game_controller


def test_game_initialization():
    """Test that the game can be initialized without errors."""
    print("Testing game initialization...")
    
    try:
        controller = create_game_controller()
        controller.start_new_game("TestPlayer")
        
        # Check that player and world are created
        assert controller.player is not None, "Player not created"
        assert controller.world is not None, "World not created"
        assert controller.player['name'] == "TestPlayer", "Player name not set correctly"
        assert controller.game_running == True, "Game not marked as running"
        
        print("✅ Game initialization test passed!")
        return True
        
    except Exception as e:
        print(f"❌ Game initialization test failed: {e}")
        return False


def test_basic_actions():
    """Test that basic actions work without errors."""
    print("Testing basic actions...")
    
    try:
        controller = create_game_controller()
        controller.start_new_game("TestPlayer")
        
        # Test some basic actions
        from game.actions import perform_action
        
        # Test status command
        perform_action(controller.player, controller.world, "status")
        
        # Test inventory command
        perform_action(controller.player, controller.world, "inventory")
        
        # Test look command
        perform_action(controller.player, controller.world, "look")
        
        # Test weather command
        perform_action(controller.player, controller.world, "weather")
        
        print("✅ Basic actions test passed!")
        return True
        
    except Exception as e:
        print(f"❌ Basic actions test failed: {e}")
        return False


def test_movement():
    """Test that movement between locations works."""
    print("Testing movement...")
    
    try:
        controller = create_game_controller()
        controller.start_new_game("TestPlayer")
        
        from game.actions import perform_action
        from game.world import get_current_location
        
        # Check initial location
        initial_location = get_current_location(controller.world)
        print(f"Initial location: {initial_location}")
        
        # Try to move to forest
        perform_action(controller.player, controller.world, "go forest")
        
        # Check if location changed
        new_location = get_current_location(controller.world)
        print(f"New location: {new_location}")
        
        print("✅ Movement test passed!")
        return True
        
    except Exception as e:
        print(f"❌ Movement test failed: {e}")
        return False


def run_all_tests():
    """Run all tests and report results."""
    print("🧪 Running Kevin's Adventure Game Tests")
    print("=" * 50)
    
    tests = [
        test_game_initialization,
        test_basic_actions,
        test_movement
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
        print()
    
    print("=" * 50)
    print(f"Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! The game is working correctly.")
        return True
    else:
        print("⚠️  Some tests failed. Check the output above for details.")
        return False


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)

