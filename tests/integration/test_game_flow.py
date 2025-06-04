"""
Integration tests for complete game flow and module interactions.
"""

from unittest.mock import MagicMock, patch

import pytest

from game.actions import perform_action
from game.player import create_player
from game.world import initialize_world
from main import main


class TestGameInitialization:
    """Test game initialization and setup."""

    def test_create_player_and_world_integration(self):
        """Test that player and world are properly initialized together."""
        player = create_player("Kevin")
        world = initialize_world()

        # Player should start in a location that exists in the world
        assert player["location"] in world["locations"]

        # Current world location should match player location
        assert world["current_location"] == player["location"]

        # Player should be able to access items in starting location
        starting_location = player["location"]
        available_items = world["locations"][starting_location]["items"]
        assert isinstance(available_items, list)

    def test_player_world_consistency(self):
        """Test consistency between player and world state."""
        player = create_player("TestPlayer")
        world = initialize_world()

        # Ensure player location exists in world
        assert player["location"] in world["locations"]

        # Ensure world current location is valid
        assert world["current_location"] in world["locations"]

        # Test that we can get available locations from player's location
        from game.world import get_available_locations

        world["current_location"] = player["location"]
        available = get_available_locations(world)
        assert isinstance(available, list)
        assert len(available) > 0


class TestMovementIntegration:
    """Test player movement integration across modules."""

    def test_complete_movement_flow(self):
        """Test complete movement from action to world state update."""
        player = create_player("TestPlayer")
        world = initialize_world()

        # Test movement from Village to Forest
        with patch("builtins.print"):  # Suppress output
            perform_action(player, world, "go forest")

        # Both player and world should be updated
        assert player["location"] == "Forest"
        assert world["current_location"] == "Forest"

    def test_movement_with_location_interaction(self):
        """Test movement followed by location interaction."""
        player = create_player("TestPlayer")
        world = initialize_world()

        # Move to forest and interact
        with patch("builtins.print"), patch(
            "locations.forest.enter_forest"
        ) as mock_forest:

            perform_action(player, world, "go forest")
            perform_action(player, world, "interact")

            # Should have called forest interaction
            mock_forest.assert_called_once_with(world, player)

    def test_invalid_movement_preserves_state(self):
        """Test that invalid movement doesn't change game state."""
        player = create_player("TestPlayer")
        world = initialize_world()

        original_player_location = player["location"]
        original_world_location = world["current_location"]

        # Try invalid movement
        with patch("builtins.print"):
            perform_action(player, world, "go nonexistent")

        # State should be unchanged
        assert player["location"] == original_player_location
        assert world["current_location"] == original_world_location


class TestInventoryWorldIntegration:
    """Test inventory and world item interactions."""

    def test_take_item_complete_flow(self):
        """Test complete flow of taking an item from world to inventory."""
        player = create_player("TestPlayer")
        world = initialize_world()

        # Ensure there's an item to take
        world["locations"]["Village"]["items"] = ["map", "bread"]
        initial_world_items = len(world["locations"]["Village"]["items"])
        initial_inventory_size = len(player["inventory"])

        with patch("builtins.print"):
            perform_action(player, world, "take map")

        # Item should be moved from world to inventory
        assert "map" in player["inventory"]
        assert "map" not in world["locations"]["Village"]["items"]
        assert len(player["inventory"]) == initial_inventory_size + 1
        assert len(world["locations"]["Village"]["items"]) == initial_world_items - 1

    def test_drop_item_complete_flow(self):
        """Test complete flow of dropping an item from inventory to world."""
        player = create_player("TestPlayer")
        world = initialize_world()

        # Give player an item
        player["inventory"] = ["sword"]
        initial_world_items = len(world["locations"]["Village"]["items"])

        with patch("builtins.print"):
            perform_action(player, world, "drop sword")

        # Item should be moved from inventory to world
        assert "sword" not in player["inventory"]
        assert "sword" in world["locations"]["Village"]["items"]
        assert len(world["locations"]["Village"]["items"]) == initial_world_items + 1

    def test_use_item_affects_player_and_world(self):
        """Test that using items can affect both player and world state."""
        player = create_player("TestPlayer")
        world = initialize_world()
        player["inventory"] = ["bread"]
        player["health"] = 50

        with patch("builtins.print"):
            perform_action(player, world, "use bread")

        # Bread should heal player and be removed from inventory
        assert player["health"] > 50
        assert "bread" not in player["inventory"]


