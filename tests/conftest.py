"""
Pytest configuration and shared fixtures for Kevin's Adventure Game tests.
"""

import pytest
import tempfile
import os
import shutil
from unittest.mock import patch, MagicMock

# Import game modules
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from game.player import create_player
from game.world import initialize_world
from game.items import get_item_description


@pytest.fixture
def sample_player():
    """Create a sample player for testing."""
    return create_player("TestPlayer")


@pytest.fixture
def sample_world():
    """Create a sample world for testing."""
    return initialize_world()


@pytest.fixture
def player_with_items():
    """Create a player with some items in inventory."""
    player = create_player("TestPlayer")
    player["inventory"] = ["map", "bread", "stick", "torch"]
    player["gold"] = 150
    return player


@pytest.fixture
def damaged_player():
    """Create a player with reduced health."""
    player = create_player("TestPlayer")
    player["health"] = 50
    return player


@pytest.fixture
def rich_player():
    """Create a player with lots of gold."""
    player = create_player("TestPlayer")
    player["gold"] = 1000
    return player


@pytest.fixture
def world_with_items():
    """Create a world with additional items in locations."""
    world = initialize_world()
    world["locations"]["Village"]["items"].extend(["sword", "potion"])
    world["locations"]["Forest"]["items"].extend(["mushrooms", "herbs"])
    return world


@pytest.fixture
def empty_world():
    """Create a world with no items in any location."""
    world = initialize_world()
    for location in world["locations"]:
        world["locations"][location]["items"] = []
    return world


@pytest.fixture
def temp_save_dir():
    """Create a temporary directory for save file testing."""
    temp_dir = tempfile.mkdtemp()
    yield temp_dir
    shutil.rmtree(temp_dir)


@pytest.fixture
def mock_input():
    """Mock the input function for testing user interactions."""
    with patch('builtins.input') as mock:
        yield mock


@pytest.fixture
def mock_print():
    """Mock the print function to capture output."""
    with patch('builtins.print') as mock:
        yield mock


@pytest.fixture
def mock_random():
    """Mock random functions for predictable testing."""
    with patch('random.random') as mock_random, \
         patch('random.choice') as mock_choice, \
         patch('random.randint') as mock_randint:
        
        # Set default return values
        mock_random.return_value = 0.5
        mock_choice.return_value = "test_item"
        mock_randint.return_value = 10
        
        yield {
            'random': mock_random,
            'choice': mock_choice,
            'randint': mock_randint
        }


@pytest.fixture
def mock_file_operations():
    """Mock file operations for testing save/load functionality."""
    with patch('builtins.open', create=True) as mock_open, \
         patch('os.path.exists') as mock_exists, \
         patch('os.listdir') as mock_listdir, \
         patch('json.dump') as mock_json_dump, \
         patch('json.load') as mock_json_load:
        
        yield {
            'open': mock_open,
            'exists': mock_exists,
            'listdir': mock_listdir,
            'json_dump': mock_json_dump,
            'json_load': mock_json_load
        }


@pytest.fixture(autouse=True)
def reset_game_state():
    """Reset any global game state before each test."""
    # This fixture runs automatically before each test
    # Add any global state reset logic here if needed
    yield
    # Cleanup after test if needed


# Pytest markers for test categorization
def pytest_configure(config):
    """Configure pytest with custom markers."""
    config.addinivalue_line(
        "markers", "unit: mark test as a unit test"
    )
    config.addinivalue_line(
        "markers", "integration: mark test as an integration test"
    )
    config.addinivalue_line(
        "markers", "scenario: mark test as a scenario test"
    )
    config.addinivalue_line(
        "markers", "performance: mark test as a performance test"
    )
    config.addinivalue_line(
        "markers", "slow: mark test as slow running"
    )


# Custom pytest hooks
def pytest_collection_modifyitems(config, items):
    """Modify test collection to add markers based on test location."""
    for item in items:
        # Add markers based on test file location
        if "unit" in str(item.fspath):
            item.add_marker(pytest.mark.unit)
        elif "integration" in str(item.fspath):
            item.add_marker(pytest.mark.integration)
        elif "scenarios" in str(item.fspath):
            item.add_marker(pytest.mark.scenario)
        elif "performance" in str(item.fspath):
            item.add_marker(pytest.mark.performance)


# Test data constants
TEST_ITEMS = [
    "map", "bread", "stick", "berries", "torch", "gemstone", 
    "rope", "pickaxe", "mushrooms", "sword", "gold_coin"
]

TEST_LOCATIONS = ["Village", "Forest", "Cave", "Mountain"]

TEST_PLAYER_NAMES = ["Kevin", "TestPlayer", "Alice", "Bob"]


# Helper functions for tests
def assert_player_health_in_range(player, min_health=0, max_health=100):
    """Assert that player health is within valid range."""
    assert min_health <= player["health"] <= max_health, \
        f"Player health {player['health']} not in range [{min_health}, {max_health}]"


def assert_valid_location(world, location):
    """Assert that a location exists in the world."""
    assert location in world["locations"], \
        f"Location '{location}' not found in world"


def assert_item_in_inventory(player, item):
    """Assert that an item is in the player's inventory."""
    assert item in player["inventory"], \
        f"Item '{item}' not found in player inventory: {player['inventory']}"


def assert_item_not_in_inventory(player, item):
    """Assert that an item is not in the player's inventory."""
    assert item not in player["inventory"], \
        f"Item '{item}' unexpectedly found in player inventory: {player['inventory']}"

