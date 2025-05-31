import React, { useState, useEffect } from 'react';
import styled from 'styled-components';
import GameInterface from './components/GameInterface';
import StartScreen from './components/StartScreen';
import { GameSession } from './types/game';
import './App.css';

const AppContainer = styled.div`
  min-height: 100vh;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 20px;
`;

const App: React.FC = () => {
  const [gameSession, setGameSession] = useState<GameSession | null>(null);
  const [isLoading, setIsLoading] = useState(false);

  const startNewGame = async (playerName: string) => {
    setIsLoading(true);
    try {
      const response = await fetch('http://localhost:8000/game/new', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ player_name: playerName }),
      });

      if (response.ok) {
        const data = await response.json();
        setGameSession({
          sessionId: data.session_id,
          playerName: playerName,
          player: data.player,
          world: data.world,
        });
      } else {
        console.error('Failed to create new game');
      }
    } catch (error) {
      console.error('Error creating new game:', error);
    } finally {
      setIsLoading(false);
    }
  };

  const endGame = () => {
    setGameSession(null);
  };

  return (
    <AppContainer>
      {!gameSession ? (
        <StartScreen onStartGame={startNewGame} isLoading={isLoading} />
      ) : (
        <GameInterface gameSession={gameSession} onEndGame={endGame} />
      )}
    </AppContainer>
  );
};

export default App;

