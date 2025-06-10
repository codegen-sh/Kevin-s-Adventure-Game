# Configuration file with various fake secrets for TruffleHog testing
# WARNING: These are FAKE secrets for testing purposes only!

import os

class Config:
    # Fake AWS credentials
    AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"
    AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
    AWS_SESSION_TOKEN = "AQoEXAMPLEH4aoAH0gNCAPyJxz4BlCFFxWNE1OPTgk5TthT+FvwqnKwRcOIfrRh3c/LTo6UDdyJwOOvEVPvLXCrrrUtdnniCEXAMPLE/IvU1dYUg2RVAJBanLiHb4IgRmpRV3zrkuWJOgQs8IZZaIv2BXIa2R4OlgkBN9bkUDNCJiBeb/AXlzBBko7b15fjrBs2+cTQtpZ3CYWFXG8C5zqx37wnOE49mRl/+OtkIKGO7fAE"
    
    # Fake API keys
    STRIPE_SECRET_KEY = "sk_test_4eC39HqLyjWDarjtT1zdp7dc"
    STRIPE_PUBLISHABLE_KEY = "pk_test_TYooMQauvdEDq54NiTphI7jx"
    OPENAI_API_KEY = "sk-proj-1234567890abcdef1234567890abcdef1234567890abcdef"
    GITHUB_TOKEN = "ghp_1234567890abcdef1234567890abcdef12345678"
    
    # Fake database credentials
    DATABASE_URL = "postgresql://username:password123@localhost:5432/mydatabase"
    REDIS_URL = "redis://:mypassword@localhost:6379/0"
    MONGODB_URI = "mongodb://admin:secretpassword@localhost:27017/myapp"
    
    # Fake JWT secrets
    JWT_SECRET = "super-secret-jwt-key-that-should-not-be-hardcoded"
    JWT_REFRESH_SECRET = "another-secret-key-for-refresh-tokens"
    
    # Fake encryption keys
    ENCRYPTION_KEY = "1234567890abcdef1234567890abcdef"
    AES_KEY = "abcdef1234567890abcdef1234567890"
    
    # Fake third-party service keys
    SENDGRID_API_KEY = "SG.1234567890abcdef.1234567890abcdef1234567890abcdef1234567890abcdef"
    TWILIO_AUTH_TOKEN = "1234567890abcdef1234567890abcdef"
    SLACK_BOT_TOKEN = "xoxb-1234567890-1234567890-1234567890abcdef"
    
    # Fake private keys (shortened for brevity)
    RSA_PRIVATE_KEY = """-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEA1234567890abcdef1234567890abcdef1234567890abcdef
1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef
1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef
-----END RSA PRIVATE KEY-----"""

    # Fake OAuth credentials
    GOOGLE_CLIENT_SECRET = "GOCSPX-1234567890abcdef1234567890abcdef"
    FACEBOOK_APP_SECRET = "1234567890abcdef1234567890abcdef"
    
    # Fake webhook secrets
    WEBHOOK_SECRET = "whsec_1234567890abcdef1234567890abcdef"
    
    @classmethod
    def get_secret(cls, key):
        """Get secret from environment or fallback to hardcoded value"""
        return os.getenv(key, getattr(cls, key, None))

