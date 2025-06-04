"""
Unit tests for the text formatting module.
"""

import pytest
from unittest.mock import patch

from utils.text_formatting import (
    wrap_text,
    print_welcome_message,
    print_help,
    format_inventory,
    print_separator,
    print_event,
    print_game_over,
    print_invalid_action
)


class TestWrapText:
    """Test text wrapping functionality."""
    
    def test_wrap_text_default_width(self):
        """Test wrapping text with default width."""
        long_text = "This is a very long line of text that should be wrapped at the default width of 80 characters to ensure proper formatting."
        result = wrap_text(long_text)
        
        lines = result.split('\n')
        for line in lines:
            assert len(line) <= 80
    
    def test_wrap_text_custom_width(self):
        """Test wrapping text with custom width."""
        text = "This is a test line that should be wrapped at 20 characters."
        result = wrap_text(text, width=20)
        
        lines = result.split('\n')
        for line in lines:
            assert len(line) <= 20
    
    def test_wrap_text_short_text(self):
        """Test wrapping text shorter than width."""
        text = "Short text"
        result = wrap_text(text, width=80)
        
        assert result == text
        assert '\n' not in result
    
    def test_wrap_text_empty_string(self):
        """Test wrapping empty string."""
        result = wrap_text("", width=80)
        assert result == ""
    
    def test_wrap_text_single_word_longer_than_width(self):
        """Test wrapping single word longer than width."""
        text = "supercalifragilisticexpialidocious"
        result = wrap_text(text, width=10)
        
        # Should not break the word
        assert text in result


class TestPrintWelcomeMessage:
    """Test welcome message printing."""
    
    @patch('builtins.print')
    def test_print_welcome_message(self, mock_print):
        """Test that welcome message is printed."""
        print_welcome_message()
        
        mock_print.assert_called_once()
        printed_text = mock_print.call_args[0][0]
        
        assert "Welcome to Kevin's Adventure Game!" in printed_text
        assert "Explore a world of mystery" in printed_text
        assert "Type 'help'" in printed_text
    
    @patch('builtins.print')
    def test_welcome_message_content(self, mock_print):
        """Test welcome message contains expected content."""
        print_welcome_message()
        
        printed_text = mock_print.call_args[0][0]
        
        # Check for key phrases
        expected_phrases = [
            "Kevin's Adventure Game",
            "mystery and danger",
            "forests, caves, villages, and mountains",
            "Good luck, adventurer"
        ]
        
        for phrase in expected_phrases:
            assert phrase in printed_text


class TestPrintHelp:
    """Test help message printing."""
    
    @patch('builtins.print')
    def test_print_help(self, mock_print):
        """Test that help message is printed."""
        print_help()
        
        mock_print.assert_called_once()
        printed_text = mock_print.call_args[0][0]
        
        assert "Available commands:" in printed_text
    
    @patch('builtins.print')
    def test_help_message_commands(self, mock_print):
        """Test help message contains expected commands."""
        print_help()
        
        printed_text = mock_print.call_args[0][0]
        
        # Check for essential commands
        expected_commands = [
            "move", "look", "inventory", "pickup", "drop", 
            "use", "examine", "status", "interact", "help", "quit"
        ]
        
        for command in expected_commands:
            assert command in printed_text.lower()


class TestFormatInventory:
    """Test inventory formatting functionality."""
    
    def test_format_empty_inventory(self):
        """Test formatting empty inventory."""
        result = format_inventory([])
        assert result == "empty"
    
    def test_format_single_item_inventory(self):
        """Test formatting inventory with single item."""
        result = format_inventory(["sword"])
        assert result == "sword"
    
    def test_format_multiple_items_inventory(self):
        """Test formatting inventory with multiple items."""
        items = ["sword", "shield", "potion"]
        result = format_inventory(items)
        
        assert result == "sword, shield, potion"
        assert all(item in result for item in items)
    
    def test_format_inventory_preserves_order(self):
        """Test that inventory formatting preserves item order."""
        items = ["first", "second", "third"]
        result = format_inventory(items)
        
        assert result == "first, second, third"
    
    def test_format_inventory_with_duplicate_items(self):
        """Test formatting inventory with duplicate items."""
        items = ["bread", "bread", "sword"]
        result = format_inventory(items)
        
        assert result == "bread, bread, sword"
        assert result.count("bread") == 2


class TestPrintSeparator:
    """Test separator printing functionality."""
    
    @patch('builtins.print')
    def test_print_separator_default(self, mock_print):
        """Test printing separator with default parameters."""
        print_separator()
        
        mock_print.assert_called_once_with("-" * 80)
    
    @patch('builtins.print')
    def test_print_separator_custom_char(self, mock_print):
        """Test printing separator with custom character."""
        print_separator(char="=", length=40)
        
        mock_print.assert_called_once_with("=" * 40)
    
    @patch('builtins.print')
    def test_print_separator_custom_length(self, mock_print):
        """Test printing separator with custom length."""
        print_separator(char="*", length=20)
        
        mock_print.assert_called_once_with("*" * 20)
    
    @patch('builtins.print')
    def test_print_separator_zero_length(self, mock_print):
        """Test printing separator with zero length."""
        print_separator(length=0)
        
        mock_print.assert_called_once_with("")


