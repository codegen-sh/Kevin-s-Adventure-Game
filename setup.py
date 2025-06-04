#!/usr/bin/env python3
"""Setup script for Kevin's Adventure Game."""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="kevins-adventure-game",
    version="1.0.0",
    author="Kevin",
    description="A text-based adventure game with modular design",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/codegen-sh/Kevin-s-Adventure-Game",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Games/Entertainment :: Role-Playing",
    ],
    python_requires=">=3.7",
    entry_points={
        "console_scripts": [
            "kevins-adventure=main:main",
        ],
    },
    extras_require={
        "dev": [
            "black>=23.0.0",
            "flake8>=6.0.0",
            "mypy>=1.0.0",
            "pytest>=7.0.0",
            "sphinx>=5.0.0",
            "pre-commit>=3.0.0",
            "sphinx-rtd-theme>=1.0.0",
        ],
    },
)

