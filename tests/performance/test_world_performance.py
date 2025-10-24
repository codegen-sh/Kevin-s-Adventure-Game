"""
Performance tests for world-related operations.
"""

import time
from unittest.mock import patch

import pytest

from game.world import (change_location, get_all_locations,
                        get_available_locations, get_current_location,
                        get_location_description, initialize_world,
                        interact_with_location)


class TestWorldInitializationPerformance:
    """Test performance of world initialization."""

    def test_world_initialization_speed(self, benchmark):
        """Benchmark world initialization speed."""
        result = benchmark(initialize_world)

        # Verify the result is correct
        assert "current_location" in result
        assert "locations" in result
        assert len(result["locations"]) == 4

    def test_multiple_world_initialization(self, benchmark):
        """Benchmark creating multiple worlds."""

        def create_multiple_worlds():
            worlds = []
            for i in range(100):
                worlds.append(initialize_world())
            return worlds

        result = benchmark(create_multiple_worlds)
        assert len(result) == 100

        # Verify all worlds are properly initialized
        for world in result:
            assert "current_location" in world
            assert len(world["locations"]) == 4


class TestLocationOperationPerformance:
    """Test performance of location-related operations."""

    def test_get_current_location_speed(self, benchmark, sample_world):
        """Benchmark getting current location."""
        result = benchmark(get_current_location, sample_world)
        assert result == "Village"

    def test_get_location_description_speed(self, benchmark, sample_world):
        """Benchmark getting location description."""
        result = benchmark(get_location_description, sample_world, "Village")
        assert isinstance(result, str)
        assert len(result) > 0

    def test_get_available_locations_speed(self, benchmark, sample_world):
        """Benchmark getting available locations."""
        result = benchmark(get_available_locations, sample_world)
        assert isinstance(result, list)
        assert len(result) > 0

    def test_get_all_locations_speed(self, benchmark, sample_world):
        """Benchmark getting all locations."""
        result = benchmark(get_all_locations, sample_world)
        assert isinstance(result, list)
        assert len(result) == 4


class TestLocationChangePerformance:
    """Test performance of location changes."""

    def test_change_location_speed(self, benchmark, sample_world):
        """Benchmark location change operation."""

        def change_to_forest():
            return change_location(sample_world, "Forest")

        result = benchmark(change_to_forest)
        assert result is True
        assert sample_world["current_location"] == "Forest"

    def test_multiple_location_changes(self, benchmark, sample_world):
        """Benchmark multiple location changes."""

        def perform_location_tour():
            locations = ["Forest", "Cave", "Forest", "Village", "Mountain", "Village"]
            results = []
            for location in locations:
                results.append(change_location(sample_world, location))
            return results

        results = benchmark(perform_location_tour)
        assert all(results)  # All changes should be successful

    def test_invalid_location_change_speed(self, benchmark, sample_world):
        """Benchmark invalid location change (should be fast)."""

        def try_invalid_change():
            return change_location(sample_world, "NonexistentLocation")

        result = benchmark(try_invalid_change)
        assert result is False


class TestLocationInteractionPerformance:
    """Test performance of location interactions."""

    @patch("locations.village.visit_village")
    def test_village_interaction_speed(
        self, mock_village, benchmark, sample_world, sample_player
    ):
        """Benchmark village interaction."""
        sample_world["current_location"] = "Village"

        def interact_with_village():
            interact_with_location(sample_world, sample_player)

        benchmark(interact_with_village)
        mock_village.assert_called()

    @patch("locations.forest.enter_forest")
    def test_forest_interaction_speed(
        self, mock_forest, benchmark, sample_world, sample_player
    ):
        """Benchmark forest interaction."""
        sample_world["current_location"] = "Forest"

        def interact_with_forest():
            interact_with_location(sample_world, sample_player)

        benchmark(interact_with_forest)
        mock_forest.assert_called()

    @patch("locations.cave.explore_cave")
    def test_cave_interaction_speed(
        self, mock_cave, benchmark, sample_world, sample_player
    ):
        """Benchmark cave interaction."""
        sample_world["current_location"] = "Cave"

        def interact_with_cave():
            interact_with_location(sample_world, sample_player)

        benchmark(interact_with_cave)
        mock_cave.assert_called()

    @patch("locations.mountain.climb_mountain")
    def test_mountain_interaction_speed(
        self, mock_mountain, benchmark, sample_world, sample_player
    ):
        """Benchmark mountain interaction."""
        sample_world["current_location"] = "Mountain"

        def interact_with_mountain():
            interact_with_location(sample_world, sample_player)

        benchmark(interact_with_mountain)
        mock_mountain.assert_called()


