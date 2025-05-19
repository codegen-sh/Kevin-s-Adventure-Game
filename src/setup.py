"""
Setup script for Kevin's Adventure Game.
"""
from setuptools import find_packages, setup

setup(
    name="kevin_adventure",
    version="1.0.0",
    description="A text-based adventure game",
    author="Kevin",
    packages=find_packages(),
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "kevin-adventure=main:main",
        ],
    },
)

