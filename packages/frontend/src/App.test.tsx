import React from 'react';
import { render, screen } from '@testing-library/react';
import App from './App';

// Mock the gameApi module to avoid ES module issues
jest.mock('./services/gameApi', () => ({
  gameApi: {
    createNewGame: jest.fn(),
    getGameState: jest.fn(),
    performAction: jest.fn(),
    saveGame: jest.fn(),
    listSaves: jest.fn(),
  },
}));

test('renders start screen initially', () => {
  render(<App />);
  const titleElement = screen.getByText(/Kevin's Adventure Game/i);
  expect(titleElement).toBeInTheDocument();
});

