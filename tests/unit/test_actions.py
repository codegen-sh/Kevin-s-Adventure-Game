"""
Unit tests for the actions module.
"""

import pytest
from unittest.mock import patch, call, MagicMock

from game.actions import (
    perform_action,
    handle_movement,
    handle_take_item,
    handle_drop_item,
    handle_use_item,
    handle_look,
    handle_inventory,
    handle_status
)


class TestPerformAction:
    """Test the main action dispatcher functionality."""
    
    @patch('game.actions.handle_movement')
    def test_perform_action_go_command(self, mock_handle_movement, sample_player, sample_world):
        """Test performing a 'go' movement command."""
        perform_action(sample_player, sample_world, "go forest")
        
        mock_handle_movement.assert_called_once_with(sample_player, sample_world, "Forest")
    
    @patch('game.actions.handle_movement')
    def test_perform_action_move_command(self, mock_handle_movement, sample_player, sample_world):
        """Test performing a 'move' movement command."""
        perform_action(sample_player, sample_world, "move mountain")
        
        mock_handle_movement.assert_called_once_with(sample_player, sample_world, "Mountain")
    
    @patch('game.actions.handle_take_item')
    def test_perform_action_take_command(self, mock_handle_take, sample_player, sample_world):
        """Test performing a 'take' command."""
        perform_action(sample_player, sample_world, "take sword")
        
        mock_handle_take.assert_called_once_with(sample_player, sample_world, "sword")
    
    @patch('game.actions.handle_take_item')
    def test_perform_action_pick_up_command(self, mock_handle_take, sample_player, sample_world):
        """Test performing a 'pick up' command."""
        perform_action(sample_player, sample_world, "pick up bread")
        
        mock_handle_take.assert_called_once_with(sample_player, sample_world, "bread")
    
    @patch('game.actions.handle_drop_item')
    def test_perform_action_drop_command(self, mock_handle_drop, sample_player, sample_world):
        """Test performing a 'drop' command."""
        perform_action(sample_player, sample_world, "drop map")
        
        mock_handle_drop.assert_called_once_with(sample_player, sample_world, "map")
    
    @patch('game.actions.handle_use_item')
    def test_perform_action_use_command(self, mock_handle_use, sample_player, sample_world):
        """Test performing a 'use' command."""
        perform_action(sample_player, sample_world, "use torch")
        
        mock_handle_use.assert_called_once_with(sample_player, sample_world, "torch")
    
    @patch('game.actions.handle_look')
    def test_perform_action_look_commands(self, mock_handle_look, sample_player, sample_world):
        """Test performing look-related commands."""
        commands = ["look", "examine", "describe"]
        
        for command in commands:
            mock_handle_look.reset_mock()
            perform_action(sample_player, sample_world, command)
            mock_handle_look.assert_called_once_with(sample_player, sample_world)
    
    @patch('game.actions.handle_inventory')
    def test_perform_action_inventory_commands(self, mock_handle_inventory, sample_player, sample_world):
        """Test performing inventory-related commands."""
        commands = ["inventory", "inv", "items"]
        
        for command in commands:
            mock_handle_inventory.reset_mock()
            perform_action(sample_player, sample_world, command)
            mock_handle_inventory.assert_called_once_with(sample_player)
    
    @patch('game.actions.handle_status')
    def test_perform_action_status_commands(self, mock_handle_status, sample_player, sample_world):
        """Test performing status-related commands."""
        commands = ["status", "health", "stats"]
        
        for command in commands:
            mock_handle_status.reset_mock()
            perform_action(sample_player, sample_world, command)
            mock_handle_status.assert_called_once_with(sample_player)
    
    @patch('game.world.interact_with_location')
    def test_perform_action_interact_commands(self, mock_interact, sample_player, sample_world):
        """Test performing interaction commands."""
        commands = ["interact", "explore", "search"]
        
        for command in commands:
            mock_interact.reset_mock()
            perform_action(sample_player, sample_world, command)
            mock_interact.assert_called_once_with(sample_world, sample_player)
    
    @patch('utils.text_formatting.print_invalid_action')
    def test_perform_action_invalid_command(self, mock_print_invalid, sample_player, sample_world):
        """Test performing an invalid command."""
        perform_action(sample_player, sample_world, "invalid_command")
        
        mock_print_invalid.assert_called_once_with("invalid_command")
    
    def test_perform_action_case_insensitive(self, sample_player, sample_world):
        """Test that actions are case insensitive."""
        with patch('game.actions.handle_look') as mock_handle_look:
            perform_action(sample_player, sample_world, "LOOK")
            mock_handle_look.assert_called_once()
    
    def test_perform_action_strips_whitespace(self, sample_player, sample_world):
        """Test that actions strip whitespace."""
        with patch('game.actions.handle_look') as mock_handle_look:
            perform_action(sample_player, sample_world, "  look  ")
            mock_handle_look.assert_called_once()


