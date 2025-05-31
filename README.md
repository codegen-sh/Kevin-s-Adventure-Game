# 🏰 Kevin's Adventure Game

A modern text-based adventure game with a React frontend and Python FastAPI backend, organized as a monorepo.

## 🌟 Features

- **Interactive Web Interface**: Modern React frontend with responsive design
- **Real-time Game State**: Live updates and smooth user experience
- **RESTful API**: FastAPI backend with automatic documentation
- **Monorepo Architecture**: Organized workspace for both frontend and backend
- **Save/Load System**: Persistent game progress
- **Rich Game World**: Multiple locations, items, and interactive elements

## 🏗️ Architecture

This project uses a monorepo structure with the following organization:

```
Kevin-s-Adventure-Game/
├── packages/
│   ├── frontend/          # React TypeScript frontend
│   │   ├── src/
│   │   │   ├── components/    # React components
│   │   │   ├── services/      # API services
│   │   │   ├── types/         # TypeScript types
│   │   │   └── ...
│   │   └── package.json
│   └── backend/           # Python FastAPI backend
│       ├── api/               # API routes and main app
│       ├── game/              # Game logic modules
│       ├── locations/         # Location-specific code
│       ├── utils/             # Utility functions
│       ├── main.py            # Original CLI game
│       └── requirements.txt
├── scripts/               # Development and deployment scripts
├── package.json          # Root package.json with workspace config
└── README.md
```

## 🚀 Quick Start

### Prerequisites

- **Node.js** 18+ and npm 8+
- **Python** 3.8+
- **Git**

### Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/codegen-sh/Kevin-s-Adventure-Game.git
   cd Kevin-s-Adventure-Game
   ```

2. **Run the setup script:**
   ```bash
   ./scripts/setup-dev.sh
   ```

3. **Start development servers:**
   ```bash
   npm run dev
   ```

4. **Open your browser:**
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:8000
   - API Documentation: http://localhost:8000/docs

## 📝 Available Scripts

### Root Level Commands

- `npm run dev` - Start both frontend and backend in development mode
- `npm run build` - Build both frontend and backend for production
- `npm run test` - Run all tests
- `npm run install:all` - Install all dependencies

### Frontend Commands

- `npm run dev:frontend` - Start frontend development server
- `npm run build:frontend` - Build frontend for production

### Backend Commands

- `npm run dev:backend` - Start backend development server
- `npm run start:backend` - Start backend in production mode

## 🎮 How to Play

1. **Start the Game**: Enter your adventurer name on the start screen
2. **Explore**: Use commands like \"look around\", \"go to forest\", \"take item\"
3. **Interact**: Click quick action buttons or type custom commands
4. **Manage**: Check your inventory, health, and status
5. **Save**: Use the save button to preserve your progress

### Common Commands

- `look around` - Examine your current location
- `go to [location]` - Move to a different location
- `take [item]` - Pick up an item
- `use [item]` - Use an item from your inventory
- `check inventory` - View your items
- `check status` - View your character stats

## 🛠️ Development

### Backend Development

The backend is built with FastAPI and provides a RESTful API for the game logic.

**Key Files:**
- `packages/backend/api/main.py` - FastAPI application and routes
- `packages/backend/game/` - Core game logic modules
- `packages/backend/locations/` - Location-specific functionality

**API Endpoints:**
- `POST /game/new` - Create a new game session
- `GET /game/{session_id}/state` - Get current game state
- `POST /game/action` - Perform a game action
- `GET /game/{session_id}/save` - Save game progress

### Frontend Development

The frontend is built with React and TypeScript, providing a modern web interface.

**Key Components:**
- `StartScreen` - Game initialization
- `GameInterface` - Main game layout
- `PlayerStatus` - Character information display
- `LocationInfo` - Current location details
- `ActionInput` - Command input interface
- `GameLog` - Game message history

### Testing

```bash
# Run frontend tests
cd packages/frontend && npm test

# Run backend tests
cd packages/backend && python -m pytest
```

## 🔧 Configuration

### Environment Variables

Create `.env` files in the respective packages for environment-specific configuration:

**Frontend (.env):**
```
REACT_APP_API_URL=http://localhost:8000
```

**Backend (.env):**
```
CORS_ORIGINS=http://localhost:3000,http://127.0.0.1:3000
```

## 📦 Deployment

### Production Build

```bash
npm run build
```

### Docker Support (Coming Soon)

Docker configurations will be added for easy deployment.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Commit your changes: `git commit -m 'Add amazing feature'`
4. Push to the branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🎯 Roadmap

- [ ] Add more locations and quests
- [ ] Implement multiplayer functionality
- [ ] Add sound effects and music
- [ ] Create mobile app version
- [ ] Add achievement system
- [ ] Implement character progression

## 🐛 Known Issues

- Save files are currently stored locally on the backend
- Game sessions are stored in memory (will reset on server restart)

## 📞 Support

If you encounter any issues or have questions, please [open an issue](https://github.com/codegen-sh/Kevin-s-Adventure-Game/issues) on GitHub.

---

**Happy Adventuring!** 🗡️⚔️🛡️

