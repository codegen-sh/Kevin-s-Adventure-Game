from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import Dict, List, Optional, Any
import uuid
import json
from datetime import datetime

from game.player import create_player, get_player_status
from game.world import initialize_world, get_current_location
from game.actions import perform_action
from utils.save_load import save_game_data, load_game_data
from utils.text_formatting import get_help_text

app = FastAPI(
    title="Kevin's Adventure Game API",
    description="A RESTful API for Kevin's Adventure Game",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# In-memory storage for game sessions (in production, use a database)
game_sessions: Dict[str, Dict[str, Any]] = {}

# Pydantic models for API requests/responses
class GameSession(BaseModel):
    session_id: str
    player_name: str
    created_at: datetime
    last_updated: datetime

class PlayerStatus(BaseModel):
    name: str
    health: int
    max_health: int
    experience: int
    level: int
    inventory: List[Dict[str, Any]]
    location: str
    status_text: str

class GameAction(BaseModel):
    action: str

class GameResponse(BaseModel):
    success: bool
    message: str
    player_status: Optional[PlayerStatus] = None
    location: Optional[str] = None
    available_actions: Optional[List[str]] = None

class SaveGameRequest(BaseModel):
    save_name: str

# Helper functions
def get_session(session_id: str) -> Dict[str, Any]:
    if session_id not in game_sessions:
        raise HTTPException(status_code=404, detail="Game session not found")
    return game_sessions[session_id]

def create_player_status(player: Dict[str, Any], world: Dict[str, Any]) -> PlayerStatus:
    status_text = get_player_status(player)
    current_location = get_current_location(world)
    
    return PlayerStatus(
        name=player.get("name", "Unknown"),
        health=player.get("health", 100),
        max_health=player.get("max_health", 100),
        experience=player.get("experience", 0),
        level=player.get("level", 1),
        inventory=player.get("inventory", []),
        location=current_location,
        status_text=status_text
    )

# API Routes
@app.get("/")
async def root():
    return {"message": "Welcome to Kevin's Adventure Game API!"}

@app.post("/game/new", response_model=GameSession)
async def create_new_game(player_name: str = "Kevin"):
    """Create a new game session"""
    session_id = str(uuid.uuid4())
    player = create_player(player_name)
    world = initialize_world()
    
    game_sessions[session_id] = {
        "player": player,
        "world": world,
        "created_at": datetime.now(),
        "last_updated": datetime.now()
    }
    
    return GameSession(
        session_id=session_id,
        player_name=player_name,
        created_at=datetime.now(),
        last_updated=datetime.now()
    )

@app.get("/game/{session_id}/status", response_model=PlayerStatus)
async def get_game_status(session_id: str):
    """Get current game status"""
    session = get_session(session_id)
    return create_player_status(session["player"], session["world"])

@app.post("/game/{session_id}/action", response_model=GameResponse)
async def perform_game_action(session_id: str, action: GameAction):
    """Perform a game action"""
    session = get_session(session_id)
    player = session["player"]
    world = session["world"]
    
    try:
        # Perform the action using the existing game logic
        result = perform_action(player, world, action.action.lower())
        
        # Update session timestamp
        session["last_updated"] = datetime.now()
        
        # Get updated status
        player_status = create_player_status(player, world)
        current_location = get_current_location(world)
        
        return GameResponse(
            success=True,
            message=f"Action '{action.action}' performed successfully",
            player_status=player_status,
            location=current_location,
            available_actions=get_available_actions(current_location)
        )
    except Exception as e:
        return GameResponse(
            success=False,
            message=f"Error performing action: {str(e)}"
        )

@app.get("/game/{session_id}/help")
async def get_help(session_id: str):
    """Get help information"""
    get_session(session_id)  # Verify session exists
    return {"help_text": get_help_text()}

@app.post("/game/{session_id}/save")
async def save_game(session_id: str, save_request: SaveGameRequest):
    """Save the current game state"""
    session = get_session(session_id)
    
    try:
        save_game_data(session["player"], session["world"], save_request.save_name)
        return {"success": True, "message": f"Game saved as '{save_request.save_name}'"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to save game: {str(e)}")

@app.get("/game/saves")
async def list_saves():
    """List all available save files"""
    try:
        from utils.save_load import list_save_files
        saves = list_save_files()
        return {"saves": saves}
    except Exception as e:
        return {"saves": [], "error": str(e)}

@app.post("/game/load/{save_name}")
async def load_game(save_name: str):
    """Load a saved game"""
    try:
        from utils.save_load import load_game
        player, world = load_game(save_name)
        
        if player is None or world is None:
            raise HTTPException(status_code=404, detail="Save file not found or corrupted")
        
        session_id = str(uuid.uuid4())
        game_sessions[session_id] = {
            "player": player,
            "world": world,
            "created_at": datetime.now(),
            "last_updated": datetime.now()
        }
        
        return {
            "success": True,
            "session_id": session_id,
            "message": f"Game loaded from '{save_name}'"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to load game: {str(e)}")

@app.delete("/game/{session_id}")
async def end_game_session(session_id: str):
    """End a game session"""
    if session_id in game_sessions:
        del game_sessions[session_id]
        return {"success": True, "message": "Game session ended"}
    else:
        raise HTTPException(status_code=404, detail="Game session not found")

@app.get("/game/sessions")
async def list_active_sessions():
    """List all active game sessions (for debugging)"""
    return {
        "active_sessions": len(game_sessions),
        "sessions": [
            {
                "session_id": sid,
                "created_at": session["created_at"],
                "last_updated": session["last_updated"]
            }
            for sid, session in game_sessions.items()
        ]
    }

def get_available_actions(location: str) -> List[str]:
    """Get available actions for the current location"""
    # This is a simplified version - you might want to expand this based on game state
    base_actions = ["look", "inventory", "status", "help", "save", "quit"]
    
    # Add location-specific actions
    location_actions = {
        "village": ["talk", "shop", "rest"],
        "forest": ["explore", "hunt", "gather"],
        "mountain": ["climb", "mine", "camp"]
    }
    
    return base_actions + location_actions.get(location.lower(), [])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

