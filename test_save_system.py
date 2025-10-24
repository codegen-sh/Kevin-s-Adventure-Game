#!/usr/bin/env python3
"""
Test script for the enhanced save/load system.
This script verifies that all components work correctly.
"""

import os
import sys
import json
import tempfile
import shutil
from pathlib import Path

# Add the game directory to the path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from game.player import create_player
from game.world import initialize_world
from game.save_manager import SaveManager
from utils.serialization import SaveDataSerializer, SaveDataValidator
from utils.backup_manager import BackupManager
from utils.save_load import save_to_slot, load_from_slot, list_save_slots


def test_serialization():
    """Test the serialization system."""
    print("Testing serialization system...")
    
    # Create test data
    player = create_player("TestPlayer")
    world = initialize_world()
    
    serializer = SaveDataSerializer()
    
    # Test serialization
    try:
        serialized_data = serializer.serialize(player, world, compress=True)
        print("✓ Serialization successful")
    except Exception as e:
        print(f"✗ Serialization failed: {e}")
        return False
    
    # Test deserialization
    try:
        loaded_player, loaded_world, metadata = serializer.deserialize(serialized_data)
        print("✓ Deserialization successful")
    except Exception as e:
        print(f"✗ Deserialization failed: {e}")
        return False
    
    # Verify data integrity
    if loaded_player["name"] == player["name"] and loaded_world["current_location"] == world["current_location"]:
        print("✓ Data integrity verified")
        return True
    else:
        print("✗ Data integrity check failed")
        return False


def test_save_manager():
    """Test the save manager functionality."""
    print("\nTesting save manager...")
    
    # Create temporary directory for testing
    with tempfile.TemporaryDirectory() as temp_dir:
        save_manager = SaveManager(temp_dir, max_slots=5)
        
        # Create test data
        player = create_player("TestPlayer")
        world = initialize_world()
        
        # Test save slot creation
        try:
            success = save_manager.create_save_slot(1, player, world)
            if success:
                print("✓ Save slot creation successful")
            else:
                print("✗ Save slot creation failed")
                return False
        except Exception as e:
            print(f"✗ Save slot creation error: {e}")
            return False
        
        # Test save slot loading
        try:
            result = save_manager.load_save_slot(1)
            if result:
                loaded_player, loaded_world, metadata = result
                print("✓ Save slot loading successful")
            else:
                print("✗ Save slot loading failed")
                return False
        except Exception as e:
            print(f"✗ Save slot loading error: {e}")
            return False
        
        # Test slot listing
        try:
            slots = save_manager.list_save_slots()
            if len(slots) == 5 and slots[0]["exists"]:
                print("✓ Save slot listing successful")
            else:
                print("✗ Save slot listing failed")
                return False
        except Exception as e:
            print(f"✗ Save slot listing error: {e}")
            return False
        
        # Test statistics
        try:
            stats = save_manager.get_save_statistics()
            if stats["total_slots"] == 1:
                print("✓ Save statistics successful")
            else:
                print("✗ Save statistics failed")
                return False
        except Exception as e:
            print(f"✗ Save statistics error: {e}")
            return False
    
    return True


def test_backup_manager():
    """Test the backup manager functionality."""
    print("\nTesting backup manager...")
    
    # Create temporary directory for testing
    with tempfile.TemporaryDirectory() as temp_dir:
        save_dir = Path(temp_dir) / "saves"
        save_dir.mkdir()
        
        backup_manager = BackupManager(str(save_dir))
        
        # Create a test save file
        test_save_data = {
            "player": create_player("TestPlayer"),
            "world": initialize_world()
        }
        
        test_file = save_dir / "test_save.json"
        with open(test_file, 'w') as f:
            json.dump(test_save_data, f)
        
        # Test backup creation
        try:
            backup_filename = backup_manager.create_backup("test_save.json", "test")
            if backup_filename:
                print("✓ Backup creation successful")
            else:
                print("✗ Backup creation failed")
                return False
        except Exception as e:
            print(f"✗ Backup creation error: {e}")
            return False
        
        # Test backup listing
        try:
            backups = backup_manager.list_backups()
            if len(backups) > 0:
                print("✓ Backup listing successful")
            else:
                print("✗ Backup listing failed")
                return False
        except Exception as e:
            print(f"✗ Backup listing error: {e}")
            return False
        
        # Test backup verification
        try:
            is_valid = backup_manager.verify_backup_integrity(backup_filename)
            if is_valid:
                print("✓ Backup verification successful")
            else:
                print("✗ Backup verification failed")
                return False
        except Exception as e:
            print(f"✗ Backup verification error: {e}")
            return False
    
    return True


def test_integration():
    """Test the integration with the main save/load functions."""
    print("\nTesting integration...")
    
    # Create temporary directory for testing
    with tempfile.TemporaryDirectory() as temp_dir:
        # Temporarily change the save directory
        import utils.save_load
        original_save_manager = utils.save_load.save_manager
        utils.save_load.save_manager = SaveManager(temp_dir)
        
        try:
            # Create test data
            player = create_player("IntegrationTest")
            world = initialize_world()
            
            # Test save to slot
            success = save_to_slot(1, player, world)
            if success:
                print("✓ Integration save successful")
            else:
                print("✗ Integration save failed")
                return False
            
            # Test load from slot
            loaded_player, loaded_world = load_from_slot(1)
            if loaded_player and loaded_world:
                print("✓ Integration load successful")
            else:
                print("✗ Integration load failed")
                return False
            
            # Test slot listing
            slots = list_save_slots()
            if len(slots) > 0 and slots[0]["exists"]:
                print("✓ Integration slot listing successful")
            else:
                print("✗ Integration slot listing failed")
                return False
            
        finally:
            # Restore original save manager
            utils.save_load.save_manager = original_save_manager
    
    return True


def test_error_handling():
    """Test error handling and recovery."""
    print("\nTesting error handling...")
    
    # Create temporary directory for testing
    with tempfile.TemporaryDirectory() as temp_dir:
        save_manager = SaveManager(temp_dir)
        
        # Test loading non-existent slot
        try:
            result = save_manager.load_save_slot(99)
            if result is None:
                print("✓ Non-existent slot handling successful")
            else:
                print("✗ Non-existent slot handling failed")
                return False
        except Exception as e:
            print(f"✗ Non-existent slot handling error: {e}")
            return False
        
        # Test invalid slot ID
        try:
            success = save_manager.create_save_slot(0, {}, {})  # Invalid slot ID
            if not success:
                print("✓ Invalid slot ID handling successful")
            else:
                print("✗ Invalid slot ID handling failed")
                return False
        except Exception as e:
            print(f"✗ Invalid slot ID handling error: {e}")
            return False
    
    return True


def main():
    """Run all tests."""
    print("Running Enhanced Save/Load System Tests")
    print("=" * 50)
    
    tests = [
        test_serialization,
        test_save_manager,
        test_backup_manager,
        test_integration,
        test_error_handling
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        try:
            if test():
                passed += 1
            else:
                print(f"Test {test.__name__} failed!")
        except Exception as e:
            print(f"Test {test.__name__} crashed: {e}")
    
    print("\n" + "=" * 50)
    print(f"Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! The enhanced save/load system is working correctly.")
        return 0
    else:
        print("❌ Some tests failed. Please check the implementation.")
        return 1


if __name__ == "__main__":
    sys.exit(main())

