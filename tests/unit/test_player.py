"""
Unit tests for the player module.
"""

from unittest.mock import call, patch

import pytest

from game.player import (add_item_to_inventory, create_player, damage_player,
                         get_player_status, heal_player, move_player,
                         remove_item_from_inventory)


class TestCreatePlayer:
    """Test player creation functionality."""

    def test_create_player_with_name(self):
        """Test creating a player with a given name."""
        player = create_player("Kevin")

        assert player["name"] == "Kevin"
        assert player["health"] == 100
        assert player["inventory"] == []
        assert player["location"] == "Village"
        assert player["gold"] == 100

    def test_create_player_with_different_name(self):
        """Test creating a player with a different name."""
        player = create_player("Alice")

        assert player["name"] == "Alice"
        assert player["health"] == 100

    def test_create_player_with_empty_name(self):
        """Test creating a player with an empty name."""
        player = create_player("")

        assert player["name"] == ""
        assert player["health"] == 100

    def test_create_player_with_special_characters(self):
        """Test creating a player with special characters in name."""
        player = create_player("Test-Player_123")

        assert player["name"] == "Test-Player_123"


class TestGetPlayerStatus:
    """Test player status display functionality."""

    def test_get_player_status_empty_inventory(self, sample_player):
        """Test status display with empty inventory."""
        status = get_player_status(sample_player)

        assert "Health: 100" in status
        assert "Inventory: empty" in status
        assert "Gold: 100" in status

    def test_get_player_status_with_items(self, player_with_items):
        """Test status display with items in inventory."""
        status = get_player_status(player_with_items)

        assert "Health: 100" in status
        assert "map" in status
        assert "bread" in status
        assert "Gold: 150" in status

    def test_get_player_status_damaged_player(self, damaged_player):
        """Test status display with damaged player."""
        status = get_player_status(damaged_player)

        assert "Health: 50" in status


class TestAddItemToInventory:
    """Test adding items to player inventory."""

    @patch("builtins.print")
    def test_add_item_to_empty_inventory(self, mock_print, sample_player):
        """Test adding an item to an empty inventory."""
        add_item_to_inventory(sample_player, "sword")

        assert "sword" in sample_player["inventory"]
        assert len(sample_player["inventory"]) == 1
        mock_print.assert_called_once_with("You picked up: sword")

    @patch("builtins.print")
    def test_add_multiple_items(self, mock_print, sample_player):
        """Test adding multiple items to inventory."""
        add_item_to_inventory(sample_player, "sword")
        add_item_to_inventory(sample_player, "shield")

        assert "sword" in sample_player["inventory"]
        assert "shield" in sample_player["inventory"]
        assert len(sample_player["inventory"]) == 2

    @patch("builtins.print")
    def test_add_duplicate_items(self, mock_print, sample_player):
        """Test adding duplicate items to inventory."""
        add_item_to_inventory(sample_player, "bread")
        add_item_to_inventory(sample_player, "bread")

        assert sample_player["inventory"].count("bread") == 2

    @patch("builtins.print")
    def test_add_item_to_existing_inventory(self, mock_print, player_with_items):
        """Test adding an item to an inventory that already has items."""
        initial_count = len(player_with_items["inventory"])
        add_item_to_inventory(player_with_items, "new_item")

        assert "new_item" in player_with_items["inventory"]
        assert len(player_with_items["inventory"]) == initial_count + 1


class TestRemoveItemFromInventory:
    """Test removing items from player inventory."""

    @patch("builtins.print")
    def test_remove_existing_item(self, mock_print, player_with_items):
        """Test removing an item that exists in inventory."""
        result = remove_item_from_inventory(player_with_items, "map")

        assert result is True
        assert "map" not in player_with_items["inventory"]
        mock_print.assert_called_once_with("You dropped: map")

    @patch("builtins.print")
    def test_remove_nonexistent_item(self, mock_print, player_with_items):
        """Test removing an item that doesn't exist in inventory."""
        result = remove_item_from_inventory(player_with_items, "nonexistent")

        assert result is None
        mock_print.assert_called_once_with(
            "You don't have nonexistent in your inventory."
        )

    @patch("builtins.print")
    def test_remove_item_from_empty_inventory(self, mock_print, sample_player):
        """Test removing an item from an empty inventory."""
        result = remove_item_from_inventory(sample_player, "sword")

        assert result is None
        mock_print.assert_called_once_with("You don't have sword in your inventory.")

    @patch("builtins.print")
    def test_remove_duplicate_item(self, mock_print, sample_player):
        """Test removing one instance of a duplicate item."""
        sample_player["inventory"] = ["bread", "bread", "map"]

        result = remove_item_from_inventory(sample_player, "bread")

        assert result is True
        assert sample_player["inventory"].count("bread") == 1
        assert "map" in sample_player["inventory"]


