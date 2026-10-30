# Project Blueprint

## Vision

This project is a 3D tactical grid MOBA prototype.

The game aims to blend:
- tactical positioning on a grid-like terrain
- lane pressure and push timing
- objective-based combat
- elemental terrain interaction
- passive lane monsters and drake-like progression
- lane shops and base economy

## Core axes

- X = horizontal positioning / lanes / flanks
- Y = elevation / verticality / platforms / walls / high ground
- Z = depth / lane progression / push distance / objective approach

## Core loop

1. A player character acts.
2. Terrain and elemental effects resolve.
3. Nearby mobs and waves evaluate their next step.
4. Passive lane objectives react.
5. Lane pressure and objective states update.
6. The next character resolves actions.

## Map structure

- 3 lanes: top, mid, bottom
- central flank / rotation zone
- two bases: blue and red
- objective tower per lane
- passive objective in each lane or central sector
- lane shops and base shop

## Systems

- Character turn order and initiative
- Wave push logic
- Mob pathing and aggro logic
- Terrain tile system
- Elemental tile effects
- Progression tiles and buffs
- Shop logic and lane economy
- Respawn and death pressure triggers

## Files to continue from

- [README.md](../README.md)
- [FIRST_SPEC.md](../FIRST_SPEC.md)
- [SKILL_BIBLE.md](../SKILL_BIBLE.md)
- [docs/GAMEPLAY_CORE.md](GAMEPLAY_CORE.md)
- [docs/GAMEPLAY_MAP.md](GAMEPLAY_MAP.md)
- [docs/GAMEPLAY_TERRAIN.md](GAMEPLAY_TERRAIN.md)
- [docs/GAMEPLAY_TURN_SYSTEM.md](GAMEPLAY_TURN_SYSTEM.md)

## Prototype priorities

1. Build a small playable test map with 3 lanes and 1 central flank.
2. Implement lane pressure and mob push logic.
3. Add elemental terrain tiles and progression tiles.
4. Add lane shops and base shop rules.
5. Add passive lane objectives and drake-like enemies.
6. Validate decision making through loop iteration.

## Next milestone

Build a one-map prototype demonstrating:
- one lane push loop
- one passive neutral objective
- one terrain interaction tile set
- one lane shop access rule
- one death+respawn loop
- one buy action costed in PA
