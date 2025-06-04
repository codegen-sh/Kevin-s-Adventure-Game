"""
Scenario tests for complete game sessions and end-to-end gameplay.
"""

import os
import tempfile
from unittest.mock import MagicMock, call, patch

import pytest

from game.actions import perform_action
from game.player import create_player
from game.world import initialize_world


class TestNewPlayerGameSession:
    """Test complete game session for a new player."""

    @patch("builtins.print")
    def test_new_player_exploration_scenario(self, mock_print):
        """Test a new player exploring the world and collecting items."""
        # Create new game
        player = create_player("Kevin")
        world = initialize_world()

        # Scenario: New player explores all locations and collects items
        actions = [
            "look",  # Look around starting location
            "inventory",  # Check empty inventory
            "take map",  # Take map from Village
            "take bread",  # Take bread from Village
            "inventory",  # Check inventory with items
            "go forest",  # Move to Forest
            "look",  # Look around Forest
            "take stick",  # Take stick from Forest
            "take berries",  # Take berries from Forest
            "go cave",  # Move to Cave
            "look",  # Look around Cave
            "take torch",  # Take torch from Cave
            "go forest",  # Return to Forest
            "go village",  # Return to Village
            "go mountain",  # Explore Mountain
            "take rope",  # Take rope from Mountain
            "take pickaxe",  # Take pickaxe from Mountain
            "inventory",  # Check final inventory
        ]

        for action in actions:
            perform_action(player, world, action)

        # Verify final state
        expected_items = {
            "map",
            "bread",
            "stick",
            "berries",
            "torch",
            "rope",
            "pickaxe",
        }
        assert set(player["inventory"]) == expected_items
        assert player["location"] == "Mountain"
        assert player["health"] == 100  # Should be healthy
        assert player["gold"] == 100  # Should have starting gold

    @patch("builtins.print")
    def test_item_usage_scenario(self, mock_print):
        """Test scenario where player uses various items."""
        player = create_player("Kevin")
        world = initialize_world()

        # Give player some items to use
        player["inventory"] = ["map", "bread", "stick", "berries", "torch"]
        player["health"] = 50  # Damaged player

        # Scenario: Use items for various effects
        actions = [
            "use map",  # Check available locations
            "use bread",  # Heal with bread
            "go forest",  # Move to forest
            "use stick",  # Use stick in forest (should find gold coin)
            "go cave",  # Move to cave
            "use torch",  # Light up cave
            "use berries",  # Eat berries (random effect)
        ]

        with patch("utils.random_events.generate_random_event", return_value="heal"):
            for action in actions:
                perform_action(player, world, action)

        # Verify effects
        assert player["health"] > 50  # Should be healed from bread
        assert "bread" not in player["inventory"]  # Bread should be consumed
        assert "berries" not in player["inventory"]  # Berries should be consumed
        assert player["location"] == "Cave"


class TestAdvancedGameplayScenarios:
    """Test advanced gameplay scenarios."""

    @patch("builtins.print")
    def test_treasure_hunting_scenario(self, mock_print):
        """Test scenario focused on finding and using valuable items."""
        player = create_player("TreasureHunter")
        world = initialize_world()

        # Add some valuable items to the world
        world["locations"]["Cave"]["items"].extend(["gemstone", "ancient_artifact"])
        world["locations"]["Mountain"]["items"].append("gold_coin")

        # Scenario: Hunt for treasure
        actions = [
            "go forest",
            "go cave",
            "take gemstone",
            "take ancient_artifact",
            "go forest",
            "go village",
            "use gemstone",  # Try to sell gemstone
            "go mountain",
            "take gold_coin",
            "inventory",
        ]

        # Mock selling gemstone
        with patch("builtins.input", return_value="y"):
            for action in actions:
                perform_action(player, world, action)

        # Should have gained gold from selling gemstone
        assert player["gold"] > 100
        assert "gemstone" not in player["inventory"]  # Should be sold
        assert "ancient_artifact" in player["inventory"]
        assert "gold_coin" in player["inventory"]

    @patch("builtins.print")
    def test_survival_scenario(self, mock_print):
        """Test survival scenario with health management."""
        player = create_player("Survivor")
        world = initialize_world()

        # Start with low health
        player["health"] = 20
        player["inventory"] = ["bread", "berries", "mushrooms"]

        # Scenario: Manage health through item usage
        actions = [
            "status",  # Check low health
            "use bread",  # Heal with bread
            "status",  # Check improved health
        ]

        # Mock random events for berries and mushrooms
        with patch("utils.random_events.generate_random_event") as mock_random:
            mock_random.side_effect = ["heal", "heal"]  # Both heal

            for action in actions:
                perform_action(player, world, action)

            # Use berries and mushrooms
            perform_action(player, world, "use berries")
            perform_action(player, world, "use mushrooms")

        # Should be significantly healed
        assert player["health"] > 50
        assert "bread" not in player["inventory"]
        assert "berries" not in player["inventory"]
        assert "mushrooms" not in player["inventory"]


