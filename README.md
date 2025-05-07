🌈🌈
# Kevin's Adventure Game

A text-based adventure game where you navigate through different locations, collect items, and encounter mythical creatures.

Last updated: May 7, 2025  
OS: Linux modal 4.4.0 x86_64 GNU/Linux

## Description

Kevin's Adventure Game is an interactive text-based adventure where players can explore various locations including forests, mountains, and villages. Players can collect items, interact with the environment, and experience random events based on weather conditions.

## Features

- Multiple locations to explore (Forest, Mountain, Village)
- Item collection and inventory management
- Weather system that affects gameplay
- Mythical creature encounters
- Save and load game functionality
- Random events during gameplay

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/codegen-sh/Kevin-s-Adventure-Game.git
   ```

2. Navigate to the project directory:
   ```
   cd Kevin-s-Adventure-Game
   ```

3. Make sure you have Python installed (Python 3.6 or higher recommended)

## Usage

1. Run the game:
   ```
   python main.py
   ```

2. Follow the on-screen prompts to play the game
3. Type 'help' at any time to see available commands
4. Type 'quit' to save your progress and exit the game

## Game Commands

- `help` - Display available commands
- `look` - Examine your surroundings
- `go [direction]` - Move in a direction (north, south, east, west)
- `take [item]` - Pick up an item
- `use [item]` - Use an item from your inventory
- `inventory` - Check your inventory
- `status` - Check your player status
- `save` - Save your current game
- `quit` - Save and exit the game

## Project Structure

```
Kevin-s-Adventure-Game/
├── game/
│   ├── items.py       - Item definitions and functionality
│   ├── mythical.py    - Mythical creature encounters
│   ├── player.py      - Player character functionality
│   ├── state.py       - Game state management
│   ├── weather.py     - Weather system
│   └── world.py       - World and location management
├── locations/
│   ├── forest.py      - Forest location
│   ├── mountain.py    - Mountain location
│   └── village.py     - Village location
├── utils/
│   ├── random_events.py    - Random event generation
│   ├── save_load.py        - Save/load game functionality
│   └── text_formatting.py  - Text display utilities
└── main.py            - Main game loop
```

## Contributing

This is a test repository. Feel free to fork and experiment with the code!

## License

This project is open source and available for educational purposes.

