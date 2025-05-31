'use client';

import { Player } from '@/types/game';
import { Heart, MapPin, Star, Package } from 'lucide-react';

interface PlayerStatusProps {
  player: Player | null;
}

export const PlayerStatus: React.FC<PlayerStatusProps> = ({ player }) => {
  if (!player) {
    return (
      <div className="adventure-card">
        <h2 className="text-xl font-bold mb-4 text-adventure-primary">Player Status</h2>
        <p className="text-gray-500">No active game session</p>
      </div>
    );
  }

  const healthPercentage = (player.health / player.max_health) * 100;

  return (
    <div className="adventure-card">
      <h2 className="text-xl font-bold mb-4 text-adventure-primary">Player Status</h2>
      
      <div className="space-y-4">
        {/* Player Name */}
        <div>
          <h3 className="font-semibold text-adventure-secondary">{player.name}</h3>
        </div>

        {/* Health Bar */}
        <div className="flex items-center space-x-2">
          <Heart className="w-5 h-5 text-red-500" />
          <div className="flex-1">
            <div className="flex justify-between text-sm mb-1">
              <span>Health</span>
              <span>{player.health}/{player.max_health}</span>
            </div>
            <div className="w-full bg-gray-200 rounded-full h-2">
              <div
                className={`h-2 rounded-full transition-all duration-300 ${
                  healthPercentage > 60
                    ? 'bg-green-500'
                    : healthPercentage > 30
                    ? 'bg-yellow-500'
                    : 'bg-red-500'
                }`}
                style={{ width: `${healthPercentage}%` }}
              ></div>
            </div>
          </div>
        </div>

        {/* Location */}
        <div className="flex items-center space-x-2">
          <MapPin className="w-5 h-5 text-blue-500" />
          <span className="font-medium">{player.location}</span>
        </div>

        {/* Level and Experience */}
        <div className="flex items-center space-x-2">
          <Star className="w-5 h-5 text-yellow-500" />
          <span>Level {player.level} (XP: {player.experience})</span>
        </div>

        {/* Inventory */}
        <div>
          <div className="flex items-center space-x-2 mb-2">
            <Package className="w-5 h-5 text-adventure-secondary" />
            <span className="font-medium">Inventory ({player.inventory.length} items)</span>
          </div>
          <div className="bg-gray-50 rounded p-2 max-h-32 overflow-y-auto">
            {player.inventory.length === 0 ? (
              <span className="text-gray-500 text-sm">Empty</span>
            ) : (
              <div className="grid grid-cols-2 gap-1">
                {player.inventory.map((item, index) => (
                  <span
                    key={index}
                    className="text-sm bg-adventure-accent text-adventure-text px-2 py-1 rounded"
                  >
                    {typeof item === 'string' ? item : item.name}
                  </span>
                ))}
              </div>
            )}
          </div>
        </div>
      </div>
    </div>
  );
};

