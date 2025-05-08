🌈🌈
# Kevin's Adventure Game

A text-based adventure game where you explore a magical world filled with quests, items, and mythical creatures.

Last updated: May 8, 2025  
OS: Linux modal 4.4.0 x86_64 GNU/Linux

## 🎮 Game Overview

Kevin's Adventure Game is an interactive text-based adventure where players navigate through different locations, interact with characters, collect items, and face mythical creatures. The game features dynamic weather systems, random events, and a save/load mechanism to continue your adventure.

## 🚀 Features

- **Multiple Locations**: Explore the village, forest, and mountain areas
- **Item Collection**: Find and use various items throughout your journey
- **Character Interaction**: Meet and interact with different characters
- **Weather System**: Dynamic weather that affects gameplay
- **Mythical Creatures**: Encounter various mythical beings
- **Save/Load System**: Save your progress and continue later

## 📋 Installation

1. Clone the repository:
   ```
   git clone https://github.com/codegen-sh/Kevin-s-Adventure-Game.git
   ```

2. Navigate to the game directory:
   ```
   cd Kevin-s-Adventure-Game
   ```

3. Run the game:
   ```
   python main.py
   ```

## 🎲 How to Play

1. Follow the text prompts that appear on screen
2. Type commands to interact with the game world:
   - `go [direction]` - Move in a direction (north, south, east, west)
   - `look` - Examine your surroundings
   - `inventory` or `i` - Check your inventory
   - `take [item]` - Pick up an item
   - `use [item]` - Use an item in your inventory
   - `talk [character]` - Speak with a character
   - `help` - Display available commands
   - `save` - Save your current progress
   - `load` - Load a previously saved game
   - `quit` - Exit the game

## 🧩 Game Structure

- `main.py` - Entry point for the game
- `game/` - Core game mechanics
  - `player.py` - Player character functionality
  - `items.py` - Item definitions and interactions
  - `world.py` - World map and navigation
  - `state.py` - Game state management
  - `weather.py` - Weather system
  - `mythical.py` - Mythical creatures
- `locations/` - Different game locations
  - `village.py` - Village area
  - `forest.py` - Forest area
  - `mountain.py` - Mountain area
- `utils/` - Utility functions
  - `save_load.py` - Save/load functionality
  - `text_formatting.py` - Text display utilities
  - `random_events.py` - Random event generator

## 🤝 Contributing

This is a test repository, but feel free to fork it and create your own adventure!

## 📝 License

This project is open source and available for educational purposes.