class TestHandleMovement:
    """Test movement handling functionality."""
    
    @patch('game.world.get_current_location')
    @patch('game.world.get_available_locations')
    @patch('game.world.change_location')
    @patch('game.player.move_player')
    @patch('game.world.get_location_description')
    @patch('builtins.print')
    def test_handle_movement_valid_location(self, mock_print, mock_get_desc, mock_move_player, 
                                          mock_change_location, mock_get_available, 
                                          mock_get_current, sample_player, sample_world):
        """Test handling movement to a valid location."""
        mock_get_current.return_value = "Village"
        mock_get_available.return_value = ["Forest", "Mountain"]
        mock_change_location.return_value = True
        mock_get_desc.return_value = "A dense forest..."
        
        handle_movement(sample_player, sample_world, "Forest")
        
        mock_change_location.assert_called_once_with(sample_world, "Forest")
        mock_move_player.assert_called_once_with(sample_player, "Forest")
        mock_get_desc.assert_called_once_with(sample_world, "Forest")
    
    @patch('game.world.get_current_location')
    @patch('game.world.get_available_locations')
    @patch('builtins.print')
    def test_handle_movement_invalid_location(self, mock_print, mock_get_available, 
                                            mock_get_current, sample_player, sample_world):
        """Test handling movement to an invalid location."""
        mock_get_current.return_value = "Village"
        mock_get_available.return_value = ["Forest", "Mountain"]
        
        handle_movement(sample_player, sample_world, "Cave")
        
        mock_print.assert_any_call("You cannot go to Cave from Village.")
        mock_print.assert_any_call("Available locations: Forest, Mountain")
    
    @patch('game.world.get_current_location')
    @patch('game.world.get_available_locations')
    @patch('game.world.change_location')
    @patch('builtins.print')
    def test_handle_movement_change_location_fails(self, mock_print, mock_change_location, 
                                                 mock_get_available, mock_get_current, 
                                                 sample_player, sample_world):
        """Test handling movement when change_location fails."""
        mock_get_current.return_value = "Village"
        mock_get_available.return_value = ["Forest", "Mountain"]
        mock_change_location.return_value = False
        
        handle_movement(sample_player, sample_world, "Forest")
        
        mock_print.assert_called_with("You cannot go to Forest from here.")


