#!/bin/bash
# Run linting checks

echo "Running flake8 linting..."
flake8 .

echo "Running mypy type checking..."
mypy .

echo "Running pylint..."
pylint game/ utils/ locations/ || true

echo "Linting complete!"
