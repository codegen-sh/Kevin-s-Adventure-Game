"""
Unit tests for the items module.
"""

from unittest.mock import MagicMock, call, patch

import pytest

from game.items import (add_item_to_world, get_available_items,
                        get_item_description, remove_item_from_world,
                        transfer_item, use_item)


class TestGetItemDescription:
    """Test item description functionality."""

    def test_get_known_item_descriptions(self):
        """Test getting descriptions for known items."""
        known_items = {
            "map": "map",
            "bread": "bread",
            "stick": "stick",
            "berries": "berries",
            "torch": "torch",
            "gemstone": "gemstone",
            "rope": "rope",
            "pickaxe": "pickaxe",
            "sword": "sword",
        }

        for item, expected_keyword in known_items.items():
            description = get_item_description(item)
            assert isinstance(description, str)
            assert len(description) > 0
            assert expected_keyword.lower() in description.lower()

    def test_get_unknown_item_description(self):
        """Test getting description for unknown item."""
        description = get_item_description("unknown_item")
        assert description == "A mysterious item."

    def test_get_empty_item_description(self):
        """Test getting description for empty item name."""
        description = get_item_description("")
        assert description == "A mysterious item."

    def test_get_none_item_description(self):
        """Test getting description for None item."""
        description = get_item_description(None)
        assert description == "A mysterious item."


