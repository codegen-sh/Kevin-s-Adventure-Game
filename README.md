🌈🌈
# Kevin's Adventure Game

A text-based adventure game where you navigate through different locations, interact with items, and experience random events in a fantasy world.

Last updated: May 12, 2025  
OS: Linux modal 4.4.0 x86_64 GNU/Linux

## Overview

Kevin's Adventure Game is an interactive text-based adventure where players can explore various locations including forests, mountains, and villages. The game features a dynamic weather system, mythical creatures, and random events that create a unique experience with each playthrough.

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/codegen-sh/Kevin-s-Adventure-Game.git
   ```

2. Navigate to the project directory:
   ```
   cd Kevin-s-Adventure-Game
   ```

3. Run the game:
   ```
   python main.py
   ```

## Game Features

- **Multiple Locations**: Explore forests, mountains, and villages, each with unique characteristics and challenges
- **Dynamic Weather System**: Experience changing weather conditions that affect gameplay
- **Item Collection**: Find and use various items throughout your adventure
- **Player Stats**: Track your progress with player statistics
- **Save/Load System**: Save your progress and continue your adventure later
- **Random Events**: Encounter unexpected situations that make each playthrough unique
- **Mythical Creatures**: Interact with fantasy beings throughout your journey

## Game Structure

- `main.py`: Entry point for the game
- `game/`: Core game mechanics
  - `player.py`: Player character management
  - `items.py`: Item definitions and interactions
  - `world.py`: World map and navigation
  - `state.py`: Game state management
  - `weather.py`: Dynamic weather system
  - `mythical.py`: Mythical creatures and encounters
- `locations/`: Different game locations
  - `forest.py`: Forest location and events
  - `mountain.py`: Mountain location and events
  - `village.py`: Village location and events
- `utils/`: Utility functions
  - `random_events.py`: Random event generation
  - `save_load.py`: Game save/load functionality
  - `text_formatting.py`: Text display formatting

## Commands

- `help`: Display available commands
- `look`: Examine your surroundings
- `go [direction]`: Move in a specified direction
- `take [item]`: Pick up an item
- `use [item]`: Use an item in your inventory
- `inventory`: Check your current items
- `stats`: View your player statistics
- `save`: Save your current game
- `load`: Load a previously saved game
- `quit`: Exit the game

## Contributing

This is a test repository. Feel free to fork and experiment with the code!

## License

This project is for testing purposes only.

