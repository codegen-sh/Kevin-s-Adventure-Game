🌈🌈
# 🎮 Kevin's Adventure Game

A text-based adventure game where you explore a fantasy world, collect items, interact with characters, and uncover secrets.

![Game Banner](https://img.shields.io/badge/Game-Adventure-brightgreen)
![Python](https://img.shields.io/badge/Python-3.6+-blue)
![License](https://img.shields.io/badge/License-MIT-yellow)

## 📖 Description

Kevin's Adventure Game is a text-based adventure game where you navigate through various locations including villages, forests, caves, and mountains. Along your journey, you'll:

- Collect and use items
- Interact with NPCs
- Experience random events
- Solve puzzles
- Discover hidden locations
- Battle enemies
- Save and load your progress

## 🚀 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/codegen-sh/Kevin-s-Adventure-Game.git
   cd Kevin-s-Adventure-Game
   ```

2. Make sure you have Python 3.6+ installed:
   ```bash
   python --version
   ```

3. Run the game:
   ```bash
   python main.py
   ```

## 🎮 How to Play

1. When you start the game, you'll be asked if you want to load a saved game or start a new one.
2. If starting a new game, you'll be prompted to enter your character's name.
3. You'll begin your adventure in the Village.
4. Type commands to interact with the game world.

### Commands

- **Movement**:
  - `go [location]` or `move [location]`: Travel to a connected location
  - `locations`: Show available locations you can travel to

- **Exploration**:
  - `look` or `look around`: Examine your surroundings
  - `examine [item]` or `look [item]`: Get a description of an item

- **Inventory**:
  - `inventory` or `inv`: Check your inventory
  - `take [item]` or `pickup [item]`: Pick up an item
  - `drop [item]`: Drop an item from your inventory
  - `use [item]` or `interact [item]`: Use an item from your inventory

- **Other**:
  - `interact`: Interact with your current location
  - `status`: Check your current health, gold, and inventory
  - `help`: Show the help message
  - `quit`: Save and exit the game

## 🗺️ Game World

The game world consists of several interconnected locations:

- **Village**: A peaceful starting area with friendly NPCs
- **Forest**: A mysterious woodland with valuable resources and potential dangers
- **Cave**: A dark cavern with hidden treasures and traps
- **Mountain**: A challenging terrain with rare items and spectacular views

## 💾 Save System

- The game automatically saves your progress when you quit
- You can have multiple save files for different playthroughs
- Save files are stored in the `saves` directory

## 🛠️ Project Structure

```
Kevin-s-Adventure-Game/
├── game/                  # Core game mechanics
│   ├── actions.py         # Player action handling
│   ├── items.py           # Item definitions and effects
│   ├── mythical.py        # Mythical creatures and events
│   ├── player.py          # Player state management
│   ├── state.py           # Game state tracking
│   ├── weather.py         # Weather system
│   └── world.py           # World generation and management
├── locations/             # Location-specific code
│   ├── cave.py            # Cave location logic
│   ├── forest.py          # Forest location logic
│   ├── mountain.py        # Mountain location logic
│   └── village.py         # Village location logic
├── utils/                 # Utility functions
│   ├── random_events.py   # Random event generation
│   ├── save_load.py       # Save/load functionality
│   └── text_formatting.py # Text display formatting
├── main.py                # Main game entry point
└── README.md              # This file
```

## 🤝 Contributing

Contributions are welcome! Feel free to submit a pull request or open an issue if you have ideas for improvements or have found a bug.

## 📜 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgements

- Inspired by classic text adventure games
- Special thanks to all contributors and testers
