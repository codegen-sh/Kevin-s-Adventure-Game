import React, { forwardRef } from 'react';
import styled from 'styled-components';

const LogContainer = styled.div`
  background: #1a1a1a;
  border-radius: 12px;
  padding: 20px;
  border: 2px solid #e1e5e9;
  height: 300px;
  overflow-y: auto;
  font-family: 'Courier New', monospace;
  color: #00ff00;
  line-height: 1.5;
  
  /* Custom scrollbar */
  &::-webkit-scrollbar {
    width: 8px;
  }
  
  &::-webkit-scrollbar-track {
    background: #2a2a2a;
    border-radius: 4px;
  }
  
  &::-webkit-scrollbar-thumb {
    background: #555;
    border-radius: 4px;
  }
  
  &::-webkit-scrollbar-thumb:hover {
    background: #777;
  }
`;

const LogTitle = styled.h4`
  color: #333;
  margin: 0 0 15px 0;
  font-size: 1rem;
  display: flex;
  align-items: center;
  gap: 8px;
  font-family: inherit;
`;

const LogMessage = styled.div<{ isUserInput?: boolean }>`
  margin-bottom: 8px;
  color: ${props => props.isUserInput ? '#ffff00' : '#00ff00'};
  
  ${props => props.isUserInput && `
    &::before {
      content: '> ';
      color: #ffff00;
      font-weight: bold;
    }
  `}
`;

const EmptyLog = styled.div`
  color: #666;
  font-style: italic;
  text-align: center;
  padding: 40px 0;
  font-family: inherit;
`;

interface GameLogProps {
  messages: string[];
}

const GameLog = forwardRef<HTMLDivElement, GameLogProps>(({ messages }, ref) => {
  return (
    <div>
      <LogTitle>📜 Game Log</LogTitle>
      <LogContainer ref={ref}>
        {messages.length === 0 ? (
          <EmptyLog>Game log will appear here...</EmptyLog>
        ) : (
          messages.map((message, index) => (
            <LogMessage 
              key={index} 
              isUserInput={message.startsWith('> ')}
            >
              {message.startsWith('> ') ? message.substring(2) : message}
            </LogMessage>
          ))
        )}
      </LogContainer>
    </div>
  );
});

GameLog.displayName = 'GameLog';

export default GameLog;