class TestHandleTakeItem:
    """Test item taking functionality."""
    
    @patch('game.world.get_current_location')
    @patch('game.player.add_item_to_inventory')
    def test_handle_take_item_success(self, mock_add_item, mock_get_current, 
                                    sample_player, sample_world):
        """Test successfully taking an item."""
        mock_get_current.return_value = "Village"
        sample_world["locations"]["Village"]["items"] = ["map", "bread"]
        
        handle_take_item(sample_player, sample_world, "map")
        
        mock_add_item.assert_called_once_with(sample_player, "map")
        assert "map" not in sample_world["locations"]["Village"]["items"]
        assert "bread" in sample_world["locations"]["Village"]["items"]
    
    @patch('game.world.get_current_location')
    @patch('builtins.print')
    def test_handle_take_item_not_available(self, mock_print, mock_get_current, 
                                          sample_player, sample_world):
        """Test taking an item that's not available."""
        mock_get_current.return_value = "Village"
        sample_world["locations"]["Village"]["items"] = ["bread"]
        
        handle_take_item(sample_player, sample_world, "sword")
        
        mock_print.assert_any_call("There is no sword here to take.")
        mock_print.assert_any_call("Available items: bread")
    
    @patch('game.world.get_current_location')
    @patch('builtins.print')
    def test_handle_take_item_no_items_available(self, mock_print, mock_get_current, 
                                               sample_player, sample_world):
        """Test taking an item when no items are available."""
        mock_get_current.return_value = "Village"
        sample_world["locations"]["Village"]["items"] = []
        
        handle_take_item(sample_player, sample_world, "sword")
        
        mock_print.assert_called_once_with("There is no sword here to take.")


class TestHandleDropItem:
    """Test item dropping functionality."""
    
    @patch('game.player.remove_item_from_inventory')
    @patch('game.world.get_current_location')
    def test_handle_drop_item_success(self, mock_get_current, mock_remove_item, 
                                    sample_player, sample_world):
        """Test successfully dropping an item."""
        mock_get_current.return_value = "Village"
        mock_remove_item.return_value = True
        sample_world["locations"]["Village"]["items"] = []
        
        handle_drop_item(sample_player, sample_world, "sword")
        
        mock_remove_item.assert_called_once_with(sample_player, "sword")
        assert "sword" in sample_world["locations"]["Village"]["items"]
    
    @patch('game.player.remove_item_from_inventory')
    @patch('game.world.get_current_location')
    def test_handle_drop_item_not_in_inventory(self, mock_get_current, mock_remove_item, 
                                             sample_player, sample_world):
        """Test dropping an item not in inventory."""
        mock_get_current.return_value = "Village"
        mock_remove_item.return_value = False
        initial_items = sample_world["locations"]["Village"]["items"].copy()
        
        handle_drop_item(sample_player, sample_world, "sword")
        
        # Items in location should remain unchanged
        assert sample_world["locations"]["Village"]["items"] == initial_items


class TestHandleUseItem:
    """Test item usage functionality."""
    
    @patch('game.items.use_item')
    def test_handle_use_item_in_inventory(self, mock_use_item, player_with_items, sample_world):
        """Test using an item that's in inventory."""
        handle_use_item(player_with_items, sample_world, "map")
        
        mock_use_item.assert_called_once_with(player_with_items, "map", sample_world)
    
    @patch('builtins.print')
    def test_handle_use_item_not_in_inventory(self, mock_print, sample_player, sample_world):
        """Test using an item that's not in inventory."""
        handle_use_item(sample_player, sample_world, "sword")
        
        mock_print.assert_called_once_with("You don't have sword in your inventory.")


class TestHandleLook:
    """Test look functionality."""
    
    @patch('game.world.get_current_location')
    @patch('game.world.get_location_description')
    @patch('game.world.get_available_locations')
    @patch('builtins.print')
    def test_handle_look_with_items(self, mock_print, mock_get_available, 
                                  mock_get_desc, mock_get_current, 
                                  sample_player, sample_world):
        """Test looking around with items present."""
        mock_get_current.return_value = "Village"
        mock_get_desc.return_value = "A peaceful village"
        mock_get_available.return_value = ["Forest", "Mountain"]
        sample_world["locations"]["Village"]["items"] = ["map", "bread"]
        
        handle_look(sample_player, sample_world)
        
        mock_print.assert_any_call("\nA peaceful village")
        mock_print.assert_any_call("Items here: map, bread")
        mock_print.assert_any_call("You can go to: Forest, Mountain")
    
    @patch('game.world.get_current_location')
    @patch('game.world.get_location_description')
    @patch('game.world.get_available_locations')
    @patch('builtins.print')
    def test_handle_look_no_items(self, mock_print, mock_get_available, 
                                mock_get_desc, mock_get_current, 
                                sample_player, sample_world):
        """Test looking around with no items present."""
        mock_get_current.return_value = "Village"
        mock_get_desc.return_value = "A peaceful village"
        mock_get_available.return_value = ["Forest", "Mountain"]
        sample_world["locations"]["Village"]["items"] = []
        
        handle_look(sample_player, sample_world)
        
        mock_print.assert_any_call("\nA peaceful village")
        mock_print.assert_any_call("You can go to: Forest, Mountain")
        # Should not print items line when no items