class TestLocationTransitionIntegration:
    """Test transitions between different locations."""

    def test_village_to_forest_transition(self):
        """Test complete transition from Village to Forest."""
        player = create_player("TestPlayer")
        world = initialize_world()

        with patch("builtins.print"):
            # Start in Village, move to Forest
            perform_action(player, world, "go forest")

            # Verify we're in Forest
            assert player["location"] == "Forest"
            assert world["current_location"] == "Forest"

            # Should be able to interact with Forest
            with patch("locations.forest.enter_forest") as mock_forest:
                perform_action(player, world, "interact")
                mock_forest.assert_called_once()

    def test_forest_to_cave_transition(self):
        """Test transition from Forest to Cave."""
        player = create_player("TestPlayer")
        world = initialize_world()

        with patch("builtins.print"):
            # Village -> Forest -> Cave
            perform_action(player, world, "go forest")
            perform_action(player, world, "go cave")

            assert player["location"] == "Cave"
            assert world["current_location"] == "Cave"

    def test_complete_world_exploration(self):
        """Test exploring all locations in the world."""
        player = create_player("TestPlayer")
        world = initialize_world()

        visited_locations = set()

        with patch("builtins.print"):
            # Start in Village
            visited_locations.add(player["location"])

            # Go to Forest
            perform_action(player, world, "go forest")
            visited_locations.add(player["location"])

            # Go to Cave
            perform_action(player, world, "go cave")
            visited_locations.add(player["location"])

            # Back to Forest
            perform_action(player, world, "go forest")

            # Back to Village
            perform_action(player, world, "go village")

            # Go to Mountain
            perform_action(player, world, "go mountain")
            visited_locations.add(player["location"])

        # Should have visited all major locations
        expected_locations = {"Village", "Forest", "Cave", "Mountain"}
        assert visited_locations == expected_locations


class TestGameStateConsistency:
    """Test that game state remains consistent across operations."""

    def test_player_health_consistency(self):
        """Test that player health remains consistent across actions."""
        player = create_player("TestPlayer")
        world = initialize_world()

        initial_health = player["health"]

        with patch("builtins.print"):
            # Perform various actions that shouldn't affect health
            perform_action(player, world, "look")
            perform_action(player, world, "inventory")
            perform_action(player, world, "go forest")
            perform_action(player, world, "go village")

        # Health should remain unchanged
        assert player["health"] == initial_health

    def test_world_location_consistency(self):
        """Test that world location stays consistent with player location."""
        player = create_player("TestPlayer")
        world = initialize_world()

        locations_to_visit = [
            "Forest",
            "Cave",
            "Forest",
            "Village",
            "Mountain",
            "Village",
        ]

        with patch("builtins.print"):
            for location in locations_to_visit:
                perform_action(player, world, f"go {location.lower()}")

                # Player and world should always be in sync
                if player["location"] == location:  # If movement was successful
                    assert world["current_location"] == player["location"]

    def test_inventory_consistency_across_locations(self):
        """Test that inventory remains consistent when moving between locations."""
        player = create_player("TestPlayer")
        world = initialize_world()

        # Give player some items
        player["inventory"] = ["map", "bread", "stick"]
        original_inventory = player["inventory"].copy()

        with patch("builtins.print"):
            # Move around
            perform_action(player, world, "go forest")
            perform_action(player, world, "go cave")
            perform_action(player, world, "go forest")
            perform_action(player, world, "go village")

        # Inventory should remain unchanged
        assert player["inventory"] == original_inventory


