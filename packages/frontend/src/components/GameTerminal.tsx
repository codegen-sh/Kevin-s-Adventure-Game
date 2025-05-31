'use client';

import { useEffect, useRef } from 'react';

interface GameTerminalProps {
  gameLog: string[];
  isLoading: boolean;
}

export const GameTerminal: React.FC<GameTerminalProps> = ({ gameLog, isLoading }) => {
  const terminalRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (terminalRef.current) {
      terminalRef.current.scrollTop = terminalRef.current.scrollHeight;
    }
  }, [gameLog]);

  return (
    <div className="adventure-card">
      <h2 className="text-xl font-bold mb-4 text-adventure-primary">Game Terminal</h2>
      <div ref={terminalRef} className="game-terminal">
        {gameLog.length === 0 ? (
          <div className="text-gray-500">Welcome to Kevin's Adventure Game! Start a new game to begin.</div>
        ) : (
          gameLog.map((line, index) => (
            <div key={index} className="mb-1">
              {line.startsWith('> ') ? (
                <span className="text-yellow-400">{line}</span>
              ) : line.startsWith('Error:') ? (
                <span className="text-red-400">{line}</span>
              ) : (
                <span>{line}</span>
              )}
            </div>
          ))
        )}
        {isLoading && (
          <div className="text-blue-400 animate-pulse">Processing...</div>
        )}
      </div>
    </div>
  );
};