class TestUseItem:
    """Test item usage functionality."""

    def test_use_item_not_in_inventory(self, sample_player, sample_world):
        """Test using an item not in inventory."""
        result = use_item(sample_player, "sword", sample_world)
        assert result is False

    @patch("builtins.print")
    @patch("game.world.get_available_locations")
    def test_use_map(
        self, mock_get_available, mock_print, player_with_items, sample_world
    ):
        """Test using a map item."""
        mock_get_available.return_value = ["Forest", "Mountain"]

        result = use_item(player_with_items, "map", sample_world)

        assert result is True
        mock_print.assert_any_call(
            "You consult the map. It shows the following locations you can go to:"
        )
        mock_print.assert_any_call("- Forest")
        mock_print.assert_any_call("- Mountain")

    @patch("builtins.print")
    @patch("game.player.heal_player")
    @patch("game.player.remove_item_from_inventory")
    def test_use_bread(
        self, mock_remove, mock_heal, mock_print, player_with_items, sample_world
    ):
        """Test using bread item."""
        result = use_item(player_with_items, "bread", sample_world)

        assert result is True
        mock_print.assert_called_with(
            "You eat the bread. It's delicious and restores some health."
        )
        mock_heal.assert_called_once_with(player_with_items, 20)
        mock_remove.assert_called_once_with(player_with_items, "bread")

    @patch("builtins.print")
    @patch("game.player.add_item_to_inventory")
    def test_use_stick_in_forest(
        self, mock_add_item, mock_print, player_with_items, sample_world
    ):
        """Test using stick in forest location."""
        sample_world["current_location"] = "Forest"

        result = use_item(player_with_items, "stick", sample_world)

        assert result is True
        mock_print.assert_any_call(
            "You wave the stick around. It makes a satisfying swoosh sound."
        )
        mock_print.assert_any_call(
            "A nearby bird is startled and drops a shiny object!"
        )
        mock_add_item.assert_called_once_with(player_with_items, "gold_coin")

    @patch("builtins.print")
    def test_use_stick_outside_forest(
        self, mock_print, player_with_items, sample_world
    ):
        """Test using stick outside forest location."""
        sample_world["current_location"] = "Village"

        result = use_item(player_with_items, "stick", sample_world)

        assert result is True
        mock_print.assert_called_once_with(
            "You wave the stick around. It makes a satisfying swoosh sound."
        )

    @patch("builtins.print")
    @patch("game.player.heal_player")
    @patch("game.player.damage_player")
    @patch("game.player.remove_item_from_inventory")
    @patch("utils.random_events.generate_random_event")
    def test_use_berries_heal(
        self,
        mock_random_event,
        mock_remove,
        mock_damage,
        mock_heal,
        mock_print,
        player_with_items,
        sample_world,
    ):
        """Test using berries with healing effect."""
        mock_random_event.return_value = "heal"

        result = use_item(player_with_items, "berries", sample_world)

        assert result is True
        mock_print.assert_any_call("You eat the berries. They're sweet and juicy.")
        mock_print.assert_any_call("You feel refreshed and gain some health.")
        mock_heal.assert_called_once_with(player_with_items, 10)
        mock_remove.assert_called_once_with(player_with_items, "berries")

    @patch("builtins.print")
    @patch("game.player.heal_player")
    @patch("game.player.damage_player")
    @patch("game.player.remove_item_from_inventory")
    @patch("utils.random_events.generate_random_event")
    def test_use_berries_poison(
        self,
        mock_random_event,
        mock_remove,
        mock_damage,
        mock_heal,
        mock_print,
        player_with_items,
        sample_world,
    ):
        """Test using berries with poison effect."""
        mock_random_event.return_value = "poison"

        result = use_item(player_with_items, "berries", sample_world)

        assert result is True
        mock_print.assert_any_call("You eat the berries. They're sweet and juicy.")
        mock_print.assert_any_call(
            "Uh oh, those weren't safe to eat. You lose some health."
        )
        mock_damage.assert_called_once_with(player_with_items, 5)
        mock_remove.assert_called_once_with(player_with_items, "berries")

    @patch("builtins.print")
    def test_use_torch_in_cave(self, mock_print, player_with_items, sample_world):
        """Test using torch in cave."""
        sample_world["current_location"] = "Cave"
        original_description = sample_world["locations"]["Cave"]["description"]

        result = use_item(player_with_items, "torch", sample_world)

        assert result is True
        mock_print.assert_called_with(
            "You light the torch, illuminating the dark cave around you."
        )
        assert sample_world["locations"]["Cave"]["description"] != original_description

    @patch("builtins.print")
    def test_use_torch_outside_cave(self, mock_print, player_with_items, sample_world):
        """Test using torch outside cave."""
        sample_world["current_location"] = "Village"

        result = use_item(player_with_items, "torch", sample_world)

        assert result is True
        mock_print.assert_called_with(
            "You light the torch. It provides warmth and light."
        )

    @patch("builtins.print")
    @patch("builtins.input")
    @patch("game.player.remove_item_from_inventory")
    def test_use_gemstone_sell_in_village(
        self, mock_remove, mock_input, mock_print, player_with_items, sample_world
    ):
        """Test using gemstone and selling it in village."""
        sample_world["current_location"] = "Village"
        mock_input.return_value = "y"
        initial_gold = player_with_items["gold"]

        result = use_item(player_with_items, "gemstone", sample_world)

        assert result is True
        mock_print.assert_any_call(
            "You examine the gemstone closely. It glimmers with an otherworldly light."
        )
        mock_print.assert_any_call(
            "A merchant notices your gemstone and offers to buy it for 50 gold!"
        )
        mock_print.assert_any_call("You sold the gemstone for 50 gold.")
        assert player_with_items["gold"] == initial_gold + 50
        mock_remove.assert_called_once_with(player_with_items, "gemstone")

    @patch("builtins.print")
    @patch("builtins.input")
    def test_use_gemstone_keep_in_village(
        self, mock_input, mock_print, player_with_items, sample_world
    ):
        """Test using gemstone and keeping it in village."""
        sample_world["current_location"] = "Village"
        mock_input.return_value = "n"
        initial_gold = player_with_items["gold"]

        result = use_item(player_with_items, "gemstone", sample_world)

        assert result is True
        mock_print.assert_any_call("You decide to keep the gemstone.")
        assert player_with_items["gold"] == initial_gold

    @patch("builtins.print")
    def test_use_unknown_item(self, mock_print, player_with_items, sample_world):
        """Test using an unknown item."""
        player_with_items["inventory"].append("unknown_item")

        result = use_item(player_with_items, "unknown_item", sample_world)

        assert result is False
        mock_print.assert_called_once_with(
            "You're not sure how to use the unknown_item."
        )


class TestGetAvailableItems:
    """Test getting available items in locations."""

    def test_get_available_items_village(self, sample_world):
        """Test getting available items in Village."""
        items = get_available_items(sample_world, "Village")

        assert isinstance(items, list)
        assert "map" in items
        assert "bread" in items

    def test_get_available_items_forest(self, sample_world):
        """Test getting available items in Forest."""
        items = get_available_items(sample_world, "Forest")

        assert isinstance(items, list)
        assert "stick" in items
        assert "berries" in items

    def test_get_available_items_empty_location(self, empty_world):
        """Test getting available items in location with no items."""
        items = get_available_items(empty_world, "Village")

        assert isinstance(items, list)
        assert len(items) == 0


class TestAddItemToWorld:
    """Test adding items to world locations."""

    @patch("builtins.print")
    def test_add_new_item_to_location(self, mock_print, sample_world):
        """Test adding a new item to a location."""
        initial_items = sample_world["locations"]["Village"]["items"].copy()

        add_item_to_world(sample_world, "Village", "new_item")

        assert "new_item" in sample_world["locations"]["Village"]["items"]
        assert (
            len(sample_world["locations"]["Village"]["items"]) == len(initial_items) + 1
        )
        mock_print.assert_called_once_with("A new_item has been added to Village.")

    @patch("builtins.print")
    def test_add_existing_item_to_location(self, mock_print, sample_world):
        """Test adding an item that already exists in location."""
        initial_items = sample_world["locations"]["Village"]["items"].copy()

        add_item_to_world(sample_world, "Village", "map")  # map already exists

        assert sample_world["locations"]["Village"]["items"] == initial_items
        mock_print.assert_called_once_with("There's already a map in Village.")


