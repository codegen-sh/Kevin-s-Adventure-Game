🌈🌈
# Kevin's Adventure Game

A text-based adventure game where you play as Kevin, exploring a world filled with different locations, items, and mythical creatures.

Last updated: May 18, 2025  
OS: Linux modal 4.4.0 x86_64 GNU/Linux

## 🎮 Game Features

- **Multiple Locations**: Explore forests, mountains, villages, and more
- **Item Collection**: Find and use various items throughout your journey
- **Player Status**: Track your health, inventory, and progress
- **Save/Load System**: Continue your adventure where you left off
- **Weather System**: Experience different weather conditions that affect gameplay
- **Random Events**: Encounter unexpected situations that make each playthrough unique
- **Mythical Creatures**: Interact with various mythical beings throughout the game

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
2. Follow the prompts and type your actions to navigate through the game world.
3. Type 'help' at any time to see available commands.
4. Type 'quit' to save your progress and exit the game.

## 🧩 Game Structure

- **game/**: Core game mechanics and objects
  - `player.py`: Player character management
  - `world.py`: Game world and location management
  - `items.py`: In-game items and their effects
  - `mythical.py`: Mythical creatures and interactions
  - `weather.py`: Weather system affecting gameplay
  - `state.py`: Game state management

- **locations/**: Different areas to explore
  - `forest.py`: Forest location and events
  - `mountain.py`: Mountain location and events
  - `village.py`: Village location and events

- **utils/**: Helper functions
  - `save_load.py`: Game saving and loading functionality
  - `text_formatting.py`: Text display and formatting
  - `random_events.py`: Random event generation

## 🛠️ Development

This is a test repository for experimenting with game development concepts. Feel free to fork and expand upon the game with new features, locations, or gameplay mechanics.

## 📝 License

This project is open source and available for educational purposes.

