import React, { useState, useEffect, useRef, useCallback } from 'react';
import styled from 'styled-components';
import { GameSession, GameState } from '../types/game';
import { gameApi } from '../services/gameApi';
import PlayerStatus from './PlayerStatus';
import LocationInfo from './LocationInfo';
import ActionInput from './ActionInput';
import GameLog from './GameLog';

const GameContainer = styled.div`
  background: rgba(255, 255, 255, 0.95);
  border-radius: 20px;
  padding: 20px;
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
  max-width: 1200px;
  width: 100%;
  height: 80vh;
  display: grid;
  grid-template-columns: 1fr 300px;
  grid-template-rows: auto 1fr auto;
  gap: 20px;
  grid-template-areas:
    "header sidebar"
    "main sidebar"
    "input sidebar";
`;

const Header = styled.div`
  grid-area: header;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding-bottom: 15px;
  border-bottom: 2px solid #e1e5e9;
`;

const Title = styled.h1`
  color: #333;
  font-size: 1.8rem;
  margin: 0;
  background: linear-gradient(45deg, #667eea, #764ba2);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
`;

const EndGameButton = styled.button`
  background: #dc3545;
  color: white;
  border: none;
  padding: 8px 16px;
  border-radius: 8px;
  cursor: pointer;
  font-weight: 600;
  transition: background-color 0.2s ease;

  &:hover {
    background: #c82333;
  }
`;

const MainContent = styled.div`
  grid-area: main;
  display: flex;
  flex-direction: column;
  gap: 15px;
  overflow: hidden;
`;

const Sidebar = styled.div`
  grid-area: sidebar;
  display: flex;
  flex-direction: column;
  gap: 15px;
`;

const InputArea = styled.div`
  grid-area: input;
`;

interface GameInterfaceProps {
  gameSession: GameSession;
  onEndGame: () => void;
}

const GameInterface: React.FC<GameInterfaceProps> = ({ gameSession, onEndGame }) => {
  const [gameState, setGameState] = useState<GameState | null>(null);
  const [gameLog, setGameLog] = useState<string[]>([]);
  const [isLoading, setIsLoading] = useState(false);
  const logRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    // Scroll to bottom of log when new messages are added
    if (logRef.current) {
      logRef.current.scrollTop = logRef.current.scrollHeight;
    }
  }, [gameLog]);

  const addToLog = useCallback((message: string) => {
    setGameLog(prev => [...prev, message]);
  }, []);

  const loadGameState = useCallback(async () => {
    try {
      const state = await gameApi.getGameState(gameSession.sessionId);
      setGameState(state);
      addToLog(`Welcome to ${state.current_location}!`);
    } catch (error) {
      console.error('Error loading game state:', error);
      addToLog('Error loading game state. Please try again.');
    }
  }, [gameSession.sessionId, addToLog]);

  useEffect(() => {
    loadGameState();
  }, [loadGameState]);

  const performAction = useCallback(async (action: string) => {
    if (!gameState || isLoading) return;

    setIsLoading(true);
    addToLog(`> ${action}`);

    try {
      const response = await gameApi.performAction({
        session_id: gameSession.sessionId,
        action: action
      });

      addToLog(response.message);
      
      // Update game state
      const newState = await gameApi.getGameState(gameSession.sessionId);
      setGameState(newState);
    } catch (error) {
      console.error('Error performing action:', error);
      addToLog('Error performing action. Please try again.');
    } finally {
      setIsLoading(false);
    }
  }, [gameState, isLoading, addToLog, gameSession.sessionId]);

  const handleSaveGame = async () => {
    try {
      await gameApi.saveGame(gameSession.sessionId);
      addToLog('Game saved successfully!');
    } catch (error) {
      console.error('Error saving game:', error);
      addToLog('Error saving game. Please try again.');
    }
  };

  if (!gameState) {
    return (
      <GameContainer>
        <div>Loading game...</div>
      </GameContainer>
    );
  }

  return (
    <GameContainer>
      <Header>
        <Title>🏰 Kevin's Adventure</Title>
        <div>
          <button onClick={handleSaveGame} style={{ marginRight: '10px' }}>
            💾 Save Game
          </button>
          <EndGameButton onClick={onEndGame}>
            🚪 End Game
          </EndGameButton>
        </div>
      </Header>

      <MainContent>
        <LocationInfo 
          location={gameState.current_location}
          description={gameState.world.locations[gameState.current_location]?.description || ''}
          availableActions={gameState.available_actions}
        />
        <GameLog ref={logRef} messages={gameLog} />
      </MainContent>

      <Sidebar>
        <PlayerStatus player={gameState.player} />
      </Sidebar>

      <InputArea>
        <ActionInput 
          onAction={performAction} 
          isLoading={isLoading}
          availableActions={gameState.available_actions}
        />
      </InputArea>
    </GameContainer>
  );
};

export default GameInterface;
