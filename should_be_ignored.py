# This file should be ignored by .trufflehogignore
# Contains fake secrets for testing

# Fake GitHub token (should be ignored)
GITHUB_TOKEN = "ghp_1234567890abcdefghijklmnopqrstuvwxyz123"

def ignored_function():
    print(f"Using token: {GITHUB_TOKEN}")
