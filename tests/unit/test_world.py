"""
Unit tests for the world module.
"""

from unittest.mock import MagicMock, patch

import pytest

from game.world import (change_location, get_all_locations,
                        get_available_locations, get_current_location,
                        get_location_description, initialize_world,
                        interact_with_location, is_location_accessible)


class TestInitializeWorld:
    """Test world initialization functionality."""

    def test_initialize_world_structure(self):
        """Test that world is initialized with correct structure."""
        world = initialize_world()

        assert "current_location" in world
        assert "locations" in world
        assert world["current_location"] == "Village"
        assert isinstance(world["locations"], dict)

    def test_initialize_world_locations(self):
        """Test that all expected locations are present."""
        world = initialize_world()
        locations = world["locations"]

        expected_locations = ["Village", "Forest", "Cave", "Mountain"]
        for location in expected_locations:
            assert location in locations

    def test_initialize_world_location_structure(self):
        """Test that each location has required structure."""
        world = initialize_world()

        for location_name, location_data in world["locations"].items():
            assert "description" in location_data
            assert "connections" in location_data
            assert "items" in location_data
            assert isinstance(location_data["description"], str)
            assert isinstance(location_data["connections"], list)
            assert isinstance(location_data["items"], list)

    def test_initialize_world_village_details(self):
        """Test Village location specific details."""
        world = initialize_world()
        village = world["locations"]["Village"]

        assert "peaceful village" in village["description"].lower()
        assert "Forest" in village["connections"]
        assert "Mountain" in village["connections"]
        assert "map" in village["items"]
        assert "bread" in village["items"]

    def test_initialize_world_forest_details(self):
        """Test Forest location specific details."""
        world = initialize_world()
        forest = world["locations"]["Forest"]

        assert "forest" in forest["description"].lower()
        assert "Village" in forest["connections"]
        assert "Cave" in forest["connections"]
        assert "stick" in forest["items"]
        assert "berries" in forest["items"]


class TestGetCurrentLocation:
    """Test getting current location functionality."""

    def test_get_current_location_initial(self, sample_world):
        """Test getting initial current location."""
        location = get_current_location(sample_world)
        assert location == "Village"

    def test_get_current_location_after_change(self, sample_world):
        """Test getting current location after changing it."""
        sample_world["current_location"] = "Forest"
        location = get_current_location(sample_world)
        assert location == "Forest"


class TestGetLocationDescription:
    """Test getting location descriptions."""

    def test_get_village_description(self, sample_world):
        """Test getting Village description."""
        description = get_location_description(sample_world, "Village")

        assert isinstance(description, str)
        assert len(description) > 0
        assert "village" in description.lower()

    def test_get_forest_description(self, sample_world):
        """Test getting Forest description."""
        description = get_location_description(sample_world, "Forest")

        assert isinstance(description, str)
        assert "forest" in description.lower()

    def test_get_cave_description(self, sample_world):
        """Test getting Cave description."""
        description = get_location_description(sample_world, "Cave")

        assert isinstance(description, str)
        assert "cave" in description.lower()

    def test_get_mountain_description(self, sample_world):
        """Test getting Mountain description."""
        description = get_location_description(sample_world, "Mountain")

        assert isinstance(description, str)
        assert "mountain" in description.lower()


class TestGetAvailableLocations:
    """Test getting available locations from current location."""

    def test_get_available_from_village(self, sample_world):
        """Test getting available locations from Village."""
        sample_world["current_location"] = "Village"
        available = get_available_locations(sample_world)

        assert "Forest" in available
        assert "Mountain" in available
        assert "Cave" not in available  # Not directly connected

    def test_get_available_from_forest(self, sample_world):
        """Test getting available locations from Forest."""
        sample_world["current_location"] = "Forest"
        available = get_available_locations(sample_world)

        assert "Village" in available
        assert "Cave" in available
        assert "Mountain" not in available  # Not directly connected

    def test_get_available_from_cave(self, sample_world):
        """Test getting available locations from Cave."""
        sample_world["current_location"] = "Cave"
        available = get_available_locations(sample_world)

        assert "Forest" in available
        assert "Village" not in available  # Not directly connected
        assert "Mountain" not in available  # Not directly connected

    def test_get_available_from_mountain(self, sample_world):
        """Test getting available locations from Mountain."""
        sample_world["current_location"] = "Mountain"
        available = get_available_locations(sample_world)

        assert "Village" in available
        assert "Forest" not in available  # Not directly connected
        assert "Cave" not in available  # Not directly connected


class TestChangeLocation:
    """Test changing current location functionality."""

    def test_change_to_valid_location(self, sample_world):
        """Test changing to a valid connected location."""
        sample_world["current_location"] = "Village"
        result = change_location(sample_world, "Forest")

        assert result is True
        assert sample_world["current_location"] == "Forest"

    def test_change_to_invalid_location(self, sample_world):
        """Test changing to an invalid/unconnected location."""
        sample_world["current_location"] = "Village"
        result = change_location(sample_world, "Cave")  # Not directly connected

        assert result is False
        assert sample_world["current_location"] == "Village"  # Should remain unchanged

    def test_change_to_nonexistent_location(self, sample_world):
        """Test changing to a location that doesn't exist."""
        sample_world["current_location"] = "Village"
        result = change_location(sample_world, "NonexistentPlace")

        assert result is False
        assert sample_world["current_location"] == "Village"

    def test_change_location_multiple_times(self, sample_world):
        """Test changing location multiple times."""
        # Village -> Forest
        result1 = change_location(sample_world, "Forest")
        assert result1 is True
        assert sample_world["current_location"] == "Forest"

        # Forest -> Cave
        result2 = change_location(sample_world, "Cave")
        assert result2 is True
        assert sample_world["current_location"] == "Cave"

        # Cave -> Forest (back)
        result3 = change_location(sample_world, "Forest")
        assert result3 is True
        assert sample_world["current_location"] == "Forest"


