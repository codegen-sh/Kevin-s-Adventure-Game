"""
Setup script for Kevin's Adventure Game.
"""
from setuptools import setup, find_packages

setup(
    name="kevins-adventure-game",
    version="0.1.0",
    description="A text-based adventure game",
    author="Codegen",
    packages=find_packages(),
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "kevins-adventure=main:main",
        ],
    },
)

