# Kevin's Adventure Game Architecture

This document describes the architecture of Kevin's Adventure Game, a text-based adventure game.

## Overview

The game is built using a modular, object-oriented architecture that separates concerns and makes the code more maintainable. The main components are:

1. **Game Engine**: Manages the game loop and user input processing
2. **Player**: Represents the player character and their state
3. **World**: Represents the game world and locations
4. **Items**: Represents items that can be found and used in the game
5. **Commands**: Implements the command pattern for handling player actions
6. **Locations**: Represents different locations in the game world
7. **Utilities**: Provides utility functions for the game

## Component Details

### Game Engine

The `GameEngine` class in `game/engine.py` is responsible for:
- Starting a new game
- Loading and saving games
- Running the main game loop
- Processing user input

### Player

The `Player` class in `game/player.py` represents the player character and their state:
- Name
- Health
- Inventory
- Location
- Gold

It provides methods for:
- Getting player status
- Adding and removing items from inventory
- Moving to a new location
- Healing and taking damage

### World

The `World` class in `game/world.py` represents the game world and its locations:
- Current location
- Available locations
- Location descriptions
- Location connections
- Items at each location

It provides methods for:
- Getting the current location
- Changing the current location
- Getting available locations
- Interacting with locations

### Items

The `Item` class in `game/items.py` represents items that can be found and used in the game:
- Name
- Description
- Use effect
- Consumable flag

It provides methods for:
- Using items
- Getting item descriptions

### Commands

The command pattern is implemented in `game/commands.py` to handle player actions:
- `Command`: Abstract base class for commands
- Concrete command classes for each action type (move, look, inventory, etc.)
- Command registry for looking up commands by name

### Locations

Each location in the game is represented by a module in the `locations/` directory:
- `cave.py`: Cave location and events
- `forest.py`: Forest location and events
- `mountain.py`: Mountain location and events
- `village.py`: Village location and events

### Utilities

Utility functions are provided in the `utils/` directory:
- `random_events.py`: Generates random events
- `save_load.py`: Handles saving and loading games
- `text_formatting.py`: Formats text output

## Design Patterns

The game uses several design patterns:

1. **Command Pattern**: Used for handling player actions
2. **Factory Pattern**: Used for creating game objects
3. **Singleton Pattern**: Used for the game engine
4. **Strategy Pattern**: Used for item use effects

## Data Flow

1. The game engine processes user input
2. The input is parsed and converted to a command
3. The command is executed, updating the player and world state
4. The updated state is displayed to the user
5. The process repeats until the game ends

## Extensibility

The game is designed to be easily extensible:

1. **Adding new commands**: Create a new command class in `game/commands.py` and add it to the command registry
2. **Adding new items**: Add a new item to the `ITEMS` dictionary in `game/items.py`
3. **Adding new locations**: Create a new location module in the `locations/` directory and update the world initialization in `game/world.py`
4. **Adding new events**: Add new event functions to the location modules