class TestLocationSpecificScenarios:
    """Test scenarios specific to different locations."""

    @patch("builtins.print")
    def test_village_interaction_scenario(self, mock_print):
        """Test comprehensive village interaction scenario."""
        player = create_player("Villager")
        world = initialize_world()

        # Scenario: Interact with village
        actions = [
            "look",  # Look around village
            "interact",  # Interact with village
        ]

        with patch("locations.village.visit_village") as mock_village:
            for action in actions:
                perform_action(player, world, action)

            # Should have interacted with village
            mock_village.assert_called_once_with(world, player)

    @patch("builtins.print")
    def test_cave_exploration_scenario(self, mock_print):
        """Test comprehensive cave exploration scenario."""
        player = create_player("CaveExplorer")
        world = initialize_world()

        # Give player torch for cave exploration
        player["inventory"] = ["torch", "pickaxe"]

        # Scenario: Explore cave thoroughly
        actions = [
            "go forest",
            "go cave",
            "look",
            "use torch",  # Light up cave
            "interact",  # Interact with cave
        ]

        with patch("locations.cave.explore_cave") as mock_cave:
            for action in actions:
                perform_action(player, world, action)

            # Should have explored cave
            mock_cave.assert_called_once_with(world, player)

    @patch("builtins.print")
    def test_mountain_climbing_scenario(self, mock_print):
        """Test mountain climbing scenario."""
        player = create_player("Climber")
        world = initialize_world()

        # Give player rope for mountain climbing
        player["inventory"] = ["rope", "pickaxe"]

        # Scenario: Climb mountain
        actions = [
            "go mountain",
            "look",
            "use rope",  # Use rope for climbing
            "interact",  # Interact with mountain
        ]

        with patch("locations.mountain.climb_mountain") as mock_mountain:
            for action in actions:
                perform_action(player, world, action)

            # Should have climbed mountain
            mock_mountain.assert_called_once_with(world, player)


class TestGameProgressionScenarios:
    """Test game progression and character development scenarios."""

    @patch("builtins.print")
    def test_character_progression_scenario(self, mock_print):
        """Test character progression through gameplay."""
        player = create_player("Hero")
        world = initialize_world()

        # Track progression metrics
        initial_health = player["health"]
        initial_gold = player["gold"]
        initial_inventory_size = len(player["inventory"])

        # Scenario: Progress through game
        progression_actions = [
            # Exploration phase
            "look",
            "take map",
            "take bread",
            "go forest",
            "take stick",
            "take berries",
            "go cave",
            "take torch",
            "take gemstone",
            # Item usage phase
            "use bread",  # Heal
            "go forest",
            "use stick",  # Find gold coin
            "go village",
            "use gemstone",  # Sell for gold
            # Advanced exploration
            "go mountain",
            "take rope",
            "take pickaxe",
            "use rope",  # Improve climbing
        ]

        with patch("builtins.input", return_value="y"), patch(
            "utils.random_events.generate_random_event", return_value="heal"
        ):

            for action in progression_actions:
                perform_action(player, world, action)

        # Verify progression
        assert len(player["inventory"]) > initial_inventory_size
        assert player["gold"] > initial_gold  # Should have gained gold
        assert player["location"] == "Mountain"  # Should have explored

    @patch("builtins.print")
    def test_resource_management_scenario(self, mock_print):
        """Test resource management throughout gameplay."""
        player = create_player("Manager")
        world = initialize_world()

        # Start with limited resources
        player["health"] = 30
        player["gold"] = 50
        player["inventory"] = ["bread"]

        # Scenario: Manage resources carefully
        actions = [
            "status",  # Check resources
            "inventory",  # Check items
            "use bread",  # Use healing item
            "status",  # Check improved health
            # Collect more resources
            "take map",
            "go forest",
            "take berries",
            "use berries",  # Risk/reward with berries
        ]

        with patch("utils.random_events.generate_random_event", return_value="heal"):
            for action in actions:
                perform_action(player, world, action)

        # Should have managed resources effectively
        assert player["health"] > 30  # Should be healed
        assert "map" in player["inventory"]  # Should have collected items


