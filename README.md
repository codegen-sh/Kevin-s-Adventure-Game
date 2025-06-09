# 🌟 Kevin's Adventure Game

A rich, text-based adventure game featuring exploration, inventory management, mythical creatures, and dynamic weather systems.

## 🎮 Game Features

### 🗺️ Exploration
- **4 Unique Locations**: Village, Forest, Mountain, and Cave
- **Dynamic Location Connections**: Navigate between interconnected areas
- **Location-Specific Items**: Each area contains unique items to discover

### 🎒 Inventory & Items
- **Comprehensive Inventory System**: Collect, use, and manage items
- **Location-Based Items**: Find bread and maps in the village, berries and sticks in the forest, and more
- **Interactive Item Usage**: Items affect gameplay and player stats

### 🐉 Mythical Creatures
- **Creature Summoning System**: Encounter and interact with mythical beings
- **Player Assistance**: Creatures can aid your adventure in various ways

### 🌤️ Dynamic Weather
- **6 Weather Conditions**: Clear, cloudy, rainy, stormy, foggy, and windy
- **Weather Effects**: Environmental conditions that impact gameplay

### 💾 Save System
- **Game State Persistence**: Save and load your progress
- **Multiple Save Slots**: Manage different game sessions
- **Automatic Save**: Progress is saved when quitting

### 🎲 Random Events
- **Dynamic Encounters**: Experience unexpected events during your journey
- **Player Impact**: Events can heal, damage, or provide items to the player

## 🚀 Getting Started

### Prerequisites
- Python 3.6 or higher

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

### Basic Commands
- **help** - Display available commands and game instructions
- **quit** - Save your progress and exit the game

### Game Flow
1. **Start/Load**: Choose to start a new game or load a saved game
2. **Explore**: Navigate between the Village, Forest, Mountain, and Cave
3. **Interact**: Discover items, encounter creatures, and experience random events
4. **Manage**: Keep track of your health, inventory, and gold
5. **Save**: Your progress is automatically saved when you quit

### Locations

| Location | Description | Connected To | Notable Items |
|----------|-------------|--------------|---------------|
| **Village** | A peaceful village with friendly inhabitants | Forest, Mountain | Map, Bread |
| **Forest** | Dense, mysterious woodland | Village, Cave | Stick, Berries |
| **Cave** | Dark cave with glittering minerals | Forest | Torch, Gemstone |
| **Mountain** | Snow-capped peak with treacherous paths | Village | Rope, Pickaxe |

## 🏗️ Project Structure

```
Kevin-s-Adventure-Game/
├── main.py                 # Game entry point and main loop
├── game/                   # Core game mechanics
│   ├── items.py           # Item system and interactions
│   ├── mythical.py        # Mythical creature summoning
│   ├── player.py          # Player state and actions
│   ├── state.py           # World state management
│   ├── weather.py         # Dynamic weather system
│   └── world.py           # World initialization and location management
├── locations/             # Location-specific interactions
│   ├── forest.py          # Forest area gameplay
│   ├── mountain.py        # Mountain area gameplay
│   └── village.py         # Village area gameplay
└── utils/                 # Utility functions
    ├── random_events.py   # Random event generation
    ├── save_load.py       # Game save/load functionality
    └── text_formatting.py # Text display and formatting
```

## 🛠️ Technical Details

- **Language**: Python 3
- **Architecture**: Modular design with separated concerns
- **Save Format**: JSON-based save files
- **Text Interface**: Rich console-based interaction

## 🎨 Game Mechanics

### Player Stats
- **Health**: Affects survival and gameplay options
- **Gold**: Currency for transactions and upgrades
- **Inventory**: Collected items and tools
- **Location**: Current position in the game world

### Weather System
The game features a dynamic weather system that cycles through:
- Clear skies
- Cloudy conditions  
- Rainy weather
- Stormy conditions
- Foggy atmosphere
- Windy conditions

## 🤝 Contributing

This is a test repository for demonstrating text-based adventure game mechanics. Feel free to explore the code and understand the game structure!

## 📝 License

This project is a demonstration/test repository for educational purposes.

---

*Last updated: June 2025*  
*Compatible with: Python 3.6+*