class TestActionChaining:
    """Test chaining multiple actions together."""

    def test_explore_and_collect_items(self):
        """Test exploring locations and collecting items."""
        player = create_player("TestPlayer")
        world = initialize_world()

        with patch("builtins.print"):
            # Look around starting location
            perform_action(player, world, "look")

            # Take items from Village
            perform_action(player, world, "take map")
            perform_action(player, world, "take bread")

            # Move to Forest
            perform_action(player, world, "go forest")

            # Take items from Forest
            perform_action(player, world, "take stick")
            perform_action(player, world, "take berries")

            # Check inventory
            perform_action(player, world, "inventory")

        # Should have collected items from both locations
        expected_items = {"map", "bread", "stick", "berries"}
        assert set(player["inventory"]) == expected_items

    def test_use_items_in_different_locations(self):
        """Test using items in different locations for different effects."""
        player = create_player("TestPlayer")
        world = initialize_world()
        player["inventory"] = ["stick", "torch"]

        with patch("builtins.print"):
            # Use stick in Village (should have no special effect)
            perform_action(player, world, "use stick")

            # Move to Forest and use stick (should find gold coin)
            perform_action(player, world, "go forest")
            with patch("game.player.add_item_to_inventory") as mock_add:
                perform_action(player, world, "use stick")
                mock_add.assert_called_with(player, "gold_coin")

            # Move to Cave and use torch (should light up cave)
            perform_action(player, world, "go cave")
            original_description = world["locations"]["Cave"]["description"]
            perform_action(player, world, "use torch")
            # Description should be modified
            assert world["locations"]["Cave"]["description"] != original_description


class TestErrorHandlingIntegration:
    """Test error handling across integrated systems."""

    def test_invalid_actions_dont_break_state(self):
        """Test that invalid actions don't break game state."""
        player = create_player("TestPlayer")
        world = initialize_world()

        original_player = player.copy()
        original_world_location = world["current_location"]

        with patch("builtins.print"):
            # Try various invalid actions
            perform_action(player, world, "invalid_command")
            perform_action(player, world, "go nowhere")
            perform_action(player, world, "take nothing")
            perform_action(player, world, "use nonexistent")

        # Game state should be preserved
        assert player["name"] == original_player["name"]
        assert player["health"] == original_player["health"]
        assert player["location"] == original_player["location"]
        assert world["current_location"] == original_world_location

    def test_edge_case_item_operations(self):
        """Test edge cases in item operations."""
        player = create_player("TestPlayer")
        world = initialize_world()

        with patch("builtins.print"):
            # Try to take item that doesn't exist
            perform_action(player, world, "take nonexistent")

            # Try to drop item not in inventory
            perform_action(player, world, "drop nonexistent")

            # Try to use item not in inventory
            perform_action(player, world, "use nonexistent")

        # Player should still be in valid state
        assert player["health"] > 0
        assert player["location"] in world["locations"]
        assert isinstance(player["inventory"], list)


class TestMainGameLoop:
    """Test the main game loop integration."""

    @patch("builtins.input")
    @patch("builtins.print")
    def test_main_game_loop_new_game(self, mock_print, mock_input):
        """Test main game loop with new game."""
        # Simulate user input: new game, look around, quit
        mock_input.side_effect = ["n", "look", "quit"]

        with patch("utils.save_load.save_game") as mock_save:
            main()
            mock_save.assert_called_once()

    @patch("builtins.input")
    @patch("builtins.print")
    @patch("utils.save_load.list_save_files")
    def test_main_game_loop_no_save_files(
        self, mock_list_saves, mock_print, mock_input
    ):
        """Test main game loop when no save files exist."""
        mock_list_saves.return_value = []
        mock_input.side_effect = ["y", "quit"]  # Try to load, then quit

        with patch("utils.save_load.save_game"):
            main()

        # Should have checked for save files
        mock_list_saves.assert_called_once()

    @patch("builtins.input")
    @patch("builtins.print")
    def test_main_game_loop_help_command(self, mock_print, mock_input):
        """Test main game loop with help command."""
        mock_input.side_effect = ["n", "help", "quit"]

        with patch("utils.save_load.save_game"), patch(
            "utils.text_formatting.print_help"
        ) as mock_help:
            main()
            mock_help.assert_called_once()