class TestPrintEvent:
    """Test event message printing."""
    
    @patch('utils.text_formatting.print_separator')
    @patch('utils.text_formatting.wrap_text')
    @patch('builtins.print')
    def test_print_event(self, mock_print, mock_wrap, mock_separator):
        """Test printing event message."""
        event_text = "Something exciting happened!"
        mock_wrap.return_value = event_text
        
        print_event(event_text)
        
        # Should call separator twice (before and after)
        assert mock_separator.call_count == 2
        mock_wrap.assert_called_once_with(event_text)
        mock_print.assert_called_once_with(event_text)
    
    @patch('utils.text_formatting.print_separator')
    @patch('builtins.print')
    def test_print_event_with_long_text(self, mock_print, mock_separator):
        """Test printing event with long text that needs wrapping."""
        long_text = "This is a very long event message that should be wrapped properly to ensure good formatting and readability."
        
        print_event(long_text)
        
        # Should still call separator and print
        assert mock_separator.call_count == 2
        mock_print.assert_called_once()


class TestPrintGameOver:
    """Test game over message printing."""
    
    @patch('utils.text_formatting.print_separator')
    @patch('builtins.print')
    def test_print_game_over(self, mock_print, mock_separator):
        """Test printing game over message."""
        print_game_over()
        
        # Should call separator twice with "=" character
        expected_calls = [
            pytest.mock.call("="),
            pytest.mock.call("=")
        ]
        mock_separator.assert_has_calls(expected_calls)
        
        # Should print the game over message
        mock_print.assert_called_once()
        printed_text = mock_print.call_args[0][0]
        assert "Game Over" in printed_text
        assert "Thank you for playing" in printed_text


class TestPrintInvalidAction:
    """Test invalid action message printing."""
    
    @patch('builtins.print')
    def test_print_invalid_action(self, mock_print):
        """Test printing invalid action message."""
        action = "invalid_command"
        print_invalid_action(action)
        
        mock_print.assert_called_once()
        printed_text = mock_print.call_args[0][0]
        
        assert action in printed_text
        assert "don't understand" in printed_text
        assert "help" in printed_text
    
    @patch('builtins.print')
    def test_print_invalid_action_empty_string(self, mock_print):
        """Test printing invalid action message with empty string."""
        print_invalid_action("")
        
        mock_print.assert_called_once()
        printed_text = mock_print.call_args[0][0]
        
        assert "don't understand ''" in printed_text
        assert "help" in printed_text
    
    @patch('builtins.print')
    def test_print_invalid_action_special_characters(self, mock_print):
        """Test printing invalid action message with special characters."""
        action = "!@#$%"
        print_invalid_action(action)
        
        mock_print.assert_called_once()
        printed_text = mock_print.call_args[0][0]
        
        assert action in printed_text


class TestTextFormattingIntegration:
    """Test integration between text formatting functions."""
    
    @patch('builtins.print')
    def test_event_and_separator_integration(self, mock_print):
        """Test that event printing properly uses separators."""
        event_text = "Test event"
        
        with patch('utils.text_formatting.print_separator') as mock_separator:
            print_event(event_text)
            
            # Should call separator before and after
            assert mock_separator.call_count == 2
            
            # Should print the wrapped text
            mock_print.assert_called_once()
    
    def test_inventory_formatting_with_various_inputs(self):
        """Test inventory formatting with various input types."""
        test_cases = [
            ([], "empty"),
            (["item"], "item"),
            (["a", "b", "c"], "a, b, c"),
            (["item with spaces", "another item"], "item with spaces, another item")
        ]
        
        for inventory, expected in test_cases:
            result = format_inventory(inventory)
            assert result == expected
    
    @patch('builtins.print')
    def test_multiple_message_types(self, mock_print):
        """Test printing multiple types of messages."""
        # Test sequence of different message types
        print_welcome_message()
        print_help()
        print_invalid_action("test")
        print_game_over()
        
        # Should have called print multiple times
        assert mock_print.call_count == 4


class TestTextFormattingEdgeCases:
    """Test edge cases and error conditions."""
    
    def test_wrap_text_with_none_input(self):
        """Test wrap_text with None input."""
        with pytest.raises(AttributeError):
            wrap_text(None)
    
    def test_format_inventory_with_none_input(self):
        """Test format_inventory with None input."""
        with pytest.raises(TypeError):
            format_inventory(None)
    
    def test_format_inventory_with_non_list_input(self):
        """Test format_inventory with non-list input."""
        with pytest.raises(AttributeError):
            format_inventory("not a list")
    
    def test_wrap_text_with_negative_width(self):
        """Test wrap_text with negative width."""
        # Should handle gracefully or raise appropriate error
        text = "Test text"
        try:
            result = wrap_text(text, width=-1)
            # If it doesn't raise an error, result should be reasonable
            assert isinstance(result, str)
        except ValueError:
            # Acceptable to raise ValueError for negative width
            pass
    
    def test_print_separator_with_negative_length(self):
        """Test print_separator with negative length."""
        with patch('builtins.print') as mock_print:
            print_separator(length=-1)
            # Should handle gracefully
            mock_print.assert_called_once()


class TestTextFormattingPerformance:
    """Test performance characteristics of text formatting functions."""
    
    def test_format_large_inventory_performance(self):
        """Test formatting large inventory performs reasonably."""
        large_inventory = [f"item_{i}" for i in range(1000)]
        
        import time
        start_time = time.time()
        result = format_inventory(large_inventory)
        end_time = time.time()
        
        # Should complete quickly (less than 1 second)
        assert end_time - start_time < 1.0
        assert isinstance(result, str)
        assert len(result) > 0
    
    def test_wrap_very_long_text_performance(self):
        """Test wrapping very long text performs reasonably."""
        very_long_text = "This is a test sentence. " * 1000
        
        import time
        start_time = time.time()
        result = wrap_text(very_long_text, width=80)
        end_time = time.time()
        
        # Should complete quickly
        assert end_time - start_time < 1.0
        assert isinstance(result, str)
        assert len(result) > 0

