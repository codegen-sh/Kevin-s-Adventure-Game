'use client';

import { useGame } from '@/hooks/useGame';
import { GameHeader } from '@/components/GameHeader';
import { GameTerminal } from '@/components/GameTerminal';
import { PlayerStatus } from '@/components/PlayerStatus';
import { ActionPanel } from '@/components/ActionPanel';

export default function Home() {
  const {
    gameState,
    createNewGame,
    performAction,
    saveGame,
    loadGame,
    getHelp,
    endGame,
  } = useGame();

  const hasActiveGame = !!gameState.session;

  return (
    <div className="min-h-screen bg-adventure-bg">
      <GameHeader
        onNewGame={createNewGame}
        onEndGame={endGame}
        hasActiveGame={hasActiveGame}
        isLoading={gameState.isLoading}
        playerName={gameState.player?.name}
      />
      
      <main className="container mx-auto px-4 py-8">
        {gameState.error && (
          <div className="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded mb-6">
            <strong>Error:</strong> {gameState.error}
          </div>
        )}
        
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
          {/* Game Terminal - Takes up 2 columns on large screens */}
          <div className="lg:col-span-2">
            <GameTerminal
              gameLog={gameState.gameLog}
              isLoading={gameState.isLoading}
            />
          </div>
          
          {/* Sidebar with Player Status and Actions */}
          <div className="space-y-6">
            <PlayerStatus player={gameState.player} />
            
            <ActionPanel
              onAction={performAction}
              onHelp={getHelp}
              onSave={saveGame}
              onLoad={loadGame}
              isLoading={gameState.isLoading}
              hasActiveGame={hasActiveGame}
            />
          </div>
        </div>
        
        {/* Welcome Message for New Users */}
        {!hasActiveGame && gameState.gameLog.length === 0 && (
          <div className="mt-8 adventure-card text-center">
            <h2 className="text-2xl font-bold text-adventure-primary mb-4">
              Welcome to Kevin's Adventure Game!
            </h2>
            <p className="text-adventure-text mb-6 leading-relaxed">
              Embark on an epic text-based adventure through mystical lands filled with 
              danger, treasure, and mystery. Explore villages, forests, mountains, and caves 
              as you build your character and uncover the secrets of this magical world.
            </p>
            <div className="grid grid-cols-1 md:grid-cols-3 gap-4 text-sm">
              <div className="bg-adventure-bg p-4 rounded">
                <h3 className="font-bold text-adventure-secondary mb-2">🏰 Explore</h3>
                <p>Visit villages, forests, mountains, and mysterious caves</p>
              </div>
              <div className="bg-adventure-bg p-4 rounded">
                <h3 className="font-bold text-adventure-secondary mb-2">⚔️ Adventure</h3>
                <p>Collect items, fight monsters, and gain experience</p>
              </div>
              <div className="bg-adventure-bg p-4 rounded">
                <h3 className="font-bold text-adventure-secondary mb-2">💾 Progress</h3>
                <p>Save your game and continue your journey anytime</p>
              </div>
            </div>
            <p className="mt-6 text-gray-600">
              Click "New Game" to start your adventure!
            </p>
          </div>
        )}
      </main>
      
      <footer className="bg-adventure-primary text-white py-4 mt-12">
        <div className="container mx-auto px-4 text-center">
          <p>&copy; 2024 Kevin's Adventure Game - Powered by FastAPI & Next.js</p>
        </div>
      </footer>
    </div>
  );
}

