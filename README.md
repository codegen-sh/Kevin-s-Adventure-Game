🌈🌈
# Kevin's Adventure Game

A text-based adventure game where you navigate through different locations, interact with items, and experience random events in a fantasy world.

Last updated: May 12, 2025  
OS: Linux modal 4.4.0 x86_64 GNU/Linux

## 🎮 Game Overview

Kevin's Adventure Game is an interactive text-based adventure where players can:
- Explore different locations (forest, mountain, village)
- Collect and use items
- Interact with mythical creatures
- Experience dynamic weather changes
- Save and load game progress

## 📋 Requirements

- Python 3.6 or higher

## 🚀 Installation

1. Clone the repository:
   ```
   git clone https://github.com/codegen-sh/Kevin-s-Adventure-Game.git
   cd Kevin-s-Adventure-Game
   ```

2. No additional dependencies are required!

## 🎲 How to Play

1. Start the game:
   ```
   python main.py
   ```

2. Choose to start a new game or load a saved game
3. Follow the on-screen prompts to navigate through the world
4. Type commands to perform actions (see Command Reference below)

## 🎯 Command Reference

- `go [direction]` - Move in a specific direction (north, south, east, west)
- `look` - Examine your current surroundings
- `inventory` - Check your current items
- `take [item]` - Pick up an item
- `use [item]` - Use an item in your inventory
- `talk` - Interact with characters in your location
- `save` - Save your current game progress
- `help` - Display available commands
- `quit` - Save and exit the game

## 🗺️ Game Structure

The game is organized into several modules:

- `game/` - Core game mechanics
  - `player.py` - Player status and inventory management
  - `world.py` - World map and location tracking
  - `items.py` - Item definitions and interactions
  - `mythical.py` - Mythical creatures and encounters
  - `weather.py` - Dynamic weather system
  - `state.py` - Game state management

- `locations/` - Different game locations
  - `forest.py` - Forest location and events
  - `mountain.py` - Mountain location and events
  - `village.py` - Village location and events

- `utils/` - Utility functions
  - `save_load.py` - Game saving and loading functionality
  - `text_formatting.py` - Text display formatting
  - `random_events.py` - Random event generation

## 🔄 Contributing

This is a test repository for demonstration purposes. No contributions are currently being accepted.

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