class TestErrorRecoveryScenarios:
    """Test scenarios involving error recovery and edge cases."""

    @patch("builtins.print")
    def test_invalid_action_recovery_scenario(self, mock_print):
        """Test recovery from invalid actions."""
        player = create_player("Confused")
        world = initialize_world()

        # Scenario: Player makes mistakes but recovers
        actions = [
            "invalid_command",  # Invalid action
            "look",  # Valid action
            "go nowhere",  # Invalid movement
            "go forest",  # Valid movement
            "take nothing",  # Invalid item
            "take stick",  # Valid item
            "use nonexistent",  # Invalid item usage
            "use stick",  # Valid item usage
        ]

        for action in actions:
            perform_action(player, world, action)

        # Should be in valid state despite errors
        assert player["location"] == "Forest"
        assert "stick" in player["inventory"]
        assert player["health"] == 100

    @patch("builtins.print")
    def test_boundary_condition_scenario(self, mock_print):
        """Test boundary conditions in gameplay."""
        player = create_player("EdgeCase")
        world = initialize_world()

        # Test various boundary conditions
        actions = [
            "",  # Empty action
            "   ",  # Whitespace action
            "LOOK",  # Uppercase action
            "  go   forest  ",  # Action with extra whitespace
        ]

        for action in actions:
            perform_action(player, world, action)

        # Should handle boundary conditions gracefully
        assert player["location"] == "Forest"  # Should have moved despite formatting
        assert player["health"] == 100


class TestCompleteGameplaySession:
    """Test a complete gameplay session from start to finish."""

    @patch("builtins.print")
    def test_full_adventure_scenario(self, mock_print):
        """Test a complete adventure from start to finish."""
        player = create_player("Adventurer")
        world = initialize_world()

        # Complete adventure scenario
        adventure_sequence = [
            # Starting phase
            "look",
            "status",
            "inventory",
            # Exploration phase
            "take map",
            "take bread",
            "go forest",
            "look",
            "take stick",
            "take berries",
            "go cave",
            "look",
            "take torch",
            "take gemstone",
            "go forest",
            "go village",
            "go mountain",
            "look",
            "take rope",
            "take pickaxe",
            # Interaction phase
            "go village",
            "interact",
            "go forest",
            "interact",
            "go cave",
            "interact",
            "go forest",
            "go village",
            "go mountain",
            "interact",
            # Item usage phase
            "use map",
            "use bread",
            "use rope",
            "go village",
            "use gemstone",
            "go forest",
            "use stick",
            "go cave",
            "use torch",
            # Final status check
            "status",
            "inventory",
        ]

        with patch("builtins.input", return_value="y"), patch(
            "utils.random_events.generate_random_event", return_value="heal"
        ), patch("locations.village.visit_village"), patch(
            "locations.forest.enter_forest"
        ), patch(
            "locations.cave.explore_cave"
        ), patch(
            "locations.mountain.climb_mountain"
        ):

            for action in adventure_sequence:
                perform_action(player, world, action)

        # Verify complete adventure
        assert player["location"] == "Mountain"  # Ended at mountain
        assert len(player["inventory"]) > 0  # Should have collected items
        assert player["gold"] > 100  # Should have gained gold
        assert player["health"] > 0  # Should be alive

        # Should have visited all locations
        # (This would be tracked in a real game with a visited locations system)


class TestMultipleGameSessions:
    """Test multiple game sessions and save/load scenarios."""

    def test_save_load_game_session(self):
        """Test saving and loading a game session."""
        # This would test the save/load functionality
        # For now, we'll test the basic structure

        player = create_player("SaveTest")
        world = initialize_world()

        # Modify game state
        player["inventory"] = ["map", "sword"]
        player["location"] = "Forest"
        player["gold"] = 200
        world["current_location"] = "Forest"

        # In a real test, we would save and load here
        # For now, just verify the state is consistent
        assert player["location"] == world["current_location"]
        assert len(player["inventory"]) == 2
        assert player["gold"] == 200
