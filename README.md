# 🎮 Kevin's Adventure Game

A text-based adventure game where you explore a mystical world filled with forests, caves, villages, and mountains. Embark on an epic journey as Kevin, collecting items, interacting with characters, and uncovering the secrets of this magical realm.

## 🌟 Features

- **Multiple Locations**: Explore diverse environments including:
  - 🏘️ Village - A bustling settlement with shops and NPCs
  - 🌲 Forest - Lush woodlands with hidden treasures and creatures
  - ⛰️ Mountain - Challenging peaks with rare items and dangers
  - 🕳️ Cave - Dark underground passages with mysteries to uncover

- **Dynamic Gameplay**:
  - 🎒 Inventory management system
  - 💰 Gold and trading mechanics
  - 🌤️ Dynamic weather system
  - 🐉 Mythical creature encounters
  - 🎲 Random events and encounters
  - 💾 Save/Load game functionality

- **Rich Interactions**:
  - Item collection and usage
  - Character interactions
  - Location-specific activities
  - Status tracking (health, inventory, location)

## 🚀 Getting Started

### Prerequisites

- Python 3.6 or higher
- No additional dependencies required (uses only Python standard library)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/codegen-sh/Kevin-s-Adventure-Game.git
   cd Kevin-s-Adventure-Game
   ```

2. **Run the game:**
   ```bash
   python main.py
   ```

## 🎯 How to Play

### Starting the Game

When you launch the game, you'll be prompted to either:
- Start a new adventure as Kevin
- Load a previously saved game

### Available Commands

| Command | Description |
|---------|-------------|
| `move [location]` | Travel to a new location |
| `look` | Examine your current surroundings |
| `inventory` | Check your current items |
| `pickup [item]` | Collect an item |
| `drop [item]` | Remove an item from inventory |
| `use [item]` | Use an item from your inventory |
| `examine [item]` | Get detailed information about an item |
| `status` | View your current health, gold, and location |
| `interact` | Engage with your current location |
| `help` | Display all available commands |
| `quit` | Save your progress and exit the game |

### Game Tips

- 💡 Type `help` anytime to see available commands
- 💾 Your game automatically saves when you quit
- 🔍 Use `look` and `examine` to discover hidden items and secrets
- 💰 Manage your gold wisely for trading in villages
- ❤️ Keep an eye on your health during adventures

## 📁 Project Structure

```
Kevin-s-Adventure-Game/
├── main.py                 # Main game entry point
├── game/                   # Core game mechanics
│   ├── items.py           # Item definitions and management
│   ├── mythical.py        # Mythical creature system
│   ├── player.py          # Player state and actions
│   ├── state.py           # Game state management
│   ├── weather.py         # Dynamic weather system
│   └── world.py           # World initialization and management
├── locations/             # Location-specific content
│   ├── forest.py          # Forest area interactions
│   ├── mountain.py        # Mountain area interactions
│   └── village.py         # Village area interactions
├── utils/                 # Utility functions
│   ├── random_events.py   # Random event generation
│   ├── save_load.py       # Save/load game functionality
│   └── text_formatting.py # Text display and formatting
└── README.md              # This file
```

## 🎨 Game Features in Detail

### Locations
- **Village**: Trade with merchants, interact with NPCs, and resupply
- **Forest**: Encounter wildlife, find herbs, and discover hidden paths
- **Mountain**: Face challenging terrain, find rare minerals, and test your courage
- **Cave**: Explore dark passages, find ancient artifacts, and face underground dangers

### Weather System
The game features a dynamic weather system that affects gameplay:
- ☀️ Clear skies
- ☁️ Cloudy conditions
- 🌧️ Rainy weather
- ⛈️ Storms
- 🌫️ Fog
- 💨 Windy conditions

### Save System
- Automatic save on quit
- Multiple save slots supported
- Load any previous save file
- Progress preservation across sessions

## 🤝 Contributing

This is a test repository for educational purposes. Feel free to:
- Report bugs or issues
- Suggest new features
- Submit improvements
- Add new locations or items

## 📝 License

This project is created for educational and testing purposes.

## 🎮 About

Kevin's Adventure Game is a text-based RPG that demonstrates classic adventure game mechanics in Python. Perfect for learning game development concepts or enjoying a nostalgic text-based gaming experience.

---

**Last Updated**: May 29, 2025  
**Version**: 1.0  
**Platform**: Cross-platform (Python)

Happy adventuring! 🗺️✨

