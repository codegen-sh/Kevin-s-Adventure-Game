'use client';

import { useState, useCallback } from 'react';
import { gameApi } from '@/lib/api';
import { GameState, GameSession, Player, GameResponse } from '@/types/game';

export const useGame = () => {
  const [gameState, setGameState] = useState<GameState>({
    session: null,
    player: null,
    currentLocation: '',
    gameLog: [],
    isLoading: false,
    error: null,
  });

  const addToLog = useCallback((message: string) => {
    setGameState(prev => ({
      ...prev,
      gameLog: [...prev.gameLog, message],
    }));
  }, []);

  const setLoading = useCallback((loading: boolean) => {
    setGameState(prev => ({ ...prev, isLoading: loading }));
  }, []);

  const setError = useCallback((error: string | null) => {
    setGameState(prev => ({ ...prev, error }));
  }, []);

  const createNewGame = useCallback(async (playerName: string = 'Kevin') => {
    try {
      setLoading(true);
      setError(null);
      
      const session = await gameApi.createNewGame(playerName);
      const player = await gameApi.getGameStatus(session.session_id);
      
      setGameState(prev => ({
        ...prev,
        session,
        player,
        currentLocation: player.location,
        gameLog: [`Welcome to Kevin's Adventure Game, ${playerName}!`, `You are in ${player.location}.`],
      }));
      
      addToLog(`Game started! Type 'help' for available commands.`);
    } catch (error) {
      setError('Failed to create new game');
      console.error('Error creating new game:', error);
    } finally {
      setLoading(false);
    }
  }, [addToLog, setLoading, setError]);

  const performAction = useCallback(async (action: string) => {
    if (!gameState.session) {
      setError('No active game session');
      return;
    }

    try {
      setLoading(true);
      setError(null);
      
      const response = await gameApi.performAction(gameState.session.session_id, { action });
      
      if (response.success) {
        addToLog(`> ${action}`);
        addToLog(response.message);
        
        if (response.player_status) {
          setGameState(prev => ({
            ...prev,
            player: response.player_status!,
            currentLocation: response.location || prev.currentLocation,
          }));
        }
      } else {
        addToLog(`Error: ${response.message}`);
      }
    } catch (error) {
      setError('Failed to perform action');
      addToLog('Error: Failed to perform action');
      console.error('Error performing action:', error);
    } finally {
      setLoading(false);
    }
  }, [gameState.session, addToLog, setLoading, setError]);

  const saveGame = useCallback(async (saveName: string) => {
    if (!gameState.session) {
      setError('No active game session');
      return;
    }

    try {
      setLoading(true);
      setError(null);
      
      const response = await gameApi.saveGame(gameState.session.session_id, { save_name: saveName });
      
      if (response.success) {
        addToLog(`Game saved as "${saveName}"`);
      } else {
        addToLog(`Failed to save game: ${response.message}`);
      }
    } catch (error) {
      setError('Failed to save game');
      addToLog('Error: Failed to save game');
      console.error('Error saving game:', error);
    } finally {
      setLoading(false);
    }
  }, [gameState.session, addToLog, setLoading, setError]);

  const loadGame = useCallback(async (saveName: string) => {
    try {
      setLoading(true);
      setError(null);
      
      const response = await gameApi.loadGame(saveName);
      
      if (response.success) {
        const player = await gameApi.getGameStatus(response.session_id);
        
        setGameState(prev => ({
          ...prev,
          session: {
            session_id: response.session_id,
            player_name: player.name,
            created_at: new Date().toISOString(),
            last_updated: new Date().toISOString(),
          },
          player,
          currentLocation: player.location,
          gameLog: [`Game loaded from "${saveName}"`, `You are in ${player.location}.`],
        }));
        
        addToLog('Game loaded successfully!');
      } else {
        addToLog(`Failed to load game: ${response.message}`);
      }
    } catch (error) {
      setError('Failed to load game');
      addToLog('Error: Failed to load game');
      console.error('Error loading game:', error);
    } finally {
      setLoading(false);
    }
  }, [addToLog, setLoading, setError]);

  const getHelp = useCallback(async () => {
    if (!gameState.session) {
      setError('No active game session');
      return;
    }

    try {
      const response = await gameApi.getHelp(gameState.session.session_id);
      addToLog('> help');
      addToLog(response.help_text);
    } catch (error) {
      addToLog('Error: Failed to get help');
      console.error('Error getting help:', error);
    }
  }, [gameState.session, addToLog]);

  const endGame = useCallback(async () => {
    if (!gameState.session) return;

    try {
      await gameApi.endGameSession(gameState.session.session_id);
      setGameState({
        session: null,
        player: null,
        currentLocation: '',
        gameLog: [],
        isLoading: false,
        error: null,
      });
    } catch (error) {
      console.error('Error ending game session:', error);
    }
  }, [gameState.session]);

  return {
    gameState,
    createNewGame,
    performAction,
    saveGame,
    loadGame,
    getHelp,
    endGame,
  };
};

