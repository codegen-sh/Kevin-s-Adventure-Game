"""
Unit tests for player module.
"""
import unittest
from game.player import (
    create_player,
    get_player_status,
    add_item_to_inventory,
    remove_item_from_inventory,
    move_player,
    heal_player,
    damage_player
)
from game.constants import DEFAULT_HEALTH, DEFAULT_GOLD, MAX_HEALTH, MIN_HEALTH


class TestPlayer(unittest.TestCase):
    """Test cases for player functionality."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.player = create_player("TestPlayer")
    
    def test_create_player(self):
        """Test player creation."""
        player = create_player("Kevin")
        
        self.assertEqual(player["name"], "Kevin")
        self.assertEqual(player["health"], DEFAULT_HEALTH)
        self.assertEqual(player["gold"], DEFAULT_GOLD)
        self.assertEqual(player["inventory"], [])
        self.assertEqual(player["location"], "Village")
    
    def test_get_player_status(self):
        """Test player status display."""
        status = get_player_status(self.player)
        
        self.assertIn("Health:", status)
        self.assertIn("Gold:", status)
        self.assertIn("Items:", status)
    
    def test_add_item_to_inventory(self):
        """Test adding items to inventory."""
        result = add_item_to_inventory(self.player, "sword")
        
        self.assertTrue(result)
        self.assertIn("sword", self.player["inventory"])
    
    def test_remove_item_from_inventory(self):
        """Test removing items from inventory."""
        # Add item first
        add_item_to_inventory(self.player, "sword")
        
        # Remove it
        result = remove_item_from_inventory(self.player, "sword")
        
        self.assertTrue(result)
        self.assertNotIn("sword", self.player["inventory"])
    
    def test_remove_nonexistent_item(self):
        """Test removing item that doesn't exist."""
        result = remove_item_from_inventory(self.player, "nonexistent")
        
        self.assertFalse(result)
    
    def test_move_player(self):
        """Test moving player to new location."""
        move_player(self.player, "Forest")
        
        self.assertEqual(self.player["location"], "Forest")
    
    def test_heal_player(self):
        """Test healing player."""
        # Damage player first
        self.player["health"] = 50
        
        healed = heal_player(self.player, 30)
        
        self.assertEqual(healed, 30)
        self.assertEqual(self.player["health"], 80)
    
    def test_heal_player_max_health(self):
        """Test healing doesn't exceed max health."""
        self.player["health"] = 90
        
        healed = heal_player(self.player, 30)
        
        self.assertEqual(healed, 10)  # Only healed 10 to reach max
        self.assertEqual(self.player["health"], MAX_HEALTH)
    
    def test_damage_player(self):
        """Test damaging player."""
        initial_health = self.player["health"]
        
        damage_player(self.player, 20)
        
        self.assertEqual(self.player["health"], initial_health - 20)
    
    def test_damage_player_min_health(self):
        """Test damage doesn't go below minimum health."""
        damage_player(self.player, 200)  # More than max health
        
        self.assertEqual(self.player["health"], MIN_HEALTH)


if __name__ == "__main__":
    unittest.main()

