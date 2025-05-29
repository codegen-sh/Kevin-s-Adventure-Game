#!/usr/bin/env python3
"""
Test Suite for Kevin's Adventure Game
Tests both the original and improved versions of the game.
"""

import sys
import os

# Add the current directory to the Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_imports():
    """Test that all modules can be imported without errors."""
    print("Testing imports...")
    
    try:
        # Test original modules
        import main
        from game import actions, player, world, items, mythical, weather, state
        from locations import forest, mountain, village, cave
        from utils import save_load, text_formatting, random_events
        print("✓ Original modules imported successfully")
        
        # Test new modules
        from game import engine, player_class, world_class, config
        print("✓ New modules imported successfully")
        
        return True
    except ImportError as e:
        print(f"✗ Import error: {e}")
        return False


def test_player_class():
    """Test the new Player class functionality."""
    print("\nTesting Player class...")
    
    try:
        from game.player_class import Player
        
        # Create a player
        player = Player("TestPlayer", health=80, gold=50)
        assert player.name == "TestPlayer"
        assert player.health == 80
        assert player.gold == 50
        assert player.is_alive == True
        print("✓ Player creation works")
        
        # Test inventory
        player.add_item("sword")
        assert player.has_item("sword")
        player.remove_item("sword")
        assert not player.has_item("sword")
        print("✓ Inventory management works")
        
        # Test health system
        player.take_damage(30)
        assert player.health == 50
        player.heal(20)
        assert player.health == 70
        print("✓ Health system works")
        
        # Test gold system
        player.add_gold(25)
        assert player.gold == 75
        assert player.spend_gold(30) == True
        assert player.gold == 45
        print("✓ Gold system works")
        
        return True
    except Exception as e:
        print(f"✗ Player class test failed: {e}")
        return False


def test_world_class():
    """Test the new World class functionality."""
    print("\nTesting World class...")
    
    try:
        from game.world_class import World, Location, create_default_world
        
        # Test location creation
        location = Location("TestLocation", "A test location", ["OtherLocation"], ["test_item"])
        assert location.name == "TestLocation"
        assert location.has_item("test_item")
        print("✓ Location creation works")
        
        # Test world creation
        world = World()
        world.add_location(location)
        assert world.get_location("TestLocation") is not None
        print("✓ World creation works")
        
        # Test default world
        default_world = create_default_world()
        assert len(default_world.locations) == 4
        assert "Village" in default_world.locations
        print("✓ Default world creation works")
        
        return True
    except Exception as e:
        print(f"✗ World class test failed: {e}")
        return False


def test_game_engine():
    """Test the game engine functionality."""
    print("\nTesting Game Engine...")
    
    try:
        from game.engine import GameEngine
        
        engine = GameEngine()
        engine.start_new_game("TestPlayer")
        
        assert engine.player is not None
        assert engine.world is not None
        assert engine.running == True
        print("✓ Game engine initialization works")
        
        return True
    except Exception as e:
        print(f"✗ Game engine test failed: {e}")
        return False


def test_original_compatibility():
    """Test that the original game still works."""
    print("\nTesting original game compatibility...")
    
    try:
        # Test that we can create player and world using original functions
        from game.player import create_player
        from game.world import initialize_world
        
        player = create_player("TestPlayer")
        world = initialize_world()
        
        assert player["name"] == "TestPlayer"
        assert "Village" in world["locations"]
        print("✓ Original game functions work")
        
        return True
    except Exception as e:
        print(f"✗ Original compatibility test failed: {e}")
        return False


def test_actions_system():
    """Test the actions system."""
    print("\nTesting actions system...")
    
    try:
        from game.actions import perform_action
        from game.player import create_player
        from game.world import initialize_world
        
        player = create_player("TestPlayer")
        world = initialize_world()
        
        # This should not crash
        perform_action(player, world, "look")
        perform_action(player, world, "inventory")
        perform_action(player, world, "status")
        
        print("✓ Actions system works")
        return True
    except Exception as e:
        print(f"✗ Actions system test failed: {e}")
        return False


def run_all_tests():
    """Run all tests and report results."""
    print("=" * 60)
    print("Kevin's Adventure Game - Test Suite")
    print("=" * 60)
    
    tests = [
        test_imports,
        test_original_compatibility,
        test_player_class,
        test_world_class,
        test_game_engine,
        test_actions_system
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        try:
            if test():
                passed += 1
        except Exception as e:
            print(f"✗ Test {test.__name__} crashed: {e}")
    
    print("\n" + "=" * 60)
    print(f"Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! The refactoring was successful.")
        return True
    else:
        print("❌ Some tests failed. Please check the issues above.")
        return False


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)

