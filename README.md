🌈🌈
# Kevin's Adventure Game

A text-based adventure game where you explore a magical world, collect items, and embark on exciting quests.

Last updated: April 30, 2025  
OS: Linux modal 4.4.0 x86_64 GNU/Linux

## 🎮 Game Overview

Kevin's Adventure Game is an interactive text-based adventure where you navigate through various locations including:
- A peaceful village
- A mysterious forest
- A dark cave
- A treacherous mountain

During your journey, you'll:
- Collect and use items
- Interact with your environment
- Manage your health and inventory
- Experience random events
- Encounter mythical creatures

## 🚀 Installation

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

## 🎯 How to Play

1. When you start the game, you'll be asked if you want to load a saved game or start a new one.
2. You'll begin in the village with some gold and basic items.
3. Navigate through the world by typing commands at the prompt.
4. Your goal is to explore all locations, collect valuable items, and survive your adventure.

### Available Commands

- `move [location]`: Move to a new location
- `look`: Examine your surroundings
- `inventory`: Check your inventory
- `pickup [item]`: Pick up an item
- `drop [item]`: Drop an item from your inventory
- `use [item]`: Use an item
- `examine [item]`: Get a description of an item
- `status`: Check your current status
- `interact`: Interact with your current location
- `help`: Show the help message
- `quit`: Save and exit the game

## 💾 Save/Load System

The game automatically saves your progress when you quit. You can load your saved game when you start the game again.

## 🧩 Game Structure

The game is organized into several modules:

- `main.py`: The main game loop and entry point
- `game/`: Core game mechanics
  - `player.py`: Player stats and inventory management
  - `world.py`: World map and location management
  - `items.py`: Item definitions and interactions
  - `mythical.py`: Mythical creatures and encounters
  - `state.py`: Game state management
  - `weather.py`: Weather system affecting gameplay
- `locations/`: Location-specific interactions
  - `village.py`: Village interactions
  - `forest.py`: Forest interactions
  - `mountain.py`: Mountain interactions
- `utils/`: Utility functions
  - `text_formatting.py`: Text display formatting
  - `save_load.py`: Game save/load functionality
  - `random_events.py`: Random event generation

## 🛠️ Development

This is a test repository for demonstrating game development concepts. Feel free to fork and extend with your own features!

## 📝 License

This project is open source and available for educational purposes.

