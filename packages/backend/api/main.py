from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Dict, List, Optional
import sys
import os

# Add the backend directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from game.player import create_player, get_player_status, add_item_to_inventory, remove_item_from_inventory
from game.world import initialize_world, get_current_location, get_available_locations
from game.items import perform_item_action, get_item_description
from utils.save_load import save_game, load_game, list_save_files

app = FastAPI(
    title="Kevin's Adventure Game API",
    description="REST API for Kevin's Adventure Game",
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

# In-memory game sessions (in production, use a database)
game_sessions: Dict[str, Dict] = {}

# Pydantic models
class GameSession(BaseModel):
    player_name: str

class ActionRequest(BaseModel):
    session_id: str
    action: str

class GameState(BaseModel):
    player: Dict
    world: Dict
    current_location: str
    available_actions: List[str]
    message: str

@app.get("/")
async def root():
    return {"message": "Welcome to Kevin's Adventure Game API!"}

@app.post("/game/new", response_model=Dict)
async def create_new_game(session: GameSession):
    """Create a new game session"""
    session_id = f"session_{len(game_sessions) + 1}"
    
    player = create_player(session.player_name)
    world = initialize_world()
    
    game_sessions[session_id] = {
        "player": player,
        "world": world
    }
    
    return {
        "session_id": session_id,
        "message": f"New game created for {session.player_name}!",
        "player": player,
        "world": world
    }

@app.get("/game/{session_id}/state", response_model=GameState)
async def get_game_state(session_id: str):
    """Get current game state"""
    if session_id not in game_sessions:
        raise HTTPException(status_code=404, detail="Game session not found")
    
    session = game_sessions[session_id]
    player = session["player"]
    world = session["world"]
    
    current_location = get_current_location(world)
    available_locations = get_available_locations(world, current_location)
    
    available_actions = [
        "look around",
        "check inventory",
        "check status",
        f"go to {loc.lower()}" for loc in available_locations
    ]
    
    # Add location-specific items as actions
    location_items = world["locations"][current_location].get("items", [])
    for item in location_items:
        available_actions.append(f"take {item}")
    
    return GameState(
        player=player,
        world=world,
        current_location=current_location,
        available_actions=available_actions,
        message=f"You are in the {current_location}."
    )

@app.post("/game/action", response_model=Dict)
async def perform_action(action_request: ActionRequest):
    """Perform a game action"""
    session_id = action_request.session_id
    action = action_request.action.lower()
    
    if session_id not in game_sessions:
        raise HTTPException(status_code=404, detail="Game session not found")
    
    session = game_sessions[session_id]
    player = session["player"]
    world = session["world"]
    
    message = ""
    
    try:
        if action == "look around":
            current_location = get_current_location(world)
            location_info = world["locations"][current_location]
            message = f"You are in the {current_location}. {location_info['description']}"
            if location_info.get("items"):
                message += f" You see: {', '.join(location_info['items'])}"
        
        elif action == "check inventory":
            inventory = player.get("inventory", [])
            if inventory:
                message = f"Your inventory contains: {', '.join(inventory)}"
            else:
                message = "Your inventory is empty."
        
        elif action == "check status":
            message = get_player_status(player)
        
        elif action.startswith("go to "):
            destination = action.replace("go to ", "").title()
            current_location = get_current_location(world)
            available_locations = get_available_locations(world, current_location)
            
            if destination in available_locations:
                world["current_location"] = destination
                player["location"] = destination
                message = f"You travel to the {destination}."
            else:
                message = f"You can't go to {destination} from here. Available locations: {', '.join(available_locations)}"
        
        elif action.startswith("take "):
            item = action.replace("take ", "")
            current_location = get_current_location(world)
            location_items = world["locations"][current_location].get("items", [])
            
            if item in location_items:
                add_item_to_inventory(player, item)
                world["locations"][current_location]["items"].remove(item)
                message = f"You picked up: {item}"
            else:
                message = f"There is no {item} here."
        
        elif action.startswith("use "):
            item = action.replace("use ", "")
            if item in player.get("inventory", []):
                # This would call the existing item action logic
                message = f"You used {item}. {get_item_description(item)}"
            else:
                message = f"You don't have {item} in your inventory."
        
        else:
            message = f"Unknown action: {action}. Try 'look around', 'check inventory', 'go to [location]', or 'take [item]'."
    
    except Exception as e:
        message = f"Error performing action: {str(e)}"
    
    return {
        "message": message,
        "player": player,
        "world": world
    }

@app.get("/game/{session_id}/save")
async def save_game_session(session_id: str):
    """Save the current game session"""
    if session_id not in game_sessions:
        raise HTTPException(status_code=404, detail="Game session not found")
    
    session = game_sessions[session_id]
    player = session["player"]
    world = session["world"]
    
    try:
        save_game(player, world, f"save_{session_id}")
        return {"message": "Game saved successfully!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to save game: {str(e)}")

@app.get("/game/saves")
async def list_saves():
    """List all available save files"""
    try:
        saves = list_save_files()
        return {"saves": saves}
    except Exception as e:
        return {"saves": [], "error": str(e)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

