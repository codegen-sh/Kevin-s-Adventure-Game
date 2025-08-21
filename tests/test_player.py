"""
Tests for the player module.
"""

import unittest

from game.player import Player


class TestPlayer(unittest.TestCase):
    """Test cases for the Player class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.player = Player("TestPlayer", health=100, inventory=["sword", "potion"], location="Village", gold=50)
    
    def test_initialization(self):
        """Test player initialization."""
        self.assertEqual(self.player.name, "TestPlayer")
        self.assertEqual(self.player.health, 100)
        self.assertEqual(self.player.inventory, ["sword", "potion"])
        self.assertEqual(self.player.location, "Village")
        self.assertEqual(self.player.gold, 50)
    
    def test_get_status(self):
        """Test get_status method."""
        status = self.player.get_status()
        self.assertIn("Health: 100", status)
        self.assertIn("Inventory: sword, potion", status)
        self.assertIn("Gold: 50", status)
    
    def test_add_item(self):
        """Test add_item method."""
        self.player.add_item("map")
        self.assertIn("map", self.player.inventory)
        self.assertEqual(len(self.player.inventory), 3)
    
    def test_remove_item(self):
        """Test remove_item method."""
        result = self.player.remove_item("sword")
        self.assertTrue(result)
        self.assertNotIn("sword", self.player.inventory)
        self.assertEqual(len(self.player.inventory), 1)
        
        # Try to remove an item that doesn't exist
        result = self.player.remove_item("axe")
        self.assertFalse(result)
        self.assertEqual(len(self.player.inventory), 1)
    
    def test_move(self):
        """Test move method."""
        self.player.move("Forest")
        self.assertEqual(self.player.location, "Forest")
    
    def test_heal(self):
        """Test heal method."""
        self.player.health = 50
        self.player.heal(20)
        self.assertEqual(self.player.health, 70)
        
        # Test healing beyond max health
        self.player.heal(50)
        self.assertEqual(self.player.health, 100)
    
    def test_take_damage(self):
        """Test take_damage method."""
        self.player.take_damage(30)
        self.assertEqual(self.player.health, 70)
        
        # Test taking damage beyond health
        self.player.take_damage(100)
        self.assertEqual(self.player.health, 0)
    
    def test_has_item(self):
        """Test has_item method."""
        self.assertTrue(self.player.has_item("sword"))
        self.assertFalse(self.player.has_item("axe"))
    
    def test_to_dict(self):
        """Test to_dict method."""
        player_dict = self.player.to_dict()
        self.assertEqual(player_dict["name"], "TestPlayer")
        self.assertEqual(player_dict["health"], 100)
        self.assertEqual(player_dict["inventory"], ["sword", "potion"])
        self.assertEqual(player_dict["location"], "Village")
        self.assertEqual(player_dict["gold"], 50)
    
    def test_from_dict(self):
        """Test from_dict method."""
        player_dict = {
            "name": "DictPlayer",
            "health": 80,
            "inventory": ["map", "bread"],
            "location": "Mountain",
            "gold": 30
        }
        player = Player.from_dict(player_dict)
        self.assertEqual(player.name, "DictPlayer")
        self.assertEqual(player.health, 80)
        self.assertEqual(player.inventory, ["map", "bread"])
        self.assertEqual(player.location, "Mountain")
        self.assertEqual(player.gold, 30)


if __name__ == "__main__":
    unittest.main()

