import axios from 'axios';
import { GameSession, GameResponse, GameAction, SaveGameRequest, Player } from '@/types/game';

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

export const gameApi = {
  // Create a new game session
  createNewGame: async (playerName: string = 'Kevin'): Promise<GameSession> => {
    const response = await api.post(`/game/new?player_name=${encodeURIComponent(playerName)}`);
    return response.data;
  },

  // Get current game status
  getGameStatus: async (sessionId: string): Promise<Player> => {
    const response = await api.get(`/game/${sessionId}/status`);
    return response.data;
  },

  // Perform a game action
  performAction: async (sessionId: string, action: GameAction): Promise<GameResponse> => {
    const response = await api.post(`/game/${sessionId}/action`, action);
    return response.data;
  },

  // Get help information
  getHelp: async (sessionId: string): Promise<{ help_text: string }> => {
    const response = await api.get(`/game/${sessionId}/help`);
    return response.data;
  },

  // Save the game
  saveGame: async (sessionId: string, saveRequest: SaveGameRequest): Promise<{ success: boolean; message: string }> => {
    const response = await api.post(`/game/${sessionId}/save`, saveRequest);
    return response.data;
  },

  // List available saves
  listSaves: async (): Promise<{ saves: string[]; error?: string }> => {
    const response = await api.get('/game/saves');
    return response.data;
  },

  // Load a saved game
  loadGame: async (saveName: string): Promise<{ success: boolean; session_id: string; message: string }> => {
    const response = await api.post(`/game/load/${encodeURIComponent(saveName)}`);
    return response.data;
  },

  // End game session
  endGameSession: async (sessionId: string): Promise<{ success: boolean; message: string }> => {
    const response = await api.delete(`/game/${sessionId}`);
    return response.data;
  },

  // List active sessions (for debugging)
  listActiveSessions: async (): Promise<{ active_sessions: number; sessions: any[] }> => {
    const response = await api.get('/game/sessions');
    return response.data;
  },
};

export default api;

