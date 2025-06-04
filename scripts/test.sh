#!/bin/bash
# Run tests

echo "Running unit tests..."
python -m pytest tests/ -v

echo "Running tests with coverage..."
python -m pytest tests/ --cov=game --cov=utils --cov=locations --cov-report=html --cov-report=term

echo "Testing complete!"
echo "Coverage report available in htmlcov/index.html"
