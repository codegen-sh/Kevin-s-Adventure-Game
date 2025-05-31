'use client';

import { useState } from 'react';
import { Send, HelpCircle, Save, FolderOpen } from 'lucide-react';

interface ActionPanelProps {
  onAction: (action: string) => void;
  onHelp: () => void;
  onSave: (saveName: string) => void;
  onLoad: (saveName: string) => void;
  isLoading: boolean;
  hasActiveGame: boolean;
}

export const ActionPanel: React.FC<ActionPanelProps> = ({
  onAction,
  onHelp,
  onSave,
  onLoad,
  isLoading,
  hasActiveGame,
}) => {
  const [currentAction, setCurrentAction] = useState('');
  const [showSaveDialog, setShowSaveDialog] = useState(false);
  const [showLoadDialog, setShowLoadDialog] = useState(false);
  const [saveName, setSaveName] = useState('');

  const handleSubmitAction = (e: React.FormEvent) => {
    e.preventDefault();
    if (currentAction.trim() && !isLoading) {
      onAction(currentAction.trim());
      setCurrentAction('');
    }
  };

  const handleSave = () => {
    if (saveName.trim()) {
      onSave(saveName.trim());
      setSaveName('');
      setShowSaveDialog(false);
    }
  };

  const handleLoad = () => {
    if (saveName.trim()) {
      onLoad(saveName.trim());
      setSaveName('');
      setShowLoadDialog(false);
    }
  };

  const quickActions = [
    { label: 'Look', action: 'look' },
    { label: 'Inventory', action: 'inventory' },
    { label: 'Status', action: 'status' },
    { label: 'Explore', action: 'explore' },
    { label: 'Rest', action: 'rest' },
    { label: 'Go Village', action: 'go village' },
    { label: 'Go Forest', action: 'go forest' },
    { label: 'Go Mountain', action: 'go mountain' },
  ];

  return (
    <div className="adventure-card">
      <h2 className="text-xl font-bold mb-4 text-adventure-primary">Actions</h2>
      
      {/* Command Input */}
      <form onSubmit={handleSubmitAction} className="mb-4">
        <div className="flex space-x-2">
          <input
            type="text"
            value={currentAction}
            onChange={(e) => setCurrentAction(e.target.value)}
            placeholder="Enter your action..."
            className="adventure-input flex-1"
            disabled={isLoading || !hasActiveGame}
          />
          <button
            type="submit"
            disabled={isLoading || !hasActiveGame || !currentAction.trim()}
            className="adventure-button flex items-center space-x-1"
          >
            <Send className="w-4 h-4" />
            <span>Send</span>
          </button>
        </div>
      </form>

      {/* Quick Actions */}
      <div className="mb-4">
        <h3 className="font-semibold mb-2 text-adventure-secondary">Quick Actions</h3>
        <div className="grid grid-cols-2 gap-2">
          {quickActions.map((action) => (
            <button
              key={action.action}
              onClick={() => onAction(action.action)}
              disabled={isLoading || !hasActiveGame}
              className="adventure-button-secondary text-sm py-1 px-2"
            >
              {action.label}
            </button>
          ))}
        </div>
      </div>

      {/* Utility Buttons */}
      <div className="flex space-x-2">
        <button
          onClick={onHelp}
          disabled={isLoading || !hasActiveGame}
          className="adventure-button flex items-center space-x-1 flex-1"
        >
          <HelpCircle className="w-4 h-4" />
          <span>Help</span>
        </button>
        
        <button
          onClick={() => setShowSaveDialog(true)}
          disabled={isLoading || !hasActiveGame}
          className="adventure-button flex items-center space-x-1 flex-1"
        >
          <Save className="w-4 h-4" />
          <span>Save</span>
        </button>
        
        <button
          onClick={() => setShowLoadDialog(true)}
          disabled={isLoading}
          className="adventure-button flex items-center space-x-1 flex-1"
        >
          <FolderOpen className="w-4 h-4" />
          <span>Load</span>
        </button>
      </div>

      {/* Save Dialog */}
      {showSaveDialog && (
        <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
          <div className="bg-white p-6 rounded-lg max-w-md w-full mx-4">
            <h3 className="text-lg font-bold mb-4">Save Game</h3>
            <input
              type="text"
              value={saveName}
              onChange={(e) => setSaveName(e.target.value)}
              placeholder="Enter save name..."
              className="adventure-input mb-4"
              autoFocus
            />
            <div className="flex space-x-2">
              <button
                onClick={handleSave}
                disabled={!saveName.trim()}
                className="adventure-button flex-1"
              >
                Save
              </button>
              <button
                onClick={() => {
                  setShowSaveDialog(false);
                  setSaveName('');
                }}
                className="adventure-button-secondary flex-1"
              >
                Cancel
              </button>
            </div>
          </div>
        </div>
      )}

      {/* Load Dialog */}
      {showLoadDialog && (
        <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
          <div className="bg-white p-6 rounded-lg max-w-md w-full mx-4">
            <h3 className="text-lg font-bold mb-4">Load Game</h3>
            <input
              type="text"
              value={saveName}
              onChange={(e) => setSaveName(e.target.value)}
              placeholder="Enter save name..."
              className="adventure-input mb-4"
              autoFocus
            />
            <div className="flex space-x-2">
              <button
                onClick={handleLoad}
                disabled={!saveName.trim()}
                className="adventure-button flex-1"
              >
                Load
              </button>
              <button
                onClick={() => {
                  setShowLoadDialog(false);
                  setSaveName('');
                }}
                className="adventure-button-secondary flex-1"
              >
                Cancel
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};