class TestWorldScalingPerformance:
    """Test how world operations scale with complexity."""

    def test_world_with_many_items_performance(self, benchmark):
        """Test performance with worlds containing many items."""

        def create_item_heavy_world():
            world = initialize_world()
            # Add many items to each location
            for location in world["locations"]:
                world["locations"][location]["items"] = [
                    f"item_{i}" for i in range(100)
                ]
            return world

        result = benchmark(create_item_heavy_world)

        # Verify items were added
        for location in result["locations"]:
            assert len(result["locations"][location]["items"]) == 100

    def test_location_operations_with_many_items(self, benchmark):
        """Test location operations with many items."""
        world = initialize_world()
        # Add many items to Village
        world["locations"]["Village"]["items"] = [f"item_{i}" for i in range(1000)]

        def get_village_info():
            description = get_location_description(world, "Village")
            available = get_available_locations(world)
            return description, available

        result = benchmark(get_village_info)
        assert len(result) == 2  # description and available locations

    def test_world_traversal_performance(self, benchmark):
        """Test performance of traversing the entire world."""

        def traverse_entire_world():
            world = initialize_world()
            visited = []

            # Visit all locations in a systematic way
            locations_to_visit = [
                ("Village", "Forest"),
                ("Forest", "Cave"),
                ("Cave", "Forest"),
                ("Forest", "Village"),
                ("Village", "Mountain"),
                ("Mountain", "Village"),
            ]

            for current, next_loc in locations_to_visit:
                world["current_location"] = current
                if change_location(world, next_loc):
                    visited.append(next_loc)

            return visited

        result = benchmark(traverse_entire_world)
        assert len(result) > 0


class TestMemoryUsagePerformance:
    """Test memory usage of world operations."""

    def test_world_memory_efficiency(self, benchmark):
        """Test memory efficiency of world creation."""

        def create_and_destroy_worlds():
            worlds = []
            for i in range(50):
                world = initialize_world()
                worlds.append(world)

            # Simulate some operations
            for world in worlds:
                get_current_location(world)
                get_all_locations(world)

            return len(worlds)

        result = benchmark(create_and_destroy_worlds)
        assert result == 50

    def test_location_data_access_patterns(self, benchmark):
        """Test different patterns of accessing location data."""
        world = initialize_world()

        def access_location_data():
            results = []

            # Pattern 1: Sequential access
            for location in world["locations"]:
                results.append(get_location_description(world, location))

            # Pattern 2: Random access
            import random

            locations = list(world["locations"].keys())
            for _ in range(10):
                location = random.choice(locations)
                results.append(get_location_description(world, location))

            return len(results)

        result = benchmark(access_location_data)
        assert result > 0


class TestConcurrentWorldOperations:
    """Test performance under concurrent-like operations."""

    def test_rapid_location_changes(self, benchmark):
        """Test rapid succession of location changes."""
        world = initialize_world()

        def rapid_changes():
            changes = [
                "Forest",
                "Village",
                "Forest",
                "Cave",
                "Forest",
                "Village",
                "Mountain",
                "Village",
                "Forest",
                "Cave",
                "Forest",
                "Village",
            ]

            successful_changes = 0
            for location in changes:
                if change_location(world, location):
                    successful_changes += 1

            return successful_changes

        result = benchmark(rapid_changes)
        assert result > 0

    def test_simultaneous_world_queries(self, benchmark):
        """Test multiple simultaneous queries to world state."""
        world = initialize_world()

        def multiple_queries():
            results = []

            # Simulate multiple simultaneous queries
            for _ in range(20):
                results.append(get_current_location(world))
                results.append(get_available_locations(world))
                results.append(get_all_locations(world))
                results.append(get_location_description(world, "Village"))

            return len(results)

        result = benchmark(multiple_queries)
        assert result == 80  # 20 iterations * 4 queries each


class TestWorldPerformanceRegression:
    """Test for performance regressions in world operations."""

    def test_baseline_world_operations(self, benchmark):
        """Establish baseline performance for world operations."""

        def baseline_operations():
            world = initialize_world()

            # Standard set of operations
            current = get_current_location(world)
            description = get_location_description(world, current)
            available = get_available_locations(world)
            all_locations = get_all_locations(world)

            # Change location and repeat
            change_location(world, "Forest")
            current = get_current_location(world)
            description = get_location_description(world, current)
            available = get_available_locations(world)

            return len(all_locations)

        result = benchmark(baseline_operations)
        assert result == 4

    def test_world_operation_consistency(self, benchmark):
        """Test that world operations maintain consistent performance."""

        def consistent_operations():
            times = []

            for _ in range(10):
                start_time = time.time()

                world = initialize_world()
                get_current_location(world)
                get_available_locations(world)
                change_location(world, "Forest")

                end_time = time.time()
                times.append(end_time - start_time)

            # Check that performance is consistent (no outliers)
            avg_time = sum(times) / len(times)
            max_deviation = max(abs(t - avg_time) for t in times)

            return (
                max_deviation < avg_time * 2
            )  # No operation should take more than 2x average

        result = benchmark(consistent_operations)
        assert result is True
