# Test file with fake secrets for pre-push hook testing
# This is just for demonstration purposes

# Fake AWS access key (this will trigger TruffleHog)
AWS_ACCESS_KEY = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

def main():
    print("Testing pre-push hook with fake secrets")
    print(f"Using AWS key: {AWS_ACCESS_KEY}")

if __name__ == "__main__":
    main()
