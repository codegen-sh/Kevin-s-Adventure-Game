#!/bin/bash

# Kevin's Adventure Game - Development Setup Script

echo "🏰 Setting up Kevin's Adventure Game development environment..."

# Check if Node.js is installed
if ! command -v node &> /dev/null; then
    echo "❌ Node.js is not installed. Please install Node.js 18+ first."
    exit 1
fi

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8+ first."
    exit 1
fi

# Install root dependencies
echo "📦 Installing root dependencies..."
npm install

# Setup backend
echo "🐍 Setting up backend..."
cd packages/backend

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating Python virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment and install dependencies
echo "Installing Python dependencies..."
source venv/bin/activate
pip install -r requirements.txt

cd ../..

# Setup frontend
echo "⚛️ Setting up frontend..."
cd packages/frontend
npm install

cd ../..

echo "✅ Development environment setup complete!"
echo ""
echo "🚀 To start development:"
echo "   npm run dev"
echo ""
echo "📝 Available commands:"
echo "   npm run dev          - Start both frontend and backend in development mode"
echo "   npm run dev:frontend - Start only frontend"
echo "   npm run dev:backend  - Start only backend"
echo "   npm run build        - Build both frontend and backend"
echo "   npm run test         - Run all tests"
echo ""
echo "🌐 URLs:"
echo "   Frontend: http://localhost:3000"
echo "   Backend API: http://localhost:8000"
echo "   API Docs: http://localhost:8000/docs"