class TestMovePlayer:
    """Test player movement functionality."""

    @patch("builtins.print")
    def test_move_player_to_new_location(self, mock_print, sample_player):
        """Test moving player to a new location."""
        move_player(sample_player, "Forest")

        assert sample_player["location"] == "Forest"
        mock_print.assert_called_once_with("You moved to: Forest")

    @patch("builtins.print")
    def test_move_player_multiple_times(self, mock_print, sample_player):
        """Test moving player multiple times."""
        move_player(sample_player, "Forest")
        move_player(sample_player, "Cave")

        assert sample_player["location"] == "Cave"
        expected_calls = [call("You moved to: Forest"), call("You moved to: Cave")]
        mock_print.assert_has_calls(expected_calls)


class TestHealPlayer:
    """Test player healing functionality."""

    @patch("builtins.print")
    def test_heal_damaged_player(self, mock_print, damaged_player):
        """Test healing a damaged player."""
        heal_player(damaged_player, 30)

        assert damaged_player["health"] == 80
        mock_print.assert_called_once_with(
            "You healed for 30 health. Current health: 80"
        )

    @patch("builtins.print")
    def test_heal_player_to_max_health(self, mock_print, damaged_player):
        """Test healing a player beyond max health."""
        heal_player(damaged_player, 100)

        assert damaged_player["health"] == 100
        mock_print.assert_called_once_with(
            "You healed for 100 health. Current health: 100"
        )

    @patch("builtins.print")
    def test_heal_healthy_player(self, mock_print, sample_player):
        """Test healing a player already at full health."""
        heal_player(sample_player, 20)

        assert sample_player["health"] == 100
        mock_print.assert_called_once_with(
            "You healed for 20 health. Current health: 100"
        )

    @patch("builtins.print")
    def test_heal_with_zero_amount(self, mock_print, damaged_player):
        """Test healing with zero amount."""
        initial_health = damaged_player["health"]
        heal_player(damaged_player, 0)

        assert damaged_player["health"] == initial_health
        mock_print.assert_called_once_with(
            f"You healed for 0 health. Current health: {initial_health}"
        )


class TestDamagePlayer:
    """Test player damage functionality."""

    @patch("builtins.print")
    def test_damage_healthy_player(self, mock_print, sample_player):
        """Test damaging a healthy player."""
        damage_player(sample_player, 30)

        assert sample_player["health"] == 70
        mock_print.assert_called_once_with("You took 30 damage. Current health: 70")

    @patch("builtins.print")
    @patch("game.player.print_game_over")
    def test_damage_player_to_death(self, mock_game_over, mock_print, sample_player):
        """Test damaging a player to death."""
        damage_player(sample_player, 150)

        assert sample_player["health"] == 0
        mock_print.assert_any_call("You took 150 damage. Current health: 0")
        mock_print.assert_any_call("You have been defeated.")
        mock_game_over.assert_called_once()

    @patch("builtins.print")
    @patch("game.player.print_game_over")
    def test_damage_player_exactly_to_zero(
        self, mock_game_over, mock_print, sample_player
    ):
        """Test damaging a player exactly to zero health."""
        damage_player(sample_player, 100)

        assert sample_player["health"] == 0
        mock_game_over.assert_called_once()

    @patch("builtins.print")
    def test_damage_with_zero_amount(self, mock_print, sample_player):
        """Test damaging with zero amount."""
        initial_health = sample_player["health"]
        damage_player(sample_player, 0)

        assert sample_player["health"] == initial_health
        mock_print.assert_called_once_with("You took 0 damage. Current health: 100")

    @patch("builtins.print")
    def test_damage_already_dead_player(self, mock_print, sample_player):
        """Test damaging a player who is already dead."""
        sample_player["health"] = 0
        damage_player(sample_player, 10)

        assert sample_player["health"] == 0