class TestHandleInventory:
    """Test inventory display functionality."""
    
    @patch('builtins.print')
    def test_handle_inventory_with_items(self, mock_print, player_with_items):
        """Test displaying inventory with items."""
        handle_inventory(player_with_items)
        
        mock_print.assert_called_once_with("Inventory: map, bread, stick, torch")
    
    @patch('builtins.print')
    def test_handle_inventory_empty(self, mock_print, sample_player):
        """Test displaying empty inventory."""
        handle_inventory(sample_player)
        
        mock_print.assert_called_once_with("Your inventory is empty.")


class TestHandleStatus:
    """Test status display functionality."""
    
    @patch('builtins.print')
    @patch('game.actions.handle_inventory')
    def test_handle_status(self, mock_handle_inventory, mock_print, sample_player):
        """Test displaying player status."""
        handle_status(sample_player)
        
        expected_calls = [
            call("Name: TestPlayer"),
            call("Health: 100/100"),
            call("Gold: 100"),
            call("Location: Village")
        ]
        mock_print.assert_has_calls(expected_calls)
        mock_handle_inventory.assert_called_once_with(sample_player)
    
    @patch('builtins.print')
    @patch('game.actions.handle_inventory')
    def test_handle_status_damaged_player(self, mock_handle_inventory, mock_print, damaged_player):
        """Test displaying status for damaged player."""
        handle_status(damaged_player)
        
        mock_print.assert_any_call("Health: 50/100")


class TestActionEdgeCases:
    """Test edge cases and error conditions."""
    
    def test_perform_action_empty_string(self, sample_player, sample_world):
        """Test performing an empty action."""
        with patch('utils.text_formatting.print_invalid_action') as mock_print_invalid:
            perform_action(sample_player, sample_world, "")
            mock_print_invalid.assert_called_once_with("")
    
    def test_perform_action_whitespace_only(self, sample_player, sample_world):
        """Test performing an action with only whitespace."""
        with patch('utils.text_formatting.print_invalid_action') as mock_print_invalid:
            perform_action(sample_player, sample_world, "   ")
            mock_print_invalid.assert_called_once_with("")
    
    def test_handle_movement_empty_location(self, sample_player, sample_world):
        """Test movement with empty location name."""
        with patch('game.world.get_current_location') as mock_get_current, \
             patch('game.world.get_available_locations') as mock_get_available, \
             patch('builtins.print') as mock_print:
            
            mock_get_current.return_value = "Village"
            mock_get_available.return_value = ["Forest", "Mountain"]
            
            handle_movement(sample_player, sample_world, "")
            
            mock_print.assert_any_call("You cannot go to  from Village.")
    
    def test_handle_take_item_empty_item(self, sample_player, sample_world):
        """Test taking an empty item name."""
        with patch('game.world.get_current_location') as mock_get_current, \
             patch('builtins.print') as mock_print:
            
            mock_get_current.return_value = "Village"
            sample_world["locations"]["Village"]["items"] = ["map"]
            
            handle_take_item(sample_player, sample_world, "")
            
            mock_print.assert_any_call("There is no  here to take.")

