# Turn and Mob System

## Desired structure

The world should react after every character action.

## Turn order

1. Initiative ordering for actors
2. Character takes turn
3. Reactive terrain effects trigger
4. Adjacent mobs resolve movement and attack decisions
5. Passive objectives update
6. Lane pressure shifts
7. Next actor resolves

## Mob behavior

Mobs should:
- advance toward the opponent objective in Z depth
- attack the nearest valid target
- respect blocked / hazardous tiles
- react to elemental terrain and objectives
- stop or delay if the lane is contested

## Passive objective behavior

Passive lane objectives can behave like drake / Nash style units.

They should:
- occupy a meaningful lane tile or route
- provide small but important buffs
- alter terrain or pressure state
- force a decision between push and secure

## Pressure system

Each lane should have a pressure value:
- lane secure
- lane contested
- lane under push
- lane critical

Pressure can rise or fall based on:
- hero presence
- mob waves
- terrain shifts
- objective wins
- tower state
- dead units

## Push behavior

The lane should not simply be a corridor.
It should be a rhythm system:
- push forward
- stop and secure
- contest the neutral objective
- rotate when the lane thickens
- punish when enemy pressure peaks

## Death and push windows

Deaths create windows.

A death should immediately increase the opponent’s ability to:
- push a lane
- contest the objective
- claim a progression tile
- secure the path to the tower

This is how the map stays lively.
