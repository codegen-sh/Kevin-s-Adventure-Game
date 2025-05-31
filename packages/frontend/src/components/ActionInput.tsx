import React, { useState, useRef, useEffect } from 'react';
import styled from 'styled-components';

const InputContainer = styled.div`
  background: #f8f9fa;
  border-radius: 12px;
  padding: 20px;
  border: 2px solid #e1e5e9;
`;

const InputTitle = styled.h4`
  color: #333;
  margin: 0 0 15px 0;
  font-size: 1rem;
  display: flex;
  align-items: center;
  gap: 8px;
`;

const InputForm = styled.form`
  display: flex;
  gap: 10px;
`;

const ActionInputField = styled.input`
  flex: 1;
  padding: 12px 16px;
  border: 2px solid #e1e5e9;
  border-radius: 8px;
  font-size: 1rem;
  transition: border-color 0.3s ease;

  &:focus {
    outline: none;
    border-color: #667eea;
  }

  &:disabled {
    background: #f5f5f5;
    cursor: not-allowed;
  }
`;

const SubmitButton = styled.button`
  background: linear-gradient(45deg, #667eea, #764ba2);
  color: white;
  border: none;
  padding: 12px 20px;
  border-radius: 8px;
  font-weight: 600;
  cursor: pointer;
  transition: transform 0.2s ease;
  min-width: 80px;

  &:hover:not(:disabled) {
    transform: translateY(-1px);
  }

  &:disabled {
    opacity: 0.6;
    cursor: not-allowed;
    transform: none;
  }
`;

const QuickActionsContainer = styled.div`
  margin-top: 15px;
`;

const QuickActionsTitle = styled.div`
  color: #666;
  font-size: 0.9rem;
  margin-bottom: 8px;
`;

const QuickActionsList = styled.div`
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
`;

const QuickActionButton = styled.button`
  background: white;
  color: #667eea;
  border: 1px solid #667eea;
  padding: 6px 12px;
  border-radius: 6px;
  font-size: 0.85rem;
  cursor: pointer;
  transition: all 0.2s ease;

  &:hover {
    background: #667eea;
    color: white;
  }

  &:disabled {
    opacity: 0.5;
    cursor: not-allowed;
  }
`;

const LoadingSpinner = styled.div`
  border: 2px solid #f3f3f3;
  border-top: 2px solid #667eea;
  border-radius: 50%;
  width: 16px;
  height: 16px;
  animation: spin 1s linear infinite;

  @keyframes spin {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
  }
`;

interface ActionInputProps {
  onAction: (action: string) => void;
  isLoading: boolean;
  availableActions: string[];
}

const ActionInput: React.FC<ActionInputProps> = ({ 
  onAction, 
  isLoading, 
  availableActions 
}) => {
  const [inputValue, setInputValue] = useState('');
  const inputRef = useRef<HTMLInputElement>(null);

  useEffect(() => {
    // Focus input when component mounts or loading finishes
    if (!isLoading && inputRef.current) {
      inputRef.current.focus();
    }
  }, [isLoading]);

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (inputValue.trim() && !isLoading) {
      onAction(inputValue.trim());
      setInputValue('');
    }
  };

  const handleQuickAction = (action: string) => {
    if (!isLoading) {
      onAction(action);
    }
  };

  const quickActions = [
    'look around',
    'check inventory',
    'check status',
  ];

  // Add movement actions from available actions
  const movementActions = availableActions
    .filter(action => action.startsWith('go to'))
    .slice(0, 3);

  const allQuickActions = [...quickActions, ...movementActions];

  return (
    <InputContainer>
      <InputTitle>⌨️ Enter Command</InputTitle>
      
      <InputForm onSubmit={handleSubmit}>
        <ActionInputField
          ref={inputRef}
          type="text"
          value={inputValue}
          onChange={(e) => setInputValue(e.target.value)}
          placeholder="Type your action here... (e.g., 'look around', 'go to forest')"
          disabled={isLoading}
          autoComplete="off"
        />
        <SubmitButton type="submit" disabled={!inputValue.trim() || isLoading}>
          {isLoading ? <LoadingSpinner /> : '➤'}
        </SubmitButton>
      </InputForm>

      <QuickActionsContainer>
        <QuickActionsTitle>Quick Actions:</QuickActionsTitle>
        <QuickActionsList>
          {allQuickActions.map((action, index) => (
            <QuickActionButton
              key={index}
              onClick={() => handleQuickAction(action)}
              disabled={isLoading}
            >
              {action}
            </QuickActionButton>
          ))}
        </QuickActionsList>
      </QuickActionsContainer>
    </InputContainer>
  );
};

export default ActionInput;

