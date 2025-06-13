#!/usr/bin/env python3
"""
Large test file for debugging garbled commit issue.
This file contains repetitive content with various encodings to test if file size affects the issue.
"""

import json
import sys
from typing import Dict, List, Any

class DebugTester:
    """Class for testing various encoding scenarios."""
    
    def __init__(self):
        self.test_data = {
            "ascii": "Simple ASCII text",
            "unicode_basic": "Café naïve résumé",
            "unicode_extended": "∑∏∆∇∂∫√∞≠≤≥±×÷",
            "emoji": "🔧🐛🔍🚀🎉✨🌍🌈",
            "mixed": "Hello 世界 🌍 café ∑∏∆",
            "symbols": "©®™€£¥§¶†‡•…‰‹›""''–—"
        }
    
    def generate_test_content(self, iterations: int = 50) -> List[str]:
        """Generate test content with various encodings."""
        content = []
        
        for i in range(iterations):
            content.append(f"# Test iteration {i + 1}")
            content.append(f"ASCII: This is test number {i + 1}")
            content.append(f"Unicode: Test №{i + 1} with special chars: àáâãäåæç")
            content.append(f"Emoji: Test {i + 1} 🔧🐛🔍 debugging")
            content.append(f"Math: ∑(i={i}) = {i * (i + 1) // 2}")
            content.append(f"Mixed: Test {i + 1} 世界 🌍 café ∑∏∆")
            content.append("")
        
        return content
    
    def test_json_encoding(self) -> Dict[str, Any]:
        """Test JSON encoding with various character sets."""
        return {
            "test_id": "json_encoding_test",
            "data": self.test_data,
            "repeated_data": [self.test_data for _ in range(10)],
            "large_string": "A" * 1000 + "🔧" + "B" * 1000,
            "unicode_array": [f"Item {i} with unicode: ∑∏∆∇∂∫√∞≠≤≥±×÷" for i in range(20)]
        }
    
    def run_all_tests(self):
        """Run all encoding tests."""
        print("Starting encoding tests...")
        
        # Test 1: Basic content generation
        content = self.generate_test_content(25)
        print(f"Generated {len(content)} lines of test content")
        
        # Test 2: JSON encoding
        json_data = self.test_json_encoding()
        json_str = json.dumps(json_data, ensure_ascii=False, indent=2)
        print(f"Generated JSON with {len(json_str)} characters")
        
        # Test 3: File operations
        try:
            with open("temp_test.txt", "w", encoding="utf-8") as f:
                f.write("\n".join(content))
            print("Successfully wrote test content to file")
        except Exception as e:
            print(f"Error writing file: {e}")
        
        return content, json_data

def main():
    """Main function for testing."""
    tester = DebugTester()
    content, json_data = tester.run_all_tests()
    
    print("\n=== Test Summary ===")
    print(f"Content lines: {len(content)}")
    print(f"JSON keys: {len(json_data)}")
    print("Test completed successfully!")
    
    # Print some sample content
    print("\n=== Sample Content ===")
    for i, line in enumerate(content[:10]):
        print(f"{i+1:2d}: {line}")
    
    if len(content) > 10:
        print("... (truncated)")

if __name__ == "__main__":
    main()

# Additional test content with various patterns
TEST_PATTERNS = [
    "Pattern 1: " + "A" * 100,
    "Pattern 2: " + "🔧" * 50,
    "Pattern 3: " + "∑∏∆∇∂∫√∞≠≤≥±×÷" * 10,
    "Pattern 4: " + "àáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿ" * 5,
    "Pattern 5: Mixed " + "ABC🔧∑∏∆àáâ" * 20
]

# Large comment block for testing
"""
This is a large comment block designed to test how the create_signed_commit tool
handles files with significant content. The goal is to determine if file size
or specific character encodings cause the garbled commit issue.

Test characters:
- Basic ASCII: ABCDEFGHIJKLMNOPQRSTUVWXYZ
- Numbers: 0123456789
- Special chars: !@#$%^&*()_+-=[]{}|;:,.<>?
- Accented chars: àáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿ
- Math symbols: ∑∏∆∇∂∫√∞≠≤≥±×÷
- Emoji: 🔧🐛🔍🚀🎉✨🌍🌈
- Mixed: Hello 世界 🌍 café ∑∏∆

This comment is intentionally long to test if the issue is related to file size
or specific content patterns. We're repeating various character sets to see
if any particular encoding causes problems during the commit process.

Repeated test line: Test 🔧 with unicode ∑∏∆ and accents àáâ
Repeated test line: Test 🔧 with unicode ∑∏∆ and accents àáâ
Repeated test line: Test 🔧 with unicode ∑∏∆ and accents àáâ
Repeated test line: Test 🔧 with unicode ∑∏∆ and accents àáâ
Repeated test line: Test 🔧 with unicode ∑∏∆ and accents àáâ
"""
