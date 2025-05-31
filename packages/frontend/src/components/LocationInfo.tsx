import React from 'react';
import styled from 'styled-components';

const LocationContainer = styled.div`
  background: #f8f9fa;
  border-radius: 12px;
  padding: 20px;
  border: 2px solid #e1e5e9;
`;

const LocationTitle = styled.h2`
  color: #333;
  margin: 0 0 15px 0;
  font-size: 1.5rem;
  display: flex;
  align-items: center;
  gap: 10px;
`;

const LocationDescription = styled.p`
  color: #666;
  line-height: 1.6;
  margin-bottom: 20px;
  font-size: 1rem;
`;

const ActionsTitle = styled.h4`
  color: #333;
  margin: 0 0 10px 0;
  font-size: 1rem;
`;

const ActionsList = styled.div`
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
`;

const ActionChip = styled.span`
  background: linear-gradient(45deg, #667eea, #764ba2);
  color: white;
  padding: 4px 12px;
  border-radius: 20px;
  font-size: 0.85rem;
  font-weight: 500;
`;

const getLocationEmoji = (location: string): string => {
  const emojiMap: Record<string, string> = {
    'Village': '🏘️',
    'Forest': '🌲',
    'Mountain': '⛰️',
    'Cave': '🕳️',
    'Castle': '🏰',
    'Desert': '🏜️',
    'Ocean': '🌊',
    'Dungeon': '🏚️',
  };
  
  return emojiMap[location] || '📍';
};

interface LocationInfoProps {
  location: string;
  description: string;
  availableActions: string[];
}

const LocationInfo: React.FC<LocationInfoProps> = ({ 
  location, 
  description, 
  availableActions 
}) => {
  return (
    <LocationContainer>
      <LocationTitle>
        {getLocationEmoji(location)} {location}
      </LocationTitle>
      
      <LocationDescription>
        {description}
      </LocationDescription>
      
      {availableActions && availableActions.length > 0 && (
        <>
          <ActionsTitle>💡 Available Actions:</ActionsTitle>
          <ActionsList>
            {availableActions.slice(0, 8).map((action, index) => (
              <ActionChip key={index}>
                {action}
              </ActionChip>
            ))}
            {availableActions.length > 8 && (
              <ActionChip>
                +{availableActions.length - 8} more...
              </ActionChip>
            )}
          </ActionsList>
        </>
      )}
    </LocationContainer>
  );
};

export default LocationInfo;

