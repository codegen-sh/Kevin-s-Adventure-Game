🌈🌈
# Kevin's Adventure Game

A text-based adventure game where you explore a magical world filled with villages, forests, caves, and mountains.

Last updated: May 8, 2025  
OS: Linux modal 4.4.0 x86_64 GNU/Linux

## Game Overview

In Kevin's Adventure Game, you play as Kevin, an adventurer exploring a world full of mystery and danger. Navigate through different locations, collect items, manage your health and gold, and uncover the secrets of this magical realm.

### Features

- **Multiple Locations**: Explore a village, forest, cave, and mountain, each with unique items and challenges
- **Inventory System**: Collect, use, and drop items throughout your journey
- **Health Management**: Monitor your health as you face dangers in your adventure
- **Save/Load System**: Save your progress and continue your adventure later
- **Random Events**: Encounter unexpected situations that make each playthrough unique

## Installation

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

## How to Play

When you start the game, you'll have the option to load a saved game or start a new adventure. If you start a new game, you'll begin in the village with some gold and an empty inventory.

### Available Commands

- `move [location]`: Move to a new location (e.g., `move Forest`)
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

### Locations

- **Village**: A small, peaceful village with thatched-roof houses and friendly inhabitants
- **Forest**: A dense, mysterious forest with towering trees and the sound of rustling leaves
- **Cave**: A dark, damp cave with echoing sounds and glittering minerals on the walls
- **Mountain**: A tall, snow-capped mountain with treacherous paths and breathtaking views

### Items

Each location contains unique items that you can collect and use:

- Village: map, bread
- Forest: stick, berries
- Cave: torch, gemstone
- Mountain: rope, pickaxe

## Game Structure

The game is organized into several modules:

- `main.py`: The main game loop and entry point
- `game/`: Core game mechanics (player, world, items)
- `locations/`: Location-specific interactions
- `utils/`: Utility functions for saving/loading, text formatting, and random events

## Contributing

Feel free to fork this repository and contribute to the game by adding new locations, items, or gameplay mechanics!

## License

This project is open source and available for educational purposes.

