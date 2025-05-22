"""
Tests for the player module.
"""
import pytest

from kevin_adventure_game.game.player import (
    add_item_to_inventory,
    create_player,
    damage_player,
    get_player_status,
    heal_player,
    move_player,
    remove_item_from_inventory,
)


def test_create_player():
    """Test creating a player."""
    player = create_player("TestPlayer")
    assert player["name"] == "TestPlayer"
    assert player["health"] == 100
    assert player["inventory"] == []
    assert player["location"] == "Village"
    assert player["gold"] == 100


def test_get_player_status():
    """Test getting player status."""
    player = {
        "name": "TestPlayer",
        "health": 80,
        "inventory": ["sword", "potion"],
        "location": "Forest",
        "gold": 50,
    }
    status = get_player_status(player)
    assert "Health: 80" in status
    assert "sword, potion" in status
    assert "Gold: 50" in status


def test_add_item_to_inventory(capsys):
    """Test adding an item to inventory."""
    player = create_player("TestPlayer")
    add_item_to_inventory(player, "sword")
    assert "sword" in player["inventory"]
    captured = capsys.readouterr()
    assert "You picked up: sword" in captured.out


def test_remove_item_from_inventory(capsys):
    """Test removing an item from inventory."""
    player = create_player("TestPlayer")
    player["inventory"] = ["sword", "potion"]
    
    # Test removing an item that exists
    result = remove_item_from_inventory(player, "sword")
    assert result is True
    assert "sword" not in player["inventory"]
    captured = capsys.readouterr()
    assert "You dropped: sword" in captured.out
    
    # Test removing an item that doesn't exist
    result = remove_item_from_inventory(player, "axe")
    assert result is False
    captured = capsys.readouterr()
    assert "You don't have axe in your inventory" in captured.out


def test_move_player(capsys):
    """Test moving the player."""
    player = create_player("TestPlayer")
    move_player(player, "Forest")
    assert player["location"] == "Forest"
    captured = capsys.readouterr()
    assert "You moved to: Forest" in captured.out


def test_heal_player(capsys):
    """Test healing the player."""
    player = create_player("TestPlayer")
    player["health"] = 50
    
    # Test normal healing
    heal_player(player, 20)
    assert player["health"] == 70
    captured = capsys.readouterr()
    assert "You healed for 20 health" in captured.out
    
    # Test healing beyond max health
    heal_player(player, 40)
    assert player["health"] == 100  # Should cap at 100
    captured = capsys.readouterr()
    assert "You healed for 40 health" in captured.out


def test_damage_player(capsys):
    """Test damaging the player."""
    player = create_player("TestPlayer")
    
    # Test normal damage
    damage_player(player, 30)
    assert player["health"] == 70
    captured = capsys.readouterr()
    assert "You took 30 damage" in captured.out
    
    # Test fatal damage
    damage_player(player, 80)
    assert player["health"] == 0  # Should not go below 0
    captured = capsys.readouterr()
    assert "You took 80 damage" in captured.out
    assert "You have been defeated" in captured.out

