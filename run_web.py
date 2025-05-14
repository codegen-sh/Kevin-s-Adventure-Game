#!/usr/bin/env python3
"""
Run script for Kevin's Adventure Game web interface.
This script starts the Flask web server.
"""

from app import app

if __name__ == '__main__':
    print("Starting Kevin's Adventure Game web server...")
    print("Open your browser and navigate to http://localhost:5000")
    app.run(debug=True, host='0.0.0.0', port=5000)

