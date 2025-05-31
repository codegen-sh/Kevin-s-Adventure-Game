'use client';

import { useState } from 'react';
import { Play, RotateCcw, User } from 'lucide-react';

interface GameHeaderProps {
  onNewGame: (playerName: string) => void;
  onEndGame: () => void;
  hasActiveGame: boolean;
  isLoading: boolean;
  playerName?: string;
}

export const GameHeader: React.FC<GameHeaderProps> = ({
  onNewGame,
  onEndGame,
  hasActiveGame,
  isLoading,
  playerName,
}) => {
  const [showNewGameDialog, setShowNewGameDialog] = useState(false);
  const [newPlayerName, setNewPlayerName] = useState('Kevin');

  const handleNewGame = () => {
    onNewGame(newPlayerName.trim() || 'Kevin');
    setShowNewGameDialog(false);
  };

  return (
    <>
      <header className="bg-adventure-primary text-white shadow-lg">
        <div className="container mx-auto px-4 py-6">
          <div className="flex items-center justify-between">
            <div>
              <h1 className="text-3xl font-bold font-adventure">🏰 Kevin's Adventure Game</h1>
              <p className="text-adventure-bg opacity-90 mt-1">
                A modern web interface for the classic text adventure
              </p>
            </div>
            
            <div className="flex items-center space-x-4">
              {hasActiveGame && playerName && (
                <div className="flex items-center space-x-2 bg-adventure-secondary px-3 py-2 rounded">
                  <User className="w-4 h-4" />
                  <span className="font-medium">{playerName}</span>
                </div>
              )}
              
              <button
                onClick={() => setShowNewGameDialog(true)}
                disabled={isLoading}
                className="bg-adventure-accent hover:bg-yellow-600 text-adventure-text font-bold py-2 px-4 rounded transition-colors duration-200 flex items-center space-x-2"
              >
                <Play className="w-4 h-4" />
                <span>New Game</span>
              </button>
              
              {hasActiveGame && (
                <button
                  onClick={onEndGame}
                  disabled={isLoading}
                  className="bg-red-600 hover:bg-red-700 text-white font-bold py-2 px-4 rounded transition-colors duration-200 flex items-center space-x-2"
                >
                  <RotateCcw className="w-4 h-4" />
                  <span>End Game</span>
                </button>
              )}
            </div>
          </div>
        </div>
      </header>

      {/* New Game Dialog */}
      {showNewGameDialog && (
        <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
          <div className="bg-white p-6 rounded-lg max-w-md w-full mx-4">
            <h3 className="text-lg font-bold mb-4 text-adventure-primary">Start New Game</h3>
            <p className="text-gray-600 mb-4">
              {hasActiveGame 
                ? "Starting a new game will end your current session. Are you sure?"
                : "Enter your character name to begin your adventure!"
              }
            </p>
            <input
              type="text"
              value={newPlayerName}
              onChange={(e) => setNewPlayerName(e.target.value)}
              placeholder="Character name"
              className="adventure-input mb-4"
              autoFocus
            />
            <div className="flex space-x-2">
              <button
                onClick={handleNewGame}
                disabled={!newPlayerName.trim()}
                className="adventure-button flex-1"
              >
                Start Adventure
              </button>
              <button
                onClick={() => {
                  setShowNewGameDialog(false);
                  setNewPlayerName('Kevin');
                }}
                className="adventure-button-secondary flex-1"
              >
                Cancel
              </button>
            </div>
          </div>
        </div>
      )}
    </>
  );
};

