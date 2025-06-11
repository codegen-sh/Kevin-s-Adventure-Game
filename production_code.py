# Production code - should NOT be ignored
# This should detect secrets if they exist

# This would be a real secret that should be detected
# AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"  # Commented out for safety

def production_function():
    # This is clean production code
    api_endpoint = "https://api.example.com"
    return f"Connecting to: {api_endpoint}"
