#!/usr/bin/env python3
"""
Test file for debugging garbled commit issue.
This file contains various types of content to test encoding.
"""

def test_function():
    """Test function with various characters."""
    message = "Hello, World! 🌍"
    special_chars = "àáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿ"
    unicode_test = "Testing Unicode: ∑∏∆∇∂∫√∞≠≤≥±×÷"
    
    print(f"Message: {message}")
    print(f"Special chars: {special_chars}")
    print(f"Unicode: {unicode_test}")
    
    # Test with some code patterns
    data = {
        "key1": "value1",
        "key2": [1, 2, 3, 4, 5],
        "key3": {"nested": True}
    }
    
    return data

if __name__ == "__main__":
    result = test_function()
    print(f"Result: {result}")
