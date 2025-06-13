#!/usr/bin/env python3
"""
Out-of-sync test file for debugging garbled commit issue.
This test simulates being out of sync with remote and then pushing changes.
"""

# Test with extensive Unicode and special characters
UNICODE_TEST = "àáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿ"
MATH_SYMBOLS = "∑∏∆∇∂∫√∞≠≤≥±×÷"
EMOJI_TEST = "🔧🐛🔍🚀🎉✨🌍🌈💻🎯🔥⚡"
SYMBOLS = "©®™€£¥§¶†‡•…‰‹›""''–—"
MIXED_CONTENT = "Hello 世界 🌍 café naïve résumé ∑∏∆"

def test_out_of_sync_encoding():
    """Test function with various character encodings while out of sync."""
    print("Testing out-of-sync scenario with Unicode characters:")
    print(f"Unicode: {UNICODE_TEST}")
    print(f"Math: {MATH_SYMBOLS}")
    print(f"Emoji: {EMOJI_TEST}")
    print(f"Symbols: {SYMBOLS}")
    print(f"Mixed: {MIXED_CONTENT}")
    
    # Create some data structures with special characters
    test_data = {
        "café": "naïve résumé",
        "math": "∑(x²) = ∫f(x)dx",
        "emoji_count": "🔧×5 = 🔧🔧🔧🔧🔧",
        "unicode_string": "àáâãäåæç" * 10,
        "mixed_array": [
            "Item 1: Hello 世界 🌍",
            "Item 2: café ∑∏∆",
            "Item 3: Testing ©®™€£¥",
            "Item 4: Math ∂∫√∞≠≤≥±×÷"
        ]
    }
    
    return test_data

# Large comment block with various encodings
"""
This is a comprehensive test of character encodings in an out-of-sync scenario.

ASCII: ABCDEFGHIJKLMNOPQRSTUVWXYZ 0123456789
Unicode Basic: àáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿ
Unicode Extended: ∑∏∆∇∂∫√∞≠≤≥±×÷
Emoji: 🔧🐛🔍🚀🎉✨🌍🌈💻🎯🔥⚡
Symbols: ©®™€£¥§¶†‡•…‰‹›""''–—
Mixed: Hello 世界 🌍 café naïve résumé ∑∏∆

Repeated patterns:
🔧 Unicode test: àáâãäåæç ∑∏∆∇∂∫√∞≠≤≥±×÷ 🔧
🔧 Unicode test: àáâãäåæç ∑∏∆∇∂∫√∞≠≤≥±×÷ 🔧
🔧 Unicode test: àáâãäåæç ∑∏∆∇∂∫√∞≠≤≥±×÷ 🔧
🔧 Unicode test: àáâãäåæç ∑∏∆∇∂∫√∞≠≤≥±×÷ 🔧
🔧 Unicode test: àáâãäåæç ∑∏∆∇∂∫√∞≠≤≥±×÷ 🔧

This should help us determine if being out of sync causes encoding issues.
"""

if __name__ == "__main__":
    result = test_out_of_sync_encoding()
    print("\nTest completed!")
    print(f"Result keys: {list(result.keys())}")
    for key, value in result.items():
        print(f"{key}: {value}")
