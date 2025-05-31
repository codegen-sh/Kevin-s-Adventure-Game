import axios from 'axios';
import { GameState, ActionRequest, ActionResponse } from '../types/game';

const API_BASE_URL = 'http://localhost:8000';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

export const gameApi = {
  createNewGame: async (playerName: string) => {
    const response = await api.post('/game/new', { player_name: playerName });
    return response.data;
  },

  getGameState: async (sessionId: string): Promise<GameState> => {
    const response = await api.get(`/game/${sessionId}/state`);
    return response.data;
  },

  performAction: async (actionRequest: ActionRequest): Promise<ActionResponse> => {
    const response = await api.post('/game/action', actionRequest);
    return response.data;
  },

  saveGame: async (sessionId: string) => {
    const response = await api.get(`/game/${sessionId}/save`);
    return response.data;
  },

  listSaves: async () => {
    const response = await api.get('/game/saves');
    return response.data;
  },
};

export default gameApi;

