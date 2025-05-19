# 🎮 Kevin's Adventure Game

A text-based adventure game where you navigate through different locations, interact with items, and experience random events in a fantasy world.

## 📖 About

Kevin's Adventure Game is an interactive text-based adventure where players can explore various locations including forests, mountains, and villages. The game features a dynamic weather system, mythical creatures, and random events that create a unique experience with each playthrough.

Last updated: May 19, 2025

## 🚀 Features

- **Multiple Locations**: Explore forests, mountains, and villages
- **Dynamic Weather System**: Experience changing weather conditions that affect gameplay
- **Inventory Management**: Collect and use items throughout your adventure
- **Mythical Creatures**: Encounter various mythical beings during your journey
- **Save/Load System**: Save your progress and continue your adventure later

## 🛠️ Installation

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

## 🎮 How to Play

1. Follow the text prompts that appear on screen
2. Type commands to navigate and interact with the game world
3. Common commands include:
   - `go [direction]` - Move in a specific direction (north, south, east, west)
   - `look` - Examine your surroundings
   - `inventory` or `i` - Check your inventory
   - `take [item]` - Pick up an item
   - `use [item]` - Use an item in your inventory
   - `talk to [character]` - Interact with characters
   - `save` - Save your current progress
   - `load` - Load a previously saved game
   - `help` - Display available commands
   - `quit` - Exit the game

## 🧩 Game Structure

- **game/**: Core game mechanics
  - `items.py`: Item definitions and interactions
  - `mythical.py`: Mythical creature encounters
  - `player.py`: Player character attributes and actions
  - `state.py`: Game state management
  - `weather.py`: Dynamic weather system
  - `world.py`: World building and environment
- **locations/**: Different areas to explore
  - `forest.py`: Forest location and events
  - `mountain.py`: Mountain location and events
  - `village.py`: Village location and interactions
- **utils/**: Helper functions
  - `random_events.py`: Random event generation
  - `save_load.py`: Game saving and loading functionality
  - `text_formatting.py`: Text display formatting

## 🤝 Contributing

This is a test repository, but contributions, suggestions, and feedback are welcome!

## 📜 License

This project is open source and available for educational purposes.

