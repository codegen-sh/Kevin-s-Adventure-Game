export interface Player {
  name: string;
  health: number;
  max_health: number;
  experience: number;
  level: number;
  inventory: GameItem[];
  location: string;
  status_text: string;
}

export interface GameItem {
  name: string;
  description?: string;
  type?: string;
  value?: number;
}

export interface GameSession {
  session_id: string;
  player_name: string;
  created_at: string;
  last_updated: string;
}

export interface GameResponse {
  success: boolean;
  message: string;
  player_status?: Player;
  location?: string;
  available_actions?: string[];
}

export interface GameAction {
  action: string;
}

export interface SaveGameRequest {
  save_name: string;
}

export interface GameState {
  session: GameSession | null;
  player: Player | null;
  currentLocation: string;
  gameLog: string[];
  isLoading: boolean;
  error: string | null;
}