class TestIsLocationAccessible:
    """Test location accessibility checking."""

    def test_accessible_location_from_village(self, sample_world):
        """Test checking accessible location from Village."""
        sample_world["current_location"] = "Village"

        assert is_location_accessible(sample_world, "Forest") is True
        assert is_location_accessible(sample_world, "Mountain") is True
        assert is_location_accessible(sample_world, "Cave") is False

    def test_accessible_location_from_forest(self, sample_world):
        """Test checking accessible location from Forest."""
        sample_world["current_location"] = "Forest"

        assert is_location_accessible(sample_world, "Village") is True
        assert is_location_accessible(sample_world, "Cave") is True
        assert is_location_accessible(sample_world, "Mountain") is False

    def test_nonexistent_location_accessibility(self, sample_world):
        """Test checking accessibility of nonexistent location."""
        sample_world["current_location"] = "Village"

        assert is_location_accessible(sample_world, "NonexistentPlace") is False


class TestGetAllLocations:
    """Test getting all locations in the world."""

    def test_get_all_locations(self, sample_world):
        """Test getting all locations."""
        all_locations = get_all_locations(sample_world)

        expected_locations = ["Village", "Forest", "Cave", "Mountain"]
        assert len(all_locations) == len(expected_locations)

        for location in expected_locations:
            assert location in all_locations

    def test_get_all_locations_returns_list(self, sample_world):
        """Test that get_all_locations returns a list."""
        all_locations = get_all_locations(sample_world)
        assert isinstance(all_locations, list)


class TestInteractWithLocation:
    """Test location interaction functionality."""

    @patch("locations.village.visit_village")
    def test_interact_with_village(
        self, mock_visit_village, sample_world, sample_player
    ):
        """Test interacting with Village location."""
        sample_world["current_location"] = "Village"

        interact_with_location(sample_world, sample_player)

        mock_visit_village.assert_called_once_with(sample_world, sample_player)

    @patch("locations.forest.enter_forest")
    def test_interact_with_forest(self, mock_enter_forest, sample_world, sample_player):
        """Test interacting with Forest location."""
        sample_world["current_location"] = "Forest"

        interact_with_location(sample_world, sample_player)

        mock_enter_forest.assert_called_once_with(sample_world, sample_player)

    @patch("locations.cave.explore_cave")
    def test_interact_with_cave(self, mock_explore_cave, sample_world, sample_player):
        """Test interacting with Cave location."""
        sample_world["current_location"] = "Cave"

        interact_with_location(sample_world, sample_player)

        mock_explore_cave.assert_called_once_with(sample_world, sample_player)

    @patch("locations.mountain.climb_mountain")
    def test_interact_with_mountain(
        self, mock_climb_mountain, sample_world, sample_player
    ):
        """Test interacting with Mountain location."""
        sample_world["current_location"] = "Mountain"

        interact_with_location(sample_world, sample_player)

        mock_climb_mountain.assert_called_once_with(sample_world, sample_player)

    @patch("builtins.print")
    def test_interact_with_unknown_location(
        self, mock_print, sample_world, sample_player
    ):
        """Test interacting with an unknown location."""
        sample_world["current_location"] = "UnknownPlace"

        interact_with_location(sample_world, sample_player)

        mock_print.assert_called_once_with(
            "There's nothing special to interact with here."
        )


class TestWorldIntegrity:
    """Test world data integrity and consistency."""

    def test_location_connections_are_bidirectional(self, sample_world):
        """Test that location connections are properly bidirectional."""
        locations = sample_world["locations"]

        for location_name, location_data in locations.items():
            for connected_location in location_data["connections"]:
                # Check that the connected location exists
                assert (
                    connected_location in locations
                ), f"Location {connected_location} referenced by {location_name} doesn't exist"

                # Check that the connection is bidirectional
                assert (
                    location_name in locations[connected_location]["connections"]
                ), f"Connection from {location_name} to {connected_location} is not bidirectional"

    def test_all_locations_have_required_fields(self, sample_world):
        """Test that all locations have required fields."""
        required_fields = ["description", "connections", "items"]

        for location_name, location_data in sample_world["locations"].items():
            for field in required_fields:
                assert (
                    field in location_data
                ), f"Location {location_name} missing required field: {field}"

    def test_location_descriptions_are_not_empty(self, sample_world):
        """Test that location descriptions are not empty."""
        for location_name, location_data in sample_world["locations"].items():
            assert (
                len(location_data["description"].strip()) > 0
            ), f"Location {location_name} has empty description"

    def test_current_location_exists_in_locations(self, sample_world):
        """Test that current location exists in the locations dictionary."""
        current_location = sample_world["current_location"]
        assert (
            current_location in sample_world["locations"]
        ), f"Current location {current_location} doesn't exist in locations"
