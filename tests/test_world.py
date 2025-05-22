"""
Tests for the world module.
"""

from kevin_adventure_game.game.world import (
    change_location,
    get_all_locations,
    get_available_locations,
    get_current_location,
    get_location_description,
    initialize_world,
    is_location_accessible,
)


def test_initialize_world():
    """Test initializing the world."""
    world = initialize_world()
    assert world["current_location"] == "Village"
    assert "Village" in world["locations"]
    assert "Forest" in world["locations"]
    assert "Cave" in world["locations"]
    assert "Mountain" in world["locations"]


def test_get_current_location():
    """Test getting the current location."""
    world = {"current_location": "Forest"}
    assert get_current_location(world) == "Forest"


def test_get_location_description():
    """Test getting a location description."""
    world = {
        "locations": {
            "Village": {"description": "A small village"},
        }
    }
    assert get_location_description(world, "Village") == "A small village"


def test_get_available_locations():
    """Test getting available locations."""
    world = {
        "current_location": "Village",
        "locations": {
            "Village": {"connections": ["Forest", "Mountain"]},
        },
    }
    assert get_available_locations(world) == ["Forest", "Mountain"]


def test_change_location():
    """Test changing the current location."""
    world = {
        "current_location": "Village",
        "locations": {
            "Village": {"connections": ["Forest", "Mountain"]},
            "Forest": {"connections": ["Village"]},
            "Mountain": {"connections": ["Village"]},
        },
    }

    # Test valid location change
    assert change_location(world, "Forest") is True
    assert world["current_location"] == "Forest"

    # Test invalid location change
    assert change_location(world, "Cave") is False
    assert world["current_location"] == "Forest"


def test_is_location_accessible():
    """Test checking if a location is accessible."""
    world = {
        "current_location": "Village",
        "locations": {
            "Village": {"connections": ["Forest", "Mountain"]},
        },
    }
    assert is_location_accessible(world, "Forest") is True
    assert is_location_accessible(world, "Cave") is False


def test_get_all_locations():
    """Test getting all locations."""
    world = {
        "locations": {
            "Village": {},
            "Forest": {},
            "Cave": {},
            "Mountain": {},
        }
    }
    assert set(get_all_locations(world)) == {
        "Village",
        "Forest",
        "Cave",
        "Mountain",
    }
