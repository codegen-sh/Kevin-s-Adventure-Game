export interface Player {
  name: string;
  health: number;
  inventory: string[];
  location: string;
  gold: number;
}

export interface Location {
  description: string;
  connections: string[];
  items: string[];
}

export interface World {
  current_location: string;
  locations: Record<string, Location>;
  weather?: string;
}

export interface GameSession {
  sessionId: string;
  playerName: string;
  player: Player;
  world: World;
}

export interface GameState {
  player: Player;
  world: World;
  current_location: string;
  available_actions: string[];
  message: string;
}

export interface ActionRequest {
  session_id: string;
  action: string;
}

export interface ActionResponse {
  message: string;
  player: Player;
  world: World;
}