class TestRemoveItemFromWorld:
    """Test removing items from world locations."""

    def test_remove_existing_item(self, sample_world):
        """Test removing an existing item from location."""
        result = remove_item_from_world(sample_world, "Village", "map")

        assert result is True
        assert "map" not in sample_world["locations"]["Village"]["items"]

    def test_remove_nonexistent_item(self, sample_world):
        """Test removing a non-existent item from location."""
        result = remove_item_from_world(sample_world, "Village", "nonexistent")

        assert result is False
        # Original items should remain unchanged
        assert "map" in sample_world["locations"]["Village"]["items"]
        assert "bread" in sample_world["locations"]["Village"]["items"]


class TestTransferItem:
    """Test transferring items between inventory and world."""

    @patch("game.player.remove_item_from_inventory")
    def test_transfer_from_inventory_to_world_success(
        self, mock_remove, player_with_items, sample_world
    ):
        """Test successfully transferring item from inventory to world."""
        mock_remove.return_value = True
        sample_world["current_location"] = "Village"
        initial_items = sample_world["locations"]["Village"]["items"].copy()

        result = transfer_item(
            player_with_items, sample_world, "map", from_inventory_to_world=True
        )

        assert result is True
        mock_remove.assert_called_once_with(player_with_items, "map")
        assert "map" in sample_world["locations"]["Village"]["items"]
        assert (
            len(sample_world["locations"]["Village"]["items"]) == len(initial_items) + 1
        )

    @patch("game.player.remove_item_from_inventory")
    def test_transfer_from_inventory_to_world_fail(
        self, mock_remove, player_with_items, sample_world
    ):
        """Test failing to transfer item from inventory to world."""
        mock_remove.return_value = False
        sample_world["current_location"] = "Village"
        initial_items = sample_world["locations"]["Village"]["items"].copy()

        result = transfer_item(
            player_with_items, sample_world, "nonexistent", from_inventory_to_world=True
        )

        assert result is False
        assert sample_world["locations"]["Village"]["items"] == initial_items

    @patch("game.player.add_item_to_inventory")
    def test_transfer_from_world_to_inventory_success(
        self, mock_add, sample_player, sample_world
    ):
        """Test successfully transferring item from world to inventory."""
        sample_world["current_location"] = "Village"

        result = transfer_item(
            sample_player, sample_world, "map", from_inventory_to_world=False
        )

        assert result is True
        mock_add.assert_called_once_with(sample_player, "map")
        assert "map" not in sample_world["locations"]["Village"]["items"]

    def test_transfer_from_world_to_inventory_fail(self, sample_player, sample_world):
        """Test failing to transfer item from world to inventory."""
        sample_world["current_location"] = "Village"
        initial_items = sample_world["locations"]["Village"]["items"].copy()

        result = transfer_item(
            sample_player, sample_world, "nonexistent", from_inventory_to_world=False
        )

        assert result is False
        assert sample_world["locations"]["Village"]["items"] == initial_items


class TestItemIntegrity:
    """Test item system integrity and consistency."""

    def test_all_items_have_descriptions(self):
        """Test that all known items have descriptions."""
        known_items = [
            "map",
            "bread",
            "stick",
            "berries",
            "torch",
            "gemstone",
            "rope",
            "pickaxe",
            "mushrooms",
            "mountain_herbs",
            "ancient_coin",
            "hermit's_blessing",
            "gold_coin",
            "silver_necklace",
            "ancient_artifact",
            "magic_ring",
            "mysterious_potion",
            "sword",
        ]

        for item in known_items:
            description = get_item_description(item)
            assert (
                description != "A mysterious item."
            ), f"Item {item} has no specific description"
            assert len(description) > 10, f"Item {item} has too short description"

    def test_item_descriptions_are_informative(self):
        """Test that item descriptions contain the item name or related keywords."""
        test_items = {
            "map": ["map", "navigate"],
            "bread": ["bread", "food", "eat"],
            "sword": ["sword", "weapon", "combat"],
            "torch": ["torch", "light", "flame"],
            "rope": ["rope", "climb", "tie"],
        }

        for item, keywords in test_items.items():
            description = get_item_description(item).lower()
            assert any(
                keyword in description for keyword in keywords
            ), f"Item {item} description doesn't contain expected keywords: {keywords}"
