#!/usr/bin/env python3
"""
Escape character test for debugging garbled commit issue.
This file contains problematic escaping that might break base64 encoding.
"""

# Test various escape sequences that might break base64
ESCAPE_TESTS = {
    "backslashes": "\\n\\r\\t\\\\\\\"\\\'",
    "null_bytes": "test\x00null\x00bytes",
    "control_chars": "\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f",
    "high_ascii": "\x80\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f",
    "quotes": "\"'`\"\"''``",
    "mixed_quotes": "He said \"I can't\" and she replied 'Why not?'",
    "backslash_hell": "\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\",
    "json_breaking": '{"key": "value with \\"quotes\\" and \\n newlines"}',
    "regex_chars": ".*+?^${}()|[]\\",
    "shell_chars": "$HOME `echo test` $(whoami) &amp; &lt; &gt;",
}

def test_problematic_strings():
    """Test strings that might break base64 encoding."""
    print("Testing problematic escape sequences:")
    
    for name, test_str in ESCAPE_TESTS.items():
        print(f"{name}: {repr(test_str)}")
        
    # Test with raw bytes that might cause issues
    raw_bytes = bytes(range(256))
    print(f"Raw bytes: {raw_bytes[:50]}...")
    
    return ESCAPE_TESTS

# Large string with mixed problematic content
PROBLEMATIC_CONTENT = """
This is a test with various problematic characters:

Backslashes: \\ \\\\ \\\\\\
Quotes: " ' ` "" '' ``
Newlines and tabs:
\tTabbed content
\nNew line content
\r\nWindows line endings

JSON-like content: {"test": "value with \"quotes\" and \n newlines"}
Regex chars: .*+?^${}()|[]\\
Shell injection: $HOME `echo test` $(whoami)
Control chars: \x01\x02\x03\x04\x05

Mixed escaping nightmare:
\\n\\r\\t\\\\\\"\\' combined with "quotes" and 'apostrophes'
"""

if __name__ == "__main__":
    test_problematic_strings()
    print("Escape test completed!")
