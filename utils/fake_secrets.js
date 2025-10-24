// JavaScript file with fake secrets for TruffleHog testing
// WARNING: These are FAKE secrets for testing purposes only!

const config = {
    // Fake API credentials
    apiKey: "AIzaSyDaGmWKa4JsXZ-HjGw1234567890abcdef",
    secretKey: "1234567890abcdef1234567890abcdef",
    
    // Fake AWS credentials
    aws: {
        accessKeyId: "AKIAIOSFODNN7EXAMPLE",
        secretAccessKey: "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
        region: "us-east-1"
    },
    
    // Fake database connection strings
    database: {
        url: "mysql://user:password123@localhost:3306/kevin_db",
        mongoUri: "mongodb://admin:secretpass@cluster0.mongodb.net/kevin_adventure"
    },
    
    // Fake OAuth tokens
    oauth: {
        googleClientSecret: "GOCSPX-1234567890abcdef1234567890abcdef",
        facebookAppSecret: "1234567890abcdef1234567890abcdef",
        twitterConsumerSecret: "1234567890abcdef1234567890abcdef1234567890abcdef1234567890"
    },
    
    // Fake JWT configuration
    jwt: {
        secret: "super-secret-jwt-key-do-not-share",
        refreshSecret: "another-secret-for-refresh-tokens"
    },
    
    // Fake third-party service keys
    services: {
        stripeSecretKey: "sk_live_1234567890abcdef1234567890abcdef",
        sendgridApiKey: "SG.1234567890abcdef.1234567890abcdef1234567890abcdef1234567890abcdef",
        twilioAuthToken: "1234567890abcdef1234567890abcdef",
        slackBotToken: "xoxb-1234567890-1234567890-1234567890abcdef"
    },
    
    // Fake encryption keys
    encryption: {
        key: "1234567890abcdef1234567890abcdef",
        iv: "abcdef1234567890",
        salt: "randomsalt123"
    },
    
    // Fake webhook secrets
    webhooks: {
        github: "1234567890abcdef1234567890abcdef",
        stripe: "whsec_1234567890abcdef1234567890abcdef"
    }
};

// Fake private key (shortened)
const privateKey = `-----BEGIN PRIVATE KEY-----
MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC1234567890ab
cdef1234567890abcdef1234567890abcdef1234567890abcdef1234567890ab
cdef1234567890abcdef1234567890abcdef1234567890abcdef1234567890ab
-----END PRIVATE KEY-----`;

// Function to get configuration
function getConfig() {
    return {
        ...config,
        privateKey: privateKey,
        // More fake secrets in different formats
        hardcodedPassword: "password123",
        apiToken: "Bearer 1234567890abcdef1234567890abcdef",
        basicAuth: "Basic dXNlcjpwYXNzd29yZA==", // base64 encoded user:password
    };
}

// Export for use in other modules
module.exports = {
    config,
    getConfig,
    // Fake connection function
    connectToDatabase: function() {
        const connectionString = "postgresql://kevin:secretpassword@localhost:5432/adventure_db";
        console.log("Connecting to database...");
        // Fake connection logic
    }
};

