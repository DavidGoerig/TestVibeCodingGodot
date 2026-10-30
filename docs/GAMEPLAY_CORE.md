# Gameplay Core

## Genre

Tactical Grid MOBA in 3D.

## Core identity

- tactical movement on a grid-like battlefield
- lane pressure and push rhythm
- terrain-driven combat and objective play
- elemental interaction on map tiles
- passive lane monsters and drake-like objectives
- economy through lane shops and base return

## Axes

- X = width / left-right control / flanks
- Y = height / plateaus / walls / high ground
- Z = depth / advancement toward the enemy objective

## Victory condition

The match is won by pushing through pressure, controlling lanes, destroying towers, and winning objective fights.

A player should feel pressure in three layers:
1. direct combat pressure
2. lane pressure
3. map and terrain pressure

## Base loop

1. Character turn begins.
2. Character moves / attacks / casts / buys.
3. Terrain resolves triggered effects.
4. Nearby lane mobs check movement and attacks.
5. Passive objectives react and update the lane state.
6. Pressure and objective clocks update.
7. Next unit acts.

## Character action economy

Use a PA-style action system.

Example:
- Move: 1 PA
- Basic attack: 1 PA
- Skill: 1-2 PA
- Buy item: 1 PA when on a valid shop tile
- Interact objective: 1 PA
- Cancel / reposition: 1 PA

The exact action budget should stay light enough for quick tactical decision-making.

## Buy logic

Buying should be a real tactical action, not a free action.

Rules:
- buy costs PA
- buy is only valid at a shop tile or base zone
- lane shops are smaller and more limited than the base
- the first tower destruction increases value of deeper lane access and more aggressive item choices

## Death logic

A character death should change map tempo.

Rules:
- character is removed from battle for a short respawn timer
- respawn occurs in base or controlled safe zone
- lane pressure shifts immediately toward the side that survived
- a dead character means the opponent gets a push window
- objective pressure intensifies following a death in a contest zone

## Objective logic

Any objective should create a decision:
- push now
- defend the lane
- contest a neutral objective
- take a flank or rotate
- secure a shop node

This keeps the game dynamic even when no direct combat is happening.
