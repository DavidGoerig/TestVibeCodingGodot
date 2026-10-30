# Map Design

## Map structure

### 3 lanes

- Top lane
- Mid lane
- Bottom lane

### Central expansion

The middle of the map contains a flanking / rotation / jungle-style zone.

This zone should offer:
- ambush routes
- neutral buffs
- terrain transitions
- access to lane pressure and side objectives
- a reason to rotate instead of brute-force a lane

## Lane design

Each lane includes:
- spawn zone
- safe approach lane
- contested middle lane
- progression tile zone
- objective threshold
- tower / structure zone
- push route to the enemy base

## Objective order

1. lane pressure creates opportunities
2. neutral progression zones give temporary power
3. lane objective is contested
4. tower falls
5. deeper push becomes available
6. base pressure or flank pressure becomes the dominant play

## Lane shop logic

- lane shops exist in secure or controlled tiles
- access is gated by map control and security state
- lane shops allow smaller, immediate buys
- base shop remains the primary major reset zone

## First tower destruction

When the first tower falls, the lane opens into a more dangerous and rewarding push lane.

Effects:
- more pathing freedom in the lane
- more risk of enemy rotation
- better access to deeper progression zones
- stronger reward for pressure and timing

## Base logic

The base remains:
- safest shop location
- respawn point
- major reset zone
- command center for staged recovery
