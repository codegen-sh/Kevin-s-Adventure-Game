import React from 'react';
import styled from 'styled-components';
import { Player } from '../types/game';

const StatusContainer = styled.div`
  background: #f8f9fa;
  border-radius: 12px;
  padding: 20px;
  border: 2px solid #e1e5e9;
`;

const StatusTitle = styled.h3`
  color: #333;
  margin: 0 0 15px 0;
  font-size: 1.2rem;
  display: flex;
  align-items: center;
  gap: 8px;
`;

const StatusItem = styled.div`
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 10px;
  padding: 8px 0;
  border-bottom: 1px solid #e1e5e9;

  &:last-child {
    border-bottom: none;
    margin-bottom: 0;
  }
`;

const StatusLabel = styled.span`
  color: #666;
  font-weight: 600;
`;

const StatusValue = styled.span`
  color: #333;
  font-weight: 700;
`;

const HealthBar = styled.div<{ health: number }>`
  width: 100%;
  height: 8px;
  background: #e1e5e9;
  border-radius: 4px;
  overflow: hidden;
  margin-top: 5px;

  &::after {
    content: '';
    display: block;
    width: ${props => props.health}%;
    height: 100%;
    background: ${props => 
      props.health > 70 ? '#28a745' :
      props.health > 30 ? '#ffc107' : '#dc3545'
    };
    transition: width 0.3s ease, background-color 0.3s ease;
  }
`;

const InventoryContainer = styled.div`
  background: #f8f9fa;
  border-radius: 12px;
  padding: 20px;
  border: 2px solid #e1e5e9;
  margin-top: 15px;
`;

const InventoryTitle = styled.h3`
  color: #333;
  margin: 0 0 15px 0;
  font-size: 1.2rem;
  display: flex;
  align-items: center;
  gap: 8px;
`;

const InventoryList = styled.ul`
  list-style: none;
  padding: 0;
  margin: 0;
`;

const InventoryItem = styled.li`
  background: white;
  padding: 8px 12px;
  margin-bottom: 5px;
  border-radius: 6px;
  border: 1px solid #e1e5e9;
  font-size: 0.9rem;
  color: #333;

  &:last-child {
    margin-bottom: 0;
  }
`;

const EmptyInventory = styled.div`
  color: #999;
  font-style: italic;
  text-align: center;
  padding: 20px 0;
`;

interface PlayerStatusProps {
  player: Player;
}

const PlayerStatus: React.FC<PlayerStatusProps> = ({ player }) => {
  return (
    <>
      <StatusContainer>
        <StatusTitle>👤 Player Status</StatusTitle>
        
        <StatusItem>
          <StatusLabel>Name:</StatusLabel>
          <StatusValue>{player.name}</StatusValue>
        </StatusItem>
        
        <StatusItem>
          <StatusLabel>Health:</StatusLabel>
          <StatusValue>{player.health}/100</StatusValue>
        </StatusItem>
        <HealthBar health={player.health} />
        
        <StatusItem>
          <StatusLabel>Location:</StatusLabel>
          <StatusValue>{player.location}</StatusValue>
        </StatusItem>
        
        <StatusItem>
          <StatusLabel>Gold:</StatusLabel>
          <StatusValue>💰 {player.gold}</StatusValue>
        </StatusItem>
      </StatusContainer>

      <InventoryContainer>
        <InventoryTitle>🎒 Inventory</InventoryTitle>
        
        {player.inventory && player.inventory.length > 0 ? (
          <InventoryList>
            {player.inventory.map((item, index) => (
              <InventoryItem key={index}>
                {item}
              </InventoryItem>
            ))}
          </InventoryList>
        ) : (
          <EmptyInventory>Your inventory is empty</EmptyInventory>
        )}
      </InventoryContainer>
    </>
  );
};

export default PlayerStatus;

