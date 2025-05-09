🌈🌈
# Kevin's Adventure Game

A text-based adventure game where you explore a magical world, collect items, and embark on an epic journey.

Last updated: May 9, 2025  
OS: Linux modal 4.4.0 x86_64 GNU/Linux

## 🎮 Game Overview

Kevin's Adventure Game is an interactive text-based adventure where you:
- Explore different locations (Village, Forest, Mountain)
- Collect and use items
- Manage your health and gold
- Interact with the environment
- Experience random events and weather changes

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
2. Follow the on-screen prompts to navigate through the world.
3. Type commands to perform actions (see Command Reference below).
4. Manage your inventory, health, and gold to survive and thrive.
5. Explore all locations to discover the secrets of the world.

## 📝 Command Reference

- `move [location]`: Move to a new location (Village, Forest, Mountain)
- `look`: Examine your surroundings
- `inventory`: Check your inventory
- `pickup [item]`: Pick up an item
- `drop [item]`: Drop an item from your inventory
- `use [item]`: Use an item
- `examine [item]`: Get a description of an item
- `status`: Check your current status
- `interact`: Interact with your current location
- `help`: Show the help message with available commands
- `quit`: Save and exit the game

## 💾 Save/Load System

- Your game is automatically saved when you quit.
- You can load a previous save when starting the game.
- Multiple save files are supported.

## 🧩 Game Structure

- `main.py`: Main game loop and initialization
- `game/`: Core game mechanics
  - Player management
  - World state
  - Items and inventory
  - Weather system
- `locations/`: Different game locations
- `utils/`: Helper functions
  - Text formatting
  - Save/load functionality
  - Random events

## 🛠️ Development

This is a test repository for TinySitter. Feel free to explore the code and make modifications to enhance the game!

## 📜 License

This project is open source and available for educational purposes.

