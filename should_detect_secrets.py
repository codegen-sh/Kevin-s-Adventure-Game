# This file should NOT be ignored - secrets should be detected
# Contains fake secrets for testing

# Fake AWS credentials (should be detected)
AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

def main():
    print(f"AWS Key: {AWS_ACCESS_KEY_ID}")
    print(f"AWS Secret: {AWS_SECRET_ACCESS_KEY}")
