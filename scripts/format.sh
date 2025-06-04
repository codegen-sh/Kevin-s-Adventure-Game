#!/bin/bash
# Format code using Black

echo "Formatting Python code with Black..."
black .

echo "Sorting imports with isort..."
isort .

echo "Code formatting complete!"
