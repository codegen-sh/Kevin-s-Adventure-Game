🌈🌈
# Kevin's Adventure Game

A text-based adventure game where you play as Kevin, exploring a world filled with villages, forests, mountains, and mythical creatures.

Last updated: May 8, 2025  
OS: Linux modal 4.4.0 x86_64 GNU/Linux

## 🎮 Game Overview

Kevin's Adventure Game is an interactive text-based adventure where players navigate through different locations, collect items, interact with the environment, and face various challenges. The game features:

- Multiple locations to explore (Village, Forest, Mountain)
- Inventory management system
- Health and gold economy
- Random events and weather effects
- Save/load game functionality
- Mythical creatures and special items

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
2. If starting a new game, you'll begin in the Village with 100 health and 100 gold.
3. Navigate through the world by typing commands like "go forest" or "go mountain".
4. Interact with your environment by typing actions like "pick up sword" or "talk to villager".
5. Type "help" at any time to see available commands.
6. Type "quit" to save your progress and exit the game.

## 🧩 Game Commands

- `go [location]` - Move to a different location (village, forest, mountain)
- `pick up [item]` - Add an item to your inventory
- `drop [item]` - Remove an item from your inventory
- `use [item]` - Use an item from your inventory
- `look` - Examine your surroundings
- `inventory` or `i` - Check your inventory
- `status` - Check your health and gold
- `help` - Display available commands
- `save` - Save your current game
- `quit` - Save and exit the game

## 📁 Project Structure

- `main.py` - Main game loop and entry point
- `game/` - Core game mechanics
  - `player.py` - Player stats and inventory management
  - `world.py` - World state and location management
  - `items.py` - Item definitions and effects
  - `mythical.py` - Mythical creatures and encounters
  - `weather.py` - Weather system affecting gameplay
  - `state.py` - Game state management
- `locations/` - Different game locations
  - `village.py` - Village location and interactions
  - `forest.py` - Forest location and interactions
  - `mountain.py` - Mountain location and interactions
- `utils/` - Utility functions
  - `save_load.py` - Game save/load functionality
  - `text_formatting.py` - Text display utilities
  - `random_events.py` - Random event generation

## 🤝 Contributing

This is a test repository, but contributions are welcome! Feel free to fork the repository and submit pull requests.

## 📝 License

This project is open source and available for educational purposes.

